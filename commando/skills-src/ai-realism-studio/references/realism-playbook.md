# Realism Playbook

Why AI looks like AI, and how to remove each tell.

## 1. The 12 tells (and the fix)
| Tell | Why it happens | Fix |
|---|---|---|
| Plastic, poreless skin; "AI sheen" | Model defaults to beauty-retouched stock | Ask for "natural skin texture, visible pores, slight shine on forehead, no retouching"; choose real-camera look (see §2); add grain in finish |
| Perfect symmetric composition, centred subject | Default framing | Off-centre framing, partial crop, foreground object partly blocking, "shot from slightly below/behind" |
| Soft, even, sourceless light | No light described | Name the source, direction, colour and time: "late-afternoon sun through a window on the left, warm, hard shadows on the wall" |
| Too clean, empty, catalogue backgrounds | Model removes clutter | Ask for lived-in detail specific to the place: receipts, chargers, napkins, a half-drunk tea glass, plastic chairs, AC unit, Arabic signage |
| Generic "anywhere" place | Location vague | Exact local setting: "Maadi street café, Road 9, metal chairs, morning traffic"; Gulf: "Deira souq stall, fluorescent lights, mirrored shelves of oud bottles" |
| Hands with wrong fingers, melting objects | Hard geometry + motion | Keep hands simple (one grip, little finger motion), shorter shots, keyframe the hand pose, reject takes with errors |
| Text/labels garbled | Models can't spell reliably | Put the real label in via reference image or composite it in post; avoid close-up readable text in motion |
| Faces change between frames | Identity drift | Character sheet + reference images; image-to-video from a fixed keyframe; shorter clips |
| Floaty, slow-motion, weightless motion | Default "cinematic" pacing | Describe real speed and physics: "quick natural movement, coffee sloshes slightly, cup set down with a small clink" |
| Camera glides too smoothly | Default gimbal motion | "handheld, slight natural shake, small reframe" for UGC; "locked-off tripod" for product |
| Over-saturated, HDR, teal-orange grade | Model's idea of "cinematic" | Ask for a real stock/device: "shot on iPhone 15, default camera, no filter" or "Kodak Portra 400 colours, muted"; grade down in finish |
| Silent or music-only clips | No sound design | Room tone + foley (cup, footsteps, traffic, AC hum); real VO pacing with breaths and small hesitations |

## 2. Capture-device presets (put one in every prompt)
- **Phone UGC:** "vertical 9:16, shot on iPhone front camera at arm's length, slight wide-angle distortion, auto exposure, a bit of noise in shadows, handheld, natural indoor light from a window".
- **Phone back camera (lifestyle):** "iPhone 1x lens, 26mm, deep focus, everyday snapshot, slightly imperfect framing".
- **Product studio:** "Sony A7 IV, 90mm macro, f/8, softbox from top-left, white sweep or real surface (marble, wood, linen), tiny dust specks, true-to-life colour".
- **Cinema:** "Sony FX3, 35mm prime, f/2, shallow depth of field, natural motivated light, 24 fps, subtle film grain".
- **Documentary/street:** "50mm, handheld, available light, candid, people not looking at camera".

## 3. Prompt anatomy (in this order)
1. Shot type + capture device (§2)
2. Subject (who, age, look, wardrobe — specific, varied)
3. Action — ONE action, real speed
4. Place — exact, local, lived-in
5. Light — source, direction, time, colour
6. Imperfections — at least 3
7. Camera movement (video) — named, with speed
8. Physics / what changes over the clip (video)
9. Product lock — "the bottle exactly as in the reference image, same label and cap"
10. Style negatives — "no retouching, no cinematic grading, no text overlays, no slow motion"

## 4. Motion rules (video)
- 3–6 s per generated shot; build length in the edit, not in one generation.
- Start frame = approved still; add an end frame when the move or reveal matters.
- One subject action + one camera move per shot.
- Name the speed ("over 2 seconds", "quick"), and the end state.
- Generate 2–4 takes; choose the one with the fewest tells, not the prettiest.
- Avoid: hands manipulating small objects for long, readable text in motion, crowds walking toward camera, mirrors, water pouring for more than 2 s (unless it's the hero and you take many tries).

## 5. UGC realism (creator-style talking ads)
- Script like speech, not copy: short sentences, one filler word, one self-correction, a real reaction ("honestly I didn't expect…"). Write in English, adapt with egyptian-voice (or Gulf Arabic for KSA/UAE when asked).
- Frame: front cam, eyes slightly off the lens sometimes, head partly cut, messy real room.
- Cut every 2–4 s (jump cuts like real creators), add native-style captions (motion-studio), product enters by hand within 3 s.
- Voice: natural pace with breaths; avoid a perfect studio voice. Lip-sync: prefer models with native audio (e.g., Veo) or a dedicated lip-sync step; reject any take with mouth drift.
- Present as an ad, never as a genuine customer review (see Rules).

## 6. Product work (perfume, abaya, jewelry, skincare, food)
- Always start from the client's real product photos (2–4 angles). Composite the real label/logo in post if the model blurs it.
- Perfume: glass refraction, liquid level, cap reflections; real surfaces (marble, oud wood, sand only if it fits); one light hitting the bottle edge.
- Abaya: fabric weight, drape and creases; real model poses; Gulf locations (mall corridor, villa entrance, majlis) or Cairo (Zamalek street) as fits the brand.
- Jewelry: macro, sparkle points from a small hard light, skin texture where it touches.
- Food: steam, crumbs, sauce drips, half-eaten states; real Egyptian tableware.

## 7. Realism QA checklist (score every shot; any ✗ = regenerate)
1. Hands: correct fingers, natural grip, no merging.
2. Product: shape, label, logo, colour identical to the reference.
3. Text: no garbled letters anywhere visible.
4. Identity: same face/body across frames and shots.
5. Physics: gravity, liquids, fabric, hair behave correctly; no morphing objects.
6. Light: one consistent source; shadows match direction.
7. Background: no warping lines, melting signage or duplicated people.
8. Skin/material: texture present; no plastic sheen.
9. Place: reads as the intended city/country.
10. Motion speed: real-time, not floaty.
11. Sound (video): room tone + foley present, voice in sync.
12. The "friend test": show it to someone without context — do they question it? If yes, find out what tipped them and log it.

## 8. Finishing (post)
- `scripts/realism_finish.py` presets: `phone` (social/UGC: slight sharpening, phone-style noise, mild compression), `cinema` (film grain, gentle halation-like softness, vignette, 24 fps), `still` (grain, subtle chromatic aberration, vignette, JPEG quality ~88).
- Grade down: lower saturation 5–10%, lift blacks slightly, keep skin natural.
- Mix: room tone under everything, foley on every touch, loudness -14 LUFS for social.
