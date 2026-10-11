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

## V2: Commercial hero prompts (use these; 11 Oct feedback)
The first output looked real but read as a dark film still. Outreach samples need **Mode B: commercial hero**: bright, the product large in frame, one strong idea, props from the brand story. "Mayura" means peacock, so the props are peacock feathers in teal, emerald and gold. All four prompts passed `prompt_lint.py` with 0 errors and 0 warnings.

**Attach their real bottle photo as `@product` first.** The V1 label ("MAYURA KHAMAS" on a peacock cap) was invented by the model. Unless that's their actual bottle, don't send it: product truth.

### B1: Peacock pedestal (send this one)
```
High-end commercial product photography, Phase One camera, 100mm macro, f/11, crisp focus edge to edge. The exact Mayura Khamas perfume bottle from @product stands at the center of a bright, airy scene, filling about half the frame — already there, same bottle shape, cap, label and amber liquid as the reference. It sits on a smooth cream sandstone pedestal surrounded by exactly 5 real peacock feathers fanned out behind it like a crown, their blue-green eyes sharp and iridescent. Soft warm-white background with a gentle gradient to pale gold. Lighting: large softbox from the upper left for clean highlights on the glass, a thin rim light from behind that makes the amber liquid glow, a soft fill from the right. Exactly 3 small amber droplets resting on the pedestal. Bright, luxurious, clean, rich colour, glossy magazine advertising look.
NEGATIVE: label and bottle must exactly match @product, no invented text or logo, no extra bottles, no dark or moody lighting, no smoke, no ring or halo object, no plastic CGI look, no watermark or reference-image border bleed.
```
### B2: Amber splash
```
High-end commercial product photography, Sony A1, 90mm macro, f/8, high-speed flash freezing motion. The exact Mayura Khamas perfume bottle from @product floats in mid-air at a slight angle, filling about half the frame — already there, same shape, cap, label and amber liquid as the reference. Around it, a frozen splash of golden amber liquid curls in one clean ribbon from the lower left to the upper right, with exactly 7 crisp droplets suspended in the air. Background: smooth deep-teal to emerald gradient inspired by peacock colours. Lighting: strong key light from the right, white rim light outlining the glass, bright highlights in the droplets. Crisp, saturated, premium perfume-ad look.
NEGATIVE: label and bottle must exactly match @product, no invented text, exactly 7 droplets, no extra bottles, no muddy or dark exposure, no smoke, no glow halo, no plastic CGI look.
```
### B3: Dubai dune at golden hour
```
High-end commercial product photography, 85mm, f/5.6, golden hour. The exact Mayura Khamas perfume bottle from @product stands on the crest of a smooth sand dune in the Dubai desert, filling about a third of the frame — already there, same shape, cap, label and amber liquid as the reference. The sun sits low behind it on the left, shining through the amber liquid so the bottle glows warmly, with a long soft shadow across the sand. Clean wind ripples in the sand, a clear pale-blue sky fading to warm gold at the horizon, exactly 1 peacock feather lying in the sand beside the bottle. Bright, warm, airy, luxurious Gulf perfume campaign.
NEGATIVE: label and bottle must exactly match @product, no invented text, no extra bottles, no people, no dark or moody lighting, no lens-flare rings, no halo object, no CGI plastic look.
```
### B4: 6-second video from B1 (Kling, No Native Audio on)
```
SCENE: bright warm-white studio, soft gradient background to pale gold.
CHARACTERS: no people. The exact Mayura Khamas perfume bottle from @product stands on a cream sandstone pedestal from frame one, with exactly 5 peacock feathers fanned behind it.
BEATS:
 0.0-2.0s: Still hero shot; light slowly brightens across the glass from left to right.
 2.0-4.0s: The 5 feathers gently sway open a little, as if touched by a soft breeze.
 4.0-6.0s: A thin rim light grows behind the bottle and the amber liquid glows warmer.
CAMERA: slow push-in toward the label over 6 seconds, Phase One 100mm macro look.
STYLE: high-end commercial perfume ad, bright, clean, rich colour, softbox from upper left.
NEGATIVE PROMPT: bottle and label must exactly match @product throughout, exactly 5 feathers, no extra objects, no dark or moody lighting, no smoke, no ring or halo object, no speech.
```
Finish Mode B lightly: `realism_finish.py image.png --preset still --strength 0.3`, or skip it. Add any text or logo in Canva, never in the prompt.

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
