#!/usr/bin/env python3
"""Commando Intel collector.

Reads intel/targets.yml, pulls public data per platform, writes normalised files to
intel/data/<run-date>/:
  profiles.json   one record per account (followers, posts, bio…)
  posts.csv       one row per post/video (date, format, views, likes, comments, shares, caption…)
  heatmaps.json   YouTube "most replayed" curves (public retention proxy)
  run_log.json    what worked, what failed and why

Sources, in order of preference:
  1. Apify actors (if APIFY_TOKEN is set) — reliable, residential proxies, paid per result
  2. Open source — instaloader (Instagram), yt-dlp (TikTok, YouTube, Facebook video)
Public data only. No logins.
"""
import csv, datetime as dt, json, os, random, sys, time, traceback, urllib.request

import yaml

ROOT = os.path.dirname(os.path.abspath(__file__))
TODAY = dt.datetime.utcnow().strftime('%Y-%m-%d')
OUT = os.path.join(ROOT, 'data', TODAY)
os.makedirs(OUT, exist_ok=True)

POST_FIELDS = ['client', 'role', 'name', 'platform', 'handle', 'post_id', 'url', 'date', 'format', 'duration_s',
               'views', 'likes', 'comments', 'shares', 'caption', 'hashtags', 'source']
profiles, posts, heatmaps, log = [], [], {}, []


def note(target, platform, source, status, detail=''):
    log.append({'name': target['name'], 'platform': platform, 'source': source, 'status': status, 'detail': str(detail)[:400]})
    print(f"[{status}] {target['name']} / {platform} via {source} {detail if status != 'ok' else ''}"[:300], flush=True)


def tags(text):
    return ' '.join(w for w in (text or '').split() if w.startswith('#'))


def row(t, platform, handle, **k):
    r = {f: '' for f in POST_FIELDS}
    r.update(client=t.get('client', ''), role=t.get('role', ''), name=t['name'], platform=platform, handle=handle)
    r.update({a: b for a, b in k.items() if b is not None})
    r['caption'] = (r['caption'] or '').replace('\n', ' ')[:500]
    r['hashtags'] = tags(r['caption'])
    return r


# ---------------- Apify ----------------
APIFY = os.environ.get('APIFY_TOKEN')
ACTORS = {  # most-used, highest-rated actors (Oct 2026)
    'instagram': 'apify~instagram-scraper',
    'tiktok': 'clockworks~tiktok-scraper',
    'facebook': 'apify~facebook-posts-scraper',
    'youtube': 'streamers~youtube-scraper',
}


def apify_run(actor, payload, timeout=300):
    url = f'https://api.apify.com/v2/acts/{actor}/run-sync-get-dataset-items?token={APIFY}&timeout={timeout}'
    req = urllib.request.Request(url, data=json.dumps(payload).encode(), headers={'Content-Type': 'application/json'})
    with urllib.request.urlopen(req, timeout=timeout + 30) as r:
        return json.loads(r.read())


def apify_collect(t, platform, handle, n):
    if platform == 'instagram':
        items = apify_run(ACTORS[platform], {'directUrls': [f'https://www.instagram.com/{handle}/'], 'resultsType': 'posts', 'resultsLimit': n})
        for it in items:
            posts.append(row(t, platform, handle, post_id=it.get('shortCode'), url=it.get('url'), date=it.get('timestamp'),
                             format=it.get('type'), duration_s=it.get('videoDuration'), views=it.get('videoViewCount') or it.get('videoPlayCount'),
                             likes=it.get('likesCount'), comments=it.get('commentsCount'), caption=it.get('caption'), source='apify'))
        prof = apify_run(ACTORS[platform], {'directUrls': [f'https://www.instagram.com/{handle}/'], 'resultsType': 'details'})
        if prof:
            p = prof[0]
            profiles.append({'name': t['name'], 'platform': platform, 'handle': handle, 'followers': p.get('followersCount'),
                             'following': p.get('followsCount'), 'posts': p.get('postsCount'), 'bio': p.get('biography'), 'source': 'apify'})
    elif platform == 'tiktok':
        items = apify_run(ACTORS[platform], {'profiles': [handle], 'resultsPerPage': n, 'shouldDownloadVideos': False})
        for it in items:
            a = it.get('authorMeta', {})
            posts.append(row(t, platform, handle, post_id=it.get('id'), url=it.get('webVideoUrl'), date=it.get('createTimeISO'), format='video',
                             duration_s=(it.get('videoMeta') or {}).get('duration'), views=it.get('playCount'), likes=it.get('diggCount'),
                             comments=it.get('commentCount'), shares=it.get('shareCount'), caption=it.get('text'), source='apify'))
        if items:
            a = items[0].get('authorMeta', {})
            profiles.append({'name': t['name'], 'platform': platform, 'handle': handle, 'followers': a.get('fans'), 'following': a.get('following'),
                             'posts': a.get('video'), 'likes_total': a.get('heart'), 'bio': a.get('signature'), 'source': 'apify'})
    elif platform == 'facebook':
        items = apify_run(ACTORS[platform], {'startUrls': [{'url': f'https://www.facebook.com/{handle}'}], 'resultsLimit': n})
        for it in items:
            posts.append(row(t, platform, handle, post_id=it.get('postId'), url=it.get('url'), date=it.get('time'), format='post',
                             views=it.get('viewsCount'), likes=it.get('likes'), comments=it.get('comments'), shares=it.get('shares'),
                             caption=it.get('text'), source='apify'))
    elif platform == 'youtube':
        items = apify_run(ACTORS[platform], {'startUrls': [{'url': f'https://www.youtube.com/@{handle}/videos'}], 'maxResults': n})
        for it in items:
            posts.append(row(t, platform, handle, post_id=it.get('id'), url=it.get('url'), date=it.get('date'), format='video',
                             views=it.get('viewCount'), likes=it.get('likes'), comments=it.get('commentsCount'), caption=it.get('title'), source='apify'))
    else:
        raise ValueError(f'no actor for {platform}')


