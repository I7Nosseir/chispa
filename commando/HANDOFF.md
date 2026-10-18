# Commando OS: handoff (updated 17 Oct 2026)

The founder runs The Commando (Sparq Study, Ignite Uni, Nova). He doesn't code. This file is the single record of the work done with Claude since 7 Oct 2026. Read it first in any new chat.

## Where things live
- Repo `I7Nosseir/chispa`, branch `claude/elegant-brown-yt0vko` (the Vite app itself is untouched).
  - `commando/skills-src/`: source of the new skills. `commando/skills-packaged/*.skill`: ready to upload in claude.ai Settings → Skills.
  - `commando/clients/rakha/`: colour, logo, board, design (build.mjs + rendered PNGs) and PDFs.
  - `commando/clients/la-margrita/`: prospect audit and call notes.
  - `commando/leads/`: calling list (`leads-2026-10-11.xlsx` + `.csv`), `calling-playbook.md`, and `build_leads.py` (rebuilds the sheet).
  - `intel/`: GitHub Actions collector (collect.py, analyze.py, targets.yml, workflow `.github/workflows/intel-collect.yml`) and dated data in `intel/data/<date>/`.
- Claude Docs (living documents on claude.ai):
  | Doc | id |
  |---|---|
  | Mr Rakha: Competitor Scan | 692ae1fd-021b-42f8-ad8c-1b1e10b30dad |
  | Mr Rakha: Market Brief | 279efbbd-a10f-45de-9692-c07f3784c973 |
  | Mr Rakha: Avatar Pack | c46377bd-6b14-46ec-9dc0-c14f6c7bd391 |
  | Mr Rakha: Brand Book & Profile Kit | 9e0fde23-77fb-4620-a6cf-4da366b3c9fd |
  | Mr Rakha: Strategy Plan | 9ac8830b-5961-4e29-bdc7-7a150e380d2e |
  | Mr Rakha: Reference Bank | 3762bce2-630c-49c8-9393-47449ac6eef0 |
  | Mr Rakha: Shoot Day 1 Production Pack | cff76cbf-3d92-464d-ab17-ed628702be4e (https://claude.ai/code/artifact/cff76cbf-3d92-464d-ab17-ed628702be4e) |

## Connectors and tools
- **Apify MCP** (connected). Default route for live social data. Free plan includes $5/month of usage; Starter is $29.
  - Actors that work:
    - `apify/instagram-scraper` ({directUrls, resultsType: posts|details})
    - `clockworks/tiktok-scraper` ({profiles, resultsPerPage, profileScrapeSections:["videos"]} or {searchQueries})
    - `apify/facebook-posts-scraper` ({startUrls:[{url}], resultsLimit})
    - `compass/crawler-google-places` ({searchStringsArray, locationQuery, maxReviews})
  - Always cap with callOptions maxItems / maxTotalChargeUsd and fetch with `fields=`.
- GitHub Actions collector: blocked by Instagram/TikTok from datacenter IPs. Use Apify. An `APIFY_TOKEN` repo secret lets the workflow use Apify too. Never ask for the token in chat.
- Jev (TypeSafe AI post labelling): parked; waitlist.
- Posting: decided Buffer Free for the La Margrita trial; Metricool Starter (one-click connector, ~$20–25/month for 5 brands) once Rakha's accounts are live. Analytics stay on Apify.
- Weekly tracking: skipped for now (founder's call).
- Personal use only: never sold as a service.

## Skills built (upload the .skill files to keep them)
- **color-system:** OKLCH and WCAG gates, colour-blind check, 60-30-10 rule; script `palette_check.py`.
- **logo-system:** JSON spec → outlined SVG; tests at 16px, one colour, blur and avatar crop.
- **brand-board:** Nova-style board builder.
- **social-auditor:** live data, then outliers (≥2× the account's own median), flops and timing.
- **retention-lab:** retention curves, drop-offs and traffic sources.
- **reference-bank:** benchmarks and competitors → mechanics → ideas with the client's personality.
- **ai-video-prompt-engineering** (the founder's own skill, merged and extended 11 Oct):
  - His core is unchanged: beat formula, atomic actions, exact counts, identity/product lock, add/replace/already-there, calm verbs, ring/halo guard, audio, negative checklist, brand safety, model choice, story beats.
  - His lessons log is kept and grows over time.
  - Added: §0 workflow with a realism card; §14 realism QA gate + finishing; §15 rules and disclosure.
  - Added references: realism playbook, prompt library in beat format (perfume, abaya, jewelry, skincare, food, product reveal, UGC, B-roll, concept, character sheet), tool matrix.
  - Added scripts:
    - `prompt_lint.py` checks prompts against his rules; it catches every logged failure.
    - `contact_sheet.py` makes QA frame sheets.
    - `realism_finish.py` applies phone/cinema/still presets.
  - The interim ai-realism-studio was folded into it and deleted.
- **commando-hq:** routing updated for all of the above (+ AI production pipeline).

## Client 1: Mr Mohamed Rakha (free; Sparq's first teacher)
- **Who he is:**
  - IGCSE Business and IGCSE/O-level Economics teacher, 10+ years.
  - Teaches at his own center, online, and part-time at several schools. **Never name, show or hint at the schools.**
  - Bald, groomed beard, charming and witty. Hesitant on camera; speaks Egyptian Arabic.
- **Brand:**
  - Uses his own name, @mrrakha. Analyst persona. Tagline "Business, explained like it matters."
  - Whisky Lounge palette: base #141112, bone #F2E8D8, cognac #8B4A2B, gold #C69B3C, taupe #8A8580.
  - Signet "R" logo. Fonts: Cormorant Garamond + Inter (Caveat for handwriting).
- **Strategy:**
  - IG + FB + TikTok cross-posted. Phases: authority → demand → Sparq later.
  - Value-first, classy, never pushy. Audience: students and parents.
  - One shoot day a month, at his own center only.
- **Rules:**
  - Never grade-shame.
  - Avoid "Think Business" (Karim Ashmawy, Marwa Sadek) and "more than teaching" (Mohamed Saeed).
  - Show, don't claim.
  - The logo never goes at the end of a video.
- **Intel:**
  - Assem El Nady's top TikToks are music montages (no speech).
  - Marwa Sadek launched the same "real world" claim on 8 Oct 2026.
  - Benchmarks: Dr Amr Hady, Hayssam Hamouda.
- **Delivered:**
  - All the docs above.
  - Shoot Day 1 pack: 4 explainers (cinema Pepsi / monopoly, delivery fees / price elasticity, gold / inflation, White Friday / anchoring), 2 exam reels, pin-video plan, consent form.
  - Carousels "0264" (6 slides; the 0450→0264 syllabus change, first exams March 2027) and "The Margin" (7 slides; 4/6 → 6/6 answer).
  - Profile photo and Facebook cover.
- **Open items:**
  - Rakha approves the scripts (⚠️ Arabic lines), consent form and outfit 2 days before the shoot.
  - Check the 0264 facts against the Cambridge syllabus.
  - Answer the 6 open questions: shoot date, format/seats, price, verified results, A-level?, who answers WhatsApp.
  - The founder creates the accounts.
  - Save Rakha into the commando-profiles skill.

## Prospect 2: La Margrita (Neapolitan pizza, Pyramids Gardens)
See `commando/clients/la-margrita/audit-2026-10-11.md`. In short:
- 175K on TikTok, but a ~7K median. One 13.7M viral clip and no brand behind it.
- Four different names, typos, a broken phone number, defensive review replies.
- Offer: a free month of content, then a paid retainer. Packaging and logistics are the paid phase 2.
- First call on 11 Oct 2026.
- Call outcome (reported 17 Oct): they want to go **local**, reaching everyday people and leaving premium to the big brands.
  - The content direction was rewritten around Hamza, street reactions, visible value and neighbourhood moments ("Local direction" in the audit).
  - Next: send the free-month scope and book shoot day 1.

## Lead list: 100 businesses to call (11 Oct 2026)
- Files: `commando/leads/leads-2026-10-11.xlsx`.
  - Sheets: Leads, Summary, Call playbook.
  - A CSV copy sits next to it. `calling-playbook.md` is the script and the rules.
- Source:
  - Google Maps via Apify (`compass/crawler-google-places`, 6 runs, ~214 places).
  - Areas: Sheikh Zayed, 6th of October, Hadayek al Ahram/Haram, New Cairo, Maadi.
  - Cost about $1.30 of the $5 free credit ($0.004/place + $0.002 contacts add-on).
- Excluded (founder's call): education/IGCSE centers and schools. Also excluded: chains/franchises, hotel restaurants, and listings without a phone.
- Mix: 19 dental, 12 derma, 11 physio, 21 gyms, 18 beauty, 13 restaurants, 3 real estate, 2 padel, 1 café.
- Tiers: A high-paying 20 · B mid 57 · C low/quick win 23. Sorted A→C, then by Need × Ability.
- Strongest openers (verified gaps):
  - Enhanced Dental: the Google "website" is a Google Form; 274 reviews at 5.0.
  - La Vida Dental: the listing links a different name's Instagram, and its reviews are split with "The Dental Room".
  - Air Gym / H2O Gym: name mismatch.
  - Mira Dental: the "website" is its Yellow Pages profile.
  - Big Maadi restaurants (Lucille's, Carmel, Bistro Paris) have no website on their listings.
- "No socials linked" means none on Google or their site. Search their name before calling.
- Next:
  - The founder calls Tier A and logs Status/Call notes/Follow-up in the sheet.
  - Bring outcomes back; Claude updates the sheet, drafts follow-ups and picks the next niche.
  - Prices in the sheet are the PROPOSED ranges from commando-profiles. Confirm before quoting.

## Gulf leads + remote jobs (11 Oct 2026)
- File: `commando/leads/gulf-leads-and-jobs-2026-10-11.xlsx`.
  - Sheets: Gulf leads (Dubai), Remote jobs, Fair pricing, Where to look weekly.
  - Also: a CSV copy, `gulf-and-jobs-playbook.md` (approach), and `build_gulf.py`.
- 56 Dubai leads, from one Apify run (80 places) with chains removed:
  - Niches: perfume, abaya, jewelry, skincare, aesthetic, dental, real estate, fitness, coffee, restaurants.
  - Tiers: A 7 · B 33 · C 16.
- Apify free credit is spent ($0.45 left). Saudi (Riyadh, Jeddah) and Doha weren't run; do them when the credit resets or on Starter ($29).
- 14 remote/Gulf jobs from web search. Best fits: Whitecollars Senior Media Buyer (part-time, UAE e-com, Egypt-based) and Malaeb Media Buyer (remote).
- Founder adds AI content creation (images, video, product shoots, AI UGC) plus websites/apps to the services. Update the Freelance Services profile.
- Portfolio (Canva):
  - Final: "Ismail Nosseir Portfolio", design DAHXtLwdPTk, 39 slides, saved 11 Oct.
  - His original 66-slide "Ismail Nosseir Portofolio" (DAHXtGreyQI) is untouched.
  - Changes in the final:
    - Removed 27 empty campaign slides.
    - New headline "Performance Marketer & AI Content Creator".
    - Home address removed.
    - Ignite 157 users; Sparq described correctly; Novax renamed NovaxOps.
    - Typos fixed; no Rakha content.
  - Open:
    - Resolved 17 Oct: Rihla spend is 54,822 EGP (18 campaigns, 2,747 leads, 19.96 EGP CPL). It is now on the CV.
    - "Promoting Website" and AFCON share identical stats.
    - The AI video slides need watch links (a PDF can't play video).
    - Fix: share the Canva link instead of a PDF; videos play there. The Canva tools can't change share settings, so the founder does it once: Share → Share link → Anyone with the link → Can view.
    - Final view link: canva.com/d/fDOo1enlio7FeO9. The CV now uses it; the old CV link hHAmPiW466qMtnH matched neither design.
- CV: final 2-page PDF at commando/portfolio/Ismail-Nosseir-CV.pdf (source cv.html).
  - Rihla start date confirmed as Jan 2026.
  - Tutoring lines removed at the founder's request.
  - Rihla line added 17 Oct: 54,822 EGP across 18 campaigns, 2,747 leads at 19.96 EGP. The Grapes total stays off.
  - Claude's own drafts in commando/portfolio/ are superseded; use his.

## Command Center (17 Oct 2026)
- Page: https://claude.ai/artifact/9dUi5FVtR34gyXo6Rdv1y1 (source `commando/command-center/`, rebuild with `python3 build.py`).
  - Tabs: Report (phase by phase), Businesses (156 leads + 2 clients, filters, per-lead status saved in the browser), Copy kit, Approach, Forecast.
  - Each lead has: a warm note, a warm call opener, day-3 and day-8 follow-ups, and an AI audit prompt. Gulf product brands get a sample-first message and an AI image prompt instead.
- Files: `report.md` (boss report + 90-day forecast), `approach.md` (warm ladder: look → engage → give first → call only after a reply), `directory.md` (every business with location, niche, key fact).
- Forecast (realistic, day 90): 2–3 Egypt retainers (~15–30K EGP/month) + 1 website/shoot project + 1 Gulf pilot. Capacity cap is about 4 retainers while studying.
- Still open: the La Margrita call outcome isn't logged; prices are still proposals; Rakha approvals; CV number conflict; Apify credit (monthly refill or Starter $29).

## Report pack (17 Oct 2026)
Files in `commando/reports/`:
Built by a parallel session on the same day as the Command Center above. The Command Center is the main interactive page; these are plain-file copies plus a fuller prompt kit.
- `boss-report-2026-10-17.md`: everything done from 7 to 17 Oct, phase by phase, with what was found, the costs, the open items and the forecast.
  - Month 1, base case: 2 Egypt clients + 1 Gulf pilot ≈ 40–45K EGP cash in (first projects).
  - Month 3: aligned with the Command Center (2–4 Egypt retainers ≈ 15–40K EGP/month + 1–2 Gulf pilots, cap about 4 retainers while studying).
  - Assumes about 50 EGP per $1 and the proposed prices.
- The Command Center report's niche mix was corrected to the lead file's real counts (dental 19, restaurants 13).
- `all-businesses-2026-10-17.md`: all 156 leads (100 Egypt + 56 Dubai) with area, niche and one key fact.
- `how-to-approach-simple.md`: one page on how to sound warm, not like a cold caller. It covers the 4-step call, Gulf message-first, the warm vs cold table, and the daily rhythm.
- `copy-paste-kit.html` (rebuilt by `build_copy_kit.py`, which reads the prompt library and the Mayura sample):
  - 20 AI prompts and 15 outreach messages, each with a copy button.
  - Published privately at https://claude.ai/artifact/5GUiAH9AJKA1bZkrLKDSEh.
- Still waiting on the founder:
  - the first calls
  - the La Margrita call outcome
  - portfolio sharing and Watch links
  - the Rihla/Grapes spend number
  - a real product photo for the first Gulf sample
  - the Rakha items

## Batch 1 call sheets (17 Oct 2026)
- Page: https://claude.ai/artifact/ERpKu3SncEdJbP91Swz2QP.
  - Source: `command-center/batch1.py` with `batch1-template.html`. Outputs: `batch1-call-sheets.md` and `.html`.
- Batch 1 = the 27 Tier A leads (20 Egypt to call, 7 Dubai to message).
- Each sheet has a real competitor fact from the 11 Oct Google Maps pulls, then an 8-step call:
  1. permission + reason
  2. insight
  3. poke question
  4. qualify
  5. certainty
  6. small no-oriented ask
  7. loop at most twice
  8. future pace
- Each sheet has two copy buttons: the call script, and a WhatsApp/DM version that ends with an interest ask.
- Playbook tab rates every tactic by evidence:
  - Gong call data: permission opener 11.18% vs 1.5% baseline; "bad time?" opener weakest; interest CTA ~30% vs ~15%.
  - The "reason for my call" 2.1× figure comes from a secondary source and is unverified.
  - Expert methods: Voss no-oriented questions, Braun poke the bear, Belfort three tens and looping, Cialdini reciprocity.
  - Belfort's pressure tactics are left out on purpose.
- Raw Apify datasets (11 Oct; may expire): 6lW2R87jOZjOowO3p, EazaUq7ZQhmBK9hqH, Ey6e8xN48fZRAAZg1, JKlJyhqJVE5kuYn5H, WGbYh6Zx0e5Kjapyf, w4xxbqqCkzlyK6NXh (Egypt), WcjfhnjdWUs7bIfDr (Dubai).
- Notable facts:
  - Enhanced Dental's listing links Google Workspace's own Instagram/Facebook.
  - Mira links Yellow Pages' accounts.
  - Carmel California and Bistro Paris are both at 13 Street 18, which is the Building 13 dining complex, not a sign of one owner (corrected 17 Oct).
- Realism pass (17 Oct, after the founder pushed back: "why would big places talk to a 19-year-old solo freelancer?"):
  - 16 Go, 5 Pilot, 6 Park.
  - Parked: Lucille's, Carmel (viral on TikTok in 2023), Bistro Paris (3 branches), Bell's, FK Perfumes, Cocoage.
  - Replacements: Perfecta Clinic October, The Match Padel, SD Skin Clinic, Kriss Beauty.
- Each sheet now has a "reaching the decision-maker" route that uses only channels the business itself publishes. Personal mobile numbers are never hunted down: ask for a name, DM, business email, LinkedIn, walk-in, mutual contacts.
- Positioning: small fixed jobs for owner-run, single-location businesses, never "marketing management". Go back to parked leads after 2–3 local case studies.
- Next: batch 2 = Tier B (57 Egypt + 33 Dubai) once batch 1 outcomes are logged.

## Batch 2 call sheets (18 Oct 2026)
- Page: https://claude.ai/artifact/TMdUidbzPRzwS992oEMWJe.
  - Source: `command-center/batch2.py`, which reuses batch1's playbook and template. Outputs: `batch2-call-sheets.md` and `.html`.
- All 90 Tier B leads (57 Egypt, 33 Dubai): 65 Go, 24 Pilot, 1 Park (Restart Fitness, a 2-branch chain).
- Pilot covers:
  - Dubai real estate brokers, cafés and restaurants, and Dubai clinics that already have a site and Instagram;
  - Egypt real estate with fewer than 5 reviews;
  - places rated under 3.8;
  - plural names with 300+ reviews (possible branches).
- Competitor facts are generated from the raw Google Maps data, now saved at `leads/raw/places-2026-10-11.json` (294 places, recovered from the 11 Oct Apify pulls). Each one is the strongest same-search place within 5 km, preferring one that links something the lead lacks.
- Fixed in both batches: removed the unverified claim that one-star reviews "have no replies". The founder checks on the phone.

## Pricing (17 Oct 2026)
- `reports/pricing-2026-10-17.md`: first-deal menu for owner-run businesses. The founder confirms prices before quoting.
- Door-opener: Google listing fix, 1,500–2,500 EGP.
- One-page site: 6–10K EGP. Starter bundle: 8–11K EGP.
- Content: 5–8K EGP/month. Ads management: 3–5K EGP/month.
- Gulf: 10 AI images $250–400, 3 UGC ads $300–500.
- Terms: 50% deposit, 3-month minimum on monthly plans, no discounts (cut scope instead).

## Standing rules
- English first; Egyptian Arabic through the egyptian-voice skill (no MSA; business terms stay in English).
- Run everything through cringe-filter.
- Exports go out as PDFs when asked. Designs are QA'd against the dull checklist before showing.
- Git: commit to `claude/elegant-brown-yt0vko`; no PRs unless asked.
