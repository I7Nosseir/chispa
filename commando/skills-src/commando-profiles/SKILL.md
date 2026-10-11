---
name: "commando-profiles"
description: "The single source of truth for the user's businesses, personal brand, and creators — The Commando (parent), Sparq Study, Ignite Uni, Nova (custom gifts), the founder's personal brand, his freelance web/marketing services, and Adam & Anas (media-buyer duo he directs), and clients/prospects (Mr Rakha, La Margrita). Load it in any chat whenever the user mentions any of these names, says \"my business(es)\", \"my brands\", \"load profile\", \"use my profile\", \"@sparq\", \"@nova\", \"Adam\", \"Anas\", \"the duo\", etc., or whenever another skill (content, strategy, branding, research, leads) needs facts about these businesses. Also use it to create or update a profile."
---

# Commando Profiles

The fact base every other skill reads. Profiles hold **facts and decisions** (what the business is, who it serves, how it sounds and looks). Other skills apply them.

## Loading a profile
1. Identify which business(es) the request is about. If unclear, ask with tappable options.
2. Read the matching profile section(s) below (all profiles are embedded in this file, under "# Profiles"):
   - The Commando — parent company
   - Sparq Study — school learning
   - Ignite Uni — university learning
   - Nova — custom gifts
   - Founder — the user's personal brand, background, and how he likes to work
   - Freelance Services — the user's freelance websites/marketing services (used by lead-finder)
   - Adam & Anas — the media-buyer duo the founder directs (and their season story)
   - Mr Mohamed Rakha — client (IGCSE Business & Economics teacher, Sparq's first teacher)
   - La Margrita — prospect (Neapolitan pizza, Pyramids Gardens)
3. Confirm in one line what was loaded, e.g., "Loaded Nova profile (last updated …)."
4. Treat fields marked `_(to fill)_` or ❓ as unknown: ask about the ones the current task needs, state any assumption, and never invent facts like prices, numbers, or handles.

## Creating or updating a profile ("update profile", "fill Nova's profile", or new info appears in a chat)
1. Interview the user section by section, max 3 questions per turn, only on empty or changed fields. Start with: audience, offer & prices, voice, platforms, goals.
2. Show a short diff: what changes.
3. Propose the updated skill with the `propose_skills` tool (kind: improvement, target: commando-profiles) carrying this WHOLE file with the edited section and its "Last updated" line — never a partial file, or the other profiles are lost.
4. Remind the user to tap **Save** on the card so every chat uses the new version.

When a chat reveals a new durable fact (a new product, price, handle, decision), offer once at the end: "Want me to add this to the [brand] profile?"

## Adding a new business
Copy the Template section at the end, fill it through the interview, and add it to the list above.

## Shared files across the ecosystem
Profiles = Brand facts. Other skills keep their outputs as documents the user can store in a Project or Drive: Avatar Pack, Market Brief, Competitor Scan, Strategy Plan, Content Log, Performance Log. When one of these exists, it overrides assumptions in the profile for that topic.
- **Fixed home (rule 2026-10-05):** save each as a Claude Doc titled exactly `[Brand] — Avatar Pack`, `[Brand] — Market Brief`, `[Brand] — Competitor Scan`, `[Brand] — Strategy Plan`, `[Brand] — Performance Log` (one per brand, update in place, never a second copy). Before any skill runs, search the founder's Claude Docs for that title and load it; only if none exists, run the producing skill or state the assumption.

## Life dashboard
The founder's private dashboard "Command Post" (https://claude.ai/artifact/4Ez25uxUUJXoTw6WLK9CtB) holds live tasks, clients, courses, training and deen logs in its database (collections: tasks, clients, courses, learning, lifts, insights, days, settings). When a chat creates a task, client update, deadline or insight he should track, offer to add it there with the ArtifactData tool.

## Standing preferences (apply everywhere)
- Market: Egypt. Plan and write scripts in English; creators adapt them into their own Egyptian Arabic. Don't write dialect unless explicitly asked.
- Brand content (Sparq Study, Ignite Uni): English only — no Arabic, Arabizi or Arabic VO unless the founder explicitly asks (rule 2026-10-04).
- Run every content output through `cringe-filter` before showing it.
- Production engines: `commando-motion-studio` (videos) and `commando-design-studio` (carousels, posts, stills); profiles via `social-profile-optimizer`. Code-verified feature audits live in each repo at `docs/marketing/FEATURE_AUDIT.md`.

# Profiles

<!-- the-commando -->
## The Commando — Profile
Last updated: 2026-10-05 (umbrella profile; brand-level fields inherit from each brand)

### Identity
- ⚠️ **Name under review (2026-10-05):** "The Commando" is taken on social media and doesn't feel right to the founder. Keep using it internally until he picks a new one. Direction: power, leadership, discipline and relentless self-made drive (inspired by CR7's personality — never use CR7, Ronaldo, SIUU or any of his marks). Shortlist checked 2026-10-05 — .com, Instagram and TikTok all free: Crestseven, Septcrest, Talonseven, Kaptreign, Duxreign, Victreign, Legareign, Septrise, Valocrest, Reignvora. Before deciding: re-check availability and run an Egyptian trademark search (ITDA). After the rename, update every skill that names "The Commando".
- One-line description: Parent company that bonds all the founder's companies; tells the group story of a full learning journey with a personal touch
- Role in The Commando group: Parent / umbrella brand
- Stage: launching (group of early-stage companies: Ignite Uni live, Sparq Study pre-launch, Nova launching, agency active)
- Markets (country, cities): Egypt (cities to fill)
- Languages: English for group/brand content (LinkedIn, website, Instagram); founder speaks Egyptian Arabic on his own channels

### Offer
- Products / services: none of its own — see each brand's profile (Ignite Uni, Sparq Study, Nova) and Freelance Services (agency)
- Hero product: n/a (umbrella) — currently Ignite Uni is the proof point
- Seasonal or event offers: n/a — group events/milestones only

### Audience
- Primary audiences: partners & investors (LinkedIn, website); the public following the group story (Instagram) — no avatar pack needed; brand avatars live in each brand's Avatar Pack
- Secondary: future hires / campus leaders, schools and universities as partners
- Who pays vs who uses: n/a (no direct sales)

