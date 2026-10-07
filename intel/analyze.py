#!/usr/bin/env python3
"""Turn a collector run (posts.csv + profiles.json) into audit metrics.

Usage: python3 analyze.py <run_dir> [--prev <older_run_dir>] [--out audit.md]
Per account: posting rhythm, format mix, median views, engagement rates, outliers
(posts ≥ 2× the account's own median views = what the algorithm pushed), best weekday/hour,
caption length vs performance, hashtag use, and growth vs a previous run.
"""
import argparse, csv, json, os, statistics as st
from collections import Counter, defaultdict
from datetime import datetime


def num(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def parse_date(s):
    if not s:
        return None
    s = str(s).replace('Z', '+00:00')
    for fmt in (None, '%Y%m%d'):
        try:
            return datetime.fromisoformat(s) if fmt is None else datetime.strptime(s, fmt)
        except ValueError:
            continue
    return None


def load(run):
    posts = list(csv.DictReader(open(os.path.join(run, 'posts.csv'))))
    profiles = json.load(open(os.path.join(run, 'profiles.json')))
    log = json.load(open(os.path.join(run, 'run_log.json'))) if os.path.exists(os.path.join(run, 'run_log.json')) else []
    return posts, profiles, log


def account_metrics(rows, followers):
    out = {'n_posts': len(rows)}
    dates = sorted(d for d in (parse_date(r['date']) for r in rows) if d)
    if len(dates) >= 2:
        span_w = max((dates[-1] - dates[0]).days / 7, 1 / 7)
        out['posts_per_week'] = round(len(dates) / span_w, 2)
        out['first_date'], out['last_date'] = dates[0].date().isoformat(), dates[-1].date().isoformat()
        out['days_since_last_post'] = (datetime.now(dates[-1].tzinfo) - dates[-1]).days
    out['format_mix'] = dict(Counter(r['format'] or 'unknown' for r in rows))
    views = [num(r['views']) for r in rows if num(r['views'])]
    likes = [num(r['likes']) or 0 for r in rows]
    comments = [num(r['comments']) or 0 for r in rows]
    if views:
        out['median_views'] = int(st.median(views))
        out['mean_views'] = int(st.mean(views))
        ers = [((num(r['likes']) or 0) + (num(r['comments']) or 0) + (num(r['shares']) or 0)) / num(r['views'])
               for r in rows if num(r['views']) and num(r['likes']) is not None]
        if ers:  # skip when the source returned no engagement fields
            out['median_engagement_per_view_%'] = round(st.median(ers) * 100, 2)
    if followers and any(num(r['likes']) is not None for r in rows):
        out['median_engagement_per_follower_%'] = round(st.median([(l + c) / followers for l, c in zip(likes, comments)]) * 100, 2)
    if followers and views:
        out['median_views_per_follower'] = round(st.median(views) / followers, 2)
    # outliers: what the algorithm pushed beyond the account's normal reach
    base = st.median(views) if views else (st.median(likes) if likes else 0)
    key = 'views' if views else 'likes'
    scored = []
    for r in rows:
        v = num(r[key])
        if v and base:
            scored.append((round(v / base, 2), r))
    scored.sort(key=lambda x: -x[0])
    out['outliers'] = [{'x_median': s, 'url': r['url'], 'date': r['date'][:10], 'format': r['format'], key: r[key],
                        'likes': r['likes'], 'comments': r['comments'], 'caption': r['caption'][:140]} for s, r in scored if s >= 2][:8]
    out['flops'] = [{'x_median': s, 'url': r['url'], 'caption': r['caption'][:100]} for s, r in scored[-3:] if s < 0.5]
    # timing
    by_day, by_hour = defaultdict(list), defaultdict(list)
    for r in rows:
        d, v = parse_date(r['date']), num(r[key])
        if d and v:
            by_day[d.strftime('%a')].append(v); by_hour[d.hour].append(v)
    out['median_by_weekday_utc'] = {k: int(st.median(v)) for k, v in by_day.items()}
    out['median_by_hour_utc'] = {k: int(st.median(v)) for k, v in sorted(by_hour.items())}
    # captions & hashtags
    lens = [(len(r['caption']), num(r[key]) or 0) for r in rows]
    if lens:
        short = [v for l, v in lens if l < 80]; long_ = [v for l, v in lens if l >= 80]
        out['caption_short_vs_long_median'] = [int(st.median(short)) if short else None, int(st.median(long_)) if long_ else None]
    out['top_hashtags'] = Counter(h.lower() for r in rows for h in r['hashtags'].split()).most_common(8)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('run'); ap.add_argument('--prev'); ap.add_argument('--out', default=None)
    a = ap.parse_args()
    posts, profiles, log = load(a.run)
    prev_prof = {(p['name'], p['platform']): p for p in (load(a.prev)[1] if a.prev else [])}
    groups = defaultdict(list)
    for r in posts:
        groups[(r['name'], r['platform'], r['role'], r['handle'])].append(r)
    result = []
    for (name, platform, role, handle), rows in groups.items():
        prof = next((p for p in profiles if p['name'] == name and p['platform'] == platform), {})
        m = account_metrics(rows, num(prof.get('followers')))
        m.update(name=name, platform=platform, role=role, handle=handle, followers=prof.get('followers'), total_posts=prof.get('posts'))
        old = prev_prof.get((name, platform))
        if old and num(old.get('followers')) and num(prof.get('followers')):
            m['follower_growth'] = int(num(prof['followers']) - num(old['followers']))
        result.append(m)
    json.dump({'run': a.run, 'accounts': result, 'log': log}, open(os.path.join(a.run, 'audit.json'), 'w'), indent=1, default=str)

    md = [f"# Audit metrics — {os.path.basename(a.run.rstrip('/'))}", '',
          '| Account | Platform | Role | Followers | Posts/wk | Median views | Eng/view % | Eng/follower % | Outliers ≥2× |',
          '|---|---|---|---|---|---|---|---|---|']
    for m in sorted(result, key=lambda m: (m['role'], m['name'])):
        md.append(f"| {m['name']} | {m['platform']} | {m['role']} | {m.get('followers') or '—'} | {m.get('posts_per_week', '—')} | "
                  f"{m.get('median_views', '—')} | {m.get('median_engagement_per_view_%', '—')} | {m.get('median_engagement_per_follower_%', '—')} | {len(m['outliers'])} |")
    for m in result:
        md += ['', f"## {m['name']} · {m['platform']}", f"Format mix: {m['format_mix']} · last post {m.get('days_since_last_post', '?')} days ago"]
        for o in m['outliers']:
            md.append(f"- **{o['x_median']}×** {o['date']} {o['format']} — {o['caption']} ({o['url']})")
    md += ['', '## Collection log'] + [f"- {l['status']}: {l['name']} / {l['platform']} via {l['source']} {l['detail']}" for l in log]
    text = '\n'.join(md)
    open(a.out or os.path.join(a.run, 'audit.md'), 'w').write(text)
    print(text)


if __name__ == '__main__':
    main()
