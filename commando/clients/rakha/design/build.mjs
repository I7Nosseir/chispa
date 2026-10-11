// Mr Rakha design kit — carousels, profile photo, Facebook cover (HTML → PNG via Playwright).
// Usage: NODE_PATH=$(npm root -g) node build.mjs
import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';
const require = createRequire(import.meta.url);
const { chromium } = require('playwright');

const OUT = path.resolve('out');
const LOGO = path.resolve('../logo');
const C = { black: '#141112', bone: '#F2E8D8', cognac: '#8B4A2B', gold: '#C69B3C', taupe: '#8A8580', ink: '#1E1A17' };
const svg = (f, h, map = {}) => {
  let s = fs.readFileSync(path.join(LOGO, f), 'utf8');
  for (const [a, b] of Object.entries(map)) s = s.split(`"${a}"`).join(`"${b}"`);
  return s.replace('<svg ', `<svg style="height:${h}px;width:auto;display:block" `);
};
const grain = (o = 0.18) => `<div class="grain" style="opacity:${o}"></div>`;
const FONTS = `<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,500;1,600&family=Inter:wght@400;500;600;700&family=Caveat:wght@500;600;700&display=swap" rel="stylesheet">`;
const BASE_CSS = `
*{box-sizing:border-box;margin:0;padding:0}
body{width:var(--w);height:var(--h);overflow:hidden;font-family:Inter,sans-serif;-webkit-font-smoothing:antialiased}
.s{position:relative;width:var(--w);height:var(--h);overflow:hidden}
.grain{position:absolute;inset:0;pointer-events:none;mix-blend-mode:overlay;background-image:url("data:image/svg+xml;utf8,${encodeURIComponent(`<svg xmlns='http://www.w3.org/2000/svg' width='240' height='240'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='3' stitchTiles='stitch'/></filter><rect width='100%' height='100%' filter='url(#n)'/></svg>`)}")}
.hd{position:absolute;top:60px;left:76px;right:76px;display:flex;justify-content:space-between;align-items:center;font:600 20px Inter;letter-spacing:.22em;text-transform:uppercase;z-index:5}
.ft{position:absolute;bottom:56px;left:76px;right:76px;display:flex;justify-content:space-between;font:500 20px Inter;letter-spacing:.12em;z-index:5}
.serif{font-family:'Cormorant Garamond',serif}
.hand{font-family:Caveat,cursive}
.kick{font:600 22px Inter;letter-spacing:.24em;text-transform:uppercase}
.ghost{position:absolute;font-family:'Cormorant Garamond',serif;font-weight:700;line-height:.8;pointer-events:none}
`;
const page = (w, h, body) => `<!doctype html><html><head><meta charset="utf-8">${FONTS}<style>:root{--w:${w}px;--h:${h}px}${BASE_CSS}</style></head><body>${body}</body></html>`;
const head = (n, tot, fg, accent) => `<div class="hd" style="color:${fg}"><div style="display:flex;align-items:center;gap:14px">${svg('signet-mark.svg', 40, fg === C.black ? { '#F2E8D8': C.black, '#C69B3C': C.cognac } : {})}<span>Mr Rakha</span></div><span style="color:${accent}">${String(n).padStart(2, '0')} / ${String(tot).padStart(2, '0')}</span></div>`;
const foot = (fg, last) => `<div class="ft" style="color:${fg}"><span>@mrrakha</span><span>${last ? 'Save this' : 'Swipe →'}</span></div>`;