### Positioning
- Why us: one group covering the whole learning journey (school → university) with a personal touch (Nova), built by a student founder in Egypt — ❓ founder to confirm wording after rename
- Promise in one sentence: _(decide with the new name — brand-persona Mode A)_
- Proof: Ignite Uni 157 users (Oct 2026) and 20 sales with no marketing (Jul 2026); development-firm investment for 40% of Ignite (Sep 2026); founder's agency results (see Founder profile)

### Voice & personality
- 3 personality words: _(decide with the new name — brand-persona Mode A; direction: powerful, disciplined, leader)_
- Tone: "we" voice — calm confidence, milestones and proof, never hype (see Brand architecture below)
- Words/phrases we use: _(after rename)_
- Words/phrases we avoid: everything on the cringe-filter blocklist; no product pitches for the sub-brands
- Humor level: none to light

### Visual identity
- Colors (hex): _(after rename — brand-persona Mode A)_
- Fonts: _(after rename)_
- Logo usage: small "a [group] company" signature on sub-brand assets; never at the end of videos
- Look & feel of videos: _(after rename)_ — must not be swappable with Sparq, Ignite or Nova

### Channels
- Platforms + handles: LinkedIn + website + Instagram (~1/week) — handles wait for the new name ("The Commando" is taken)
- Website / links: _(after rename)_
- Current followers & results: 0 — not launched (2026-10-05)

### Goals
- 3-month goal: pick the new name, secure handles + domain, set up LinkedIn page and website ❓ confirm
- 12-month goal: ❓ (ask when a strategy task needs it)
- Main KPI: partner/investor conversations started ❓ confirm

### Team & cast
- Who appears on camera: the founder (group announcements) and the team
- Who films/edits: the founder's content system (motion + design studios)
- Consent notes: written consent from any staff, campus leaders or students shown; no minors' faces without parent/school consent

### Market
- Main competitors: n/a at group level — see each brand's Competitor Scan
- Gap we own: the only group in Egypt linking school study, university study and personal gifts into one journey ❓ confirm
- Key dates: brand launches, funding/partnership milestones, Ramadan, new academic year (Sep–Oct)

### Do's & don'ts
- Always: speak as "we"; show proof (numbers, milestones, team); keep each sub-brand's identity separate
- Never: pitch sub-brand products directly; inflate numbers; use the founder's "I" voice; use CR7/Ronaldo marks

### Brand architecture (decided 2026-10-03)
- Model: endorsed brands. Each brand has its own identity; the only shared element is a small "a Commando company" signature.
- The Commando speaks to partners & investors AND the public. Voice: "we" (the group, team, milestones, partnerships, careers). The founder speaks as "I" (thinking, lessons, journey) — keep the two distinct.
- Platforms: LinkedIn + website for partners/investors; Instagram for the public at low frequency (about 1/week: milestones, team, behind the scenes).
- Brands never post about each other's products; connections happen through planned bridges (Sparq → Ignite handover, Nova milestone gifts, founder storytelling).

<!-- sparq-study -->
## Sparq Study — Profile
Last updated: 2026-10-05 (rebuilt from a code-verified feature audit + founder answers; social handles checked 2026-10-05; ❓ = still unknown, ask when a task needs it)
Full sources in the repo: `docs/marketing/FEATURE_AUDIT.md` (what the code really does) and `docs/BRAND_PROFILE.md` (voice, visuals, video identity).

### Identity
- One-line description: The class that makes the difference: IGCSE / A-level live classes where every paper is marked question by question and explained, teachers get their evenings back, and parents finally know where their child stands.
- Tagline: "The class that makes the difference." · Bio line: "Every exam. Every mark. Explained."
- Role in The Commando group: School stage of the learning journey (planned bridge → Ignite Uni at university)
- Stage: pre-launch — onboarding the first teacher (2026-10-04). No paying teachers yet; no usage numbers or testimonials to quote.
- Markets: Egypt (Cairo private/international schools first ❓ cities)
- Curriculum: IGCSE + A-level (decided 2026-10-04). Other systems (American, national) later — not in marketing until the founder says so.
- Languages: Product in English. Content: English only for now (founder rule 2026-10-04); Arabic only when the founder asks.

### Offer (only claim LIVE features)
- How it's sold: teachers / tutoring centers pay SPARQ per student (B2B, confirmed 2026-10-04) ❓ real price; planning docs assume ~120 EGP/student/month. "SPARQ Solo" (no teacher) is planned only: never advertise.
- Hero product: **the marked paper** — every question green/amber/red, the model answer, why marks were lost (command word not followed, missing Cambridge vocabulary, band reasoning), PDF report.
- LIVE features worth marketing:
  - **Marking + grading report** (handwriting included; the teacher's own mark scheme)
  - **Reporting:** class analytics (critical gaps, momentum shifts), student trajectory + risk alerts, per-student Performance / Parent / Smart Insights PDFs, Reports Library (~10 types), teacher emails (daily snapshot, weekly digest, report after each deadline)
  - **Teacher help:** unsure answers double-checked and flagged; Review Queue, Smart Review, Flags, bulk regrade, disputes; **marking learns the teacher** (past corrections, Grading Diary, own examiner reports); "Ask SPARQ" teacher chat (at-risk students, pending reviews, session plan, update email)
  - **Mistakes Bank** (students + class view): mastery by topic, error types, persistent misconceptions, learning path; feeds the weekly practice plan (drafted Friday → teacher approves → marked); extra exercises after a slip; "breakthrough" flag
  - **Live classes:** Zoom inside the app, automatic attendance, pushed questions/quizzes, tab-switch detection, recordings; in-person QR check-in ⚠️ verify Zoom in production before filming
  - **SPARQ Live quiz:** PIN join, countdown, points and streaks, live top 10
- Do NOT market yet: parent WhatsApp reports (stubs, nothing sends), parent→teacher messages (no teacher inbox), WhatsApp auto-reply (off), tournament (no code), student diary (no code), mobile app (read-only shell — the web app works on phones), "38 hours back" / "100% consistent" claims (no proof).
- Seasonal: ❓ mock season, results day, tournament pilot Oct 22–25 (still on?). Planned: a Sparq-sponsored school football tournament in Ramadan with Kent College as partner (pre-event challenges and photo sessions, memory magazines via Nova, full media coverage).

### Audience (stakeholders)
- Student (user) — IGCSE/A-level, 15–18, ❓ year groups
- Teacher / tutor / center owner (BUYER — confirmed)
- Assistant / TA (operator)
- Parent (influencer / payer?) ❓ who actually pays the teacher
- Head of department / school admin (future buyer: schools) ❓ any school using it
- Primary avatars: _(to fill — avatar-creator)_
- Who pays vs who uses: teacher/center pays SPARQ; students use it; parents pay the teacher and influence the choice ❓ confirm parents' role

### Positioning
- Why us: the only class in Egypt where live teaching, papers marked question by question with reasons, practice from your own mistakes, and teacher reporting live in one place (Nabeeh = attendance/ops; Voya = exam tools with no teacher) ❓ verify with competitor-scanner
- Promise: Nobody is left guessing — not the student, not the teacher, not the parent.
- Proof: none yet (pre-launch). First proof to capture: the first teacher's before/after (marking time, papers marked, a student's report with dummy data). The 600-student teacher was a potential deal that collapsed — never mention it.

