#!/usr/bin/env python3
"""Validate a brand palette: OKLCH, WCAG contrast matrix, colour-blind distances,
distance to competitor/sister colours, 9-step tonal scales, CMYK approximations,
and a swatch PNG.

Usage:
  python3 palette_check.py --name rakha-A \
      --colors "base:Bone=#F4EEE3,anchor:Ink=#111013,accent:Burgundy=#5A1A22,metal:Brass=#B8935A" \
      --avoid "sparq=#0099FF,ignite=#F97316" --out ./out

Each colour is role[:Name]=#HEX. Roles: base, anchor, accent, metal, neutral, semantic.
Writes <out>/<name>.json, <name>.md and <name>.png. Exit code 1 if a hard gate fails.
"""
import argparse, json, math, os, sys

# ---------- colour maths ----------
def hex_to_rgb(h):
    h = h.strip().lstrip('#')
    return tuple(int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))

def rgb_to_hex(rgb):
    return '#' + ''.join(f'{round(max(0, min(1, c)) * 255):02X}' for c in rgb)

def to_lin(c):
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4

def to_srgb(c):
    return 12.92 * c if c <= 0.0031308 else 1.055 * (c ** (1 / 2.4)) - 0.055

def lin_rgb(rgb):
    return tuple(to_lin(c) for c in rgb)

def oklab_from_lin(r, g, b):
    l = 0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b
    m = 0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b
    s = 0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b
    l_, m_, s_ = (math.copysign(abs(x) ** (1 / 3), x) for x in (l, m, s))
    return (0.2104542553 * l_ + 0.7936177850 * m_ - 0.0040720468 * s_,
            1.9779984951 * l_ - 2.4285922050 * m_ + 0.4505937099 * s_,
            0.0259040371 * l_ + 0.7827717662 * m_ - 0.8086757660 * s_)

def lin_from_oklab(L, a, b):
    l_ = L + 0.3963377774 * a + 0.2158037573 * b
    m_ = L - 0.1055613458 * a - 0.0638541728 * b
    s_ = L - 0.0894841775 * a - 1.2914855480 * b
    l, m, s = l_ ** 3, m_ ** 3, s_ ** 3
    return (4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s,
            -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s,
            -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s)

def oklch(hexv):
    L, a, b = oklab_from_lin(*lin_rgb(hex_to_rgb(hexv)))
    C = math.hypot(a, b)
    H = (math.degrees(math.atan2(b, a)) + 360) % 360
    return L, C, H

def oklch_to_hex(L, C, H):
    # reduce chroma until in sRGB gamut
    for _ in range(60):
        a, b = C * math.cos(math.radians(H)), C * math.sin(math.radians(H))
        lin = lin_from_oklab(L, a, b)
        if all(-1e-4 <= x <= 1 + 1e-4 for x in lin):
            return rgb_to_hex(tuple(to_srgb(max(0, min(1, x))) for x in lin))
        C *= 0.93
    return rgb_to_hex(tuple(to_srgb(max(0, min(1, x))) for x in lin))

def delta_e_ok(h1, h2, transform=None):
    r1, r2 = lin_rgb(hex_to_rgb(h1)), lin_rgb(hex_to_rgb(h2))
    if transform:
        r1, r2 = transform(r1), transform(r2)
    a, b = oklab_from_lin(*r1), oklab_from_lin(*r2)
    return math.dist(a, b)

def rel_lum(hexv):
    r, g, b = lin_rgb(hex_to_rgb(hexv))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b

def contrast(h1, h2):
    a, b = rel_lum(h1), rel_lum(h2)
    return (max(a, b) + 0.05) / (min(a, b) + 0.05)

def cmyk(hexv):
    r, g, b = hex_to_rgb(hexv)
    k = 1 - max(r, g, b)
    if k >= 1:
        return (0, 0, 0, 100)
    return tuple(round(x * 100) for x in ((1 - r - k) / (1 - k), (1 - g - k) / (1 - k), (1 - b - k) / (1 - k), k))