// ---------- Carousel 1: The 2027 Business exam ----------
const c1 = [];
const T1 = 6;
c1.push(`<div class="s" style="background:radial-gradient(120% 90% at 30% 20%, #2A221E 0%, ${C.black} 60%)">
  <div class="ghost" style="color:${C.gold};opacity:.09;font-size:560px;right:-40px;top:230px">2027</div>
  ${head(1, T1, C.bone, C.gold)}
  <div style="position:absolute;left:76px;right:76px;top:230px">
    <div class="kick" style="color:${C.gold}">The Brief · Exam room</div>
    <div class="serif" style="color:${C.bone};font-size:112px;font-weight:600;line-height:.98;margin-top:28px">The IGCSE Business exam is changing.</div>
    <div style="color:${C.bone};opacity:.8;font-size:34px;line-height:1.35;margin-top:34px;max-width:780px">Four changes. One that actually decides your grade.</div>
  </div>
  <div style="position:absolute;left:76px;bottom:190px;display:flex;align-items:center;gap:34px">
    <div style="position:relative;background:${C.bone};color:${C.black};padding:26px 34px;transform:rotate(-4deg);box-shadow:0 30px 60px #0008">
      <div class="kick" style="font-size:16px;color:${C.taupe}">Business Studies</div><div class="serif" style="font-size:86px;font-weight:700;line-height:1">0450</div>
      <svg viewBox="0 0 300 100" style="position:absolute;left:-10px;top:40px;width:260px"><path d="M10 60 C 90 40, 180 70, 290 35" stroke="${C.cognac}" stroke-width="9" fill="none" stroke-linecap="round"/></svg>
    </div>
    <div class="serif" style="color:${C.gold};font-size:90px">→</div>
    <div style="background:${C.gold};color:${C.black};padding:26px 34px;transform:rotate(3deg);box-shadow:0 30px 60px #0008">
      <div class="kick" style="font-size:16px">Business · from 2027</div><div class="serif" style="font-size:86px;font-weight:700;line-height:1">0264</div>
    </div>
  </div>
  ${grain(.22)}${foot(C.bone)}</div>`);
c1.push(`<div class="s" style="background:${C.bone}">
  ${head(2, T1, C.black, C.cognac)}
  <div style="position:absolute;left:76px;right:76px;top:190px">
    <div class="kick" style="color:${C.cognac}">01 · New code, same core</div>
    <div style="display:flex;align-items:baseline;gap:30px;margin-top:20px">
      <div class="serif" style="font-size:190px;font-weight:700;color:${C.black};opacity:.28;text-decoration:line-through;text-decoration-color:${C.cognac};text-decoration-thickness:10px;line-height:1">0450</div>
      <div class="serif" style="font-size:80px;color:${C.cognac}">→</div>
    </div>
    <div class="serif" style="font-size:250px;font-weight:700;color:${C.black};line-height:.85;margin-top:-6px">0264</div>
    <div style="color:${C.ink};font-size:34px;line-height:1.4;margin-top:34px;max-width:880px">First exams in March 2027. The six units stay. The two 80-mark papers stay.</div>
  </div>
  <div style="position:absolute;left:76px;right:76px;bottom:150px;display:grid;grid-template-columns:repeat(3,1fr);gap:14px">
    ${['Understanding business activity', 'People in business', 'Marketing', 'Operations management', 'Financial information & decisions', 'External influences'].map((u, i) => `<div style="border:2px solid ${C.black};padding:18px 18px;font:600 21px/1.25 Inter;color:${C.black};background:#F7F0E4;min-height:92px"><span style="color:${C.cognac}">${i + 1} · </span>${u}</div>`).join('')}
  </div>
  ${grain(.25)}${foot(C.black)}</div>`);
