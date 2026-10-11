# Brand board anatomy

Contents: 1. The Nova board, decoded · 2. How boards like it are made (industry process) · 3. Section rules · 4. brand.json schema · Sources

## 1. The Nova board, decoded (Nova.pdf, Dec 2025)
Made in Adobe InDesign as **one tall page** (566 × 2,183 pt ≈ 760 × 2,900 px), the Behance "one-page brand sheet" format. Reading order and job of each block:

| # | Block | What's on it | Job |
|---|---|---|---|
| 1 | Hero | lowercase hand-drawn wordmark "nova" + tagline "Make your swipe iconic." on white | first recognition: name + promise |
| 2 | Overview | sand band, centred heading + 4-line paragraph: what the brand is, the name meaning (a nova = sudden brightening of a star → small details, big impact), why it exists | positioning in one breath |
| 3 | Hero mockup | full-width photo: cocoa card with white logo on linen texture | mood: material, light, premium |
| 4 | Logo colour variations | 6 tiles: every approved logo/background pair from the 3-colour palette | shows the logo system + allowed pairs |
| 5 | Brand colours | one strip: white / sand #BFB290 / cocoa #52423B | the palette (no names or roles — a gap) |
| 6 | Packaging | two mockups: pocket envelope with window showing the stickered card | the product in real life |
| 7 | Branding grid | 3×3 social feed: product mockups, a stacked bold statement ("THIS IS HOW YOUR CARD SHOULD LOOK"), small copy tiles ("ORDER YOUR CUSTOM NOVA STICKER TODAY — PEEL, STICK, DONE."), an engagement tile ("WHICH ONE WOULD YOU CHOOSE?"), a logo tile, a quote tile on cocoa | how the brand behaves on Instagram |
| 8 | Closing line | "Create your own design or choose from our curated collection." | the offer, signed off |

What makes it work: one palette used everywhere (white/sand/cocoa), one typeface family (Avenir) in three weights, generous white space, textured surfaces instead of flat colour, real copy in the brand's voice, grid rhythm (dark/light, text/visual alternate).

Gaps to elevate: no colour names, roles or proportions; no typography section; no logo rules (clear space, minimum size); no accessibility check (white on sand = 2.1:1 is used for text in the logo variation); applications limited to packaging.

## 2. How boards like it are made (industry process)
Strategy → mood board → identity design → brand board → full guidelines.
1. **Strategy:** personality words, audience, positioning (our profiles + brand-persona).
2. **Mood board:** collect images, textures, type and colour that carry the feeling; annotate why each fits; test with audience members.
3. **Identity design:** logo system (primary, secondary, mark, mono, reversed), palette (2–3 primaries + neutrals, hex/RGB/CMYK), type hierarchy (heading/body/accent), imagery style.
4. **Brand board:** one page that presents the system with real applications (Behance one-page brand sheets; larger brand books run 35–100 pages).
5. **Guidelines:** clear space, minimum sizes, misuse, voice and tone, templates.

## 3. Section rules
- **Hero:** logo large (90–130 px tall at 760 wide) + tagline; on the brand's base colour or white. Nothing else.
- **Overview:** ≤ 70 words + one-line meaning of the name/mark. Centred, on the second colour.
- **Hero mockup:** one object, one surface texture, soft shadow; the object is the most-used touchpoint (business card, product, notebook).
- **Logo variations:** exactly 6, every pair approved by color-system; include white background and one mark-only tile.
- **Colours:** width proportional to share; name + hex + role + share on each.
- **Typography:** "Aa" specimens + family + use; one sample sentence in the display face, written in the brand voice.
- **Applications:** 2–4 real touchpoints in a 2-column grid; textured surfaces from the palette.
- **Branding grid:** 9 tiles, 3 × 3; at least one statement, one logo, one mockup, one quote/copy, one data or engagement tile; alternate dark and light; real captions.
- **Closing:** the offer or descriptor in one line.

## 4. brand.json schema
```json
{
  "name": "Mr Rakha", "slug": "rakha", "width": 760,
  "tagline": "…",
  "logo": {"lockup": "path.svg", "tagline": "path.svg", "mark": "path.svg"},
  "colors": [{"role": "base|anchor|accent|metal|neutral", "name": "…", "hex": "#…", "share": 55}],
  "colorNotes": "…",
  "fonts": {"display": {"family": "…", "weight": 600, "use": "…"}, "body": {"family": "…", "use": "…"},
            "arabic": {"family": "…", "use": "…"}, "sample": "…"},
  "hero": {"bg": "#…", "logo": "lockup", "h": 96, "tagColor": "#…", "map": {}},
  "overview": {"bg": "#…", "fg": "#…", "title": "OVERVIEW", "text": "…", "meaning": "…"},
  "heroMockup": {"type": "card|card-pair|notebook|certificate|phone", "surface": "#…", "bg": "#…", "back": "#…", "logo": "mark", "logoH": 80, "backLines": ["…"]},
  "logoVariations": [{"bg": "#…", "logo": "lockup|mark", "map": {"#fromHex": "#toHex"}, "h": 46, "border": false}],
  "logoNotes": "…",
  "applications": [{"type": "notebook|certificate|phone|card|card-pair", "surface": "#…", "bg": "#…", "…": "…"}],
  "grid": [{"type": "statement|copy|logo|mockup|quote|chart", "bg": "#…", "fg": "#…", "text": "…", "kicker": "…", "small": "…", "mockup": "notebook|phone|card|certificate"}],
  "closing": "…", "closingColor": "#…", "headingColor": "#…"
}
```
`map` recolours the logo SVG by exact hex (e.g., bone text → black on a light background). Mockup options: `card` (logo, rotate), `card-pair` (back lines + front logo), `notebook` (band, title), `certificate` (title, line, border), `phone` (kicker, title). Statement text uses `\n` for stacked lines.

## Sources
- Behance brand presentation structures — https://www.behance.net/search/projects/branding%20presentation%20%20brand%20guidelines
- Brand style guide essentials (logo variants, palette, type hierarchy, imagery, voice) — https://venngage.com/blog/brand-style-guide/ · https://majoli.io/en/blog/kit-de-marque-la-checklist-complete-des-elements-indispensables-en-2026
- Mood board → brand board process — https://www.ebaqdesign.com/blog/brand-mood-board
- 60-30-10 and accessible palettes — https://visionaustralia.org/business-consulting/digital-access/Creating-accessible-digital-colour-palettes-60-30-10-design-rule
