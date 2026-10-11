# Prompt Library (Master Formula format)

Templates already follow SKILL.md §1–§10. Replace [brackets]. Upload real product photos as reference Elements (e.g. `@product`) and keep them "already there" (§5). Vary the cast. Run `scripts/prompt_lint.py` before generating.

---

## A. Stills (Nano Banana / GPT-Image / Soul)

**Perfume — Gulf souq shelf**
```
Close product photo, Sony A7 IV, 90mm macro, f/5.6. The exact [brand] [variant name] bottle from @product stands on a dark oud-wood shelf in a Deira souq perfume shop — already there, same label, cap and glass colour as the reference. Background: out-of-focus mirrored shelves with exactly 6 other unbranded bottles, warm fluorescent shop light. A small hard light from upper left draws a bright edge on the glass and a soft reflection on the wood. Fingerprints on the glass, 3 tiny dust specks, a price tag soft at the frame edge. True-to-life colour, slight film grain, unretouched.
NEGATIVE: no invented logo or text, label must exactly match @product, no extra branded bottles, no glow, no plastic sheen, no watermark or reference-image border bleed.
```

**Abaya — editorial in a real place**
```
Full-length fashion photo, 50mm, f/2.8. A [age] [Gulf / Egyptian] woman, natural makeup, visible skin texture, wears the exact [brand] abaya from @product — same fabric, embroidery and cut. She walks past a sunlit villa entrance in [Riyadh / Dubai] at 4 pm, mid-step, not looking at the camera. Warm side light, long shadow on a limestone wall. Fabric creases at the elbows; the hem lifts slightly in a light breeze. Muted colour, slight grain.
NEGATIVE: no change to embroidery pattern or colour, no extra people, no airbrushed skin, no studio backdrop.
```

**Jewelry — macro on skin**
```
Macro photo, 100mm, f/4. The exact [brand] necklace from @product rests on the collarbone of a woman in her [30s] — already there. Real skin: fine hairs, one small mole, natural shine. A single small hard light makes sparkle points on the stones. Black knit top, warm blurred interior. Slight focus falloff at the edges. Unretouched.
NEGATIVE: necklace design must exactly match @product, no extra jewelry, no plastic skin, no glow halo.
```

**Skincare — real bathroom (phone look)**
```
Snapshot on iPhone 1x lens, slightly tilted framing. The exact [brand] serum bottle from @product sits on a real bathroom shelf in a Cairo apartment next to exactly 1 toothbrush cup, 1 hair tie and 1 half-used tube. Morning light through a frosted window on the right, 4 water droplets on the bottle, edge of a mirror reflection. Everyday, unstyled.
NEGATIVE: label must exactly match @product, no extra products with logos, no studio lighting, no perfection.
```

**Food — Egyptian table (overhead)**
```
Overhead photo, 35mm, phone-like colour. A plate of [dish] on a real restaurant table in [area], with exactly 1 half-drunk glass of tea, 2 crumpled napkins, a few torn bread pieces counted as exactly 3, and a phone at the frame edge. Steam rising gently, sauce drips on the rim. Warm lamp light from top right; shadow of a hand reaching in.
NEGATIVE: no food-styling perfection, no extra plates, no text, no glow.
```

---

## B. Video (image-to-video from an approved keyframe; 5–8 s)

**Product reveal (silent, product truth)**
```
SCENE: [real surface + place], late afternoon, quiet shop.
CHARACTERS: one hand only, [skin tone], no face in frame. The exact [variant] [product] from @product is already on the surface from frame one.
BEATS:
 0.0-1.5s: Still shot of the [product] on the surface; light shifts slightly as a shadow passes.
 1.5-3.5s: The hand enters from the right and gently lifts the [product].
 3.5-5.0s: The hand slowly turns it a quarter so the label faces the camera.
CAMERA: locked-off tripod, no movement.
STYLE: Sony A7 IV, 90mm macro look, true-to-life colour, slight grain, one hard light from upper left.
NEGATIVE PROMPT: product and label must exactly match @product throughout, exactly 1 hand, no slow motion, no glow, no speech, no background bleed.
```

**UGC creator-style ad (silent visuals + separate VO — identity-stable, §8)**
```
SCENE: lived-in bedroom in [Cairo / Dubai], window light from the left, unmade bed edge in frame.
CHARACTERS: [IDENTITY LOCK] a [age] [Egyptian / Gulf] [man/woman] matching @creator exactly. The exact [product] from @product is already in their hand.
BEATS:
 0.0-1.5s: Vertical selfie framing; they glance at the lens and raise their eyebrows.
 1.5-3.0s: They bring the [product] closer to the camera, label facing the lens.
 3.0-5.0s: They tap the [product] twice with one finger and nod, mouth closed.
CAMERA: handheld front-camera at arm's length, slight natural shake, small reframe at 3.0s.
STYLE: iPhone front-camera look, auto exposure, light shadow noise, no grading.
NEGATIVE PROMPT: [IDENTITY LOCK], product must exactly match @product, no speech, no lip movement, exactly 1 person, no ring light reflection object, no text.
```
VO and captions added in edit (egyptian-voice script with transliteration; motion-studio captions). Frame as an ad, not a customer review (§15).

**Lifestyle B-roll**
```
SCENE: exit of a [Maadi café / Dubai mall], 5 pm sun, light street traffic.
CHARACTERS: [IDENTITY LOCK] person from @creator, holding the exact [product] from @product, already in hand.
BEATS:
 0.0-2.0s: They push the glass door open and step out.
 2.0-4.0s: They walk right at a natural pace, glancing at the street.
 4.0-5.0s: They pass a window; a soft lens flare crosses the frame.
CAMERA: handheld 35mm following slightly behind and to the side, small reframe.
STYLE: natural colour, slight grain, real street sound.
NEGATIVE PROMPT: [IDENTITY LOCK], product unchanged, exactly 1 main subject, no slow motion, no speech, no extra branded logos.
```

**Cinematic concept (one grounded impossible beat, §12)**
```
SCENE: [ordinary real place], [time], [atmosphere].
CHARACTERS: [IDENTITY LOCK] [person from @creator]. The exact [product] from @product already in [hand / on table].
BEATS:
 0.0-2.0s: [relatable tension, one atomic action].
 2.0-3.5s: [the product enters the moment, one atomic action].
 3.5-5.5s: [the ONE impossible beat, calm verb, tied to light/reflection/steam/scale].
 5.5-7.0s: [settles back to ordinary; genuine relief].
CAMERA: [named sequence, e.g. slow push-in → locked hold]. (If any orbit: camera motion only — no ring, halo or portal object.)
STYLE: Sony FX3, 35mm, f/2, 24 fps, motivated light from [source], subtle grain.
NEGATIVE PROMPT: [IDENTITY LOCK], product exactly as @product, [count discipline], no ring/halo/portal, no chaos or extra effects beyond the one beat, no speech.
```

---

## C. Character sheet (lock before any recurring person)
```
Character reference sheet: the same person in exactly 3 photos side by side — front, three-quarter, profile. [Age], [region], [hair], [distinguishing features: small scar on left eyebrow, freckles], wearing [wardrobe]. Neutral grey backdrop, soft even light, visible skin texture, unretouched.
NEGATIVE: the 3 photos must show the identical person, no changing jaw width or face proportions, no extra people.
```
