---
name: ai-realism-studio
description: Plans, prompts, quality-checks and finishes AI images and AI videos that pass as real footage — product shoots, lifestyle stills, AI UGC (creator-style talking ads), food, perfume, abaya, jewelry, real-estate and cinematic concept films — using Higgsfield (Kling 3.0, Seedance 2.0, Nano Banana, Soul), Veo 3.1 / Google Flow and similar tools. Builds a realism plan (camera, lens, light, imperfections, locale), keyframes first, then image-to-video one action per shot, runs a strict realism QA gate on every output, and finishes clips with real-camera texture (grain, lens, compression, room tone) via scripts. Use this skill whenever the user wants AI images, AI video, AI product photos, AI UGC, AI ads, an AI model/character, "make it look real", "realistic", "not AI-looking", or a spec concept for a brand or lead — for The Commando, Sparq Study, Ignite Uni, Nova, the founder, Mr Rakha, a client or a prospect.
---

# AI Realism Studio

Goal: output a viewer scrolls past as **real footage** — then, when told, can't believe it was AI. Realism comes from *specific camera behaviour, real light, real imperfection and local truth*, not from the word "photorealistic".

Read `references/realism-playbook.md` before the first prompt of a session. Prompts come from `references/prompt-library.md`. Tool choice from `references/tool-matrix.md`.

## Pipeline (each gate needs the founder's OK)

1. **Brief** (2 min): brand, product (real photos of the actual product are required for product work), audience (Egypt / Gulf), platform + aspect ratio, format (still, product set, UGC talker, cinematic concept), the ONE idea (from twist-lab / idea-elevator for concept films), deadline, budget in credits.
2. **Realism plan** — fill the card:
   ```
   REALISM CARD
   Capture device: (iPhone front cam / iPhone 1x / Sony FX3 35mm / 85mm macro …)
   Light: source + direction + time (window left, 5 pm sun, fluorescent shop, ring light)
   Place: exact local location (Maadi café, Deira souq stall, Zayed villa kitchen, Jeddah corniche)
   Cast: age, look, skin, wardrobe, region — DIFFERENT person from last 3 pieces
   Imperfections to include (pick 3+): handheld micro-shake, slight overexposure, lens flare, dust, crumbs, creased fabric, fingerprints, flyaway hair, background clutter, motion blur on hands
   What must stay exact: product shape, label, logo, colour, text
   Sound: room tone + 2 foley sounds (+ VO/dialogue language)
   ```
3. **Keyframes (stills first, always).** Generate 4–8 candidates per shot as images (Nano Banana / Soul / Seedream), with the real product photo as reference. Pick the best, fix details by editing (not regenerating), lock a **character sheet** (front, ¾, profile) for any recurring person.
4. **Motion.** Image-to-video from the approved keyframe (start frame, and end frame when the move matters). Rules: one action per shot, 3–6 s shots, camera move named (handheld push-in, locked tripod, slow orbit), physics described (steam rises, fabric settles). Generate 2–4 takes per shot; pick, never "hope".
5. **Realism QA gate** — run `scripts/contact_sheet.py` on every clip, read the sheet, score with the checklist in the playbook (hands, text/labels, faces between frames, physics, lighting consistency, background warping, "AI sheen"). **Any fail = regenerate that shot.** Log failures to the Lessons log.
6. **Finish.** Edit with real-edit rhythm (cuts on action, imperfect timing). Run `scripts/realism_finish.py` with the right preset (`phone` for UGC/social, `cinema` for brand films, `still` for images) to add grain, lens softness, compression and loudness-normalised audio. Add room tone + foley. VO via egyptian-voice for Arabic lines.
7. **Disclosure + delivery.** Apply the platform's AI label when publishing (see Rules). Hand off: commando-design-studio (layouts/carousels), commando-motion-studio (titles, captions), copy-engine (captions), senior-reviewer before anything is sent.

## Output per job
- Realism card · prompt pack (final prompts per shot, with model + settings + seed if available) · keyframes · picked takes · QA sheet with pass/fail per shot · finished files · Lessons log entry.

## Rules
- **Product truth:** the product must look exactly like the real one (shape, label, colour, size). AI may create the scene, never a better product than the client sells. No invented claims ("clinically proven", results, before/after for clinics).
- **People:** no real person's face or voice without written consent (no celebrities, no client's staff without consent, no lookalikes). Invented people only.
- **Testimonials:** an AI person must never be presented as a real customer giving a real review. AI UGC is framed as an ad ("creator-style"), not a fake review.
- **Labels:** TikTok requires an AI-generated label on realistic AI ad creative; Meta applies "AI info" labels and requires disclosure for social-issue/political ads. Always switch the platform's AI toggle on for realistic AI content; check the current policy pages before a campaign. Realism is for craft, not for deceiving the audience about what is real.
- **Spec work for leads/brands we don't work with:** mark "spec concept — not commissioned" in the portfolio; never post it on the brand's behalf.
- **Variety:** never reuse the same face across more than 2 portfolio pieces. Range (women, older people, Gulf and Egyptian looks) is part of the portfolio.
- Run cringe-filter on any on-screen text or VO; egyptian-voice for Egyptian Arabic.

## Lessons log (append after every job)
- 2026-10-11 (portfolio review): one male face appears in most concept films → reads as "one AI character", add range. Slides used blurry mid-motion frames → always export the sharpest hero frame for stills/thumbnails. Portfolio had no product sets or UGC talkers → that's what Gulf product brands buy; prioritise.