c1.push(`<div class="s" style="background:linear-gradient(160deg, #9A5534 0%, ${C.cognac} 45%, #5E2F1A 100%)">
  ${head(3, T1, C.bone, C.bone)}
  <div style="position:absolute;left:76px;right:76px;top:230px">
    <div class="kick" style="color:${C.bone};opacity:.85">02 · Fewer marks for memorising</div>
    <div class="serif" style="color:${C.bone};font-size:100px;font-weight:600;line-height:1;margin-top:26px">Knowing it is worth less now.</div>
  </div>
  <div style="position:absolute;left:76px;right:76px;top:720px">
    ${[['Knowledge (0450)', 40, .55], ['Knowledge (0264)', 35, 1], ['Application (0264)', 30, 1]].map(([l, v, o]) => `
      <div style="display:flex;align-items:center;gap:22px;margin-bottom:30px;opacity:${o}">
        <div style="width:300px;font:600 24px Inter;color:${C.bone}">${l}</div>
        <div style="flex:1;height:58px;background:#0003;position:relative"><div style="position:absolute;inset:0 auto 0 0;width:${v * 2}%;background:${l.startsWith('Application') ? C.gold : C.bone}"></div></div>
        <div class="serif" style="width:110px;text-align:right;font-size:60px;font-weight:700;color:${C.bone}">${v}%</div>
      </div>`).join('')}
    <div style="color:${C.bone};font-size:28px;opacity:.85;margin-top:14px">Application to the case is nearly a third of your grade.</div>
  </div>
  ${grain(.25)}${foot(C.bone)}</div>`);
c1.push(`<div class="s" style="background:${C.black}">
  <div style="position:absolute;inset:0;background:repeating-linear-gradient(100deg, transparent 0 160px, #C69B3C08 160px 220px)"></div>
  ${head(4, T1, C.bone, C.gold)}
  <div style="position:absolute;left:76px;right:76px;top:230px">
    <div class="kick" style="color:${C.gold}">03 · Paper 2 is all about the case</div>
    <div class="serif" style="color:${C.bone};font-size:96px;font-weight:600;line-height:1;margin-top:26px">Every part (a) is now applied.</div>
    <div style="color:${C.bone};opacity:.85;font-size:34px;line-height:1.4;margin-top:30px;max-width:860px">A textbook definition with no case in it? That's where the marks go.</div>
  </div>
  <div style="position:absolute;left:150px;right:150px;bottom:160px;background:${C.bone};padding:40px 44px;transform:rotate(-2deg);box-shadow:0 40px 80px #000a">
    <div class="kick" style="font-size:16px;color:${C.taupe}">Practice case · not a past paper</div>
    <div style="font:500 25px/1.5 Inter;color:${C.ink};margin-top:14px"><b>Nile Brew</b> is a café near a university. Its owner, Salma, wants to <span style="background:${C.gold}55">grow profit by 15%</span> this year. Sales fell <span style="border-bottom:4px solid ${C.cognac}">12% in the summer</span>…</div>
    <div class="hand" style="position:absolute;right:-20px;top:-46px;font-size:46px;color:${C.gold};transform:rotate(6deg)">use these!</div>
  </div>
  ${grain(.2)}${foot(C.bone)}</div>`);
c1.push(`<div class="s" style="background:${C.bone}">
  ${head(5, T1, C.black, C.cognac)}
  <div style="position:absolute;left:76px;right:76px;top:230px">
    <div class="kick" style="color:${C.cognac}">04 · What's new to learn</div>
    <div class="serif" style="color:${C.black};font-size:96px;font-weight:600;line-height:1;margin-top:26px">Three new things on your list.</div>
  </div>
  <div style="position:absolute;left:76px;right:76px;top:600px">
    ${[['Technology & digital communication', 'now part of the syllabus, including in People in business'], ['Sustainable production', 'a new topic to learn'], ['A formula list', 'ratios and formulas are given to you; using them still earns the marks']].map(([a, b], i) => `
      <div style="display:flex;gap:30px;align-items:flex-start;padding:30px 0;border-top:2px solid ${C.black}22">
        <div class="serif" style="font-size:80px;font-weight:700;line-height:.8;color:${C.cognac};width:70px">${i + 1}</div>
        <div><div class="serif" style="font-size:52px;font-weight:600;color:${C.black};line-height:1">${a}</div><div style="font-size:27px;color:${C.ink};opacity:.85;margin-top:10px">${b}</div></div>
      </div>`).join('')}
    <div style="font-size:24px;color:${C.taupe};margin-top:10px">Plus: Paper 1 questions now have four parts instead of five.</div>
  </div>
  ${grain(.25)}${foot(C.black)}</div>`);
