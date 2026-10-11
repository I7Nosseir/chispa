#!/usr/bin/env node
// Build a portable logo SVG from a JSON spec. Text is converted to outlines (paths),
// so the logo looks identical everywhere without the font installed.
//
// Usage: node build_logo.mjs spec.json out.svg
// Needs opentype.js:  npm i --prefix <workdir> opentype.js@1   then run with NODE_PATH=<workdir>/node_modules
// Fonts are fetched from Google Fonts (OFL) and cached in ./.fontcache.
//
// spec = { "width": 600, "height": 200, "background": null | "#hex",
//   "elements": [
//     {"type":"text","text":"RAKHA","font":"Bodoni Moda","weight":600,"size":96,"x":300,"y":130,
//      "anchor":"middle","tracking":0.12,"fill":"#F2E8D8"},
//     {"type":"circle","cx":100,"cy":100,"r":80,"stroke":"#C69B3C","strokeWidth":3,"fill":"none"},
//     {"type":"line","x1":0,"y1":150,"x2":600,"y2":150,"stroke":"#C69B3C","strokeWidth":2},
//     {"type":"rect","x":0,"y":0,"w":10,"h":10,"fill":"#000","rx":0},
//     {"type":"path","d":"M0 0 L10 10","stroke":"#000","strokeWidth":2,"fill":"none"} ] }
// tracking = letter-spacing as a fraction of font size.
import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';
const require = createRequire(import.meta.url);
let opentype;
try { opentype = require('opentype.js'); } catch { console.error('Install opentype.js: npm i --prefix <dir> opentype.js@1 and set NODE_PATH=<dir>/node_modules'); process.exit(2); }

const [, , specPath, outPath] = process.argv;
const spec = JSON.parse(fs.readFileSync(specPath, 'utf8'));
const cacheDir = path.join(path.dirname(path.resolve(outPath)), '.fontcache');
fs.mkdirSync(cacheDir, { recursive: true });

async function loadFont(family, weight = 400, italic = false) {
  const key = `${family.replace(/\s+/g, '_')}_${weight}${italic ? 'i' : ''}.ttf`;
  const file = path.join(cacheDir, key);
  if (!fs.existsSync(file)) {
    const axis = italic ? `ital,wght@1,${weight}` : `wght@${weight}`;
    const cssUrl = `https://fonts.googleapis.com/css2?family=${encodeURIComponent(family)}:${axis}`;
    // An old user agent makes Google Fonts serve TTF (opentype.js can't read woff2).
    const css = await (await fetch(cssUrl, { headers: { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/534' } })).text();
    const m = css.match(/url\((https:[^)]+\.ttf)\)/);
    if (!m) throw new Error(`No TTF for ${family} ${weight}: ${css.slice(0, 200)}`);
    fs.writeFileSync(file, Buffer.from(await (await fetch(m[1])).arrayBuffer()));
  }
  return opentype.parse(fs.readFileSync(file).buffer.slice(0));
}

function textPath(font, el) {
  const size = el.size, track = (el.tracking || 0) * size;
  const glyphs = font.stringToGlyphs(el.text);
  let width = 0;
  const adv = glyphs.map((g, i) => {
    const kern = i < glyphs.length - 1 ? font.getKerningValue(g, glyphs[i + 1]) : 0;
    const a = (g.advanceWidth + kern) * size / font.unitsPerEm + (i < glyphs.length - 1 ? track : 0);
    width += a; return a;
  });
  let x = el.x - (el.anchor === 'middle' ? width / 2 : el.anchor === 'end' ? width : 0);
  let d = '';
  glyphs.forEach((g, i) => { d += g.getPath(x, el.y, size).toPathData(2); x += adv[i]; });
  return { d, width };
}

const parts = [];
const report = [];
for (const el of spec.elements) {
  if (el.type === 'text') {
    const font = await loadFont(el.font, el.weight || 400, !!el.italic);
    const { d, width } = textPath(font, el);
    parts.push(`<path d="${d}" fill="${el.fill || '#000'}"${el.opacity ? ` opacity="${el.opacity}"` : ''}/>`);
    report.push(`${el.text} → ${el.font} ${el.weight || 400}, width ${width.toFixed(1)}px`);
  } else if (el.type === 'circle') {
    parts.push(`<circle cx="${el.cx}" cy="${el.cy}" r="${el.r}" fill="${el.fill || 'none'}" stroke="${el.stroke || 'none'}" stroke-width="${el.strokeWidth || 0}"/>`);
  } else if (el.type === 'line') {
    parts.push(`<line x1="${el.x1}" y1="${el.y1}" x2="${el.x2}" y2="${el.y2}" stroke="${el.stroke}" stroke-width="${el.strokeWidth || 1}" stroke-linecap="${el.cap || 'butt'}"/>`);
  } else if (el.type === 'rect') {
    parts.push(`<rect x="${el.x}" y="${el.y}" width="${el.w}" height="${el.h}" rx="${el.rx || 0}" fill="${el.fill || 'none'}" stroke="${el.stroke || 'none'}" stroke-width="${el.strokeWidth || 0}"/>`);
  } else if (el.type === 'path') {
    parts.push(`<path d="${el.d}" fill="${el.fill || 'none'}" stroke="${el.stroke || 'none'}" stroke-width="${el.strokeWidth || 0}" stroke-linecap="round" stroke-linejoin="round"/>`);
  }
}
const bg = spec.background ? `<rect width="100%" height="100%" fill="${spec.background}"/>` : '';
const svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${spec.width} ${spec.height}" width="${spec.width}" height="${spec.height}">${bg}${parts.join('')}</svg>\n`;
fs.writeFileSync(outPath, svg);
console.log(`wrote ${outPath}\n` + report.join('\n'));
