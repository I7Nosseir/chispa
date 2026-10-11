---
name: ai-video-prompt-engineering
description: Writes, checks and finishes AI video prompts (Kling, Higgsfield, Seedance, Veo/Omni) and AI image prompts (Nano Banana, GPT-Image, Soul) for photoreal output, in two style modes. Commercial hero covers bright product ads such as splash, podium and ingredient worlds. Real life covers UGC and documentary shots. Covers product shoots (perfume, abaya, jewelry, skincare, food), AI UGC ads, personal-branding clips and spec concepts, using the beat formula, identity and product lock, a prompt linter, a realism QA gate and finishing scripts. Use whenever the user asks to write, refine or troubleshoot a prompt, wants realistic or scroll-stopping AI images or video, or mentions Kling, Higgsfield, Veo, Omni, Seedance or Nano Banana. Also use when the user reports how a generation turned out, and log it in references/lessons-learned.md. Part of Commando OS.
---

# AI Video & Image Prompt Engineering

A living methodology for writing AI generation prompts that actually produce what was asked for, built from real trial-and-error across many generations. The core belief behind this skill: **the model will do exactly what it's told, including things you didn't mean to tell it** — most failures are ambiguity failures, not creativity failures.

**Before writing any prompt, check `references/lessons-learned.md`** — it's a running log of specific failures and fixes from real generations. If the current request resembles a logged failure, apply that fix proactively instead of waiting to rediscover it.

**After any generation the user reports on (success or failure), append a new entry to `references/lessons-learned.md`.** This is how the skill improves over time — see "Logging Feedback" at the bottom of this file.

## 0. The Workflow (every job)

1. **Brief:** brand, real product photos (2–4 angles, required for product work), audience (Egypt / Gulf), platform + aspect ratio, format (still, product set, UGC, concept film), the ONE idea (twist-lab / idea-elevator for concept films), credits budget.
2. **Pick the style mode first (§16):** **A, Real life** (documentary/UGC; `realism-playbook.md`) or **B, Commercial hero** (bright, staged, scroll-stopping ad; `commercial-recipes.md`). For product ads and outreach samples, the default is **B**. Then fill the realism card (see `references/realism-playbook.md` §2 for device presets):
   ```
   Capture device · Light (source, direction, time) · Exact local place · Cast (different from the last 3 pieces)
   3+ imperfections · What must stay exact (product/label/colour) · Sound (room tone + foley, or silent)
   ```
3. **Check `references/lessons-learned.md`**, then write the prompt with the Master Formula (§1) and the Negative Prompt Checklist (§9). Templates: `references/prompt-library.md`. **Before spending credits, run** `python3 scripts/prompt_lint.py prompt.txt` (`--image` for stills): it checks §1–§10 and §13 automatically and catches every failure already in the lessons log. Fix all ERRORs.
4. **Keyframes first:** generate 4–8 stills per shot, pick, fix by editing (not regenerating), lock character sheets. Then image-to-video from the approved still (start frame; end frame when the move matters). 2–4 takes per shot.
5. **Realism QA gate (§14):** contact sheet per clip, 12-point check, any fail = regenerate that shot and log why.
6. **Finish (§14):** edit, real-camera texture, room tone + foley, captions via commando-motion-studio.
7. **Rules + disclosure (§15)**, then senior-reviewer, founder approval, publish with the platform's AI label.
8. **Log** results in lessons-learned.md (see "Logging Feedback").

---

## 1. The Master Prompt Formula

Every short-form (5-10s) video prompt follows this structure:

```
SCENE: [location, time of day, atmosphere — specific, not generic]
CHARACTERS: [subject description, matching a reference image exactly — see Identity Lock]
BEATS (timestamped):
 0.0-Xs: [beat 1 — one atomic action]
 Xs-Ys: [beat 2 — one atomic action]
 ...
CAMERA: [named sequence of moves, e.g. "push-in → whip-pan → orbit → zoom-out"]
STYLE: [color grade, lighting]
NEGATIVE PROMPT: [see Negative Prompt Checklist below]
```

For static images (Nano Banana, GPT-Image), drop BEATS/CAMERA and instead describe the single composition, lighting, and framing directly, ending with the same kind of Realism Toolkit language (see §4) and negative-prompt discipline.

## 2. One Atomic Action Per Beat

Never compress a multi-step physical action into one beat. "Lid pops off" is actually two events (cap comes off, THEN foil seal peels) — compressing them causes the model to skip one or blend them badly.