### Voice & personality
- 3 words: premium · warm · sees-you
- Tone: measured, human, dry humour; never corporate, never childish
- Owned words: class, live, teacher, paper, marks, feedback, explained, parent, mock, results day, Sunday, red pen
- Never: "AI", "artificial intelligence", "machine learning", "algorithm"; lecture, PDF, summary, faculty, library (Ignite words); streamlined, revolutionize, empower; naming a school; real student data
- Humor: light

### Visual identity
- Colors: parchment #F4F0E8, paper #FFFEFB, ink #09090D, blue #0099FF (shapes, logo), text blue #0077CC (type on parchment), ice blue #9ED8FE; semantic green #178A4B / amber #C77A0E / red #D23A2E · NO gold (dropped 2026-10-04)
- Fonts: serif headlines (EB Garamond / Georgia), clean sans body (Inter Tight)
- Logo: bolt inside the rounded diamond with four neuron clusters; light mode only
- Video look: light parchment, never dark scenes, measured cinematic tempo (2–3s beats), marked-paper motion, piano/strings. Reference film: "14/30" (Oct 2026).

### Channels
- Platforms: TikTok (students), Instagram (students + parents), Facebook (parents), LinkedIn (teachers), YouTube ❓, WhatsApp Business ❓
- Handles: Instagram @sparqstudy (0 followers, 0 posts, bio "A generational learning experience" — outdated, Oct 2026) · TikTok not created · Facebook page not public ❓ · sparqstudy.com
- Current followers & results: first content (Oct 2026)

### Goals
- PROPOSED (founder to confirm): 3-month: first teacher live + 3–5 teachers/centers onboarded, one documented case study · 12-month: ❓ · Main KPI: active teachers (then students with ≥1 marked paper per week)

### Team & cast
- On camera: the founder, real teachers/students (with consent), creators; plus faceless motion films, carousels and screen recordings · Films/edits: the founder's own system (Remotion motion + design studios)
- Consent: students are minors → parental consent, dummy data in all product shots

### Market
- Competitors: Nabeeh, Voya ❓ others (centers, Instagram tutors, Save My Exams, ZNotes, PMT)
- Gap: marked + explained papers tied to the teacher's live class
- Key dates: Cambridge May/June and Oct/Nov series, mocks Jan–Feb ❓, results days (Aug / Jan)

### Do's & don'ts
- Always: show the paper and the moment; dummy data; one idea per post; English only
- Never: say AI; dark backgrounds; emojis on screen; pricing in awareness content; Ignite language

### Status (2026-10-04)
- Pre-launch (first teacher onboarding). Content produced by the founder's own system. First film "14/30" (41.5s, English VO) done; first carousel "What 14/30 never told you" drafted.
- Lowest-cost content engine: real users — student reactions, screen recordings (dummy data), teacher stories, with consent.

<!-- ignite-uni -->
## Ignite Uni — Profile
Last updated: 2026-10-05 (rebuilt from a code-verified feature audit + founder answers; social handles checked 2026-10-05; ❓ = still unknown, ask when a task needs it)
Full sources in the repo: `docs/marketing/FEATURE_AUDIT.md` (what the code really does) and `docs/BRAND_PROFILE.md` (voice, visuals, video identity).

### Identity
- Bio / end-card line: "Your lecture, finally explained." (decided 2026-10-04; "Zero-Skip" not used as a tagline)
- One-line description: Turns the lecture you were given into the study system you needed — no skipped steps. For Egyptian university students.
- Website: https://igniteuni.com
- Role in The Commando group: University stage of the learning journey (after Sparq Study)
- Stage: live — 157 users (2026-10-04); 20 sales by Jul 2026; investors from a development firm for 40% (Sep 2026); launch week Oct 5–12 2026 going ahead. The site's "1,000+ students" is not true → remove it.
- Markets: Egypt ❓ which universities / cities first (early users: GUC and GIU)
- Faculties: Medicine, Dentistry, Pharmacy first, then CS/Engineering, then Law/Business ❓ confirm order
- Languages: Product in English. Content: English only for now (founder rule 2026-10-04).

### Offer (only claim LIVE features)
- Hero product: **lecture analysis** — upload up to 3 PDF/PPTX files; 7 subject engines rebuild each chapter into a gated walkthrough: think-first → reading sections each locked behind a question → checkpoint → deep why → teach-back (graded) → workbench (code runs in-browser) → quiz → Forge.
- LIVE features worth marketing:
  - **The lecture report:** Diagnosis Report (verdict, score, strengths, misconceptions with corrections, recommendations) → **Revision Pack PDF** from the student's own wrong/skipped answers, with practice questions and model answers; Grand Exam performance report
  - **Exam Oracle** (paid tiers): upload past papers → every question solved with exam tip, key insight, alternative methods, linked lecture chapter; patterns after 2 papers, predicted exam after 5; mentor chat
  - **Campus Lectures / Public Library:** university → faculty → subject; read free when logged in; interactive parts per faculty; per-subject Revision Mode
  - **Rapid review:** night-before multi-lecture Revision with exam countdown (LIVE); Library Revision Mode (LIVE); LifeSaver cheat sheet + traps + quick-fire quiz (works, hidden: URL only) ❓ keep?
  - Solving-sheet walkthroughs, flashcards, study planner, 76 diagram templates
  - **Campus Leader program:** unlimited credits, console (publishing, announcements, earnings, marketing kit), 15% of 299 EGP per subscriber
