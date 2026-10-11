---
name: logo-system
description: Designs, builds and validates a brand logo through a decision pipeline — picks the right logo type (wordmark, lettermark, monogram, signet/emblem, combination, signature, masthead) from the brand's facts, generates 3 concept routes as real outlined SVGs in code, stress-tests each one automatically (small sizes, favicon, one-colour, reversed, every brand colour, squint/blur, avatar crop), scores them against Paul Rand's criteria plus hard gates, and delivers the full logo suite with usage rules. Use this skill whenever the user needs a logo, monogram, mark, signature, favicon, profile-picture mark, says they are "not good with logos", wants to check or critique a logo, or is building a brand board or brand identity for The Commando, Sparq Study, Ignite Uni, Nova, the founder, Mr Rakha or any client.
---

# Logo System

The founder doesn't judge logos by eye, so this skill decides with evidence: every concept is built as a real SVG, run through the same test sheet, scored, and only survivors reach him as a simple pick between two finished options.

Read `references/logo-principles.md` for logo types, Rand's criteria, typeface families and their feelings, clichés per category, and the misuse list. Scripts:
- `scripts/build_logo.mjs` — JSON spec → SVG with text converted to outlines (fonts fetched from Google Fonts, OFL only).
- `scripts/logo_test.mjs` — SVG → test sheet PNG + mono/reversed SVG variants.

Setup once per session:
```
mkdir -p <work>/tools && npm i --prefix <work>/tools opentype.js@1
export NODE_PATH=<work>/tools/node_modules:$(npm root -g)   # opentype.js + global playwright
```

## Pipeline

### 1. Inputs (never invent)
From `commando-profiles`, `brand-persona` and `color-system`: name and how people actually call the person/brand (e.g., "Mr Rakha"), personality words, archetype, audience, tagline, palette hexes, competitors' and sister brands' logos, where the logo will live (avatar, video watermark, notebooks, signage, embroidery, foil), any languages (Arabic lockup?). Missing and decisive → AskUserQuestion with tappable options; otherwise state the assumption.

### 2. Choose the logo type (decision tree — write the reasoning)
| If… | Then lean to |
|---|---|
| Personal brand, the name is short (≤ 8 letters) and is the product | **Wordmark** + a lettermark/monogram for small sizes |
| Name long or hard to say | **Lettermark / monogram** |
| Brand needs a "seal of authority" (education, finance, law, heritage, luxury) | **Signet / emblem-like monogram** (ring, seal, crest) — keep text *outside* the shape so it survives small sizes |
| New brand that must explain what it is | **Combination mark** (mark + name + descriptor) |
| Editorial, media, newsletter-like brand | **Masthead wordmark** |
| Handwritten signature | Only as a **secondary** sign-off; script faces fail small sizes and blur |
Every brand ends with a **system**, not one file: primary lockup, horizontal/stacked lockup, standalone mark for ≤ 64 px, and a one-colour version.

### 3. Generate 3 routes (distinct, not 3 colours of one idea)
Each route = concept name, the idea in one sentence (what it *means* — a story the founder can retell), type, typeface choice + why (see the feelings table in the reference), construction notes. Build each as JSON → `build_logo.mjs` → SVG (primary lockup + mark). Use only the approved palette; logo colours: anchor or bone on dark, ink on light, metal for thin details.

Craft rules: optical centring over mathematical (raise round letters slightly, check visually); tracking wider for all-caps (0.08–0.2 em), never for script; thin strokes ≥ 2% of mark height so they survive 32 px; one metal detail at most; no gradients, shadows, or bevels in the master logo.

### 4. Validate — run the test sheet for every route
```
node scripts/logo_test.mjs --logo <route>.svg --mark <route>-mark.svg \
  --colors "base=#…,anchor=#…,accent=#…,metal=#…" --name <route> --out <dir>/tests
```
Then **look at the PNG** (Read it) and judge each gate honestly.

**Hard gates (any fail → fix or demote to secondary):**
1. **16 px mark test:** the mark is recognisable at 16–24 px (favicon, tab, tiny avatar).
2. **Lockup legibility:** the name is readable at 24 px tall; descriptors/taglines inside a lockup must be readable at the smallest size that lockup is allowed — otherwise define a "no-tagline" lockup and a minimum size.
3. **One-colour test:** works in pure black and pure white with no colour help.
4. **Squint test:** at blur 4 px the overall silhouette still reads as a distinct shape.
5. **Avatar crop:** the mark fits a 110 px circle with ~15% margin and reads on base, anchor and accent.
6. **Distinctiveness:** not confusable with a competitor's or sister brand's logo, and not a category cliché (reference file list) unless deliberately subverted.
7. **Meaning check:** no unwanted reading in Arabic or English (letters forming words, shapes with religious/political/sexual readings, devil/occult cues).
8. **Name check:** trademark word search for the name in Egypt (ITDA — word elements only; logos can't be searched) and a quick web search for identical marks in education; report findings, recommend a lawyer before registration.

**Soft scores (1–5, Paul Rand's criteria + fit):** distinctive · visible · adaptable · memorable · universal · timeless · simple · fit to personality · story strength. Total /45.

### 5. Decide
Rank: hard-gate passes first, then soft score. Present the top 2 to the user with AskUserQuestion — each option = route name + one-line idea + "passes all tests" or the caveat; attach the test sheets first (SendUserFile) so he can see them. Recommend one in one sentence. Demoted routes may survive as secondary assets (e.g., a signature for sign-offs).

### 6. Deliver the logo suite
- SVG masters: primary lockup, horizontal/stacked, mark, one-colour black and white, reversed; PNG exports (512, 1024, 2048 wide) and a 1080 × 1080 avatar for each platform.
- **Usage rules:** clear space (e.g., height of the mark's letter "R" on all sides), minimum sizes (lockup with tagline, lockup without, mark), approved colour pairs (from colour-system), placement (top-left on covers; never at the end of a video, per the founder's course), and the misuse list (stretch, recolour, outline, shadow, rotate, busy photo backgrounds, tagline below minimum size).
- Hand the files to `brand-board` and `commando-design-studio`.

## Notes
- Fonts: OFL only (Google Fonts) so the founder owns usage without licences. Outlined SVGs mean no one needs the font to use the logo.
- If the founder later gets a designer, hand over the winning SVG + this skill's rationale as the brief — the tests become the acceptance criteria.