# ---------------- open source ----------------
def instaloader_collect(t, handle, n):
    import instaloader
    L = instaloader.Instaloader(download_pictures=False, download_videos=False, download_video_thumbnails=False,
                                download_comments=False, save_metadata=False, quiet=True, max_connection_attempts=1)
    p = instaloader.Profile.from_username(L.context, handle)
    profiles.append({'name': t['name'], 'platform': 'instagram', 'handle': handle, 'followers': p.followers, 'following': p.followees,
                     'posts': p.mediacount, 'bio': p.biography, 'source': 'instaloader'})
    for i, post in enumerate(p.get_posts()):
        if i >= n:
            break
        posts.append(row(t, 'instagram', handle, post_id=post.shortcode, url=f'https://www.instagram.com/p/{post.shortcode}/',
                         date=post.date_utc.isoformat(), format=post.typename, duration_s=post.video_duration,
                         views=post.video_view_count if post.is_video else None, likes=post.likes, comments=post.comments,
                         caption=post.caption, source='instaloader'))
        time.sleep(random.uniform(5, 12))


def ytdlp_collect(t, platform, handle, n):
    from yt_dlp import YoutubeDL
    url = {'tiktok': f'https://www.tiktok.com/@{handle}', 'youtube': f'https://www.youtube.com/@{handle}/videos',
           'facebook': f'https://www.facebook.com/{handle}/videos'}[platform]
    opts = {'quiet': True, 'skip_download': True, 'playlistend': n, 'ignoreerrors': True, 'sleep_interval_requests': 1}
    with YoutubeDL(opts) as y:
        info = y.extract_info(url, download=False)
    entries = [e for e in (info or {}).get('entries') or [] if e]
    if not entries:
        raise RuntimeError('no entries returned')
    first = entries[0]
    profiles.append({'name': t['name'], 'platform': platform, 'handle': handle,
                     'followers': info.get('channel_follower_count') or first.get('channel_follower_count'),
                     'posts': info.get('playlist_count'), 'bio': info.get('description', '')[:300], 'source': 'yt-dlp'})
    for e in entries[:n]:
        ts = e.get('timestamp') or 0
        posts.append(row(t, platform, handle, post_id=e.get('id'), url=e.get('webpage_url') or e.get('url'),
                         date=dt.datetime.utcfromtimestamp(ts).isoformat() if ts else e.get('upload_date'),
                         format='short' if (e.get('duration') or 0) <= 70 else 'video', duration_s=e.get('duration'),
                         views=e.get('view_count'), likes=e.get('like_count'), comments=e.get('comment_count'),
                         shares=e.get('repost_count'), caption=(e.get('title') or '') + ' ' + (e.get('description') or ''), source='yt-dlp'))
        if platform == 'youtube' and e.get('heatmap'):
            heatmaps[e['id']] = {'title': e.get('title'), 'duration': e.get('duration'), 'heatmap': e['heatmap']}


# ---------------- run ----------------
def main():
    cfg = yaml.safe_load(open(os.path.join(ROOT, 'targets.yml')))
    n = int(os.environ.get('POSTS_PER_ACCOUNT') or cfg.get('posts_per_account', 30))
    mode = os.environ.get('SOURCE_MODE') or cfg.get('source_mode', 'auto')  # auto | apify | open
    for t in cfg['targets']:
        for platform, handle in (t.get('accounts') or {}).items():
            done = False
            if APIFY and mode in ('auto', 'apify'):
                try:
                    apify_collect(t, platform, handle, n); note(t, platform, 'apify', 'ok'); done = True
                except Exception as e:
                    note(t, platform, 'apify', 'fail', e)
            if not done and mode in ('auto', 'open'):
                try:
                    if platform == 'instagram':
                        instaloader_collect(t, handle, n)
                    else:
                        ytdlp_collect(t, platform, handle, n)
                    note(t, platform, 'open-source', 'ok'); done = True
                except Exception as e:
                    note(t, platform, 'open-source', 'fail', f'{type(e).__name__}: {e}')
            time.sleep(random.uniform(2, 5))

    with open(os.path.join(OUT, 'posts.csv'), 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=POST_FIELDS); w.writeheader(); w.writerows(posts)
    for name, obj in (('profiles.json', profiles), ('heatmaps.json', heatmaps), ('run_log.json', log)):
        json.dump(obj, open(os.path.join(OUT, name), 'w'), indent=1, default=str)
    ok = sum(1 for l in log if l['status'] == 'ok')
    print(f'\nDONE {TODAY}: {len(posts)} posts, {len(profiles)} profiles, {len(heatmaps)} heatmaps, {ok}/{len(log)} sources ok')


if __name__ == '__main__':
    main()
