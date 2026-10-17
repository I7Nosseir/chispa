#!/usr/bin/env python3
"""Builds reports/copy-paste-kit.html: every AI prompt and outreach message with a copy button.

Prompts are read from the skill's prompt library and the Mayura sample, so the kit stays in sync.
Run: python3 reports/build_copy_kit.py
"""
import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LIB = (ROOT / "skills-src/ai-video-prompt-engineering/references/prompt-library.md").read_text()
MAY = (ROOT / "leads/samples/mayura-khamas-sample.md").read_text()


def blocks(text):
    return [b.strip() for b in re.findall(r"```\n(.*?)```", text, re.S)]


lib, may = blocks(LIB), blocks(MAY)

TEST_BOTTLE = """High-end commercial product photography, Phase One camera, 100mm macro, f/11, crisp focus edge to edge. An original unbranded luxury perfume bottle: tall faceted clear glass, amber liquid, a polished gold cap shaped like a closed peacock tail, and a plain cream label with no text. It stands at the center of a bright, airy scene, filling about half the frame, on a smooth cream sandstone pedestal surrounded by exactly 5 real peacock feathers fanned out behind it like a crown, their blue-green eyes sharp and iridescent. Soft warm-white background with a gentle gradient to pale gold. Lighting: large softbox from the upper left for clean highlights on the glass, a thin rim light from behind that makes the amber liquid glow, a soft fill from the right. Exactly 3 small amber droplets resting on the pedestal. Bright, luxurious, clean, rich colour, glossy magazine advertising look.
NEGATIVE: no text or letters anywhere, no logo, no real brand, exactly 1 bottle, exactly 5 feathers, no dark or moody lighting, no smoke, no ring or halo object, no plastic CGI look."""

MODE_B = """OPENER: High-end commercial product photography, [Phase One / Sony A1], [90–100mm macro], f/8–f/11, crisp focus edge to edge.
CLOSER: Bright, clean, rich colour, glossy magazine advertising look.
NEGATIVE ADD-ON: no dark or moody lighting, no muddy exposure, no plastic CGI look, no invented text."""

RECIPE = """High-end commercial product photography, Sony A1, 100mm macro, f/11, crisp focus edge to edge. The exact [brand] [product] from @product stands at the center of a bright scene, filling about half the frame — already there, same shape, label and colour as the reference. [ONE visual idea from the recipe list: on a marble pedestal with exactly 4 [story prop] behind it / a frozen splash of [liquid] with exactly 7 droplets / on a mossy rock in a sunlit forest with exactly 3 small white flowers / on a sand dune crest at golden hour]. Background: soft gradient in [brand colour 1] to [brand colour 2]. Lighting: large softbox from the upper left, thin rim light from behind on the glass edges, soft fill from the right. Bright, clean, rich colour, glossy magazine advertising look.
NEGATIVE: label and product must exactly match @product, no invented text or logo, no extra products, no dark or moody lighting, no muddy exposure, no ring or halo object, no plastic CGI look, no watermark or reference-image border bleed."""

