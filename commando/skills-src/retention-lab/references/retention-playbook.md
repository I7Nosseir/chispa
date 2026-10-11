# Retention playbook

## 1. Curve shapes and what they mean
| Shape | Meaning | Usual fix |
|---|---|---|
| Cliff in 0–2 s | first frame / first word didn't stop the scroll | start mid-action; text hook on frame 1; no logo/intro; movement or face in frame 1 |
| Steady slide 3–10 s | hook promised something but payoff feels far | pay part of the promise within 5–8 s; tighten pauses; cut setup |
| Sudden drop at a topic change | curiosity loop closed too early, nothing new opened | open the next question before closing the last ("…but that's not the weird part") |
| Drop when a graphic/slide appears | dense or static moment | animate, simplify, voice-over the key line, ≤ 2 s static |
| Spike (curve rises) | viewers skipped back → rewatch moment | do more of it: reveals, dense visual, punchline, number on screen |
| Flat high plateau | strong narrative tension | keep that structure as a template |
| End bump / >100% at start | loop rewatches | ending that flows into the opening line |
| Gentle slope to the end, low start | wrong audience reached (cold traffic) | check traffic source: niche hook, clearer topic in first line |

## 2. Rules of thumb (directional, compare with your own medians first)
- Short-form: aim for 3 s hold ≥ ~70% and average % watched ≥ ~50% (≤ 30 s videos higher). Track your own baseline; improvement matters more than any universal number.
- Long-form YouTube: the first 30 s decides; 2–3 "re-hooks" per 10 min.
- Instagram skip rate: lower is better; compare each reel to your own average skip rate shown in insights.

## 3. Algorithm states (from traffic sources + follower split)
| State | Signals | Read | Action |
|---|---|---|---|
| Not tested | most views from followers/profile; tiny For You / Reels-tab share | platform hasn't shown it to cold viewers yet, or account is new | keep posting consistently; stronger first frame |
| Tested and rejected | short burst of non-follower views then flat; low hold | cold viewers swiped — hook or topic mismatch | rework hook; test same topic with a new first 3 s |
| Pushed | high For You / Reels / Explore share, non-follower views climbing for days | retention + shares/saves passed the test | make 2–3 follow-ups on the same mechanic within a week |
| Searchable | search share growing over weeks | evergreen demand | title/caption/on-screen keywords; series it |
| Shared | high shares vs likes; DMs | identity / utility content ("send this to…") | design more "send-to-a-friend" moments |
Signals each platform rewards (2026, public statements and creator consensus): watch time and completion, rewatches, shares (especially DM sends), saves, comments, follows from the video; Instagram separates "connected" (followers) and "unconnected" reach; TikTok tests every video on a small cold audience first; YouTube Shorts weighs "viewed vs swiped away".

## 4. Beat mapping template (`beats.csv`)
```
t,beat
0,first frame + on-screen hook
3,first spoken line
8,first payoff
...
```
Use the editor's export timestamps, not the script draft.

## 5. Drop-off library columns
date · brand · platform · video · duration · 3 s hold · avg % watched · biggest leak (t, cause) · best moment (t, what) · traffic state · non-follower % · shares · saves · rule learned
