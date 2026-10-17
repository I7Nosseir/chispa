# Boss report: what I did, what I found, what's next (17 Oct 2026)

For: Ismail (founder, The Commando). From: Claude.
Covers the work from 7 to 17 Oct 2026. Everything below sits in the `commando/` folder of the repo.

## The short version
- **You have 156 businesses ready to contact:** 100 in Egypt to call, 56 in Dubai to message. Each one has a phone number, the gap I found and the offer to pitch.
- **You have the tools to pitch:** a final CV (2 pages), a final Canva portfolio (39 slides), call and message scripts, and an AI image/video skill that makes product samples.
- **Nothing is sold yet.** No calls made so far, and La Margrita's call notes never came back to me. The next 30 days are about volume: 10 calls and 10 Gulf messages a day.
- **Realistic month 1 (base case): 2 Egypt clients plus 1 Gulf pilot, about 40–45K EGP.** The full forecast is at the bottom.

---

## Phase 0: Mr Rakha (7–10 Oct)
**Did:** competitor scan, market brief, avatar pack, brand book, strategy, reference bank, Shoot Day 1 pack, 2 carousels, profile photo and cover (all in Claude Docs; ids in HANDOFF.md).
**Found:** his rivals' best TikToks are music montages, and Marwa Sadek launched the same "real world" angle on 8 Oct, so Rakha must show proof instead of making the claim.
**Waiting on you or him:** script approval (Arabic lines) 2 days before the shoot, the consent form, 6 open questions (shoot date, format, price, verified results, A-level, who answers WhatsApp), and creating the accounts.

## Phase 1: La Margrita audit (11 Oct)
**Did:** pulled live TikTok, Instagram, Facebook and Google data with Apify, then wrote the audit and the free-month offer (`clients/la-margrita/audit-2026-10-11.md`).
**Found:**
- 175K TikTok followers, but a normal post gets about 7K plays. One lucky 13.7M clip, and no system to repeat it.
- 4 different spellings of the name, a broken 12-digit phone number in a delivery post, and typos in the captions.
- A defensive owner reply (with a laughing emoji) to a 1★ hygiene review.
**Open:** I never got the call outcome. Tell me what they said and I'll write the follow-up.