- Do NOT market yet: Watch Mode (admin-only), "1-week free trial" (decided: there is none), Mistakes Bank (retired), spaced review/daily email (never fires), clan leaderboards (scores can't move), WhatsApp share card on results (missing), "1,000+ students" (not true).
- ⚠️ Revenue bugs to fix before paid ads: card payment for Library grants no access; card payments don't upgrade tier (buyers can't open Oracle).
- Prices (decided 2026-10-04): ONE unified credit pool, newest plans = higher prices, fewer credits: Starter 649 EGP (10) · Pro 1,099 (15) · Elite 2,199 (30) ❓ confirm these are the newest numbers. ⚠️ Code still grants 27/73/160 → must be fixed. Library: 299 EGP per faculty PER MONTH ⚠️ code never expires access → must be fixed. Free trial = 1 free credit at signup (+1 with referral); remove all "1-week free trial" wording. Awareness content never mentions price.

### Audience (stakeholders)
- Student (user + payer) — free (1 credit, +1 referral), paying, library subscriber
- Campus Leader (distribution partner, earns commission)
- Admin (internal) · Later: universities / professors (not for consumer content)
- Primary avatars: _(to fill — avatar-creator)_
- Who pays vs who uses: the student pays ❓ do parents pay for some?

### Positioning
- Why us: reconstruction, not summary. vs ChatGPT/Gemini: won't let you skip, grades your explanations, keeps every miss and turns it into a diagnosis + revision PDF, subject-specific engines, Oracle patterns across many past papers, faculty libraries already processed. vs studying from slides: fills skipped steps, active recall in every section. vs a private tutor: any time, every lecture, your professor's past papers, one faculty price ❓ tutor cost benchmark (market-research)
- Promise: Your lecture, finally explained — and your exam, seen coming.
- Proof: 157 users (Oct 2026), the first 80 from one WhatsApp message with zero ads ❓ confirm the 80 story; no other numbers until verified

### Voice & personality
- 3 words: smart · fast · on your side
- Tone: the friend who aced the exam; short lines, specific numbers; cheeky against the slides, never against professors
- Owned words: lecture, slides, PDF, chapter, finals, faculty, professor, library, step, symbol, forge, Oracle
- Never: class, live, teacher, parent, marked paper (SPARQ words); "revolutionize your learning"; "AI" alone as the selling point; made-up stats; grade promises
- Humor: light–bold (meme-literate)

### Visual identity
- Colors: cream #FFFAF5, orange #F97316 (shapes), text orange #C2410C (type on cream), ink #1C1917, secondary #78716C, highlight #FFF7ED, border #FDBA74; logo gradient #EC4F7A → #F2694A → #F97216
- Fonts: heavy geometric sans (Outfit / Inter Tight 800–900)
- Logo: open book + white-outlined gradient bolt
- Video look: warm light mode (one night scene max), fast kinetic type 120–128 BPM, pages splitting/reassembling. Reference film: "Obviously." (Oct 2026).

### Channels
- Platforms: WhatsApp first (CL loop), Instagram, TikTok (proof clips), LinkedIn (founder + CL recruiting), Facebook, YouTube ❓
- Handles (exist): Instagram @igniteuni (13 followers, 5 posts, Oct 2026; bio outdated — "NOT summaries, COMPLETE reconstruction") · facebook.com/igniteuni (0 followers; category wrongly set to "Clothing (brand)"; support@igniteuni.com) · LinkedIn company page not found ❓ · WhatsApp +20 109 596 0220 · TikTok not created · igniteuni.com
- Current followers & results: Instagram 13 followers / 5 posts (2026-10-05)

### Goals
- PROPOSED (founder to confirm): 3-month: from 157 users to a steady base of paying students through finals season, with Campus Leaders live in the first faculties · 12-month: ❓ · Main KPI: paying students (then active Campus Leaders, lectures analysed per week)

### Team & cast
- On camera: the founder, real students (with consent), Campus Leaders/creators; plus faceless motion films, carousels and screen recordings · Films/edits: the founder's own system (Remotion motion + design studios)
- Consent: university students (adults) — written consent for reactions/screens

### Market
- Competitors: StudyFetch, NotebookLM, ChatGPT/Gemini, Studocu, Baims, Brocali, private tutors / centers ❓ verify (competitor-scanner)
- Gap: Egypt faculty mapping + gated walkthrough + past-paper Oracle
- Key dates: midterms ❓, finals (Jan & May–June ❓ by university), Big Bang launch week Oct 5–12 2026 (confirmed)

### Do's & don'ts
- Always: show a real-looking slide and what Ignite does to it; English only; specific numbers only if verified
- Never: SPARQ visuals/words; blue palette; serif editorial look; pricing in awareness content

### Status (2026-10-04)
- Live with 157 users; launch week Oct 5–12. Content produced by the founder's own system. First film "Obviously." (46s, English VO) done; first carousel "A summary isn't studying" drafted.
- Lowest-cost content engine: real users — reactions, screen recordings, Campus Leader content, with consent.

<!-- nova -->
## Nova — Profile
Last updated: 2026-10-06 (strategy chat Jul–Aug 2026 + founder answers 2026-10-05 + Nova brand book PDF, Dec 2025; "draft" = proposed, confirm when a task needs it; ❓ = confirm)

