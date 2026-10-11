---
name: reference-bank
description: Builds and maintains a client's Reference Bank the way top creative strategists do — a scored list of benchmark creators in the niche (local, regional, global), direct competitors, and out-of-niche "mechanic" sources — then pulls their live data with social-auditor, isolates the outlier posts the algorithm pushed, decodes each into a reusable mechanic (hook, structure, format, visual device, emotion, payoff), counts which mechanics win in this market, and turns them into ideas filtered through the client's own personality so the content is proven but never a copy. Use this skill whenever the user wants references, benchmarks, inspiration, "who should we look at", "what works in this niche", competitor or creator lists, a swipe file, a pattern library, or is starting content for a new client or brand (The Commando, Sparq Study, Ignite Uni, Nova, the founder, Adam & Anas, Mr Rakha or any client).
---

# Reference Bank

Great creative work is proven mechanics + a personality nobody else has. This skill supplies the proven mechanics (from real numbers) and forces every idea through the client's personality before it leaves.

## 1. Build the list (per client, 12–20 accounts)
| Tier | What | How many | Example (Mr Rakha) |
|---|---|---|---|
| **A. Direct competitors** | same offer, same audience, same city | 3–5 | Assem El Nady, other Cairo IGCSE Business/Econ tutors |
| **B. Niche benchmarks** | same subject or audience, any country, clearly winning | 4–6 | EconplusDal, tutor2u, Economics Explained |
| **C. Local style benchmarks** | same culture/language, any niche, great at personality and storytelling | 2–4 | El Da7ee7 (Egyptian edutainment) |
| **D. Mechanic sources** | out-of-niche creators whose formats can be transplanted | 2–4 | finance explainers, business breakdown channels, documentary-style shorts |
Find candidates with web search, platform search terms the avatar would type, "similar accounts", and the founder's own suggestions. **Score each 1–5** on: audience overlap · performance (outlier frequency) · format transferability · personality strength · recency (posting in the last 30 days). Keep ≥ 3.5 average. Record handles per platform.

## 2. Collect live data
Hand the list to **social-auditor** (writes `intel/targets.yml`: `client`, `role: competitor|benchmark`, accounts). After the run, read `audit.md` and `posts.csv`.

## 3. Find what works (outliers, not averages)
- For each account, take posts ≥ 2× its own median views (or likes when views are missing). These are what the algorithm and audience chose.
- For YouTube benchmarks, read the "most replayed" peaks (retention-lab `heat` mode) — the exact moments people rewatch.
- Watch/inspect each outlier (open the link) and fill one **Mechanic card**:
```
MECHANIC — [account] · [platform] · [date] · [x× median] · [link]
Hook (first 3 s): words + visual        | Hook type: question / bold claim / story / POV / list / visual shock / contrast
Structure: e.g. claim → proof → twist → payoff → loop
Format: talking head / board / voice-over B-roll / skit / screen record / carousel / interview
Visual device: e.g. object on table, whiteboard reveal, number on screen, split screen
Emotion: curiosity / status / fear of losing marks / humour / awe / relief
Payoff: what the viewer gets (a rule, a reveal, a laugh)
Why it worked (1 line) | Transferable to client? yes/no + why
```
- With many posts, label them at scale (Jev via social-auditor) and **count**: which hook types, formats and lengths over-index among outliers vs all posts. Patterns need ≥ 3 examples.

## 4. Personality transform (the part that makes it ours)
For each winning mechanic, write 2–3 ideas that pass all four filters:
1. **Persona** — sounds and looks like the client (brand-persona Mode B; e.g., Rakha = the Analyst: calm, witty, Lucifer-level charm, Whisky Lounge look, "Business, explained like it matters.").
2. **Signature** — uses at least one client signature (board word, "…and that's how it's examined", the signet, the Brief number).
3. **Distance** — not recognisable as the source; swap at least topic, setting and payoff (idea-elevator rule).
4. **Avatar** — targets one primary avatar and a pillar from the Strategy Plan.
Then send ideas to `idea-elevator` / `twist-lab` for upgrading and `commando-content-studio` for production.

## 5. Save and refresh
Save as Claude Doc `[Brand] — Reference Bank`: the scored list (with links), Mechanic cards, pattern counts, the ideas with their source mechanic, and "do not copy" notes. Refresh monthly (re-run social-auditor; drop accounts that went quiet; add new outliers). Feed the patterns into strategy-partner's monthly plan.

## Rules
- Study, decode, transform — never re-post, re-voice or closely imitate someone's content.
- Credit inspiration internally; never publicly name competitors in client content.
- Numbers come from social-auditor runs (dated); if a source failed, say so.
