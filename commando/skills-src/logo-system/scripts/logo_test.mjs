#!/usr/bin/env node
// Logo validation sheet. Renders a logo (and optional mark/monogram) through the stress tests
// a real logo must survive, writes a PNG test sheet plus mono/reversed SVG variants.
//
// Usage:
//   NODE_PATH=$(npm root -g) node logo_test.mjs --logo logo.svg [--mark mark.svg] \
//     --colors "base=#141112,anchor=#F2E8D8,accent=#8B4A2B,metal=#C69B3C" --name rakha-A --out ./tests
// Uses the Playwright Chromium already installed in the environment.
import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';
const require = createRequire(import.meta.url);
const { chromium } = require('playwright');

const args = Object.fromEntries(process.argv.slice(2).reduce((a, v, i, arr) => (v.startsWith('--') ? [...a, [v.slice(2), arr[i + 1]]] : a), []));
const out = args.out || '.';
fs.mkdirSync(out, { recursive: true });
const name = args.name || path.basename(args.logo, '.svg');
const colors = Object.fromEntries((args.colors || 'base=#FFFFFF,anchor=#111111').split(',').map(p => p.split('=').map(s => s.trim())));
const logo = fs.readFileSync(args.logo, 'utf8');
const mark = args.mark ? fs.readFileSync(args.mark, 'utf8') : null;

// Recolour every fill/stroke to one colour (keeps "none").
const mono = (svg, c) => svg.replace(/(fill|stroke)="(?!none)[^"]*"/g, `$1="${c}"`).replace(/<rect width="100%" height="100%"[^>]*\/>/, '');
const strip = svg => svg.replace(/<rect width="100%" height="100%"[^>]*\/>/, '');
const variants = {
  [`${name}-mono-black.svg`]: mono(logo, '#111111'),
  [`${name}-mono-white.svg`]: mono(logo, '#FFFFFF'),
  [`${name}-reversed-on-anchor.svg`]: mono(logo, colors.base || '#111111'),
};
if (mark) {
  variants[`${name}-mark-mono-black.svg`] = mono(mark, '#111111');
  variants[`${name}-mark-mono-white.svg`] = mono(mark, '#FFFFFF');
}
for (const [f, s] of Object.entries(variants)) fs.writeFileSync(path.join(out, f), s);

const fit = (svg, h) => strip(svg).replace(/<svg /, `<svg style="height:${h}px;width:auto;display:block" `);
const tile = (label, bg, inner, extra = '') => `<div class="t" style="background:${bg};${extra}"><div class="in">${inner}</div><span style="color:${lum(bg) > 0.4 ? '#333' : '#ddd'}">${label}</span></div>`;
function lum(hex) { const h = (hex || '#fff').replace('#', ''); const [r, g, b] = [0, 2, 4].map(i => parseInt(h.slice(i, i + 2), 16) / 255); return 0.2126 * r + 0.7152 * g + 0.0722 * b; }

const rows = [];
rows.push(['1 · Colour on each brand colour', Object.entries(colors).map(([k, c]) => tile(`on ${k} ${c}`, c, fit(k === 'base' ? logo : mono(logo, lum(c) > 0.4 ? (colors.base && lum(colors.base) < 0.4 ? colors.base : '#111111') : (colors.anchor || '#FFFFFF')), 70))).join('')]);
rows.push(['2 · One colour (fax/stamp/embroidery/foil)', [tile('mono black on white', '#FFFFFF', fit(mono(logo, '#111111'), 70)), tile('mono white on black', '#111111', fit(mono(logo, '#FFFFFF'), 70)), tile('greyscale', colors.base || '#FFFFFF', `<div style="filter:grayscale(1)">${fit(logo, 70)}</div>`)].join('')]);
rows.push(['3 · Squint test (blur) — shape must still read', [2, 4, 7].map(b => tile(`blur ${b}px`, colors.base || '#fff', `<div style="filter:blur(${b}px)">${fit(logo, 70)}</div>`)).join('')]);
rows.push(['4 · Small sizes — full logo (px tall)', [48, 24, 16, 12].map(h => tile(`${h}px`, colors.base || '#fff', fit(logo, h))).join('')]);
if (mark) {
  rows.push(['5 · Mark at favicon / app sizes', [128, 64, 32, 24, 16].map(h => tile(`${h}px`, colors.base || '#fff', fit(mark, h))).join('')]);
  rows.push(['6 · Avatar crops (circle 110px)', [colors.base, colors.anchor, colors.accent].filter(Boolean).map(c => tile(`avatar on ${c}`, '#ffffff', `<div style="width:110px;height:110px;border-radius:50%;background:${c};display:flex;align-items:center;justify-content:center;overflow:hidden">${fit(lum(c) > 0.4 ? mono(mark, colors.base && lum(colors.base) < 0.4 ? colors.base : '#111') : mark, 70)}</div>`)).join('')]);
}

const html = `<!doctype html><meta charset="utf-8"><style>
body{margin:0;padding:28px;background:#ECEBE8;font:14px Inter,system-ui,sans-serif;width:1500px}
h1{font-size:22px;margin:0 0 18px} h2{font-size:15px;margin:22px 0 8px;color:#333}
.r{display:flex;gap:12px;flex-wrap:wrap}.t{position:relative;min-width:220px;height:170px;flex:1;border-radius:6px;display:flex;align-items:center;justify-content:center;border:1px solid #0001}
.in{display:flex;align-items:center;justify-content:center;padding:20px}.t span{position:absolute;left:10px;bottom:8px;font-size:12px}
</style><h1>Logo test sheet — ${name}</h1>${rows.map(([h, r]) => `<h2>${h}</h2><div class="r">${r}</div>`).join('')}`;
fs.writeFileSync(path.join(out, `${name}-test.html`), html);

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1556, height: 800 }, deviceScaleFactor: 1 });
await page.setContent(html);
await page.screenshot({ path: path.join(out, `${name}-test.png`), fullPage: true });
await browser.close();
console.log(`wrote ${path.join(out, name + '-test.png')} and ${Object.keys(variants).length} SVG variants`);