AI = [
    ("Start here", [
        ("Test bottle: peacock pedestal (no real product needed)", "Still · Nano Banana / Soul / GPT-Image",
         "Use this to test the bright commercial look tonight. Unbranded, so no product photo needed.", TEST_BOTTLE),
        ("Mode B building blocks", "Any still",
         "Paste the opener at the start, the closer at the end, and the negative add-on after your NEGATIVE line.", MODE_B),
        ("Commercial hero: fill-in recipe", "Still · attach @product",
         "Pick one idea in the brackets, delete the others. One visual idea per image.", RECIPE),
    ]),
    ("Mayura Khamas (attach their real bottle as @product)", [
        ("B1: Peacock pedestal (send this one)", "Still · Mode B", "Commercial hero. Bright, product half the frame.", may[3]),
        ("B2: Amber splash", "Still · Mode B", "High-speed splash on a peacock teal gradient.", may[4]),
        ("B3: Dubai dune at golden hour", "Still · Mode B", "Backlit so the amber liquid glows.", may[5]),
        ("B4: 6-second video from B1", "Video · Kling, No Native Audio on", "Start frame = your best B1 image.", may[6]),
        ("V1: Souq counter (real-life look)", "Still · Mode A", "Documentary realism. Use only if they want a 'real shop' vibe.", may[0]),
        ("V1: In-hand snapshot", "Still · Mode A", "iPhone look, hand only.", may[1]),
        ("V1: 5-second counter video", "Video · Kling", "Start frame = the V1 souq still.", may[2]),
    ]),
    ("Real-life stills (Mode A)", [
        ("Perfume: Gulf souq shelf", "Still · attach @product", "", lib[0]),
        ("Abaya: editorial in a real place", "Still · attach @product", "", lib[1]),
        ("Jewelry: macro on skin", "Still · attach @product", "", lib[2]),
        ("Skincare: real bathroom (phone look)", "Still · attach @product", "", lib[3]),
        ("Food: Egyptian table (overhead)", "Still", "Good for restaurant leads like Lucille's or La Margrita.", lib[4]),
    ]),
    ("Video (image-to-video, 5–8 s)", [
        ("Product reveal (silent)", "Video · start from an approved still", "", lib[5]),
        ("UGC creator-style ad", "Video · lock @creator first", "Add voice-over in the edit. Label it as an ad, never as a real customer review.", lib[6]),
        ("Lifestyle B-roll", "Video", "", lib[7]),
        ("Cinematic concept (one impossible beat)", "Video", "Fill every bracket. Only one impossible moment.", lib[8]),
    ]),
    ("Characters", [
        ("Character reference sheet", "Still · make before any recurring person", "Lock the face first, then reuse it as @creator.", lib[9]),
    ]),
]

OUT = [
    ("Egypt: calls and WhatsApp", [
        ("Call opener (say it in your own Arabic)", "Phone",
         "Goal: the owner's name, their WhatsApp, and permission to send the audit.",
         "Hi, I'm Ismail from The Commando. I work with [clinics / restaurants / gyms] in [area]. Quick question: who handles your marketing or social media?\n\nI looked at [Business] before calling. Your reviews are strong ([X] on Google), but [one gap from the sheet]. That usually means people who already like you online end up calling someone else.\n\nFor Grapes Holiday we cut ad spend 62% and got 2.5× the leads. Can I send you a free 2-minute audit on WhatsApp showing exactly what I'd fix? No cost, no commitment. What's the best WhatsApp, and what's your name?"),
        ("Same-day follow-up WhatsApp", "WhatsApp", "Send within a few hours of the call.",
         "Hi [Name], Ismail from The Commando. Thanks for your time today. As promised, here's the quick audit for [Business]: [gap 1], [gap 2]. Happy to walk you through the fix in 10 minutes. Does [day] at [time] work?"),
        ("Day 2 nudge", "WhatsApp", "",
         "Hi [Name], just checking you saw the audit for [Business]. The quickest win is [gap 1]. Want me to show you how I'd fix it this week?"),
        ("Receptionist won't pass you on", "Phone", "Ask for a name, not a transfer.",
         "No problem. What's the owner's or manager's name, so I address it to the right person? Is there a WhatsApp number where management reads messages? I noticed [specific gap, e.g. the phone number on your Instagram is wrong]. Could you let them know? I'll send the details on WhatsApp. When are they usually in?"),
        ("\"We already have someone for social media\"", "Phone", "",
         "Great, that's good to hear. Do they also handle the website, the Google Maps profile and replying to reviews? Most social media people don't. Can I send a free audit anyway? If your person is doing a great job, it'll confirm it. If not, you'll know what to ask them for."),
        ("Instagram DM (when the call doesn't get through)", "Instagram DM", "",
         "Hi [Business] team, I'm Ismail from The Commando. I tried calling earlier. I noticed [one gap] on your Google page, which means people searching for you may not find [your booking link / your menu / your website]. I made a 2-minute audit with the fix. Can I send it here?"),
        ("Referral ask (week 2 with a client)", "WhatsApp", "",
         "Hi [Name], glad the [website / content] is working. One quick favour: do you know 1 or 2 other business owners who have the same problem with [Google / Instagram / bookings]? I'd look after them the same way."),
    ]),
    ("Gulf: message first", [
        ("First message, with the AI sample attached", "WhatsApp / Instagram DM", "English for Dubai. Send 10 AM–1 PM Gulf time.",
         "Hi [Brand] team, I'm Ismail, a performance marketer and AI content producer. I made this image of your [product] as a quick example of what we can do without a studio shoot (attached). I make product visuals and UGC-style video ads for Gulf brands and run the ads too. Want me to send 3 more for free so you can test them in your ads?"),
        ("Mayura Khamas message", "WhatsApp +971 4 352 2319", "Only send it with their real bottle in the image.",
         "Hi Mayura Khamas team, I'm Ismail, a performance marketer and AI content creator. I made this image of your perfume as a quick example of what's possible without a studio shoot (attached). With 856 reviews you clearly have loyal customers, but there's no website or Instagram linked on your Google listing for new people to see the product. I make product visuals and ads for Gulf brands. Want me to send 3 more for free that you can use on Instagram or WhatsApp?"),
        ("Day 3 follow-up", "WhatsApp / DM", "",
         "Hi, just checking you saw the [product] image. Happy to send the 3 free versions this week. Which product should I use?"),
        ("Day 8: last note", "WhatsApp / DM", "Then stop.",
         "Last note from me. If product visuals or ad creatives become a priority, I'm here. Portfolio: [link]."),
        ("When they ask \"how much?\"", "WhatsApp / DM", "Confirm the price before you quote.",
         "A starter pack is 10 product images + 3 short video ads for $[X]. Most brands then move to a monthly pack for fresh ad creatives every week."),
        ("\"We already have an agency / photographer\"", "WhatsApp / DM", "",
         "Makes sense. Most brands I work with keep their photographer for hero shoots and use me for the weekly ad creatives the photographer can't produce fast enough. Want to test 3 against your current ads?"),
    ]),
    ("Jobs", [
        ("Cover message", "Applications", "Fill in full-time or part-time.",
         "I'm a performance marketer who also produces ad creative with AI. As Marketing Director at Grapes Holiday I cut ad spend by 62.5% while generating 2.5× the leads (3,000+ qualified leads). At Rihla Travel's launch we made 350K+ EGP in the first two weeks. I build the landing pages and AI creatives myself, so tests ship fast. Portfolio: [link]. I'm in Cairo and available [full-time/part-time] remotely."),
        ("LinkedIn note to the hiring manager", "LinkedIn", "Send right after you apply.",
         "Hi [Name], I just applied for the [role]. Quick context: at Grapes Holiday I cut ad spend 62.5% while lead volume grew 2.5×. Happy to show how in 10 minutes."),
    ]),
]


