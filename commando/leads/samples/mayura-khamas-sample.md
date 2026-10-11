# Mayura Khamas Perfumes: AI sample pack (spec concept)

**Lead:** Mayura Khamas Perfumes, Street 33B, Bur Dubai, UAE. +971 4 352 2319.
4.8★ from 856 Google reviews. Their Google listing links no website and no Instagram or TikTok.

**Why this sample:** they have a strong reputation but nothing online that shows the product. One real-looking product photo shows them what you'd do every week, before you've asked for anything.

## Step 0: get the real product (required)
1. Open Google Maps → "Mayura Khamas Perfumes Bur Dubai" → Photos. Save the 2–3 clearest photos of their bottles. If Maps doesn't have them, search the name on Instagram.
2. Crop each bottle tightly. This is your `@product` reference.
3. **If you can't find a clear bottle photo, skip Mayura** and use the next perfume lead (Adaa Lounge or R A M Perfumes). Never invent a bottle for a real brand.

## Realism card
| | |
|---|---|
| Capture | A: Sony A7 IV 90mm macro (product). B: iPhone 1x (in-hand snapshot) |
| Light | Late afternoon, one hard light from upper left, warm yellow shop light |
| Place | Old Bur Dubai souq (Meena Bazaar) perfume shop counter, wooden shelves of attar bottles |
| Cast | Hand only, man in his mid-30s, light-brown skin, plain silver ring (no face, so no identity drift) |
| Imperfections | Fingerprints, dust specks, receipt or tester strip, slight noise, motion blur on the shopkeeper's arm |
| Must stay exact | Bottle shape, cap, label, liquid colour |
| Sound (video) | Souq room tone, a soft glass tap on the counter |

## Prompt 1: hero still (Nano Banana / Soul). Send this one.
```
Close product photo, Sony A7 IV, 90mm macro, f/5.6. The exact Mayura Khamas perfume bottle from @product stands on the glass counter of a small perfume shop in the old Bur Dubai souq (Meena Bazaar) — already there, same bottle shape, cap, label and liquid colour as the reference. Behind it, out of focus: wooden shelves with exactly 8 unbranded glass attar bottles, a brass tray and warm yellow shop light. Late afternoon: one hard light from the upper left draws a bright edge along the glass and puts a small golden reflection of the liquid on the counter. Real-life details: 2 faint fingerprints on the glass, 3 tiny dust specks on the counter, a folded paper receipt soft at the bottom-right edge of the frame. True-to-life colour, slight film grain, unretouched raw-photo quality.
NEGATIVE: label, logo and bottle shape must exactly match @product, no invented text or Arabic letters, no extra branded bottles, no glow or sparkle effects, no smoke, no plastic sheen, no background or watermark bleeding in from the reference image.
```

## Prompt 2: in-hand snapshot (backup / second image)
```
Snapshot on iPhone 1x lens, vertical 4:5, slightly tilted framing. A man's hand, mid-30s, light-brown skin, a plain silver ring, holds the exact Mayura Khamas perfume bottle from @product at the shop counter in the Bur Dubai souq — already in his hand, label facing the camera, same shape, cap and colour as the reference. Background, soft focus: the shopkeeper's arm reaching for a shelf, wooden shelves of unbranded attar bottles, warm fluorescent light from above. Exactly 1 small paper tester strip on the counter. Natural skin texture with visible knuckle lines, slight motion blur on the shopkeeper's arm, auto exposure, a little noise in the shadows.
NEGATIVE: label and bottle must exactly match @product, exactly 1 hand in focus, no extra fingers, no invented logo or text, no studio lighting, no retouching, no glow.
```

## Prompt 3: 5-second video (Kling 3.0 image-to-video, start frame = Prompt 1 result)
Turn **No Native Audio** on in the settings. Add souq room tone in the edit.
```
SCENE: glass counter of a small perfume shop in the old Bur Dubai souq, late afternoon, quiet, warm yellow shop light.
CHARACTERS: one hand only, mid-30s, light-brown skin, plain silver ring, no face in frame. The exact Mayura Khamas perfume bottle from @product stands on the counter from frame one.
BEATS:
 0.0-1.5s: Still shot of the bottle; a soft shadow passes behind it as someone walks by.
 1.5-3.5s: The hand enters from the right and gently lifts the bottle.
 3.5-5.0s: The hand slowly turns the bottle a quarter so the label faces the camera.
CAMERA: locked-off tripod, Sony A7 IV 90mm macro look, no movement.
STYLE: true-to-life colour, slight grain, one hard light from the upper left catching the glass edge.
NEGATIVE PROMPT: bottle, cap and label must exactly match @product throughout, exactly 1 hand, no slow motion, no glow, no smoke, no speech, no background bleed.
```

All three prompts passed `prompt_lint.py` with 0 errors and 0 warnings.

## Generate → check → finish
1. Generate 4–6 versions of Prompt 1 with `@product` attached, and pick the best.
2. Check it against §14: label matches exactly? Bottle shape right? Any garbled text? Real texture? Does it read as the Bur Dubai souq?
3. If the label blurred, put the real label back in Canva from their photo.
4. Finish: `python3 scripts/realism_finish.py mayura.png --preset still --strength 0.8`
5. Optional: run Prompt 3, then `realism_finish.py clip.mp4 --preset phone` and `contact_sheet.py` to check it.
6. Report back how it came out, so it gets logged in lessons-learned.

## Message to send (Monday 10–11 AM Dubai time, WhatsApp +971 4 352 2319, a landline; DM instead if you find their Instagram)
> Hi Mayura Khamas team, I'm Ismail, a performance marketer and AI content creator. I made this image of your perfume as a quick example of what's possible without a studio shoot (attached). With 856 reviews you clearly have loyal customers, but there's no website or Instagram linked on your Google listing for new people to see the product. I make product visuals and ads for Gulf brands. Want me to send 3 more for free that you can use on Instagram or WhatsApp?

Day 3 follow-up: "Hi, just checking you saw the image. Happy to send the 3 free versions this week. Which bottle should I use?"

## Rules
- Label it "spec concept, not commissioned" if you ever show it in your portfolio.
- Never post it as if it's their ad, and never claim they're your client unless they say yes.
- If they use it in ads, turn on the platform's AI label.
