#!/usr/bin/env node
// Build a one-page brand board (tall single page, like a Behance brand sheet) from brand.json.
// Output: <out>/<slug>-board.html, .pdf (one tall page) and .png.
//
// Usage: NODE_PATH=$(npm root -g) node build_board.mjs brand.json <outDir>
// See ../references/board-anatomy.md for the brand.json schema and section rules.
import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';
const require = createRequire(import.meta.url);
const { chromium } = require('playwright');

const [, , specPath, outDir = '.'] = process.argv;
const B = JSON.parse(fs.readFileSync(specPath, 'utf8'));
const base = path.dirname(path.resolve(specPath));
fs.mkdirSync(outDir, { recursive: true });
const slug = (B.slug || B.name).toLowerCase().replace(/[^a-z0-9]+/g, '-');
const W = B.width || 760;
const C = Object.fromEntries(B.colors.map(c => [c.role, c.hex]));
const esc = s => String(s ?? '').replace(/&/g, '&amp;').replace(/</g, '&lt;');

const svgCache = {};
function logo(key = 'lockup', map = {}, h = 80) {
  const file = B.logo[key];
  if (!file) return '';
  let s = svgCache[file] ??= fs.readFileSync(path.resolve(base, file), 'utf8');
  for (const [from, to] of Object.entries(map)) s = s.split(`"${from}"`).join(`"${to}"`).split(`"${from.toLowerCase()}"`).join(`"${to}"`);
  return s.replace(/<svg /, `<svg style="height:${h}px;width:auto;max-width:100%;display:block" `);
}
const lum = hex => { const h = hex.replace('#', ''); const [r, g, b] = [0, 2, 4].map(i => parseInt(h.slice(i, i + 2), 16) / 255).map(c => c <= 0.04045 ? c / 12.92 : ((c + 0.055) / 1.055) ** 2.4); return 0.2126 * r + 0.7152 * g + 0.0722 * b; };
const textOn = bg => lum(bg) > 0.3 ? (C.base && lum(C.base) < 0.3 ? C.base : '#111') : (C.anchor || '#fff');

