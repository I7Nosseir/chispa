# Palette check — rakha-C-midnight-library

| Role | Name | HEX | OKLCH (L C H) | RGB | CMYK (approx) |
|---|---|---|---|---|---|
| base | Ivory | #F5F0E8 | 0.957 0.012 79.8 | 245,240,232 | 0,2,5,4 |
| anchor | Midnight | #0F172A | 0.208 0.04 265.8 | 15,23,42 | 64,45,0,84 |
| accent | Oxblood | #6E1423 | 0.356 0.123 17.5 | 110,20,35 | 0,82,68,57 |
| metal | Brass | #A8834A | 0.633 0.087 76.9 | 168,131,74 | 0,22,56,34 |
| neutral | Smoke | #6B6460 | 0.508 0.011 51.9 | 107,100,96 | 0,7,10,58 |

## Contrast
| Pair | Ratio | Allowed use |
|---|---|---|
| Ivory / Midnight | 15.74:1 | body |
| Ivory / Oxblood | 10.36:1 | body |
| Ivory / Smoke | 5.12:1 | AA text |
| Midnight / Brass | 5.11:1 | AA text |
| Oxblood / Brass | 3.36:1 | large/display only |
| Ivory / Brass | 3.08:1 | large/display only |
| Midnight / Smoke | 3.07:1 | large/display only |
| Oxblood / Smoke | 2.02:1 | decor only |
| Brass / Smoke | 1.66:1 | decor only |
| Midnight / Oxblood | 1.52:1 | decor only |

## Colour-blind distance (ΔE OKLab; <0.06 = looks the same)
| Pair | Normal | Protan | Deutan | Tritan |
|---|---|---|---|---|
| Ivory / Midnight | 0.751 | 0.742 | 0.756 | 0.753 |
| Ivory / Oxblood | 0.613 | 0.662 | 0.594 | 0.608 |
| Ivory / Brass | 0.332 | 0.351 | 0.327 | 0.327 |
| Ivory / Smoke | 0.448 | 0.45 | 0.448 | 0.448 |
| Midnight / Oxblood | 0.205 | 0.095 | 0.184 | 0.238 |
| Midnight / Brass | 0.444 | 0.416 | 0.455 | 0.444 |
| Midnight / Smoke | 0.305 | 0.295 | 0.31 | 0.307 |
| Oxblood / Brass | 0.298 | 0.326 | 0.278 | 0.281 |
| Oxblood / Smoke | 0.191 | 0.213 | 0.149 | 0.196 |
| Brass / Smoke | 0.147 | 0.131 | 0.152 | 0.142 |

## Distance to competitor / sister colours (<0.10 = too close)
| Colour | vs | ΔE |
|---|---|---|
| Ivory | sparq-blue #0099FF | 0.348 |
| Ivory | sparq-parchment #F4F0E8 | 0.001 |
| Ivory | ignite-orange #F97316 | 0.308 |
| Ivory | nova-cocoa #52423B | 0.563 |
| Ivory | nova-sand #BFB290 | 0.195 |
| Midnight | sparq-blue #0099FF | 0.484 |
| Midnight | sparq-parchment #F4F0E8 | 0.75 |
| Midnight | ignite-orange #F97316 | 0.543 |
| Midnight | nova-cocoa #52423B | 0.196 |
| Midnight | nova-sand #BFB290 | 0.565 |
| Oxblood | sparq-blue #0099FF | 0.419 |
| Oxblood | sparq-parchment #F4F0E8 | 0.612 |
| Oxblood | ignite-orange #F97316 | 0.364 |
| Oxblood | nova-cocoa #52423B | 0.108 |
| Oxblood | nova-sand #BFB290 | 0.427 |
| Brass | sparq-blue #0099FF | 0.273 |
| Brass | sparq-parchment #F4F0E8 | 0.332 |
| Brass | ignite-orange #F97316 | 0.138 |
| Brass | nova-cocoa #52423B | 0.249 |
| Brass | nova-sand #BFB290 | 0.139 |
| Smoke | sparq-blue #0099FF | 0.252 |
| Smoke | sparq-parchment #F4F0E8 | 0.448 |
| Smoke | ignite-orange #F97316 | 0.264 |
| Smoke | nova-cocoa #52423B | 0.116 |
| Smoke | nova-sand #BFB290 | 0.26 |

## Tonal scales (97 → 22 lightness)
- Ivory: #F8F5EF #E8E4DE #CECAC4 #AEAAA4 #8D8881 #6C6862 #4D4A44 #33302B #1D1A17
- Midnight: #F1F5FF #DCE5F8 #C1CBE0 #A0ABC2 #7E89A1 #5F697F #424A5D #293040 #151A27
- Oxblood: #FFF1F1 #FEDBDB #FCB5B7 #E68E92 #C7696E #A04A50 #782F35 #55181F #37030C
- Brass: #FFF3E3 #FDE0B7 #E4C599 #C6A574 #A6824B #83622E #604516 #422B00 #261700
- Smoke: #F9F4F1 #E9E3E0 #CFC9C5 #B0A9A5 #8F8783 #6E6764 #4F4946 #342F2D #1D1A18

## Result
PASS — all hard gates.
- ⚠ Gate 3: Brass on base is 3.08:1 — never body text; display ≥ 3:1 only.
- ⚠ Gate 5 (soft): Ivory is close to sparq-parchment #F4F0E8 (ΔE 0.001) — fine for a neutral/metal, but the signature colours must carry the difference.