c1.push(`<div class="s" style="background:radial-gradient(110% 80% at 70% 30%, #2A221E 0%, ${C.black} 65%)">
  <div style="position:absolute;right:-120px;top:120px;opacity:.10">${svg('signet-mark.svg', 820)}</div>
  ${head(6, T1, C.bone, C.gold)}
  <div style="position:absolute;left:76px;right:76px;top:300px">
    <div class="kick" style="color:${C.gold}">The one that matters</div>
    <div class="serif" style="color:${C.bone};font-size:150px;font-weight:600;line-height:.9;margin-top:24px">Application.</div>
    <div style="color:${C.bone};opacity:.88;font-size:36px;line-height:1.4;margin-top:40px;max-width:820px">You can't cram it the week before. You train it by reading business in the real world, every week.</div>
    <div style="margin-top:56px;display:inline-block;border:2px solid ${C.gold};color:${C.gold};padding:20px 30px;font:600 24px Inter;letter-spacing:.14em;text-transform:uppercase">Follow for The Brief, every Tuesday</div>
  </div>
  <div style="position:absolute;left:76px;bottom:120px;font-size:18px;color:${C.taupe}">Source: Cambridge International, IGCSE Business 0264 syllabus (2027–2029).</div>
  ${grain(.22)}${foot(C.bone, true)}</div>`);

// ---------- Carousel 2: The Margin ----------
const Q = 'A café near a university is thinking about raising its prices by 20%. Evaluate whether this is a good decision. [6]';
const ANS = [
  ['Raising prices by 20% will increase the revenue per customer.', ''],
  ['However, some customers may stop buying because the price is higher.', ''],
  ['This means the café could lose customers to competitors.', ''],
];
const paper = (notes, opts = {}) => `<div style="position:absolute;left:${opts.left ?? 110}px;right:${opts.right ?? 110}px;top:${opts.top ?? 330}px;background:#FBF6EC;padding:48px 52px 44px;transform:rotate(${opts.rot ?? -1.5}deg);box-shadow:0 30px 70px #0007;background-image:repeating-linear-gradient(transparent 0 57px,#8A858033 57px 58px)">
  <div style="font:600 18px Inter;letter-spacing:.2em;color:${C.taupe};text-transform:uppercase">Student answer · dummy</div>
  ${ANS.map(([t], i) => `<div class="hand" style="font-size:44px;line-height:58px;color:#2B2A33;margin-top:${i ? 0 : 14}px;${opts.hl === i ? `background:${C.gold}40` : ''}">${t}</div>`).join('')}
  ${opts.extra ?? ''}
  ${notes}
</div>`;
const note = (txt, css) => `<div class="hand" style="position:absolute;font-size:46px;font-weight:700;color:${C.cognac};line-height:1;${css}">${txt}</div>`;
const c2 = [];
const T2 = 7;
c2.push(`<div class="s" style="background:${C.black}">
  ${head(1, T2, C.bone, C.gold)}
  <div style="position:absolute;left:76px;right:76px;top:190px">
    <div class="kick" style="color:${C.gold}">The Margin · No. 01</div>
    <div class="serif" style="color:${C.bone};font-size:96px;font-weight:600;line-height:1;margin-top:22px">This answer knows everything. It still lost 2 marks.</div>
  </div>
  ${paper(`<div style="position:absolute;right:30px;bottom:-60px;width:210px;height:210px;border:7px solid ${C.cognac};border-radius:50%;transform:rotate(-8deg);display:flex;align-items:center;justify-content:center" class="hand"><span style="font-size:110px;font-weight:700;color:${C.cognac}">4/6</span></div>`, { top: 620, rot: 2 })}
  ${grain(.2)}${foot(C.bone)}</div>`);