**Bad:** `4.0-5.0s: Lid pops off, revealing the chips inside.`
**Good:**
```
4.0-4.8s: He grips the plastic lid and pulls it off, setting it aside — the foil seal underneath still intact.
4.8-5.6s: He peels back the foil seal separately, revealing the chips inside.
```

When in doubt, split it. A cheap extra beat is always safer than a merged one that gets partially dropped.

## 3. Exact Counts, Never Vague Quantities

"A few figures," "some coffee beans," "a couple of confetti pieces" — the model will invent its own number, and it's often wrong or inconsistent across the frame. Every countable element gets a hard number, stated once in the beat and reinforced in the negative prompt.

**Bad:** `A few toy figures celebrate around the trophy.`
**Good:** `Exactly 3 generic unbranded toy figures celebrate around the trophy.` + negative prompt: `exactly 3 figures, no more, no fewer`.

This applies to: people/figures in a scene, product units, confetti/particle counts, camera cuts in a fast-paced sequence, and repeated design elements (e.g. lightning-bolt icons, badge circles).

## 4. Identity Lock (for real people / real products)

**People:** define once, reuse everywhere a reference photo is used:
```
[IDENTITY LOCK] = face must exactly match reference image in every frame — no changing jaw width, no changing facial structure or proportions, no changing mouth shape, no morphing face during camera movement, no changing hair color or style
```
Two avatars in one campaign? Keep each locked against its own reference photo — never let one drift toward the other's features.

**Products:** name the specific variant once (flavor, color, model) and repeat it in every beat *and* the negative prompt. "The Original red Pringles can" must stay "the exact same Original red can" through every beat — otherwise the model quietly swaps flavor/color between shots.

**Realism Toolkit** (append to any prompt needing photorealism): `shot on 85mm portrait lens, f/1.4, shallow depth of field, natural window/key light, visible skin texture (pores, fine lines, subtle asymmetry), natural catchlight in both eyes, unretouched raw-photo quality, realistic fabric weave, slight film grain, 8k detail, no airbrushing, no plastic-skin smoothing.`

The 85mm look is for portraits and hero shots. For UGC and "real life" content, use a phone capture preset instead (`references/realism-playbook.md` §2): a cinematic lens on a creator-style clip is itself an AI tell.

## 5. Add vs. Replace vs. Already-There — Always Specify Which

If a reference photo already shows a plain/different version of an object the prompt needs to be the *real* branded product, the model needs to be told explicitly which operation is happening:

- **"Already there"** (most reliable): describe the real product as simply *already* in the character's hand/on their body from frame one. No edit event needed. Use this whenever possible.
- **"Add"**: the spot is empty in the reference (e.g. a bare hand, bare neckline) — describe the real object appearing there naturally, no swap logic needed.
- **"Replace"** (least reliable, avoid if possible): the reference shows a *different* object in that exact spot. A same-instant invisible substitution is the single most common cause of "it didn't show the right product" failures. If a replace is unavoidable, stage it as a **visible causal event** instead — a passerby hands over the correct item, a spin/transition reveals it — never an implied instant substitution.

## 6. Calm Verbs, Not Explosive Verbs

The model favors dramatic verbs over calm constraints stacked next to them. Asking for "the lid pops off explosively" while also demanding "coffee beans stay in place" will lose — the beans fly, because "explosively" wins. If something needs to stay controlled, don't pair it with an inherently violent/fast verb in the first place. Use gentle verbs from the start: "gently lift and fan apart like pages" instead of "burst apart," "a soft glow rises" instead of "a burst of light erupts."

This same principle governs **audio leakage**: bursts, pops, crunches, and impacts are exactly the visual events that trigger a model's native-audio system to add a sound effect even when told not to — calmer verbs reduce this risk too (though see §8, the real fix for audio is a settings toggle, not prompt wording).

## 7. The "No Ring/Halo/Portal" Guard

Abstract camera language ("orbit," "the camera circles the object") combined with strong material/color words ("gold," "glowing") gets literalized into an actual physical ring/halo/portal object appearing in the scene — a specific, repeatable failure mode. Any time a prompt says "orbit" or "circles around," add: `this describes camera motion only — no ring, halo, portal, or physical circular object should appear anywhere in the shot`, and repeat the guard in the negative prompt.

## 8. Audio: What Actually Works