## Phase 2: Egypt leads (11 Oct)
**Did:** 6 Apify Google Maps runs (about 214 places) across Sheikh Zayed, 6th of October, Hadayek al Ahram/Haram, New Cairo and Maadi. I kept 100 and removed education (your call), chains, hotel restaurants and listings with no phone.
**Found:**
- Mix: gyms 21, dental 19, beauty 18, restaurants 13, derma 12, physio 11, real estate 3, padel 2, café 1.
- Tiers: **A (high-paying) 20 · B 57 · C 23.**
- The common gap: strong reviews, but no website and nothing linked on Google. Big Maadi restaurants (Lucille's 2,866 reviews, Carmel 1,907, Bistro Paris 1,267) have no website on their listing.
- **Best openers** (a real mistake you can point at):
  - Enhanced Dental's "website" button opens a Google Form (274 reviews at 5.0).
  - Mira Dental's "website" is a Yellow Pages page.
  - La Vida Dental links another clinic's Instagram.
  - Air Gym and H2O Gym have name mismatches.
**Files:** `leads/leads-2026-10-11.xlsx` (with a status dropdown), `.csv`, `calling-playbook.md`.

## Phase 3: Gulf leads and remote jobs (11 Oct)
**Did:** 1 Apify run in Dubai (80 places → 56 after removing chains), 14 remote/Gulf jobs from web search, a fair-pricing sheet, and a message-first playbook.
**Found:**
- Dubai tiers: **A 7 · B 33 · C 16.** Perfume, abaya and jewelry shops fit AI product content best.
- **Top Dubai leads:**
  - Mayura Khamas Perfumes (856 reviews, no website)
  - iSmile Dental (1,313 reviews at 4.9, no website or socials)
  - FK Perfumes (3 different names across Maps, Instagram and website)
  - IDOL Perfumes
  - Nishka and Mila Gold jewellery
  - Cocoage clinic
- **Best job fits:** Whitecollars Senior Media Buyer (part-time, UAE e-commerce, Egypt-based only) and Malaeb Media Buyer (remote).
- **Fair pay** (market data, confirm before quoting):
  - Egypt full-time media buyer: 25K EGP/month or more with your results.
  - Remote Gulf role: $1,000–1,800/month.
  - AI UGC pack: $300–500.
  - AI product shoot: 10 images for $250–400.
**Not done:** Saudi (Riyadh, Jeddah) and Doha, because the Apify credit ran out.
**Files:** `leads/gulf-leads-and-jobs-2026-10-11.xlsx`, `gulf-leads-2026-10-11.csv`, `gulf-and-jobs-playbook.md`.

## Phase 4: CV and portfolio (11 Oct)
**Did:**
- **Portfolio:** cut your 66-slide Canva portfolio to a final 39 slides ("Ismail Nosseir Portfolio"). I removed 27 empty campaign slides and your home address, fixed typos, set the new headline, corrected Ignite (157 users) and Sparq, and left out all Rakha content. Your original file is untouched.
- **CV:** rebuilt as a 2-page PDF with the Rihla start date set to Jan 2026 and the tutoring lines removed.
**Found:** a number conflict. The portfolio says 54,822 EGP spend for Rihla/Grapes and the CV source says 24,600. I left the totals out of the CV until you confirm which is right. Also, the "Promoting Website" and AFCON slides show identical stats.
**Open:** set the portfolio to "anyone with the link can view", and add Watch links on the AI video slides (a PDF can't play video).

## Phase 5: Commando OS AI skill (11 Oct)
**Did:** merged your ai-video-prompt-engineering skill into Commando OS without changing your rules, and added:
- A QA gate.
- Disclosure rules.
- **Two style modes:** A "real life" and B "commercial hero".
- **10 commercial recipes:** pedestal, splash, ingredient world, dune and others.
- A prompt library.
- **3 tools:**
  - a prompt checker that catches every mistake in your lessons log
  - a frame contact sheet
  - a realism finish
- **A taste-bank system** so your saved references steer the output.
**Found:** your skill was already strong on video logic. What it lacked was a "commercial" look and a check before credits get spent.

## Phase 6: Mayura sample (11 Oct)
**Did:** wrote V1 (real-life) prompts, saw your dark result, diagnosed the cause, and wrote V2 commercial prompts (B1 peacock pedestal, B2 amber splash, B3 Dubai dune, B4 6-second video).
**Found:**
- The dark look came from a documentary-style prompt with no real product photo attached.
- The model also invented a label. **Never send a sample with an invented label for a real brand.**
- Mayura may be a multi-brand shop (in Meena Bazaar since 1981), so Inayah Abaya could be an easier first sample.
**Logged:** in `lessons-learned.md`, so it doesn't happen again.

## Phase 7: this pack (17 Oct)
- `reports/all-businesses-2026-10-17.md`: all 156 businesses with location, niche and one key fact.
- `reports/how-to-approach-simple.md`: the one-page approach guide, written so you don't sound like a cold caller.
- `reports/copy-paste-kit.html`: every AI prompt and outreach message, each with a copy button (also published as a private page).
- This report.
- The same day, a parallel session built the **Command Center** page (https://claude.ai/artifact/9dUi5FVtR34gyXo6Rdv1y1), with Report, Businesses (with per-lead warm messages), Copy kit, Approach and Forecast tabs. Use it as the main page; the files here are the plain versions plus the fuller AI prompt kit. The month-3 forecast below matches it.

## Costs so far
| Item | Cost |
|---|---|
| Apify (Egypt 6 runs + Dubai 1 run + La Margrita social pulls) | about $4.55 of the $5 free monthly credit; $0.45 left |
| Everything else (Canva, Claude, GitHub) | $0 extra |
Saudi plus Doha leads would cost about $1.50 when the credit resets, or you can take the $29 Starter plan.

## Blockers and open items (in order)
1. **Start the calls.** Nothing else matters until conversations start.
2. **La Margrita:** send me the call outcome.
3. **Portfolio sharing:** set the link to view-only public and add the video Watch links.
4. **Rihla vs Grapes ad spend:** tell me which number is right (54,822 or 24,600).
5. **Real product photo** for whichever Gulf sample you make first (Mayura or Inayah).
6. **Rakha:** script approval, the 6 questions, the accounts. Finish this deal before showing his work anywhere.
7. **Prices:** confirm the proposed ranges before you quote anyone.

---

## Forecast: what you can realistically reach

### Assumptions
- **Prices** are the proposed ones from your profile and the fair-pricing sheet, not confirmed yet.
- **Exchange rate** is assumed at about 50 EGP per $1. Check the real rate before quoting.
- **Your time:** you study at GUC and already work for Grapes and Rihla, so this assumes about 2 hours a day of outreach: 10 Egypt calls and 10 Gulf messages each weekday.
- **Conversion rates** are typical for warm-style outreach that opens with a free audit or sample: about 1 in 3 calls reach a decision-maker, and 1–3% of all contacts become paying clients in the first month.
- **First deals are usually small projects** (a website, one campaign, a sample pack). Retainers come in month 2–3.

### Month 1 (next 30 days)
| Funnel step | Conservative | Base | Strong |
|---|---|---|---|
| **Egypt:** businesses called | 100 | 100 | 100 |
| Reached the owner or manager | 25 | 35 | 45 |
| Free audit sent on WhatsApp | 15 | 20 | 28 |
| Meetings | 3 | 5 | 8 |
| **Paying clients** | 0–1 | 2 | 3 |
| **Gulf:** messages sent | 56 | 56 | 56 |
| Replies | 4 | 7 | 10 |
| Free 3-image samples sent | 2 | 3 | 5 |
| **Paid pilots ($300–500)** | 0 | 1 | 2 |
| **Jobs:** applications | 10 | 12 | 15 |
| Interviews | 1 | 2 | 3 |
| Offers | 0 | 0–1 | 1 |

### Money (cash in, month 1)
| | Conservative | Base | Strong |
|---|---|---|---|
| Egypt | 0–12K EGP (one small website) | ~23K EGP (1 website ~15K + 1 social ~8K/month) | ~45–60K EGP |
| Gulf | $0 | ~$400 (~20K EGP) | ~$1,000 (~50K EGP) |
| **Total** | **0–12K EGP** | **~40–45K EGP** | **~95–110K EGP** |

### Month 3 (day 90), if you keep the daily rhythm
- **Base:** 2–4 Egypt clients on monthly retainers (**about 15–40K EGP a month**) plus 1–2 Gulf pilots ($300–600 each), with a good chance one Gulf pilot turns into a $500–900/month retainer.
- **Capacity limit:** while you're studying, about 4 retainers is the most you can serve well. Past that, raise prices or hire a junior editor instead of taking more clients.
- **A part-time remote job** (Whitecollars-style, ~$15–25/hour × 20 hours a week ≈ $1,200–2,000/month) would add a steady base. Treat it as a bonus, not the plan.

### What moves you from conservative to strong
1. **Volume:** 10 calls a day, every weekday. Skipping days is the biggest risk.
2. **Same-day WhatsApp audit** after every call. Most deals come from the follow-up, not the call.
3. **Visit in person** the Tier A places near you (Zayed, October, Hadayek). A face converts better than a call.
4. **Gulf samples made with the real product photo.** A wrong label kills trust instantly.
5. **Ask every client for one referral** in week 2.