def card(cid, title, tag, note, text):
    shown = html.escape(text)
    shown = re.sub(r"(\[[^\]\n]{1,120}\])", r'<mark>\1</mark>', shown)
    shown = re.sub(r"^(NEGATIVE( PROMPT)?:|SCENE:|CHARACTERS:|BEATS:|CAMERA:|STYLE:|OPENER:|CLOSER:|NEGATIVE ADD-ON:)",
                   r'<b>\1</b>', shown, flags=re.M)
    note_html = f'<p class="note">{html.escape(note)}</p>' if note else ""
    return f'''<article class="card" data-search="{html.escape((title + " " + tag + " " + text).lower())}">
  <header class="card-head"><div class="card-titles"><h3>{html.escape(title)}</h3><span class="tag">{html.escape(tag)}</span></div>
  <button type="button" class="copy" data-target="{cid}" aria-label="Copy: {html.escape(title)}">Copy</button></header>
  {note_html}<pre id="{cid}" tabindex="0">{shown}</pre>
</article>'''


def section(prefix, groups):
    out, n = [], 0
    for gi, (gname, items) in enumerate(groups):
        out.append(f'<section class="group"><h2>{html.escape(gname)}</h2><div class="cards">')
        for title, tag, note, text in items:
            n += 1
            out.append(card(f"{prefix}{n}", title, tag, note, text))
        out.append("</div></section>")
    return "\n".join(out), n


ai_html, ai_n = section("ai", AI)
out_html, out_n = section("msg", OUT)

