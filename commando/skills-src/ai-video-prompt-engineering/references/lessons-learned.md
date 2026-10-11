# Lessons Learned Log

Real, observed failures and fixes from actual generations. Newest entries at the top. See the bottom of SKILL.md for the entry format and the promotion rule (2+ similar entries → becomes a numbered principle in SKILL.md itself).

---

### Portfolio review: one face everywhere, blurry thumbnails, no product/UGC work — 2026-10-11
**Tool/model:** Higgsfield (Kling 3.0 / Nano Banana), portfolio deck in Canva
**What was asked for:** A spec-concept AI video showcase (9 brands) to win clients and jobs.
**What happened:** Strong one-idea concepts, but the same male face appears in most films; several slides show blurry mid-motion frames; nothing shows product shoots or creator-style UGC, which is what Gulf product brands buy.
**Root cause:** Reused character reference across campaigns; thumbnails exported from arbitrary frames; portfolio built around concept films only.
**Fix applied:** Vary cast per piece (max 2 pieces per face); export the sharpest hero frame for any still; add product sets (perfume, abaya, jewelry, skincare) and UGC ads using prompt-library A/B templates.
**Generalizable rule:** Portfolio range (people, formats, product truth) matters as much as single-piece quality — plan the set, not just the piece.

### Ring/halo artifact from "orbit" + "gold lighting" — undated
**Tool/model:** Kling 3.0 (Higgsfield)
**What was asked for:** Camera orbiting around croissant layers during a bite, warm gold lounge lighting.
**What happened:** The model rendered an actual physical thick golden ring/coiled tube object floating in the scene, completely unrelated to camera movement.
**Root cause:** Abstract camera-motion language ("orbit") combined with strong material color words ("gold") got literalized into a physical object.
**Fix applied:** Explicit guard: "this describes camera motion only — no ring, halo, portal, or physical object should appear," repeated in the negative prompt.
**Generalizable rule:** → promoted to SKILL.md §7.

### Coffee beans flew despite "stay in place" instruction — undated
**Tool/model:** Kling 3.0 (Higgsfield)
**What was asked for:** Lid pops off explosively; beans must stay in place, not launch into the air.
**What happened:** Beans flew/scattered dramatically anyway, directly contradicting the explicit instruction.
**Root cause:** The dramatic verb "pops off explosively" overpowered the calmer "stay in place" constraint stacked right after it.
**Fix applied:** Rewrote using calm verbs from the start ("gently lift and fan apart") instead of pairing an explosive verb with a containment constraint.
**Generalizable rule:** → promoted to SKILL.md §6.

### "MATCH" clipped, "DAY" overlapping photo placeholder — undated
**Tool/model:** N/A (PPTX/LibreOffice rendering, not an AI generation)
**What was asked for:** A tournament brochure title reading "MATCH DAY" in a fixed-width black panel.
**What happened:** "MATCH" was missing its final "H"; "DAY" overlapped the photo placeholder below it.
**Root cause:** Font size too large for the box at actual render-engine character metrics — text overflowed both width and height bounds simultaneously, and estimates from theoretical character-width factors don't always match a given font's real metrics.
**Fix applied:** Reduced font size with a real safety margin (not a razor-thin calculated fit) and re-rendered to visually confirm rather than trusting the math alone.
**Generalizable rule:** → promoted to SKILL.md §13. Always re-render and visually verify after a calculated fix — don't assume the math was right the first time.

### Pringles can changed flavor/color across beats — undated
**Tool/model:** Higgsfield (image-to-video)
**What was asked for:** A single Pringles can (Original, red) shown consistently swiping off a screen, popping open, and being eaten from.
**What happened:** Three different-looking cans appeared across the sequence — the flavor/color wasn't consistent.
**Root cause:** The product was described generically ("a Pringles can") rather than as one specific, named variant repeated in every beat.
**Fix applied:** Named the exact variant once ("the Original red Pringles can") and repeated "the exact same Original red can" in every beat and the negative prompt.
**Generalizable rule:** → promoted to SKILL.md §4 (product identity lock).

### Lid-pop compressed two physical actions into one beat — undated
**Tool/model:** Higgsfield
**What was asked for:** "The lid pops off" as a single beat covering removing a plastic cap and a foil seal underneath.
**What happened:** The model conflated/skipped one of the two physical steps, producing an inconsistent result the user had to call out specifically ("detail opening the plastic lid alone then the paper covering the can").
**Root cause:** Two distinct physical actions were compressed into one instruction.
**Fix applied:** Split into two explicit beats — cap removal, then separate foil peel.
**Generalizable rule:** → promoted to SKILL.md §2.

### Egyptian Arabic dialogue rendered with wrong/ambiguous spelling — undated
**Tool/model:** Google Omni/Veo-class model
**What was asked for:** A short colloquial Egyptian Arabic line for a talking-head intro clip.
**What happened:** User reported "your Arabic writing was wrong so it read out wrong" — colloquial spelling is inherently non-standardized, and the written form didn't match natural pronunciation.
**Root cause:** Egyptian Arabic (like most spoken Arabic dialects) has no single standardized written form — ambiguous spelling can mislead a model's pronunciation even when the model itself supports the language.
**Fix applied:** Rewrote using simpler, less ambiguous colloquial verbs, provided a transliteration alongside the Arabic script, and recommended a native-speaker read-through before spending a generation on it.
**Generalizable rule:** For any non-Latin-script or dialect-heavy language, provide a transliteration alongside the script and flag that a native speaker should verify before generating — don't assume correctness just because the model claims language support.

### Identity drift correlated with talking/dialogue frames — undated
**Tool/model:** Kling 3.0
**What was asked for:** A talking-head clip with dialogue.
**What happened:** Comparing frames across the clip, jaw width, mustache thickness, and mouth shape all drifted most in frames where the mouth was mid-speech, and stayed closest to the reference in calmer frames.
**Root cause:** Dialogue/lip-sync forces the model to reconstruct the lower face every frame to match invented speech, which is the primary driver of identity drift.
**Fix applied:** Switched the whole campaign to silent clips with no dialogue; used the specific negative-prompt phrase naming jaw/proportions/mouth shape instead of a generic "stable face."
**Generalizable rule:** → promoted to SKILL.md §4 and §8.

### Two title words rendered fully overlapping each other — undated
**Tool/model:** N/A (PPTX/LibreOffice rendering)
**What was asked for:** "TOURNAMENT" and "TIMELINE" as two color-coded words side by side in a title.
**What happened:** The second word's bounding box started well inside the first word's box, causing the two words to render stacked directly on top of each other.
**Root cause:** Manual/template positioning error — the second shape's left-edge X coordinate was less than the first shape's right edge.
**Fix applied:** Recalculated safe X position for the second word based on the first word's actual character count and font size, with a wide safety margin; reduced font size on both words to guarantee both fit before a nearby image placeholder.
**Generalizable rule:** → promoted to SKILL.md §13. When two text boxes are meant to sit side by side, always confirm box2.left > box1.left + box1.actual_rendered_width, not just box1.nominal_width.

---

## Log Entry Template (copy this for new entries)

```
### [Short title] — [date if known, else "undated"]
**Tool/model:**
**What was asked for:**
**What happened:**
**Root cause:**
**Fix applied:**
**Generalizable rule:**
```
