---
name: retention-lab
description: Analyses video timelines the way top creators do — the audience-retention curve second by second (where viewers leave, where they rewatch or skip back), hook hold at 3 s and 5 s, the 50% point and end retention, mapped to the exact script beat or edit at that moment — plus traffic sources and algorithm signals (For You / Reels tab / Explore / search / profile / shares, followers vs non-followers, watch time, skip rate) to explain why a video was or wasn't pushed, and benchmarks against public "most replayed" heatmaps of top creators' videos. Tracks every video in a drop-off library so recurring mistakes and winning moments become rules for the next script. Use this skill whenever the user shares a retention graph, analytics or insights screenshot, says "why did this flop / blow up", "where did people leave", "watch time", "skip rate", "traffic source", "algorithm", or wants to improve videos for any Commando brand, the founder, Adam & Anas, Mr Rakha or a client.
---

# Retention Lab

Every drop on the curve is a viewer saying "this moment lost me"; every bump is "I went back for that". The job is to name the moment, find the cause, and turn it into a rule for the next video.

## Inputs
- **Own videos (private analytics):** screenshots or exports from YouTube Studio (Audience retention — export as CSV in Advanced mode; Traffic sources), TikTok Studio (retention graph, average watch time, watched full video, traffic sources: For You / Following / Profile / Search / Sound), Instagram professional dashboard (Reels: skip rate, average watch time, retention graph, views from followers vs non-followers, where views came from: Reels tab / Explore / Profile / Feed / Stories), Facebook (Reels/video retention).
- **The script and edit:** the final script with timestamps (from commando-content-studio / production-docs) → `beats.csv` (`t,beat`).
- **Benchmarks:** public YouTube "most replayed" heatmaps collected by social-auditor (`heatmaps.json`) for reference-bank creators.

## Pipeline
1. **Digitise the curve.** CSV export → use directly. Screenshot → read it carefully (Read the image) and record points at 0,1,2,3,5,8 s, then every ~10% of the duration, plus every visible bump or cliff: `t,retention`. Note the axis (seconds or %), and state reading accuracy (±3 pts).
2. **Run the analysis:**
   `python3 scripts/retention.py own curve.csv --duration <s> --beats beats.csv --name "<video>" --png curve.png`
   → hook hold (3 s / 5 s), half-audience point, end retention, average % watched, top drops and spikes, each mapped to the nearest beat; a chart with beats marked.
3. **Diagnose each event** with the cause table in `references/retention-playbook.md` (e.g., drop at 0–2 s = visual/first-frame problem; drop right after the hook = promise not paid quickly; mid cliff at a topic change = lost curiosity loop; spike = rewatch of a dense or surprising moment → do more of that; end bump = loop/rewatch).
4. **Read the algorithm signals.** From traffic sources and follower split decide which of four states the video is in (playbook §3): *not tested* (few non-follower views), *tested and rejected* (non-follower test then flat — hook/hold failed), *pushed* (high For You/Reels share, rising non-followers), *searchable* (search share growing — long-tail). Explain it in one line the founder can act on.
5. **Benchmark.** For the same format, compare hook hold and average % watched against the brand's own median (Performance Log) and, where available, the benchmark creators' heatmaps (`retention.py heat heatmaps.json`): where their most-replayed moments sit (often the payoff, a reveal, or a dense visual) — copy the *mechanic*, not the content.
6. **Write the verdict** (≤ 10 lines): the 1 biggest leak with timestamp and cause, the 1 moment to repeat, 3 concrete edits/script rules for the next video, and the algorithm state. Add the video to the **Drop-off Library** in the brand's Performance Log doc (`[Brand] — Performance Log`): date · video · hook hold 3 s · avg % watched · biggest leak (t, cause) · best moment (t) · traffic state · rule learned.
7. **Close the loop.** Rules that repeat in 3+ videos become standing rules: hand them to commando-content-studio (script rules), cringe-filter/senior-reviewer (checks), and strategy-partner (format decisions).

## Notes
- Compare like with like: short (<60 s) vs long; same platform; same format.
- Small samples lie: one video is a hint, five are a pattern.
- Retention beats views: a 3,000-view video with 70% avg watched is a better template than a lucky 50K with 20%.
- Platforms change what they show; record exactly which metrics were available with each entry.