// ---------- code-made mockups (no stock photos needed) ----------
const texture = (bg, kind = 'linen') => `background-color:${bg};background-image:url(&quot;data:image/svg+xml;utf8,${encodeURIComponent(`<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'><filter id='n'><feTurbulence type='${kind === 'linen' ? 'fractalNoise' : 'turbulence'}' baseFrequency='${kind === 'linen' ? '0.9 0.05' : '0.8'}' numOctaves='3' seed='7'/><feColorMatrix values='0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 ${lum(bg) > 0.3 ? 0.10 : 0.22} 0'/></filter><rect width='100%' height='100%' filter='url(#n)'/></svg>`)}&quot;)`;
const mockups = {
  card: (m) => `<div class="mk" style="${texture(m.surface || C.neutral || '#999')};height:${m.h || 300}px">
      <div class="card" style="background:${m.bg || C.base};transform:rotate(${m.rotate ?? -14}deg)">${logo(m.logo || 'lockup', m.map, m.logoH || 46)}</div></div>`,
  'card-pair': (m) => `<div class="mk" style="${texture(m.surface || C.neutral || '#999')};height:${m.h || 300}px">
      <div class="card" style="background:${m.back || C.anchor};transform:translate(-95px,-30px) rotate(-8deg);box-shadow:0 18px 40px #0005;align-items:flex-start;justify-content:flex-start;padding:26px">
        <div style="color:${textOn(m.back || C.anchor)};font:500 10px/1.7 var(--body);letter-spacing:.06em;text-align:left;max-width:150px">${(m.backLines || []).map(esc).join('<br>')}</div></div>
      <div class="card" style="background:${m.bg || C.base};transform:translate(95px,34px) rotate(6deg)">${logo(m.logo || 'mark', m.map, m.logoH || 70)}</div></div>`,
  notebook: (m) => `<div class="mk" style="${texture(m.surface || C.anchor, 'paper')};height:${m.h || 300}px">
      <div class="nb" style="background:${m.bg || C.base}"><div class="nbband" style="background:${m.band || C.metal}"></div>
      <div style="position:absolute;top:22%;left:0;right:0;display:flex;justify-content:center">${logo(m.logo || 'mark', m.map, 64)}</div>
      <div class="nbt" style="color:${m.fg || textOn(m.bg || C.base)}">${esc(m.title || '')}</div></div></div>`,
  certificate: (m) => `<div class="mk" style="${texture(m.surface || C.neutral || '#999')};height:${m.h || 300}px">
      <div class="cert" style="background:${m.bg || C.anchor};color:${m.fg || C.base};border-color:${m.border || C.metal}">
      ${logo(m.logo || 'mark', m.map, 40)}<div class="ct1">${esc(m.title || 'Certificate')}</div><div class="ct2">${esc(m.line || '')}</div></div></div>`,
  phone: (m) => `<div class="mk" style="${texture(m.surface || C.neutral || '#999')};height:${m.h || 300}px">
      <div class="ph"><div class="phs" style="background:${m.bg || C.base};color:${m.fg || textOn(m.bg || C.base)}">
      <div style="font:600 9px var(--body);letter-spacing:.2em;opacity:.7">${esc(m.kicker || '')}</div>
      <div style="font:600 22px/1.15 var(--display);margin-top:8px">${esc(m.title || '')}</div></div></div></div>`,
};

// ---------- grid tiles (the "BRANDING" social grid) ----------
const tile = t => {
  const bg = t.bg || C.base, fg = t.fg || textOn(bg);
  switch (t.type) {
    case 'statement': return `<div class="tl" style="background:${bg};color:${fg}"><div class="stm">${t.text.split('\n').map(esc).join('<br>')}</div></div>`;
    case 'copy': return `<div class="tl c" style="background:${bg};color:${fg}">${t.kicker ? `<div class="kk" style="color:${t.kickerColor || C.metal || fg}">${esc(t.kicker)}</div>` : ''}<div class="cp">${esc(t.text)}</div>${t.small ? `<div class="sm">${esc(t.small)}</div>` : ''}</div>`;
    case 'logo': return `<div class="tl c" style="${t.texture ? texture(bg) : `background:${bg}`}">${logo(t.logo || 'mark', t.map, t.h || 90)}</div>`;
    case 'mockup': return `<div class="tl m">${mockups[t.mockup]({ ...t, h: 228 })}</div>`;
    case 'quote': return `<div class="tl c" style="background:${bg};color:${fg}"><div class="q" style="color:${t.markColor || C.metal}">“</div><div class="cp" style="font-family:var(--display);font-size:17px">${esc(t.text)}</div>${t.small ? `<div class="sm">${esc(t.small)}</div>` : ''}</div>`;
    case 'chart': {
      const v = t.values || [3, 4, 3.5, 5, 6, 7.5, 9];
      const mx = Math.max(...v), pts = v.map((y, i) => `${10 + i * (180 / (v.length - 1))},${110 - (y / mx) * 90}`).join(' ');
      return `<div class="tl c" style="background:${bg};color:${fg}"><div class="kk" style="color:${C.metal || fg}">${esc(t.kicker || '')}</div>
        <svg viewBox="0 0 200 120" style="width:80%;margin:6px 0"><polyline points="${pts}" fill="none" stroke="${t.line || C.metal}" stroke-width="2.5"/><line x1="10" y1="112" x2="190" y2="112" stroke="${fg}" stroke-opacity=".35"/></svg>
        <div class="cp" style="font-size:12px">${esc(t.text || '')}</div></div>`;
    }
    default: return `<div class="tl" style="background:${bg}"></div>`;
  }
};

const H = (t) => `<h2 style="color:${B.headingColor || C.base}">${esc(t)}</h2>`;
const sections = [];
// 1 Hero
sections.push(`<section class="hero" style="background:${B.hero?.bg || '#FFFFFF'}">${logo(B.hero?.logo || 'lockup', B.hero?.map, B.hero?.h || 120)}
  <div class="tag" style="color:${B.hero?.tagColor || textOn(B.hero?.bg || '#fff')}">${esc(B.tagline)}</div></section>`);
// 2 Overview
if (B.overview) sections.push(`<section class="ov" style="background:${B.overview.bg || C.metal};color:${B.overview.fg || textOn(B.overview.bg || C.metal)}">
  <h2 style="color:inherit">${esc(B.overview.title || 'OVERVIEW')}</h2><p>${esc(B.overview.text)}</p>${B.overview.meaning ? `<p class="mn">${esc(B.overview.meaning)}</p>` : ''}</section>`);
// 3 Hero mockup
if (B.heroMockup) sections.push(`<section class="full">${mockups[B.heroMockup.type]({ ...B.heroMockup, h: B.heroMockup.h || 420 })}</section>`);
// 4 Logo variations
if (B.logoVariations?.length) sections.push(`<section class="pad">${H('LOGO VARIATIONS')}<div class="lv">${B.logoVariations.map(v =>
  `<div style="background:${v.bg};${v.border ? 'outline:1px solid #0002;outline-offset:-1px' : ''}">${logo(v.logo || 'lockup', v.map, v.h || 46)}</div>`).join('')}</div>
  ${B.logoNotes ? `<p class="note">${esc(B.logoNotes)}</p>` : ''}</section>`);
// 5 Colours
sections.push(`<section class="pad">${H('BRAND COLORS')}<div class="pal">${B.colors.map(c =>
  `<div style="flex:${c.share || 10};background:${c.hex};color:${textOn(c.hex)}"><b>${esc(c.name)}</b><span>${c.hex}</span><span>${esc(c.role)}${c.share ? ' · ' + c.share + '%' : ''}</span></div>`).join('')}</div>
  ${B.colorNotes ? `<p class="note">${esc(B.colorNotes)}</p>` : ''}</section>`);
// 6 Typography
if (B.fonts) sections.push(`<section class="pad">${H('TYPOGRAPHY')}<div class="ty">
  <div><div style="font-family:var(--display);font-weight:${B.fonts.display.weight || 600};font-size:46px;line-height:1">Aa</div><b>${esc(B.fonts.display.family)}</b><span>${esc(B.fonts.display.use || 'Headlines')}</span></div>
  <div><div style="font-family:var(--body);font-weight:${B.fonts.body.weight || 400};font-size:46px;line-height:1">Aa</div><b>${esc(B.fonts.body.family)}</b><span>${esc(B.fonts.body.use || 'Body, captions')}</span></div>
  ${B.fonts.arabic ? `<div><div style="font-family:'${B.fonts.arabic.family}';font-size:40px;line-height:1.1">أب</div><b>${esc(B.fonts.arabic.family)}</b><span>${esc(B.fonts.arabic.use || 'Arabic')}</span></div>` : ''}
  </div>${B.fonts.sample ? `<p class="spec" style="font-family:var(--display)">${esc(B.fonts.sample)}</p>` : ''}</section>`);
// 7 Applications
if (B.applications?.length) sections.push(`<section class="pad">${H(B.applicationsTitle || 'APPLICATIONS')}<div class="ap">${B.applications.map(a => `<div>${mockups[a.type]({ ...a, h: 300 })}</div>`).join('')}</div></section>`);
// 8 Social grid
if (B.grid?.length) sections.push(`<section class="pad">${H(B.gridTitle || 'BRANDING')}<div class="gr">${B.grid.map(tile).join('')}</div></section>`);
// 9 Closing
if (B.closing) sections.push(`<section class="close" style="color:${B.closingColor || C.base}">${esc(B.closing)}</section>`);

const fontsQ = [B.fonts?.display, B.fonts?.body, B.fonts?.arabic].filter(Boolean).map(f => `family=${encodeURIComponent(f.family)}:wght@${f.weights || '400;500;600;700'}`).join('&');
const html = `<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?${fontsQ}&display=swap" rel="stylesheet">
<style>
:root{--display:'${B.fonts?.display.family || 'Georgia'}',serif;--body:'${B.fonts?.body.family || 'Inter'}',sans-serif}
*{box-sizing:border-box}body{margin:0;width:${W}px;background:#fff;font-family:var(--body);color:${C.base}}
section{width:100%}h2{font:500 19px var(--body);letter-spacing:.06em;text-align:center;margin:0 0 26px}
.hero{display:flex;flex-direction:column;align-items:center;justify-content:center;padding:96px 40px 70px}
.tag{margin-top:14px;font:400 15px var(--body);letter-spacing:.02em}
.ov{padding:64px 92px;text-align:center}.ov p{font:400 14.5px/1.55 var(--body);margin:0 auto;max-width:560px}.ov .mn{margin-top:14px;font-style:italic;opacity:.85}
.pad{padding:54px 0 10px}.note{text-align:center;font-size:12px;opacity:.7;margin:14px 60px 0}
.lv{display:grid;grid-template-columns:repeat(3,1fr);gap:14px 14px;padding:0}.lv>div{height:160px;display:flex;align-items:center;justify-content:center;padding:18px}
.pal{display:flex;height:150px;margin:0 60px}.pal>div{display:flex;flex-direction:column;justify-content:flex-end;padding:10px;font-size:11px;gap:2px;outline:1px solid #0001}.pal b{font-size:13px}
.ty{display:flex;justify-content:center;gap:60px}.ty>div{display:flex;flex-direction:column;align-items:center;gap:6px;font-size:12px}.ty span{opacity:.6}.spec{text-align:center;font-size:24px;margin:26px 60px 0}
.ap{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin:0 60px}
.gr{display:grid;grid-template-columns:repeat(3,1fr);gap:9px;margin:0 70px}
.tl{aspect-ratio:1/1.18;position:relative;overflow:hidden;display:flex;align-items:flex-end;padding:22px}.tl.c{flex-direction:column;align-items:center;justify-content:center;text-align:center}.tl.m{padding:0}
.tl.m .mk{height:100%!important}.tl.m .ph{transform:scale(.7)}.tl.m .nb{transform:scale(.75)}.tl.m .card{transform:scale(.62) rotate(-10deg)!important}.tl.m .cert{transform:scale(.62)}
.stm{font:800 25px/1.04 var(--body);letter-spacing:.01em;text-transform:uppercase}
.kk{font:600 9.5px var(--body);letter-spacing:.22em;text-transform:uppercase;margin-bottom:8px}.cp{font:600 13.5px/1.35 var(--body);max-width:90%}.sm{font-size:10px;opacity:.75;margin-top:8px;max-width:90%}
.q{font:400 54px/0.6 var(--display);margin-bottom:6px}
.mk{position:relative;width:100%;overflow:hidden;display:flex;align-items:center;justify-content:center}
.card{width:300px;height:182px;border-radius:10px;display:flex;align-items:center;justify-content:center;box-shadow:0 24px 50px #0006,0 2px 6px #0004;position:absolute}
.nb{width:190px;height:250px;border-radius:4px 10px 10px 4px;position:relative;box-shadow:0 22px 44px #0007}.nbband{position:absolute;left:14px;top:0;bottom:0;width:6px}
.nbt{position:absolute;bottom:26px;left:22px;right:8px;text-align:center;font:600 8.5px var(--body);letter-spacing:.16em}
.cert{width:300px;height:212px;border:2px solid;outline:1px solid;outline-offset:-9px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:10px;box-shadow:0 20px 40px #0005}
.ct1{font:600 20px var(--display);letter-spacing:.06em}.ct2{font-size:10px;letter-spacing:.14em;text-transform:uppercase;opacity:.8}
.ph{width:150px;height:300px;border-radius:24px;background:#111;padding:8px;box-shadow:0 22px 40px #0006}.phs{width:100%;height:100%;border-radius:17px;padding:22px 14px}
.full .mk{height:420px}
.close{text-align:center;padding:56px 40px 90px;font:400 15px/1.5 var(--body)}
</style></head><body>${sections.join('\n')}</body></html>`;

const htmlPath = path.join(outDir, `${slug}-board.html`);
fs.writeFileSync(htmlPath, html);
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: W, height: 1200 }, deviceScaleFactor: 2 });
await page.goto('file://' + path.resolve(htmlPath));
await page.waitForLoadState('networkidle').catch(() => {});
await page.evaluate(() => document.fonts.ready);
const height = await page.evaluate(() => document.body.scrollHeight);
await page.screenshot({ path: path.join(outDir, `${slug}-board.png`), fullPage: true });
await page.pdf({ path: path.join(outDir, `${slug}-board.pdf`), width: `${W}px`, height: `${height + 2}px`, printBackground: true, pageRanges: '1' });
await browser.close();
console.log(`wrote ${slug}-board.html/.png/.pdf (${W}×${height}px)`);