# Machado, Oliveira & Fernandes (2009) matrices, severity 1.0, applied in linear RGB
CVD = {
    'protan': ((0.152286, 1.052583, -0.204868), (0.114503, 0.786281, 0.099216), (-0.003882, -0.048116, 1.051998)),
    'deutan': ((0.367322, 0.860646, -0.227968), (0.280085, 0.672501, 0.047413), (-0.011820, 0.042940, 0.968881)),
    'tritan': ((1.255528, -0.076749, -0.178779), (-0.078411, 0.930809, 0.147602), (0.004733, 0.691367, 0.303900)),
}

def cvd_fn(kind):
    M = CVD[kind]
    def f(rgb):
        return tuple(max(0.0, min(1.0, sum(M[i][j] * rgb[j] for j in range(3)))) for i in range(3))
    return f

def tonal_scale(hexv, steps=9):
    L0, C0, H = oklch(hexv)
    out = []
    for i, L in enumerate([0.97, 0.92, 0.84, 0.74, 0.63, 0.52, 0.41, 0.31, 0.22][:steps]):
        taper = 1 - abs(L - 0.6) * 0.9  # lower chroma at the extremes
        out.append(oklch_to_hex(L, C0 * max(0.25, taper), H))
    return out

# ---------- report ----------
def parse_colors(s):
    items = []
    for part in [p.strip() for p in s.split(',') if p.strip()]:
        key, hexv = part.split('=')
        role, _, name = key.partition(':')
        items.append({'role': role.strip(), 'name': (name or role).strip(), 'hex': hexv.strip().upper()})
    return items

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--name', required=True)
    ap.add_argument('--colors', required=True)
    ap.add_argument('--avoid', default='')
    ap.add_argument('--out', default='.')
    args = ap.parse_args()
    cols = parse_colors(args.colors)
    avoid = [(p.split('=')[0].strip(), p.split('=')[1].strip()) for p in args.avoid.split(',') if '=' in p]
    os.makedirs(args.out, exist_ok=True)
    fails, warns = [], []
    rep = {'name': args.name, 'colors': [], 'contrast': [], 'cvd': [], 'avoid': []}

    for c in cols:
        L, C, H = oklch(c['hex'])
        c.update(oklch=[round(L, 3), round(C, 3), round(H, 1)], rgb=[round(x * 255) for x in hex_to_rgb(c['hex'])],
                 cmyk=cmyk(c['hex']), scale=tonal_scale(c['hex']))
        rep['colors'].append(c)
        if C > 0.18:
            warns.append(f"{c['name']} chroma {C:.2f} is high — reads loud, not luxury.")

    by_role = {c['role']: c for c in cols}
    for i, a in enumerate(cols):
        for b in cols[i + 1:]:
            r = contrast(a['hex'], b['hex'])
            use = 'body' if r >= 7 else 'AA text' if r >= 4.5 else 'large/display only' if r >= 3 else 'decor only'
            rep['contrast'].append({'a': a['name'], 'b': b['name'], 'ratio': round(r, 2), 'use': use})
    if 'base' in by_role and 'anchor' in by_role:
        r = contrast(by_role['base']['hex'], by_role['anchor']['hex'])
        if r < 7:
            fails.append(f"Gate 1: base/anchor body-text contrast {r:.2f} < 7:1.")
    for role in ('accent', 'metal'):
        if role in by_role and 'base' in by_role:
            r = contrast(by_role[role]['hex'], by_role['base']['hex'])
            if r < 4.5:
                warns.append(f"Gate 3: {by_role[role]['name']} on base is {r:.2f}:1 — never body text; display ≥ 3:1 only." if r >= 3
                             else f"Gate 3: {by_role[role]['name']} on base is {r:.2f}:1 — decoration only (lines, foil), no text.")

    for i, a in enumerate(cols):
        for b in cols[i + 1:]:
            row = {'a': a['name'], 'b': b['name'], 'normal': round(delta_e_ok(a['hex'], b['hex']), 3)}
            for k in CVD:
                row[k] = round(delta_e_ok(a['hex'], b['hex'], cvd_fn(k)), 3)
            rep['cvd'].append(row)
            if min(row['protan'], row['deutan']) < 0.06 and {a['role'], b['role']} & {'semantic'}:
                fails.append(f"Gate 4: {a['name']} vs {b['name']} collapse for colour-blind viewers.")

    for c in cols:
        for label, h in avoid:
            d = delta_e_ok(c['hex'], h)
            rep['avoid'].append({'color': c['name'], 'vs': label, 'hex': h, 'deltaE': round(d, 3)})
            if d < 0.10:
                near_neutral = c['oklch'][1] < 0.03
                if c['role'] in ('accent', 'anchor') and not near_neutral:
                    fails.append(f"Gate 5: {c['name']} is too close to {label} {h} (ΔE {d:.3f} < 0.10).")
                else:
                    warns.append(f"Gate 5 (soft): {c['name']} is close to {label} {h} (ΔE {d:.3f}) — fine for a neutral/metal, "
                                 "but the signature colours must carry the difference.")

    rep['hard_gate_failures'], rep['warnings'] = fails, warns
    with open(os.path.join(args.out, f'{args.name}.json'), 'w') as f:
        json.dump(rep, f, indent=2)

    md = [f"# Palette check — {args.name}", '', '| Role | Name | HEX | OKLCH (L C H) | RGB | CMYK (approx) |', '|---|---|---|---|---|---|']
    md += [f"| {c['role']} | {c['name']} | {c['hex']} | {' '.join(map(str, c['oklch']))} | {','.join(map(str, c['rgb']))} | {','.join(map(str, c['cmyk']))} |" for c in cols]
    md += ['', '## Contrast', '| Pair | Ratio | Allowed use |', '|---|---|---|']
    md += [f"| {r['a']} / {r['b']} | {r['ratio']}:1 | {r['use']} |" for r in sorted(rep['contrast'], key=lambda r: -r['ratio'])]
    md += ['', '## Colour-blind distance (ΔE OKLab; <0.06 = looks the same)', '| Pair | Normal | Protan | Deutan | Tritan |', '|---|---|---|---|---|']
    md += [f"| {r['a']} / {r['b']} | {r['normal']} | {r['protan']} | {r['deutan']} | {r['tritan']} |" for r in rep['cvd']]
    if avoid:
        md += ['', '## Distance to competitor / sister colours (<0.10 = too close)', '| Colour | vs | ΔE |', '|---|---|---|']
        md += [f"| {r['color']} | {r['vs']} {r['hex']} | {r['deltaE']} |" for r in rep['avoid']]
    md += ['', '## Tonal scales (97 → 22 lightness)'] + [f"- {c['name']}: {' '.join(c['scale'])}" for c in cols]
    md += ['', '## Result', ('FAIL — ' + '; '.join(fails)) if fails else 'PASS — all hard gates.'] + [f'- ⚠ {w}' for w in warns]
    with open(os.path.join(args.out, f'{args.name}.md'), 'w') as f:
        f.write('\n'.join(md))

    try:
        swatch(cols, os.path.join(args.out, f'{args.name}.png'), args.name)
    except Exception as e:  # PIL missing is not fatal
        print('swatch skipped:', e)
    print('\n'.join(md))
    sys.exit(1 if fails else 0)