c2.push(`<div class="s" style="background:linear-gradient(165deg,#9A5534,${C.cognac} 50%,#5E2F1A)">
  ${head(2, T2, C.bone, C.bone)}
  <div style="position:absolute;left:76px;right:76px;top:250px">
    <div class="kick" style="color:${C.bone};opacity:.85">The question</div>
    <div class="serif" style="color:${C.bone};font-size:72px;font-weight:600;line-height:1.12;margin-top:30px">A café near a university is thinking about raising its prices by 20%. <span style="background:${C.gold};color:${C.black};padding:0 10px">Evaluate</span> whether this is a good decision. <span style="opacity:.7">[6]</span></div>
    <div class="hand" style="font-size:54px;color:${C.bone};margin-top:60px;transform:rotate(-2deg)">← the word that decides the last 2 marks</div>
  </div>
  <div class="ghost" style="color:${C.bone};opacity:.13;font-size:520px;right:40px;bottom:40px">[6]</div>
  ${grain(.25)}${foot(C.bone)}</div>`);
c2.push(`<div class="s" style="background:${C.bone}">
  ${head(3, T2, C.black, C.cognac)}
  <div class="ghost" style="color:${C.cognac};opacity:.08;font-size:520px;right:-20px;top:60px">✓</div>
  <div style="position:absolute;left:76px;right:76px;top:180px"><div class="kick" style="color:${C.cognac}">Margin note 1</div>
  <div class="serif" style="color:${C.black};font-size:80px;font-weight:600;line-height:1;margin-top:18px">Good link. That's your first 2 marks.</div></div>
  ${paper(note('✓ link', 'right:-30px;top:70px;transform:rotate(-6deg)') + `<div style="position:absolute;left:40px;top:96px;width:12px;height:58px;background:${C.cognac}"></div>`, { top: 560, hl: 0 })}
  ${grain(.25)}${foot(C.black)}</div>`);
c2.push(`<div class="s" style="background:${C.black}">
  ${head(4, T2, C.bone, C.gold)}
  <div style="position:absolute;left:76px;right:76px;top:180px"><div class="kick" style="color:${C.gold}">Margin note 2</div>
  <div class="serif" style="color:${C.bone};font-size:80px;font-weight:600;line-height:1;margin-top:18px">The chain is there. Analysis: 2 more marks.</div></div>
  ${paper(note('✓ chain', 'right:-34px;top:150px;transform:rotate(5deg)') + `<svg viewBox="0 0 40 120" style="position:absolute;left:14px;top:150px;width:30px;height:120px"><path d="M30 5 C 5 30, 5 90, 30 115" stroke="${C.cognac}" stroke-width="5" fill="none"/></svg>`, { top: 560, hl: 2, rot: 1.5 })}
  ${grain(.2)}${foot(C.bone)}</div>`);
c2.push(`<div class="s" style="background:${C.bone}">
  ${head(5, T2, C.black, C.cognac)}
  <div style="position:absolute;left:76px;right:76px;top:180px"><div class="kick" style="color:${C.cognac}">Margin note 3</div>
  <div class="serif" style="color:${C.black};font-size:80px;font-weight:600;line-height:1;margin-top:18px">No decision. "Evaluate" asked for one.</div></div>
  ${paper(note('so… is it a good decision?', 'left:40px;bottom:-74px;transform:rotate(-3deg);font-size:52px') + `<div style="position:absolute;left:40px;right:40px;bottom:30px;height:4px;background:${C.cognac};opacity:.6"></div>`, { top: 560 })}
  ${grain(.25)}${foot(C.black)}</div>`);
c2.push(`<div class="s" style="background:radial-gradient(110% 80% at 30% 30%, #2A221E 0%, ${C.black} 65%)">
  ${head(6, T2, C.bone, C.gold)}
  <div style="position:absolute;left:76px;right:76px;top:160px"><div class="kick" style="color:${C.gold}">The fix: two sentences</div>
  <div class="serif" style="color:${C.bone};font-size:78px;font-weight:600;line-height:1;margin-top:18px">Add "it depends" and a decision.</div></div>
  ${paper(`<div style="position:absolute;right:-40px;top:-120px;width:180px;height:180px;border:7px solid ${C.cognac};border-radius:50%;display:flex;align-items:center;justify-content:center;transform:rotate(6deg);background:#FBF6EC" class="hand"><span style="font-size:92px;font-weight:700;color:${C.cognac}">6/6</span></div>`, {
    top: 470, rot: -1, extra: `<div class="hand" style="font-size:44px;line-height:58px;color:#2B2A33;background:${C.gold}55">It depends on competition: if it is the only café near the university, demand is likely to be price inelastic, so revenue could rise.</div><div class="hand" style="font-size:44px;line-height:58px;color:#2B2A33;background:${C.gold}55">On balance, it is a good decision only if there are few nearby competitors.</div>` })}
  ${grain(.2)}${foot(C.bone)}</div>`);
