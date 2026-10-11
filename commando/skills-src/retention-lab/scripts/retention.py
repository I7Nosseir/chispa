#!/usr/bin/env python3
"""Retention timeline analysis.

Two inputs:
  own  — your video's retention curve: CSV with columns  t,retention  (t in seconds or % of video,
         retention in % of viewers still watching; from YouTube Studio export, or points read off a
         TikTok/Instagram retention screenshot). Optional --beats CSV: t,beat  (script/edit beats).
  heat — public YouTube "most replayed" heatmaps.json from the collector (benchmark videos).

Usage:
  python3 retention.py own curve.csv --duration 45 [--beats beats.csv] [--name "Brief 01"] [--png out.png]
  python3 retention.py heat intel/data/<date>/heatmaps.json [--top 5]

Finds: hook hold (3 s / 5 s), the steepest drops (where people leave), spikes (rewatch / re-engage
moments), the 50% point, end retention, and maps each event to the nearest beat.
"""
import argparse, csv, json, statistics as st


def interp(points, t):
    for (t0, r0), (t1, r1) in zip(points, points[1:]):
        if t0 <= t <= t1:
            return r0 + (r1 - r0) * ((t - t0) / (t1 - t0) if t1 > t0 else 0)
    return points[-1][1] if t > points[-1][0] else points[0][1]


def events(points, beats=None, k=3):
    slopes = [((t1 + t0) / 2, (r1 - r0) / max(t1 - t0, 1e-6), t0, t1, r0, r1) for (t0, r0), (t1, r1) in zip(points, points[1:])]
    drops = sorted([s for s in slopes if s[1] < 0], key=lambda s: s[1])[:k]
    spikes = sorted([s for s in slopes if s[1] > 0], key=lambda s: -s[1])[:k]
    def near(t):
        if not beats:
            return ''
        b = min(beats, key=lambda b: abs(b[0] - t))
        return f'  ← beat @{b[0]:g}s: "{b[1]}"'
    return ([f'DROP {s[2]:g}–{s[3]:g}s: {s[4]:.0f}% → {s[5]:.0f}% ({s[1]:.1f} pts/s){near(s[0])}' for s in drops],
            [f'SPIKE {s[2]:g}–{s[3]:g}s: {s[4]:.0f}% → {s[5]:.0f}% (+{s[1]:.1f} pts/s, rewatch/skip-back){near(s[0])}' for s in spikes])


def own(a):
    pts = [(float(r['t']), float(r['retention'])) for r in csv.DictReader(open(a.csv))]
    pts.sort()
    if a.percent:
        pts = [(t / 100 * a.duration, r) for t, r in pts]
    beats = [(float(r['t']), r['beat']) for r in csv.DictReader(open(a.beats))] if a.beats else None
    dur = a.duration or pts[-1][0]
    half = next((t for t, r in pts if r <= 50), None)
    rep = [f'# Retention — {a.name}', '',
           f'- Hook hold: {interp(pts, 3):.0f}% at 3 s · {interp(pts, 5):.0f}% at 5 s',
           f'- Mid: {interp(pts, dur / 2):.0f}% at 50% of the video · half the audience gone by {half if half is not None else ">end"} s',
           f'- End: {pts[-1][1]:.0f}% still watching at {pts[-1][0]:g} s (of {dur:g} s)',
           f'- Area under curve (avg % watched): {st.mean(interp(pts, dur * i / 100) for i in range(101)):.0f}%']
    d, s = events(pts, beats)
    rep += ['', '## Where people leave'] + [f'- {x}' for x in d] + ['', '## Where people re-engage'] + [f'- {x}' for x in s]
    print('\n'.join(rep))
    if a.png:
        plot(pts, beats, a.png, a.name, dur)


def plot(pts, beats, path, title, dur):
    from PIL import Image, ImageDraw
    W, H, P = 1200, 520, 60
    im = Image.new('RGB', (W, H), '#FFFFFF'); d = ImageDraw.Draw(im)
    X = lambda t: P + (W - 2 * P) * t / dur
    Y = lambda r: H - P - (H - 2 * P) * max(0, min(r, 120)) / 120
    for g in (0, 25, 50, 75, 100):
        d.line([(P, Y(g)), (W - P, Y(g))], fill='#EEEEEE'); d.text((10, Y(g) - 6), f'{g}%', fill='#888888')
    d.line([(X(t), Y(r)) for t, r in pts], fill='#8B4A2B', width=4)
    for t, b in beats or []:
        d.line([(X(t), P), (X(t), H - P)], fill='#C69B3C'); d.text((X(t) + 3, P - 18), b[:22], fill='#555555')
    d.text((P, 14), title, fill='#111111'); im.save(path)


def heat(a):
    data = json.load(open(a.json))
    for vid, v in list(data.items())[: a.top]:
        hm = v['heatmap']
        pts = [((h['start_time'] + h['end_time']) / 2, h['value']) for h in hm]
        vals = [p[1] for p in pts]
        thr = st.mean(vals) + 0.6 * st.pstdev(vals)
        peaks = [(t, val) for (t, val), prev, nxt in zip(pts[1:-1], vals[:-2], vals[2:]) if val >= thr and val >= prev and val >= nxt]
        intro = st.mean(vals[: max(1, len(vals) // 20)])
        print(f"\n## {v.get('title')} ({v.get('duration')} s) — https://youtu.be/{vid}")
        print(f'- Intro intensity {intro:.2f} vs video mean {st.mean(vals):.2f} (high intro = people skip back to the hook)')
        for t, val in sorted(peaks, key=lambda p: -p[1])[:4]:
            print(f'- MOST REPLAYED @ {int(t // 60)}:{int(t % 60):02d} (intensity {val:.2f}) → open the video here and decode what happens')


if __name__ == '__main__':
    ap = argparse.ArgumentParser(); sub = ap.add_subparsers(dest='mode', required=True)
    o = sub.add_parser('own'); o.add_argument('csv'); o.add_argument('--duration', type=float, default=0)
    o.add_argument('--percent', action='store_true', help='t column is % of video'); o.add_argument('--beats')
    o.add_argument('--name', default='video'); o.add_argument('--png')
    h = sub.add_parser('heat'); h.add_argument('json'); h.add_argument('--top', type=int, default=5)
    a = ap.parse_args()
    own(a) if a.mode == 'own' else heat(a)