def swatch(cols, path, title):
    from PIL import Image, ImageDraw, ImageFont
    def font(sz, bold=False):
        for p in ('/usr/share/fonts/opentype/inter/Inter-SemiBold.otf' if bold else '/usr/share/fonts/opentype/inter/Inter-Regular.otf',
                  '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'):
            if os.path.exists(p):
                return ImageFont.truetype(p, sz)
        return ImageFont.load_default()
    W, sw, H = 1600, 1600 // max(1, len(cols)), 900
    im = Image.new('RGB', (W, H), '#FFFFFF')
    d = ImageDraw.Draw(im)
    for i, c in enumerate(cols):
        x = i * sw
        d.rectangle([x, 0, x + sw, 560], fill=c['hex'])
        ink = '#111111' if rel_lum(c['hex']) > 0.25 else '#F5F5F5'
        d.text((x + 28, 470), c['name'], font=font(34, True), fill=ink)
        d.text((x + 28, 515), f"{c['role']}  {c['hex']}", font=font(22), fill=ink)
        for j, s in enumerate(c['scale']):
            d.rectangle([x, 580 + j * 30, x + sw, 580 + (j + 1) * 30], fill=s)
    d.text((28, 860), title, font=font(22), fill='#555555')
    im.save(path)

if __name__ == '__main__':
    main()