- Prompt-level "no audio" instructions are **not reliably respected** by native-audio-capable models (Kling 3.0 etc.) — treat any text instruction as a weak second layer, not the fix.
- **The real fix is the platform's own "No Native Audio" setting/mode**, selected before generating — not prompt wording.
- Don't waste character budget on verbose audio-off paragraphs. One line in the negative prompt (`no speech`) is enough given point one above.
- **Dialogue/talking is the single biggest driver of face-identity drift** — the mouth gets reconstructed every frame to match invented speech. Silent clips (no talking) are far more identity-stable. Prefer silent storytelling over dialogue when identity consistency matters.
- **Non-English dialogue**: check the model's actual documented language support before assuming it works. Colloquial dialects (e.g. Egyptian Arabic) often aren't officially supported even when the base language is — verify directly with the tool rather than guessing, and note the finding in lessons-learned.md either way.

## 9. Negative Prompt Checklist

Every negative prompt should consider, in this order:
1. Identity lock (if a real person is in frame) — name the specific features, not a generic "stable face"
2. Product/variant consistency (if a real product is in frame) — "must exactly match the reference, no invented logo/color"
3. Count discipline — restate any hard numbers from the beats
4. Ring/halo/portal guard — if any beat uses "orbit" or "circle around"
5. Physical containment — if a beat needs something to *not* fly apart, scatter, or multiply
6. No reference-image bleed — `no background, border, or watermark artifacts bleeding into the scene` (relevant when using an Element/reference image of a product screenshot or logo)
7. `no speech` (see §8)

## 10. Real Products & Real Brands: What's Safe

- Referencing real, existing brands/products for **spec/concept work** (a portfolio piece, not implying an actual client relationship) is fine — always label it that way when shown publicly.
- **Never** depict a real, named, identifiable public figure/celebrity using or endorsing a product — this is impersonation/false-endorsement regardless of framing, full stop.
- **Never** use another company's copyrighted character design (e.g. Disney's specific visual design of a character, even if the underlying story is public domain) or trademarked toy/brand systems (e.g. LEGO's actual brick/minifig design). Describe an original design inspired by the same *idea* instead.
- When a real product's logo/label needs to appear, don't ask the AI model to render it from a text description — it garbles small text and logos reliably. Instead: upload the actual product photo as a reference Element (tagged, e.g. `@brandproduct`) and write it into the scene as already-present (§5), or composite the real logo in post (Canva/CapCut) after generation.
- Don't over-fabricate aesthetic language pointing at real luxury brands by name in a generation prompt (e.g. "Rolls-Royce grille") — it tends to pull toward reproducing that brand's actual badge/logo. Describe the *aesthetic* (chrome, tailored leather, warm light) instead.

## 11. Model Choice Matters More Than Prompt Polish

If a prompt keeps failing in the same specific way after 2-3 careful rewrites, the bottleneck may be the model's prompt-adherence ceiling, not the wording. Kling 3.0 has documented weaker instruction-following than newer/larger models (Seedance 2.0, Veo/Omni-class). When repeated failures cluster around the same kind of instruction (e.g., "stay in place" constraints never holding), it's worth testing a stronger model before continuing to iterate on wording alone. Log which model was used alongside each result in lessons-learned.md — this makes the pattern visible over time.

## 12. Story Beats That Actually Land

A generic "person holds product, smiles" reaction shot is the weakest version of any concept. What consistently tests better:
- **Tension → transformation → relief**: open on a real, relatable problem (stress, chaos, overwhelm), let the product/moment resolve it, end on genuine relief — not just satisfaction.
- **Tagline literalization**: stage the brand's actual slogan as a literal narrative event, not just an illustration of it.
- **One grounded "impossible" beat**, not full CGI chaos: tie the surprising moment to something physically plausible (light, reflection, steam, scale) so it reads as "how did they film that" rather than obviously fake. Full-chaos AI spectacle is a documented source of audience/brand backlash as of 2026 — restraint outperforms maximalism.

## 13. Format & Platform Practicals

- **Character limits**: many tools cap prompts around 2500 characters. Strip repeated boilerplate (verbose audio paragraphs, redundant restatements) before cutting substantive beat detail.
- **Bar/data charts with >13-15 categories** get unreadable in standard chart tools (labels desync from bars) — cap at ~13 and note what's been trimmed for transparency, or split into two charts.
- **PPTX/deck overlaps**: when fixing a presentation, always inspect exact shape positions and font sizes via the file itself (not just the visual render) before resizing anything — character-width-per-point estimates (~0.6-0.75in per char per 72pt for bold condensed fonts, calibrate per font if possible) let you compute a safe font size or box width instead of guessing repeatedly.

## 14. Realism QA Gate & Finishing

**QA (every clip, every still set):**
`python3 scripts/contact_sheet.py clip.mp4 --frames 12` → read the sheet and check, frame by frame:
1. hands/fingers · 2. product, label, logo, colour vs reference · 3. no garbled text · 4. same face/body across frames (identity lock held) · 5. physics (liquids, fabric, hair, gravity; nothing multiplies or morphs) · 6. one consistent light direction · 7. no warping background lines or duplicated people · 8. skin/material texture, no plastic sheen · 9. reads as the intended city/country · 10. real-time motion, not floaty · 11. sound: room tone/foley present, no leaked native audio, voice in sync · 12. "friend test" — someone without context doesn't question it.
Any ✗ = regenerate that shot (rewrite per lessons-learned if it's a known failure) and log a new entry if it isn't.

**Finish:** `python3 scripts/realism_finish.py in.mp4 --preset phone|cinema` or `in.png --preset still` (`--strength 0.5–1.5`). Adds grain, lens softness, mild compression, muted colour, -14 LUFS audio. Then room tone + foley on every touch; composite the real logo/label in post if it blurred (§10).

Detail on the 12 AI tells and their fixes, device presets, UGC and product-category rules: `references/realism-playbook.md`. Model choice per shot: `references/tool-matrix.md`.

## 15. Rules & Disclosure

- **Product truth:** the product looks exactly like the real one; AI builds the scene, never a better product. No invented claims, no clinic before/after.
- **People:** no real person's face or voice without written consent (the founder's own likeness is fine). Never celebrities or lookalikes (§10).
- **AI UGC is an ad, not a testimonial:** never present an AI person as a real customer giving a real review.
- **Labels:** TikTok requires an AI-generated label on realistic AI ad creative; Meta applies "AI info" labels and requires disclosure for social-issue/political ads. Turn the platform's AI toggle on for realistic AI content; check current policy pages before each campaign. Realism is craft, not deception.
- **Spec work:** label "spec concept — not commissioned" anywhere it's shown (§10).
- **Range:** don't reuse the same face in more than 2 portfolio pieces.
- Any on-screen text or VO goes through cringe-filter; Egyptian Arabic through egyptian-voice (with transliteration, per lessons-learned).

---

## 16. Style Modes: Real-Life vs Commercial Hero

"Photoreal" has two very different meanings, and mixing them gives a dark, moody, film-still look that impresses nobody:
- **Mode A, Real life:** looks like a phone or documentary photo of the real world. Lived-in clutter, imperfections, available light. For UGC, BTS and trust content. (`references/realism-playbook.md`)
- **Mode B, Commercial hero:** photoreal *materials* in a staged, big-budget studio shoot. The product fills 35–60% of the frame, exposure is bright, studio light is named, there's one strong visual idea (splash, levitation, ingredient world, nature podium, colour block), props come from the product's story, and the background is clean. For ads, grids, e-commerce and outreach samples. (`references/commercial-recipes.md`)

Never put Mode A imperfections (receipts, fingerprints, clutter, "late afternoon shop light") into a Mode B prompt, and don't run `realism_finish.py` on Mode B beyond `--strength 0.3`.

---

## Logging Feedback (how this skill develops)

Whenever the user reports back on an actual generation result — whether they upload the output, describe what went wrong, or confirm something worked well — do two things:

1. **Fix the immediate problem** using the principles above, or diagnose a new failure mode if none of them cover it.
2. **Append an entry to `references/lessons-learned.md`** using this format:

```
### [Short title] — [date if known, else "undated"]
**Tool/model:** [e.g. Kling 3.0, Higgsfield, Nano Banana]
**What was asked for:** [one line]
**What happened:** [what actually rendered]
**Root cause:** [why, in prompt-engineering terms]
**Fix applied:** [the specific wording/structural change]
**Generalizable rule:** [one sentence — this is what gets folded into SKILL.md itself if the pattern repeats 2+ times]
```

If the same root cause shows up in 2+ logged entries, promote it into a new numbered principle in this SKILL.md file (don't leave it buried only in the log) — that's what "the skill learns" actually means in practice: recurring lessons graduate from the log into the core methodology so they're applied automatically on the *first* attempt next time, not just after user feedback.
