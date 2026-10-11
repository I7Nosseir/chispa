# Commando OS: handoff (updated 11 Oct 2026, evening)

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
- **commando-hq:** routing updated for all of the above.

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
- CV + portfolio: the founder already has both (possibly on Canva). WAIT for his files and edit together.
  - Claude made drafts, uncommitted: commando/portfolio/ and the private artifact https://claude.ai/artifact/Vu61HyZjPKZAy9JYwRMFQf.
  - Use them only if he wants.
- Canva connector isn't connected. With it connected, Claude can read/edit his Canva designs.

## Standing rules
- English first; Egyptian Arabic through the egyptian-voice skill (no MSA; business terms stay in English).
- Run everything through cringe-filter.
- Exports go out as PDFs when asked. Designs are QA'd against the dull checklist before showing.
- Git: commit to `claude/elegant-brown-yt0vko`; no PRs unless asked.