c2.push(`<div class="s" style="background:linear-gradient(165deg,#9A5534,${C.cognac} 50%,#5E2F1A)">
  <div style="position:absolute;right:-140px;bottom:-60px;opacity:.12">${svg('signet-mark.svg', 760, { '#C69B3C': C.bone })}</div>
  ${head(7, T2, C.bone, C.bone)}
  <div style="position:absolute;left:76px;right:76px;top:280px">
    <div class="kick" style="color:${C.bone};opacity:.85">Remember it as</div>
    ${['Link.', 'Chain.', 'Decision.'].map((w, i) => `<div class="serif" style="color:${i === 2 ? C.gold : C.bone};font-size:150px;font-weight:600;line-height:.95;margin-top:${i ? 0 : 24}px">${w}</div>`).join('')}
    <div style="color:${C.bone};font-size:34px;line-height:1.4;margin-top:44px;max-width:820px">Explain gets the link. Analyse gets the chain. Evaluate needs the decision.</div>
  </div>
  ${grain(.25)}${foot(C.bone, true)}</div>`);

// ---------- Profile photo + Facebook cover ----------
const profile = `<div class="s" style="background:radial-gradient(70% 70% at 50% 45%, #2A221E 0%, ${C.black} 75%);display:flex;align-items:center;justify-content:center">
  ${svg('signet-mark.svg', 720)}${grain(.2)}</div>`;
const cover = `<div class="s" style="background:linear-gradient(100deg, ${C.black} 0%, ${C.black} 55%, #2A221E 100%)">
  <div style="position:absolute;right:120px;top:50%;transform:translateY(-50%);opacity:.9">${svg('signet-mark.svg', 420)}</div>
  <div style="position:absolute;left:220px;top:50%;transform:translateY(-50%)">
    <div class="kick" style="color:${C.gold};font-size:20px">IGCSE & O-level · Business · Economics</div>
    <div class="serif" style="color:${C.bone};font-size:78px;font-weight:600;line-height:1;margin-top:20px">Business, explained<br>like it matters.</div>
    <div style="margin-top:26px;width:120px;height:3px;background:${C.gold}"></div>
  </div>${grain(.2)}</div>`;

const jobs = [
  ...c1.map((b, i) => ({ file: `carousel-0264/${String(i + 1).padStart(2, '0')}.png`, w: 1080, h: 1350, b })),
  ...c2.map((b, i) => ({ file: `carousel-the-margin/${String(i + 1).padStart(2, '0')}.png`, w: 1080, h: 1350, b })),
  { file: 'profile/profile-1080.png', w: 1080, h: 1080, b: profile },
  { file: 'profile/facebook-cover-1640x624.png', w: 1640, h: 624, b: cover },
];
const browser = await chromium.launch();
for (const j of jobs) {
  const f = path.join(OUT, j.file); fs.mkdirSync(path.dirname(f), { recursive: true });
  const scale = j.w === 1080 && j.h === 1350 ? 1440 / 1080 : 1;
  const p = await browser.newPage({ viewport: { width: j.w, height: j.h }, deviceScaleFactor: scale });
  await p.setContent(page(j.w, j.h, j.b), { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  await p.screenshot({ path: f });
  await p.close();
}
await browser.close();
console.log(`rendered ${jobs.length} images → ${OUT}`);