### Identity
- One-line description: Custom gifts brand that adds personality to everyday things (cards, walls, notebooks) and a personal touch around each product and event in the group
- Tagline (brand book): **"Make your swipe iconic."**
- Name meaning (brand book): a nova is the sudden brightening of a star — small details, big impact.
- Brand book positioning: "a modern design brand specializing in premium credit card stickers that transform an everyday object into a personal style statement."
- Role in The Commando group: Personalization layer across the group (milestone gifts, event merch, prizes)
- Stage: launching — the founder has tried for ~2 years; first 5–6 card-sticker orders (summer 2026); own branding scheme exists
- Markets: Egypt (Cairo); university and school students first, delivered in bulk via campus leaders
- Languages / dialects: Egyptian Arabic on camera (Nova's creator); captions Egyptian Arabic, product/theme names may stay in English

### Offer
- Products: credit/debit card stickers (hero, chip area cut out, laser-cut by a Cairo laser-printing supplier) · custom FIFA cards (also framed) · football jersey collage frames (wall + desk) · posters · travel & birthday memory magazines (A4 25-page costs ≈400 EGP, market sells ≈1,000) · customized study notebooks · 365-day to-do notebook · student bundle (planner + 3 notebooks + mug + 5 bookmarks) · dua frames ❓ prices for all
- Hero product: card stickers (themes: sports icons, sports, football clubs, comics/memes, TV series)
- Seasonal or event offers: back-to-uni bundles, Ramadan/Eid (Quran-audio magnet explored), event prizes/sponsorship
- Payments: Vondera store + payment gateway considered ❓ decided?

### Audience
- Primary avatars (from avatar-creator): _(not run yet — run avatar-creator; two segments below are the starting point)_
- Segments (founder 2026-10-05): (1) students buying for themselves — self-expression through themes they love (football clubs, icons, series, memes); (2) gift-givers — friends/partners buying birthday, memory and milestone gifts
- Who pays vs who uses: segment 1 = same person; segment 2 = buyer gifts someone else (the reveal/reaction is the content)

### Positioning
- Why us (draft): made-to-order around what *you* love, at student prices, delivered on campus through campus leaders
- Promise in one sentence (draft): "Your things, with your personality on them."
- Proof: first 5–6 card-sticker orders (summer 2026); no testimonials yet — collect customer reactions with consent

### Voice & personality
- Direction chosen: **Warm & personal** (2026-10-05), expressed through the brand book's **premium, minimal, aesthetic** look
- 3 personality words (draft): personal · premium · warm
- Tone: like a friend who remembered what you love — caring, specific, never sappy
- Owned lines (brand book): "Make your swipe iconic." · "Peel, stick, done." · "The card glow-up you never knew you needed." · "Meet Nova — where your credit card becomes a piece of you." · "Create your own design or choose from our curated collection." · "This is how your card should look" · "Which one would you choose?"
- Words/phrases we use (draft): "made for you", names, the person's team/show/moment, "your", swipe, glow-up
- Words/phrases we avoid: generic gift clichés ("perfect gift for everyone"), fake urgency, cringe-filter blocklist
- Humor level: light

### Visual identity
- Colors (hex, sampled from the brand book): white #FFFFFF · sand/beige #BFB290 · cocoa brown #52423B (logo + type). Supporting tones in mockups: cream/ivory, kraft gold, soft pink accents on card designs.
- Contrast rules: brown on white 9.5:1 (body text OK) · brown on beige 4.5:1 (OK for text ≥ 18px/bold) · beige on brown 4.5:1 (same) · **white on beige 2.1:1 → logo/huge display only, never body text or captions**
- Fonts (brand book): Avenir Next (Regular, Medium, DemiBold) for body and headings; Avenir Black for bold stacked statements (e.g. "THIS / IS / HOW / YOUR / CARD / SHOULD / LOOK"). Avenir is a paid font → for code-made designs (design/motion studios, OFL only) use **Nunito Sans** as the stand-in ❓ founder to confirm, or supply licensed Avenir files
- Logo: hand-drawn, rounded, lowercase wordmark "nova" (no symbol). Six approved color pairs: beige on white · brown on beige · white on brown · white on beige · beige on brown · brown on white. Packaging uses a small white logo at the bottom center. Never at the end of videos.
- Packaging (brand book): pocket-envelope card holders (white/ivory or cream–kraft gold) with a window showing the stickered card; sticker on a blank card template for previews
- Look & feel (brand book + draft): earthy neutrals, textured fabric/linen/paper backgrounds, soft shadows, lots of white space, product close-ups of the card; mix of mockup tiles and short statement tiles on the feed. Videos: warm light, hands and real products, the making/personalizing process, peel-and-stick moments, reveal and reaction moments
- ⚠️ Tension to resolve: the brand book shows soft aesthetic designs (florals, bows, gradients, sky photos) while the hero themes are football clubs, icons, memes and series. Keep the premium earthy frame for both, and show both design styles so neither audience feels it's not for them ❓ founder to confirm

### Channels
- Platforms + handles: Instagram + TikTok — handles not created yet ❓
- Website / links: ❓ (Vondera store considered)
- Current followers & results: 0 — accounts not live (2026-10-05)

### Goals
- 3-month goal: **100 orders** by early Jan 2027 (founder 2026-10-05), mostly card stickers via campus leaders
- 12-month goal: ❓
- Main KPI: orders per month

### Team & cast
- Who appears on camera: Nova's own content creator, on camera, speaking Egyptian Arabic
- Who films/edits: Nova's creator ❓ editor
- Consent notes: customers' faces/names and gift reactions only with consent; no minors without parent consent

### Market
- Main competitors: ❓ run competitor-scanner (Egyptian card-skin / custom-gift Instagram shops)
- Gap we own (draft): student-priced personalization delivered on campus + Nova moments inside Ignite/Sparq milestones
- Key dates: back-to-uni (Sep–Oct), mid-year exams (Jan), Valentine's (Feb 14), Ramadan & Eid, Mother's Day (Mar 21), graduation (Jun–Jul), birthdays year-round, big football matches

### Do's & don'ts
- Always: show the real product and the personal detail; feature the person it's made for; credit Nova when it appears on Ignite/Sparq accounts
- Never: fake scarcity or fake reviews; use club/player logos in ads without checking rights ❓; copy SPARQ/Ignite visuals

### Content ownership
- Nova has its own content creator, who produces Nova's content. This profile is filled so the founder's skills can brief, review and support that creator (founder chose "fill fully" 2026-10-05).
- Nova still appears as a bridge: custom milestone gifts/rewards for Ignite and Sparq students, shown on those brands' accounts with Nova credited.
- Share the brand architecture rules with Nova's creator so its identity stays separate.

<!-- founder -->
## Founder — Personal Brand Profile
Last updated: 2026-10-05 (built from the founder's Claude chat history Feb–Oct 2026, Gmail/Drive scan and his answers; ❓ = confirm)

### Identity
- Name: Ismail Nosseir (full: Ismail Ahmed Samy Nosseir). Born Oct 2007 — 19 since 1 Oct 2026. Cairo (Giza), Egypt. Never put his home address or personal phone in outputs.
- Role: Founder of The Commando (Ignite Uni, Sparq Study, Nova) and of The Commando agency (smart solutions + marketing services). Also AI/automation specialist and marketing director for agencies and travel brands.
- Story in 3 lines: IGCSE graduate (Knowledge Valley Schools, 2024) who started tutoring IGCSE Business at 16 and running marketing for real businesses before university. Builds AI products by directing AI coding tools (Claude Code; previously Google Antigravity) — a "vibe coder" with a business brain, now learning real system architecture. Building several companies at once while studying at GUC.
- Expertise to be known for: marketing systems that make money (funnels, media buying, lead gen), AI content production (Higgsfield, Kling, Seedance, Nano Banana, Google Flow), AI automation (n8n, Claude Code), and building EdTech in Egypt.
- Languages: Arabic (native, Egyptian), English (fluent), French (fair); learning German (required at GUC). On camera: Egyptian Arabic; plans and scripts written in English first.

### Education
- German University in Cairo (GUC), Bachelor of Business Informatics, 2024–present. GPA ≈ 3.1 German scale (Apr 2026; 0.7 best).
- Retaking CS3/CS4 and Math 3/Math 4 (failed earlier); must pass German to graduate.
- Winter 2026: CSEN501 Databases I (5-person team project); research paper "Effect of Business Intelligence on Decision-Making" (Dr Salma Tosson, Tutorial 17). ❓ full course list and credits.

### Work & proof (use only these, never inflate)
- Marketing Director, Grapes Holiday (travel), Oct 2025– : ad spend −62.5% with 2.5× leads; 3,000+ qualified leads.
- Marketing Director (founding), Rihla Travel, Jan 2026– : 350,000+ EGP revenue in the first 2 weeks.
- NovaX creative agency (Saudi back-office): AI specialist; accounts Esplanade Mall (Riyadh), Privea Dent, IPC pet clinic, Danson, Tosy Factory; built the NovaxOps internal operations platform (novaxops.com). Prefers to be paid per phase (deposit / mid / final), not partnership.
- American Agency: proposed a multi-agent AI system (Windows server, ClickUp, Adobe apps) — pricing by phase ❓ status.
- IGCSE Business (0450) tutor since 2023, incl. 3 years with Mr Mohamed Rakha (O-level); June 2025 results: one 9, three 7s. Student numbers fell to zero in Sep 2026 — lesson he names himself: he was too harsh with students.
- Kent College (Egypt): did a content-creator trial day (left a strong impression; role needed full-time). Now pitching a Sparq-sponsored school football tournament in Ramadan with Kent as partner.
- Ignite Uni: 148 users and 20 sales with no marketing (Jul 2026); 157 users (Oct 2026); investors from a development firm for 40% (Sep 2026).
- Certifications: Google Digital Marketing; HubSpot Content Marketing (59/60), Inbound (57/60), Digital Advertising (51/60), Social Media Marketing II (52/60), Contextual Marketing exam passed — all HubSpot certs expired by Aug 2026.

### Personal brand goals
- Starting audience: zero (October 2026). Personal-brand accounts: **new accounts**, handles not chosen yet (founder 2026-10-05) — do not use or mention his existing personal account
- Positioning: the operator, not the teacher — a founder building several real companies in Egypt; every business/marketing lesson comes with proof from his own ventures
- The Commando is the main story; Ignite Uni, Sparq Study, Nova, and Adam & Anas are storylines in it (his many projects are the content, not a weakness)
- Pillars: build in public · market teardowns · against-the-crowd takes backed by results · live experiments on his own businesses · founder life
- Monetization path: content → trust → waitlist → consulting/done-for-you, courses, and his products (Ignite, Sparq, Nova)
- What the personal brand should do for the businesses: send attention and trust to Ignite, Sparq, and Nova; set up the Adam & Anas reveal
- Platforms: TikTok + Instagram Reels (3/week + stories), LinkedIn (2/week); YouTube later. Planned start: end of 2026 / new year, after Ignite and Sparq are running.
- Long-term options he is weighing: private equity (buy, build, sell companies), e-commerce, or a top tech firm (e.g. Microsoft Egypt) if solo work stalls.

### On-camera rules
- When he appears (face content): trust, authority, founder story, big announcements, events, opinions — comfortable on camera, so face content can be the default for his brand
- When content is faceless: product demos, AI-generated films, carousels
- Comfort level on camera (1–5): **5 — natural** (2026-10-05)

### Voice & personality
- 3 personality words: ambitious · direct · creative
- Topics he talks about: business thinking (e.g. "where does the world's money go"), marketing that converts, AI tools, building startups in Egypt as a student
- Topics he avoids: politics; his personal finances/income (no revenue flexing)
- Personal values & habits he's happy to show: Muslim (prayer, Quran goals), football player (training for the new season), gym (upper/lower split, building muscle), boxing fan

### How he likes to work with Claude (apply in every chat)
- He leads; Claude proposes. Ask before big creative or strategic decisions; multiple-choice questions are welcome.
- Short, direct answers; one-line answers when he asks for them. No assumptions — research and state facts; give real references (Instagram posts, Pinterest pins) with working links.
- Follow instructions exactly (formats, cell layouts, file structures) — never "improve" a format he gave.
- Arabic: never formal fusha in content; Egyptian slang via `egyptian-voice`; plan in English first. Arabic in PDFs/files must render correctly or be left out.
- No generic "AI" output: he wants senior-level, creative, non-cliché ideas (`twist-lab`, `idea-elevator`, `cringe-filter`).
- Preferred AI stack: Claude Code for building; Gemini 3 Flash Preview inside his apps; Higgsfield (Kling 3.0, Seedance, Nano Banana) and Google Flow for content; n8n for automation; CapCut Pro / Filmora for editing.
- Known struggles he has named: too many projects at once, perfectionism, imposter syndrome, losing time to daydreaming and music. Help him focus: top 3 per day, finish before starting.

### Visual identity
- Signature look (outfits, setting): a mix, mostly **elegant** (smart, clean, well-fitted) with some casual
- Colors / fonts: ❓ not set — brand-persona Mode A proposes when the personal brand starts

### Learning (active)
- Skool — AI Video Bootcamp (Daniel Riley): the one learning community he values; other learning-platform emails are noise.
- Marketing courses taken: Adam Hassan (organic content, media buying), P Creative, Beha Hinnish (content); weekly Friday social-media course.

<!-- services -->
## Freelance Services — Profile (used by lead-finder)
Last updated: 2026-10-05

- Services: websites (new/redesign), marketing (social media, content, ads); capability now includes code-made motion graphics, brand films, carousels/static design and social profile setup (see `commando-motion-studio`, `commando-design-studio`, `social-profile-optimizer`)
- Packages & price ranges — **PROPOSED 2026-10-05, founder must approve before quoting** (benchmarks: Egyptian agency ranges May–Aug 2026 — websites 18–45k EGP one-time, social management 8–18k/month pro tier, ads management 4–10k/month excl. budget, motion video 1.5–6k each; priced lower-mid as a lean operator with real proof):
  - Websites: Landing page 12–18k EGP · Business site (5–8 pages) 20–35k · E-commerce 30–50k · maintenance 10–15%/year
  - Social media management: Starter 6k/month (1 platform, 12 posts + 4 reels) · Growth 10–12k (2–3 platforms, 8 reels + stories) · Premium 15–20k (adds code-made motion graphics + monthly report)
  - Ads management: 5k/month minimum or 12% of ad spend, whichever is higher (budget paid by client)
  - Motion/brand films: 3–6k per motion video · brand film 8–15k
  - Gulf/international clients: quote in USD — ❓ set rates (estimate: websites from ~$600, social from ~$400/month)
- Target niches & cities: gyms & academies · real estate & travel (proof: Grapes Holiday, Rihla Travel) · clinics (dental, derma, vet) — cities: Cairo & Giza by default ❓ (Gulf via English outreach)
- Portfolio / proof links: portfolio exists — link ❓ (founder will send); until then cite Grapes Holiday (−62.5% ad spend, 2.5× leads), Rihla Travel (350k+ EGP in 2 weeks), novaxops.com
- Calling name & business name: Ismail, The Commando agency (⚠️ agency name changes when the group is renamed)
- Languages for calls and messages: Egyptian Arabic for Egyptian businesses; English for Gulf/international
- Guarantee or risk reversal: pay by phase (deposit / mid / final) + 2 revision rounds; no results guarantee
- Delivery time per package: landing page 1–2 weeks · business site 2–3 weeks · e-commerce 3–5 weeks · social management starts within 1 week of onboarding

<!-- adam-anas -->
## Adam & Anas — Duo Profile
Last updated: 2026-10-05 (handles and prices still not set)

### Identity
- Who: Adam and Anas, two friends of the founder, building personal brands together as young media buyers.
- Branding: their own names (no duo or agency name yet).
- Stage: just started learning media buying; already being contacted by a few business owners.
- Backing: rely on what they're learning plus the founder's experience. The founder is their director, leader, and strategic manager (behind the scenes for now).
- Market: Egypt. Content language: Egyptian Arabic on camera; plans and scripts written in English, which they adapt in their own words.
- Platforms: TikTok and Instagram equally.

### Goal
- Build their own fan base and get real clients.
- Be seen as established — earned through real case studies (Sparq Study and Ignite Uni campaigns), visible process, and results, never fake claims.

### Voice
- Ambitious, hungry, confident, real. Banter between the two.
- Ambition is shown with goals and proof, not bragging (see cringe-filter).

### Content pillars
1. $50 Experiments — real budget tests on Sparq/Ignite ads, results shown
2. Adam vs Anas — same product and budget, two ads, audience votes
3. Ad Autopsy — breakdowns of why viral ads worked
4. Business Rescue — fixing a local business's wasted ad spend (lead-finder supplies targets)
5. The Mission — on-screen counter, e.g., "Road to 10 clients in 90 days"
- Cadence: 4 videos/week across both platforms

### Season story (3 acts)
- Act 1 Build (months 1–2): duo and founder grow separate audiences; no public link. Founder builds a recognizable signature (phrase, item, voice).
- Act 2 Tease (~month 3): clues about "the person behind our strategy" — voice off-camera, hands, signature item, "our director said…". Comments speculate.
- Act 3 Reveal: joint video reveals the founder as the hidden team member; audiences merge; launch the next move.

### Individual roles (to fill)
- Both are funny; humor comes from their contrast.
- **Adam — the bold one.** A bit more serious. Delivers the hooks, the stakes, the numbers, and the big goals with a straight face. Plays it confident in rivalries.
- **Anas — the light one.** Reactions, comic timing, says what the viewer is thinking, asks the "dumb" question that makes the explanation land. Plays the underdog in rivalries.
- Dynamic: Adam sets it up seriously, Anas undercuts it, then they both deliver the real value. Never make one of them the butt of every joke — both win sometimes.
- Handles: not set yet (2026-10-05) — must be chosen before their first post
- Services & prices they offer: not set yet (2026-10-05) — decide before they take client calls

### Never
- Fake revenue, fake clients, or claimed years of experience.
- Mention the founder by name before the reveal.

### Duo branding (proposal — confirm or change)
- **On-screen name:** "Adam & Anas" — their own names, no agency name for now.
- **Speaker-coded captions:** Adam's words highlighted in electric blue, Anas's in yellow; white bold text with a dark outline. Viewers learn who's talking by color — that's the brand.
- **Signature open (mission videos):** Adam writes on the whiteboard; the counter "Day X/90 · Clients X/10" appears.
- **Signature close:** Anas changes something on the board as the punchline (e.g., "0" → "0.5").
- **Running gags:** Anas is always eating something; whoever loses a bet pays the next test.
- **Sound signature:** marker squeak + the same short sting whenever the counter updates.
- **Set:** one recognizable corner (whiteboard, laptop with Ads Manager, plants or a neon sign) so every video looks like "their place".

### Editing style — fun and simple, not top-tier (CapCut level is enough)
- Captions on every word, speaker-colored, one bold font, center safe zone.
- A cut on every line; zoom punch-in only on jokes and key numbers.
- Transitions only when the scene changes: whip or match cut. No random transitions.
- Light sound effects under the voice: pop on text, ding on numbers, record scratch on Anas fails. Never loud.
- Max one meme insert per video.
- Counter graphic stays on screen in mission videos.
- No glow, no heavy filters, no logo outro — end on the punchline.
- Scripts are planned in English, then adapted with `egyptian-voice` after approval.

<!-- rakha -->
## Mr Mohamed Rakha — Client Profile
Last updated: 2026-10-11 (client of The Commando; free; Sparq Study's first teacher)

### Identity
- One-line description: IGCSE Business and IGCSE/O-level Economics teacher with 10+ years of experience, building a personal brand from zero.
- Role in The Commando group: client. Free work as Sparq's first teacher; Sparq gets linked only after he has used it for a while.
- Stage: launching (no accounts, branding or videos before Oct 2026).
- Markets: Egypt. Teaches at his own center, online, and part-time at more than one school. **Never name, show or hint at the schools.**
- Languages: Egyptian Arabic on camera; business terms stay in English inside the Arabic. Scripts are drafted in English first, then adapted with egyptian-voice.

### Offer
- Classes at his own center plus online classes. Format, seats, prices and A-level: ❓ (open questions).
- Hero: exam mastery. Turning knowledge into Application / Analysis / Evaluation marks.

### Audience
- Primary: IGCSE / O-level Business and Economics students. Secondary: parents (they pay). Details in the Claude Doc "Mr Rakha — Avatar Pack".

### Positioning
- Persona: **The Analyst.** Real-world business explained through the exam lens. Show, don't claim.
- Tagline: "Business, explained like it matters."
- Proof he has (needs verifying before use): grade results, testimonials, alumni now at university.
- Words to avoid (competitors own them): "Think Business" (Karim Ashmawy, Marwa Sadek), "more than teaching" (Mohamed Saeed), plain "real world" claims (Marwa Sadek launched with this on 8 Oct 2026).

### Voice & personality
- Calm, witty, charming, classy. Never pushy, never salesy.
- Signature line: "…and that's how it's examined" / «…وده بقى بيجي في الامتحان إزاي».
- Never grade-shame. ("A 5 isn't a verdict.")

### Visual identity
- Palette "Whisky Lounge": base #141112, bone #F2E8D8, cognac #8B4A2B, gold #C69B3C, taupe #8A8580. Inspired by the Lucifer series look, never devilish.
- Fonts: Cormorant Garamond (display), Inter (body), Caveat (handwriting).
- Logo: signet "R" in gold rings. Never at the end of a video.
- Look: editorial / FT style.
- Appearance: bald, groomed beard.

### Channels
- Instagram, Facebook and TikTok, cross-posted. Handle plan @mrrakha (accounts not created yet).

### Goals
- Phases: authority → demand → Sparq later. Students and parents should be "dying to join".

### Team & cast
- Hesitant on camera. Filmed teaching, plus a mix to test on shoot day.
- One shoot day per month, at his own center only. Students on camera need the consent form (in the Shoot Day 1 pack).

### Market
- Competitors and benchmarks: Assem El Nady (top TikToks are music montages), Marwa Sadek, Mohamed Saeed, Karim Ashmawy, Ahmed Marwan Economics, Mahmoud M. Said, Ms Arwa Zak, Mokhtar Atef, Mayada Fahmy; local benchmarks Dr Amr Hady and Hayssam Hamouda.
- Key dates: Cambridge IGCSE Business 0450 is replaced by **0264, first exams March 2027** (check against the syllabus before claiming).

### Files (single source of truth)
- Claude Docs: "Mr Rakha — Competitor Scan / Market Brief / Avatar Pack / Brand Book & Profile Kit / Strategy Plan / Reference Bank / Shoot Day 1 Production Pack".
- Delivered designs: carousels "0264" and "The Margin", profile photo, Facebook cover.
- Backup: repo I7Nosseir/chispa, branch claude/elegant-brown-yt0vko, folder commando/ (HANDOFF.md).

### Open items (2026-10-11)
- Rakha approves the scripts (⚠️ Arabic lines), the consent form and his outfit 2 days before the shoot.
- Answers needed: shoot date, format and seats, price, verified results, A-level?, who answers WhatsApp.
- The founder creates the accounts.

<!-- la-margrita -->
## La Margrita — Prospect Profile
Last updated: 2026-10-11 (prospect; free month of content offered by phone on 11 Oct 2026)

### Identity
- Neapolitan wood-fired pizza and pasta, Pyramids Gardens (Hadayek El Ahram), 3rd Gate, Fayoum Road, 22m street, opposite Chill Out, next to District 9 Mall. Open 2 PM to 2 AM. Phone 01009679258.
- Possible other branches: Talabat lists "6th of October / Mountain View"; an Aug 2025 post mentions Square One (Gamal Abdel Nasser Axis). ❓

### Offer
- About E£200–400 per person. Quattro Stagioni 320 EGP; 3 pizzas for 750 EGP (offer, Oct 2026). Best sellers on Talabat: Margherita Napoli, Salami, Chicken Ranch, Pesto. Delivery outside Pyramids Gardens (shop pays 50% of the fee).

### Channels (11 Oct 2026, via Apify)
- TikTok @la.margrita2: 175.1K followers, 2.4M likes. Viral peaks 13.7M / 1.8M / 1.8M; recent median ~6.8K plays.
- Instagram @lamargrita: 29.9K followers; peaks 3.1M and 1.17M; recent median ~3.4K plays.
- Facebook page: ~77K followers; recent median ~8K views.
- Google Maps: 4.6★ (126 reviews). Talabat: 3.4★ (25 reviews).

### What works / what's broken
- Works: customer reactions ("first time trying Neapolitan", "Australian tastes our pizza"), the truffle pizza, Hamza the staff character, everyday comedy.
- Broken:
  - four different names (La Margrita / La Margherita / LaMargrita / لامارجريتا); hashtag misspelled #lamrgrita
  - typos in captions
  - a broken 12-digit phone number in one post
  - captions that are hashtags only
  - defensive replies to bad reviews (burnt base, cleanliness, small portions)

### Deal
- Free month: content and quick fixes only (one name, bios, pins, captions, review-reply script, 4 weekly shoots). Phase 2 (paid): brand, packaging, logistics.
- Agree in writing first: end date, retainer price, case-study permission, their weekly order count as the baseline.
- Posting through Buffer Free; they connect their own accounts (never passwords).

### Files
- Full audit and call log: repo I7Nosseir/chispa, branch claude/elegant-brown-yt0vko, commando/clients/la-margrita/audit-2026-10-11.md.

<!-- _template -->
## [Business name] — Profile
Last updated: [date]

### Identity
- One-line description:
- Role in The Commando group:
- Stage (idea / launching / growing / established):
- Markets (country, cities):
- Languages / dialects:

### Offer
- Products / services (with prices or price ranges):
- Hero product:
- Seasonal or event offers:

### Audience
- Primary avatars (from avatar-creator):
- Secondary:
- Who pays vs who uses:

### Positioning
- Why us (vs alternatives):
- Promise in one sentence:
- Proof (results, numbers, testimonials):

### Voice & personality
- 3 personality words:
- Tone: 
- Words/phrases we use:
- Words/phrases we avoid:
- Humor level (none / light / bold):

### Visual identity
- Colors (hex):
- Fonts:
- Logo usage:
- Look & feel of videos (lighting, locations, editing style):

### Channels
- Platforms + handles:
- Website / links:
- Current followers & results (dated):

### Goals
- 3-month goal:
- 12-month goal:
- Main KPI:

### Team & cast
- Who appears on camera:
- Who films/edits:
- Consent notes (minors, staff):

### Market
- Main competitors:
- Gap we own:
- Key dates (seasons, exams, admissions, holidays):

### Do's & don'ts
- Always:
- Never: