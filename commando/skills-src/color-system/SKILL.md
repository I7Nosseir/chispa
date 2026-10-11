---
name: color-system
description: Builds and validates a brand colour palette from scratch with real colour theory — meaning of each hue and hex, harmony, perceptual (OKLCH) tonal scales, 60-30-10 roles, WCAG contrast, colour-blind safety, Egypt/MENA cultural fit, and distance from competitors and sister brands — then picks one palette through a scored decision pipeline and outputs a palette card. Use this skill whenever the user needs brand colours, a palette, "which colours", "luxury colours", hex codes, a colour to match a character, film, mood or person, says they are "not good with colours", or before any logo, brand board, carousel or design for a new brand or client (The Commando, Sparq Study, Ignite Uni, Nova, the founder, Mr Rakha or any client) — even if they only describe a feeling like "premium" or "like Lucifer".
---

# Colour System

The founder is not a colour person, so this skill makes the decision *for* him and shows its reasoning in plain words. He should only have to pick between 2–3 finished, validated palettes — never between raw hex codes.

Read `references/colour-theory.md` before choosing anything. It holds the hue meanings with hex anchors, saturation/value effects, harmony rules, luxury formulas, the combination library, and Egypt/MENA notes. Run `scripts/palette_check.py` on every candidate — numbers decide pass/fail, taste decides between the passes.

## Pipeline

### 1. Brief (from the profile, never invented)
Load `commando-profiles` (and the Avatar Pack / Competitor Scan docs if they exist). Write a 6-line colour brief:
- **Personality** (3 words) and **archetype** (from brand-persona)
- **Audience** and what they must *feel* in 1 second (e.g., parents: trust; students: "this is serious but not boring")
- **Reference** the user gave (a character, film, brand, place) — decode it in step 2
- **Must avoid**: competitor colours, sister-brand colours (from their profiles), anything the user banned
- **Media**: social (screens), print (packaging, notebooks, banners), video grade
- **Market**: Egypt/MENA unless stated

If anything above is unknown and it changes the answer, ask with AskUserQuestion (tappable options, max 4). Otherwise state the assumption and continue.

### 2. Decode the reference (when the user gives one)
A reference is a *mood*, not a costume. Extract **what** makes it feel the way it does, then drop what doesn't fit the brand.
- Collect the reference's real colours: wardrobe, sets, lighting, grade (search the web; cite).
- Name the feeling each colour carries in that context (e.g., Lucifer: black suit = control; whisky/amber bar light = indulgence; burgundy tux = ceremony; gold = status).
- Strike anything with the wrong association for this brand (e.g., hellfire red, horror, religion), and say why in one line.
- What remains is the **reference DNA**: 2–4 colour roles + lighting temperature + finish (matte, gloss, metallic).

### 3. Generate 3 candidate palettes
Each candidate follows a different, named strategy from the reference file (e.g., "Monochrome + metal", "Deep base + jewel accent", "Warm neutral + dark anchor"). Every candidate has exactly these roles:

| Role | Share | Job |
|---|---|---|
| Base (60%) | backgrounds, large fields | sets the mood |
| Anchor (≈25–30%) | text, logo, dark panels | carries contrast and authority |
| Accent (≤10%) | one signature colour | recognition; used sparingly |
| Metal / highlight (optional, ≤5%) | rules, monogram, icons | luxury cue; never body text |
| Neutral support (1–2) | captions, borders, cards | keeps layouts calm |
| Semantic (only if needed) | up/down, right/wrong | charts, marked answers |

Luxury rule of thumb (from research): fewer hues, low–mid saturation, deep values, one controlled accent, strong value contrast. Saturation signals excitement; low saturation signals sophistication and sincerity (Labrecque & Milne, 2012).

### 4. Validate (run the script — hard gates first)
```
python3 scripts/palette_check.py --name "<brand>-A" --colors base=#..., anchor=#..., accent=#..., metal=#..., neutral=#... \
   --avoid "#0099FF,#F97316" --out <dir>
```
It prints and saves: OKLCH values, a full contrast matrix, colour-blind (protan/deutan/tritan) distances, distance to every `--avoid` colour, a 9-step tonal scale per colour, and a swatch PNG.

**Hard gates (fail = fix or drop the candidate):**
1. Body-text pair (anchor on base, or base on anchor) ≥ 7:1 (WCAG AAA) — premium brands live on readability.
2. Any text pair used for captions/buttons ≥ 4.5:1; large display text ≥ 3:1.
3. Accent and metal are never assigned to body text if they fail 4.5:1 on their background — the script flags this; write the rule into the usage notes.
4. No two brand colours collapse under deuteranopia or protanopia (ΔE_ok < 0.06) **if** they are meant to carry different meanings (e.g., right/wrong). Decorative pairs may be close.
5. Signature colours (anchor, accent) ≥ 0.10 ΔE_ok from each competitor's and sister brand's colours — otherwise the brand blurs. Neutrals and metals that sit close only warn (all off-whites look alike); then the signature colours or a dark base must carry the difference.
6. Cultural check: no colour whose main local reading fights the brand (see reference file, Egypt/MENA section).

**Soft scores (1–5 each, write one line of reasoning):** fit to personality · fit to reference DNA · distinctiveness in the feed · versatility (print, video, dark mode, merch) · ages well (5+ years) · works with the founder's photos/skin tones/wardrobe.

### 5. Decide
Rank candidates: hard gates must all pass; then total soft score. Present the top 2 to the user with AskUserQuestion — each option = name + 1-line feeling + the 3 main hexes in words ("ink black, cognac, gold"). Recommend one and say why in one sentence. The founder picks; never ask him to tweak hex values himself — offer "warmer / cooler / darker / lighter" variants instead and re-run the script.

### 6. Output — the Palette Card
Save as a section of the brand's Brand Book doc (or a Claude Doc titled `[Brand] — Colour System`) and hand the hexes to `logo-system` and `brand-board`:
- Each colour: name (evocative, 1–2 words), role, HEX, RGB, OKLCH, CMYK approximation (from the script; tell the printer to proof), share %, and "means for us" line.
- Approved pairs table (text/background with ratios) and banned pairs.
- Tonal scale (9 steps) per colour for UI, charts and hover states.
- Usage rules: 60-30-10 split, where accent/metal may appear, photo grade notes (temperature, contrast), video lighting notes.
- The swatch PNG.

## Tips that matter
- Pure black (#000) and pure white (#FFF) look cheap on screens next to rich colours; prefer warm off-blacks (e.g., #111013) and paper whites (e.g., #F5F0E8) unless the brand is deliberately stark.
- Metals on screen are flat colours — gold reads as gold only next to a deep base, with a slightly darker/lighter pair for "sheen" in gradients (script gives the tonal scale).
- A colour's meaning comes from its *neighbours, saturation and amount* as much as its hue: burgundy at 5% = refinement; at 60% = heaviness.
- Re-run the check when a sister brand changes its palette.