page = f'''<title>Commando Copy Kit</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,800&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;600&display=swap">
<style>
/* Layout: a working kit — sticky tab bar, then dense cards of paste-ready text, one column on phones. */
:root {{
  --bg: #F3F5F4; --surface: #FFFFFF; --ink: #142420; --muted: #56655F;
  --line: #D6DEDA; --accent: #0E7C6B; --accent-ink: #FFFFFF; --mark: #FCE8B2; --ok: #1E7A3A;
  --display: "Bricolage Grotesque", "Segoe UI", system-ui, sans-serif;
  --body: "IBM Plex Sans", "Segoe UI", system-ui, sans-serif;
  --mono: "IBM Plex Mono", ui-monospace, "SFMono-Regular", Menlo, monospace;
}}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{
  --bg: #0F1715; --surface: #17221F; --ink: #E4EEEA; --muted: #9AACA5;
  --line: #2A3A35; --accent: #3FC1A8; --accent-ink: #062019; --mark: #4A3D12; --ok: #5FD38A; color-scheme: dark }} }}
:root[data-theme="dark"] {{
  --bg: #0F1715; --surface: #17221F; --ink: #E4EEEA; --muted: #9AACA5;
  --line: #2A3A35; --accent: #3FC1A8; --accent-ink: #062019; --mark: #4A3D12; --ok: #5FD38A; color-scheme: dark }}
* {{ box-sizing: border-box }}
body {{ background: var(--bg); color: var(--ink); font: 15px/1.55 var(--body);
  padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); padding-block: 0 48px }}
body::before {{ content: ""; position: fixed; inset: 0 0 auto; height: env(safe-area-inset-top, 0px); z-index: 10; background: var(--bg) }}
.wrap {{ max-width: 980px; margin: 0 auto }}
.intro {{ padding-block: 28px 12px; display: grid; gap: 8px }}
h1 {{ font: 800 clamp(28px, 5vw, 40px)/1.05 var(--display); margin: 0; letter-spacing: -0.02em; text-wrap: balance }}
.lede {{ margin: 0; color: var(--muted); max-width: 65ch }}
.rules {{ margin: 4px 0 0; padding: 0; list-style: none; display: flex; flex-wrap: wrap; gap: 6px }}
.rules li {{ font-size: 12.5px; border: 1px solid var(--line); border-radius: 999px; padding: 3px 10px; color: var(--muted); background: var(--surface) }}
.bar {{ position: sticky; top: env(safe-area-inset-top, 0px); z-index: 5; background: var(--bg); padding-block: 10px; display: flex; flex-wrap: wrap; gap: 8px; align-items: center; border-bottom: 1px solid var(--line) }}
.tabs {{ display: flex; gap: 4px; background: var(--surface); border: 1px solid var(--line); border-radius: 10px; padding: 3px }}
.tab {{ font: 600 14px var(--body); border: 0; background: transparent; color: var(--muted); padding: 7px 14px; border-radius: 7px; cursor: pointer }}
.tab[aria-selected="true"] {{ background: var(--accent); color: var(--accent-ink) }}
.count {{ font-size: 12px; opacity: .8; margin-left: 4px; font-variant-numeric: tabular-nums }}
#q {{ flex: 1 1 200px; min-width: 0; font: 14px var(--body); color: var(--ink); background: var(--surface); border: 1px solid var(--line); border-radius: 10px; padding: 9px 12px }}
#q:focus-visible, .tab:focus-visible, .copy:focus-visible, pre:focus-visible {{ outline: 2px solid var(--accent); outline-offset: 2px }}
.group h2 {{ font: 700 13px var(--body); letter-spacing: .08em; text-transform: uppercase; color: var(--muted); margin: 28px 0 10px }}
.cards {{ display: grid; gap: 12px }}
.card {{ background: var(--surface); border: 1px solid var(--line); border-radius: 12px; padding: 14px 16px; display: grid; gap: 8px; min-width: 0 }}
.card-head {{ display: flex; gap: 12px; align-items: flex-start; justify-content: space-between }}
.card-titles {{ display: grid; gap: 2px; min-width: 0 }}
h3 {{ font: 600 17px/1.3 var(--display); margin: 0; text-wrap: balance }}
.tag {{ font: 12.5px var(--mono); color: var(--accent) }}
.note {{ margin: 0; font-size: 13.5px; color: var(--muted) }}
pre {{ margin: 0; font: 13px/1.6 var(--mono); white-space: pre-wrap; word-break: break-word; background: var(--bg); border: 1px solid var(--line); border-radius: 8px; padding: 12px; max-height: 340px; overflow: auto }}
pre b {{ color: var(--accent); font-weight: 600 }}
mark {{ background: var(--mark); color: inherit; border-radius: 3px; padding: 0 2px }}
.copy {{ flex: none; font: 600 14px var(--body); border: 0; background: var(--accent); color: var(--accent-ink); padding: 8px 16px; border-radius: 8px; cursor: pointer; min-width: 84px }}
.copy.done {{ background: var(--ok) }}
.empty {{ color: var(--muted); padding: 24px 0 }}
@media (prefers-reduced-motion: no-preference) {{ .copy {{ transition: background .15s }} }}
</style>

<div class="wrap">
  <div class="intro">
    <h1>Commando Copy Kit</h1>
    <p class="lede">Every AI prompt and outreach message, ready to paste. Tap <b>Copy</b>, paste it into Higgsfield, WhatsApp or LinkedIn, then replace the <mark>[highlighted]</mark> parts.</p>
    <ul class="rules">
      <li>Attach the real product as @product</li><li>Never send an invented label</li>
      <li>Label samples "spec concept"</li><li>AI UGC is an ad, never a fake review</li><li>Turn on the platform's AI label</li>
    </ul>
  </div>
  <div class="bar">
    <div class="tabs" role="tablist">
      <button type="button" class="tab" role="tab" id="tab-ai" aria-selected="true" aria-controls="panel-ai">AI prompts<span class="count">{ai_n}</span></button>
      <button type="button" class="tab" role="tab" id="tab-msg" aria-selected="false" aria-controls="panel-msg">Messages<span class="count">{out_n}</span></button>
    </div>
    <input id="q" type="search" placeholder="Search: perfume, day 3, receptionist…" aria-label="Search prompts and messages">
  </div>
  <div id="panel-ai" role="tabpanel" aria-labelledby="tab-ai">{ai_html}</div>
  <div id="panel-msg" role="tabpanel" aria-labelledby="tab-msg" hidden>{out_html}</div>
  <p class="empty" id="empty" hidden>Nothing matches that search.</p>
</div>

<script>
(function () {{
  var tabs = document.querySelectorAll('.tab');
  var q = document.getElementById('q');
  function show(id) {{
    tabs.forEach(function (t) {{
      var on = t.id === id;
      t.setAttribute('aria-selected', on ? 'true' : 'false');
      document.getElementById(t.getAttribute('aria-controls')).hidden = !on;
    }});
    try {{ localStorage.setItem('kit-tab', id); }} catch (e) {{}}
    filter();
  }}
  tabs.forEach(function (t) {{ t.addEventListener('click', function () {{ show(t.id); }}); }});
  function filter() {{
    var term = q.value.trim().toLowerCase(), any = false;
    var panel = document.querySelector('[role=tabpanel]:not([hidden])');
    panel.querySelectorAll('.group').forEach(function (g) {{
      var visible = 0;
      g.querySelectorAll('.card').forEach(function (c) {{
        var hit = !term || c.dataset.search.indexOf(term) !== -1;
        c.hidden = !hit; if (hit) visible++;
      }});
      g.hidden = visible === 0; if (visible) any = true;
    }});
    document.getElementById('empty').hidden = any;
  }}
  q.addEventListener('input', filter);
  function selectText(el) {{
    var r = document.createRange(); r.selectNodeContents(el);
    var s = window.getSelection(); s.removeAllRanges(); s.addRange(r);
  }}
  document.addEventListener('click', function (e) {{
    var b = e.target.closest('.copy'); if (!b) return;
    var pre = document.getElementById(b.dataset.target);
    var text = pre.innerText;
    function ok(label) {{ b.textContent = label; b.classList.add('done');
      setTimeout(function () {{ b.textContent = 'Copy'; b.classList.remove('done'); }}, 1800); }}
    function fallback() {{
      selectText(pre);
      var done = false; try {{ done = document.execCommand('copy'); }} catch (err) {{}}
      ok(done ? 'Copied' : 'Selected: press Ctrl+C');
    }}
    if (navigator.clipboard && navigator.clipboard.writeText) {{
      navigator.clipboard.writeText(text).then(function () {{ ok('Copied'); }}, fallback);
    }} else {{ fallback(); }}
  }});
  var saved = null; try {{ saved = localStorage.getItem('kit-tab'); }} catch (e) {{}}
  if (saved && document.getElementById(saved)) show(saved);
}})();
</script>
'''
(ROOT / "reports/copy-paste-kit.html").write_text(page, encoding="utf-8")
print(f"{ai_n} prompts, {out_n} messages")
