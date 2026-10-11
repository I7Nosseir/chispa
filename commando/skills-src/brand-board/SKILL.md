---
name: brand-board
description: Creates a one-page brand board (branding scheme) — a tall, Behance-style brand sheet like the Nova board, with logo hero and tagline, overview and name meaning, a hero mockup, logo colour variations, brand colours with roles and shares, typography, applications (cards, notebooks, certificates, phone/post mockups) and a 3×3 social "branding" grid — rendered in code to PDF and PNG with no stock photos. Runs color-system and logo-system first when colours or a logo don't exist yet. Use this skill whenever the user asks for a branding scheme, brand board, brand sheet, brand identity, brand guidelines page, visual identity, "something like the Nova PDF", or wants to present or hand over a brand for The Commando, Sparq Study, Ignite Uni, Nova, the founder, Mr Rakha or any client — even if they only say "make him a brand".
---

# Brand Board

A brand board is the brand's front page: in one scroll, a stranger should understand who the brand is, recognise it again, and a designer should be able to apply it without asking. It is built from decisions made elsewhere — this skill assembles and presents them, it doesn't invent them.

Read `references/board-anatomy.md` first: it breaks down the Nova board (what each section does and why), the elevated rules, and the `brand.json` schema. The builder is `scripts/build_board.mjs`.

## Pipeline

1. **Gather decisions (never invent facts).**
   - Facts, offer, audience, voice: `commando-profiles` (+ Avatar Pack, Brand Book docs if they exist).
   - Personality and tagline: `brand-persona` (Mode A if missing).
   - Colours: `color-system` output. If none exists, run `color-system` now — the founder picks from validated palettes.
   - Logo: `logo-system` output (outlined SVGs: lockup, lockup + tagline, mark). If none exists, run `logo-system` now.
   - Unknowns that change the board (e.g., which products to show as applications, whether to include Arabic) → AskUserQuestion with tappable options (max 4), else state the assumption.

2. **Plan the sections** (from the anatomy): hero → overview (+ name/mark meaning) → hero mockup → logo variations (6) → colours → typography → applications (2–4) → branding grid (9) → closing line. Choose applications that are *real touchpoints for this brand* (a teacher: notebook, certificate, business card, reel cover; a gift brand: packaging; a café: cup, menu).

3. **Write the copy** in the brand's voice (brand-persona Mode B), then run it through `cringe-filter`. Every word on the board is real, usable copy — no lorem ipsum, no fake testimonials or numbers (mark placeholders clearly or leave them out).

4. **Fill `brand.json`** (schema in the reference) and build:
   ```
   NODE_PATH=$(npm root -g) node scripts/build_board.mjs <dir>/brand.json <dir>/out
   ```
   It writes `<slug>-board.html`, `.png` (2×) and a single tall-page `.pdf`, loading fonts from Google Fonts and drawing all mockups and textures in code.

5. **QA — look at the PNG yourself (Read it in slices)** and fix before showing anyone:
   - Nothing clipped or overflowing (mockup text, notebook titles, phone screens).
   - Every text/background pair is an approved pair from color-system (no gold body text, no text under 4.5:1).
   - Palette proportion on the whole board roughly matches the shares (base and anchor dominate; accent ≤ ~10% of the area).
   - The grid has rhythm: alternate dark/light and text/visual tiles; no two identical tiles side by side; at least one statement, one logo, one mockup, one quote/copy tile.
   - Logo variations use only approved colour maps; clear space respected.
   - Sister-brand check: put it next to the sister brands' boards — it must not be confusable.

6. **Deliver.** Send the PDF and PNG with SendUserFile; save the board's decisions (colours, fonts, logo rules) into the brand's profile via `commando-profiles` (offer the update), and hand the board to `commando-design-studio` as the source of truth for posts.

## Elevated rules (beyond the Nova board)
- Every colour on the board is labelled with **role and share**, not just a swatch.
- Typography is shown (Nova skipped it) with the use of each font, plus an Arabic face when the market needs it.
- The overview ends with the **meaning of the name or mark** — the story people retell.
- Logo notes state clear space, minimum sizes and "never at the end of a video".
- Applications replace "packaging" for service brands — show where the brand actually lives.
- The board stays one scroll (≈ 3,500–4,500 px at 760 px wide). If it grows longer, cut, don't shrink type.
