---
name: social-auditor
description: Pulls real, live public data from Instagram, TikTok, Facebook, YouTube (and X) for any list of accounts — clients, competitors, benchmark creators — through Apify actors or free open-source collectors running on GitHub Actions, then audits it — posting rhythm, format mix, median views, engagement rates, outlier posts the algorithm pushed (≥2× the account's own median), flops, timing, captions, hashtags, growth since the last run — and optionally labels every post at scale with Jev (hook type, format, pillar, CTA). Use this skill whenever the user wants real numbers about any social account, a social media audit, competitor data, "what's working for X", follower or view counts, a benchmark comparison, live tracking, or data for competitor-scanner, reference-bank, retention-lab or performance-tracker — for The Commando, Sparq Study, Ignite Uni, Nova, the founder, Adam & Anas, Mr Rakha or any client.
---

# Social Auditor

Turns "I think they're doing well" into numbers. Public data only, no logins — the founder's own accounts are read from their insights instead (performance-tracker / retention-lab).

## Where the data comes from
This cloud session cannot reach social platforms, so collection runs outside it:

| Route | When | How |
|---|---|---|
| **GitHub Actions collector** (repo `I7Nosseir/chispa`, folder `intel/`, branch `claude/elegant-brown-yt0vko`) | scheduled tracking + saved history | Edit `intel/targets.yml`, push → workflow `intel-collect` runs → commits `intel/data/<date>/` (posts.csv, profiles.json, heatmaps.json, run_log.json). Uses Apify automatically when the repo secret `APIFY_TOKEN` exists; otherwise instaloader + yt-dlp. |
| **Apify MCP connector** (tools `mcp__APIFY__*`; verified 7 Oct 2026) | **default for audits inside a chat** | `call-actor` with `waitSecs: 0` for each scrape in parallel → `get-actor-run` (waitSecs 45) → `get-dataset-items` with `fields=` to keep context small. Always set `callOptions.maxItems` to cap cost. Inputs that work: Instagram profile stats `apify/instagram-scraper` {directUrls:[profile URLs], resultsType:"details"}; posts {directUrls, resultsType:"posts", resultsLimit:30}; TikTok `clockworks/tiktok-scraper` {profiles:[usernames], resultsPerPage:30, profileScrapeSections:["videos"], profileSorting:"latest"}; Facebook `apify/facebook-posts-scraper`; YouTube `streamers/youtube-scraper`. Check `fetch-actor-details` (inputSchema + pricing) before a new actor. |
| **Screenshots** | anything else | The user pastes profile/insight screenshots; read them and enter the numbers. |

Read `references/sources-and-costs.md` for every tool's status, limits, workarounds and Apify pricing at scale.

## Pipeline
1. **Targets.** Load the client's Reference Bank doc (reference-bank skill) or ask: which accounts, which platforms, role (client / competitor / benchmark). Write them into `intel/targets.yml` (`client`, `role`, `accounts: {platform: handle}`), keeping existing targets.
2. **Collect.** Commit + push (`git push -u origin claude/elegant-brown-yt0vko`). Free open-source mode is blocked by Instagram/TikTok/YouTube from GitHub's datacenter IPs (tested 7 Oct 2026; only YouTube list mode works) — use Apify for real audits. Watch the run with the GitHub MCP tools (`actions_list` → `list_workflow_runs`, `get_job_logs`). When it finishes: `git pull`. Read `run_log.json` first — report every failed source honestly and switch route (Apify, screenshots) rather than guessing numbers.
3. **Analyse.** `python3 scripts/analyze.py intel/data/<date> [--prev intel/data/<older>]` → `audit.md` + `audit.json` per account: followers, posts/week, format mix, median views, engagement per view and per follower, outliers (≥2× own median), flops, weekday/hour medians (UTC — add 3h for Cairo), caption length effect, top hashtags, growth vs previous run.
4. **Label at scale (optional).** For every post, answer the same small questions — hook type (question / bold claim / story / POV / list / visual shock), format (talking head / voice-over / skit / screen record / carousel / B-roll montage), pillar, CTA present, language, face on screen. Use **Jev** (TypeSafe, typed decisions, ~$0.04 per million input tokens; early-access key in `JEV_API_KEY`) when available — see the reference for the request shape; otherwise label with Claude in batches of 25. Store labels next to the posts so patterns can be counted, not guessed.
5. **Read the patterns** (what a senior strategist would say): which formats and hooks over-index among outliers; what the flops share; rhythm vs results; what the audience rewards with comments (conversation) vs likes (approval) vs shares (identity). Always compare an account to **itself** first (outlier ratio), then to others.
6. **Report.** Save as `[Brand] — Social Audit [date]` (Claude Doc) or append to the Competitor Scan doc: summary in 5 lines, the metrics table, top outliers with links and why they worked, gaps to exploit, 3 decisions. Hand outliers to `reference-bank` and `idea-elevator`, the data to `competitor-scanner`, own-account numbers to `performance-tracker`.

## Rules
- Public, business/creator accounts only; never collect private individuals' data beyond what a post publicly shows; never log in with scripts.
- Date every number; follower counts are snapshots.
- Don't copy content — decode the mechanic (reference-bank does that).
- Keep cost visible: estimate results × price before big Apify runs (reference file).
