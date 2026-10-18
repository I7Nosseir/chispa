#!/usr/bin/env python3
"""Batch 2 call sheets: every Tier B lead (57 Egypt + 33 Dubai), built like batch 1.

Each lead gets:
- a realism rating (Go now / Pilot only / Park for later),
- a real competitor fact: the strongest same-niche place within 5 km from the
  same Google Maps pull (leads/raw/places-2026-10-11.json, 11 Oct 2026),
- the 8-step call (permission + reason, insight, poke, qualify, certainty,
  no-oriented small ask, one loop, future pace),
- a route to the decision-maker using only channels the business publishes,
- copy buttons for the call script and the WhatsApp/DM version.

The playbook (method, sources, honesty rules) is shared with batch1.py.
Run: python3 batch2.py  → batch2-call-sheets.md + batch2-call-sheets.html
"""
import csv
import html
import json
import math
import re
from pathlib import Path

import batch1 as b1

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
LEADS = ROOT / "leads" / "all-leads-2026-10-11.csv"
RAW = ROOT / "leads" / "raw" / "places-2026-10-11.json"

NOT_A_SITE = ("facebook.", "instagram.", "forms.gle", "yellowpages", "wordpress.com", "weebly", "youtube.",
              "skedda", "linktr.ee", "wa.me", "lovable.app", "web-rack")
CHAIN = re.compile(r"gold'?s gym|gymnation|malabar|tanishq|just me|restart fitness|branch|xbeauty|nysaa", re.I)

GROUP = {
    "Dental": "clinic", "Dermatology": "clinic", "Physio": "clinic", "Aesthetic": "clinic", "Clinic": "clinic",
    "Beauty": "salon", "Gym": "gym", "Fitness": "gym", "Padel": "gym",
    "Restaurant": "food", "Cafe": "food", "Coffee": "food",
    "Real estate": "realestate",
    "Perfume": "product", "Abaya": "product", "Jewelry": "product", "Skincare": "product",
}
PLURAL = {"Dental": "dental clinics", "Dermatology": "skin clinics", "Physio": "physio clinics",
          "Aesthetic": "aesthetic clinics", "Clinic": "clinics", "Beauty": "salons", "Gym": "gyms",
          "Fitness": "fitness studios", "Padel": "padel clubs", "Restaurant": "restaurants", "Cafe": "cafés",
          "Coffee": "coffee shops", "Real estate": "real estate brokers", "Perfume": "perfume shops",
          "Abaya": "abaya shops", "Jewelry": "jewellers", "Skincare": "skincare shops"}

WHEN = {"clinic": "Before clinic hours (late morning); ask when the doctor is free",
        "salon": "11 AM–1 PM, before it gets busy", "gym": "11 AM–1 PM (quiet hours)",
        "food": "4–6 PM, never at lunch or dinner", "realestate": "11 AM–2 PM",
        "product": "Message Mon–Fri, 10 AM–1 PM Dubai time"}
ROUTE = {"clinic": b1.R_CLINIC, "salon": b1.R_SALON, "food": b1.R_REST,
         "gym": "Ask at reception for the owner or manager and when they're in (quiet hours are 11 AM–1 PM). Or DM the gym's Instagram/Facebook page.",
         "realestate": "Brokers answer their own phones. Ask for the owner or sales manager by name, or message the WhatsApp on the listing.",
         "product": "WhatsApp the listed number with the sample, or DM their Instagram if you find one. Call only after they reply."}
DUBAI_ROUTE = "Message first (WhatsApp, or Instagram DM if they have one). Ask for the manager by name in the reply. Call only after they answer."

QUESTIONS = {
    "clinic": ["Where do most new patients find you now: referrals, Instagram or Google?",
               "Which treatment do you want more of?", "Who replies to Google reviews at the moment?"],
    "salon": ["Where do new clients find you now: Instagram, word of mouth or Maps?",
              "Which service do you want to sell more?", "Do clients book by phone or WhatsApp?"],
    "gym": ["When do you sign the most members?", "What do the bad reviews usually complain about?",
            "Who runs your Instagram now?"],
    "food": ["How much of your business is delivery versus dine-in?", "Which day or time is slowest?",
             "Who runs your Instagram now?"],
    "realestate": ["Where do your best leads come from now: portals, referrals or social?",
                   "Which projects or areas do you want to push?", "Do you run any ads at the moment?"],
    "product": ["Which product sells best?", "Do you sell online or only in the shop?",
                "Do you have product photos I can work from?"],
}
OBJECTION = {
    "clinic": ("We get patients from referrals anyway.",
               "That's the best kind. This is for the second half: people who are referred and then Google you before they book. Can I show you what they see?"),
    "salon": ("We already have someone for Instagram.",
              "Great, keep them. This is the Google side: the listing, the link to your work and the review replies. Can I send the audit so you can hand it to them?"),
    "gym": ("Those bad reviews are from competitors.",
            "Some may be. A calm, public reply still shows the next reader you care. I'll write them for you. Can I send them?"),
    "food": ("Everyone around here already knows us.",
             "They do, that's your reviews. This is for the people who don't yet and decide on Maps. Can I show you what they see?"),
    "realestate": ("We get leads from the portals.",
                   "Keep them. A simple page of your own means the leads you pay for can check you out and come back without the portal. Can I send the idea?"),
    "product": ("We don't need social media, the shop is busy.",
                "That's what your reviews say. These images are for the people who check online before they walk in or order. Want the free ones?"),
}
FUTURE = {
    "clinic": "A patient searches for your treatment nearby, sees your rating and real replies, taps once and books on WhatsApp.",
    "salon": "Someone searching for a salon nearby sees your rating, taps once and lands on your work and your WhatsApp.",
    "gym": "Every review has a calm owner's reply, the rating climbs, and new members come in from Maps.",
    "food": "Someone nearby opens Maps, sees your rating and your food photos, and orders from you instead of next door.",
    "realestate": "A buyer finds your name, sees your listings and reviews on your own page and calls you directly.",
    "product": "People who find you on Maps see your products in bright photos and walk in or order before they reach the next shop.",
}


def digits(p):
    return re.sub(r"\D", "", p or "")[-9:]


def real_site(w):
    return bool(w) and not any(x in w for x in NOT_A_SITE)


def presence(p):
    out = []
    if real_site(p.get("website")):
        out.append("a website")
    if p.get("instagrams"):
        out.append("Instagram")
    if p.get("tiktoks"):
        out.append("TikTok")
    return out


def km(a, b):
    la1, lo1, la2, lo2 = map(math.radians, (a["location.lat"], a["location.lng"], b["location.lat"], b["location.lng"]))
    h = math.sin((la2 - la1) / 2) ** 2 + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2
    return 6371 * 2 * math.asin(math.sqrt(h))


def joinlist(xs):
    return xs[0] if len(xs) == 1 else ", ".join(xs[:-1]) + " and " + xs[-1]


def load():
    raw = json.loads(RAW.read_text(encoding="utf-8"))
    places = []
    for ds, items in raw.items():
        for it in items:
            if it.get("location.lat") is None or it.get("permanentlyClosed"):
                continue
            it["_ds"] = ds
            places.append(it)
    leads = [r for r in csv.DictReader(LEADS.open(encoding="utf-8-sig")) if r["Tier"].startswith("B")]
    return leads, places


def match(lead, places):
    d = digits(lead["Phone"])
    for p in places:
        if d and digits(p.get("phone")) == d:
            return p
    name = lead["Business"].lower().split(" (")[0][:14]
    for p in places:
        if (p.get("title") or "").lower().startswith(name):
            return p
    return None


def rival_for(lead, me, places):
    """Strongest same-search competitor within 5 km; prefer one with presence the lead lacks."""
    if not me:
        return None, []
    mine = set(presence(me))
    pool = []
    for p in places:
        if p is me or p.get("searchString") != me.get("searchString") or p["_ds"] != me["_ds"]:
            continue
        if not p.get("reviewsCount") or km(me, p) > 5:
            continue
        extra = [x for x in presence(p) if x not in mine]
        score = (p["reviewsCount"] or 0) * (1 + 2 * len(extra)) * (p.get("totalScore") or 4) / 5
        pool.append((score, p, extra))
    pool.sort(key=lambda x: -x[0])
    return (pool[0][1], pool[0][2]) if pool else (None, [])


def clean_name(t):
    t = re.split(r"\s[-|–]\s|\s\|\s", t)[0]
    t = re.sub(r"[؀-ۿ]+", "", t).strip(" -|،,")
    if t.islower() or t.isupper():
        t = t.title()
    return t or "a competitor"


def main_gap(r):
    g = [x.strip().rstrip(".") for x in r["Gaps"].split(" • ") if x.strip()]
    for pat in ("Google 'website'", "Website is a free", "Maps name", "different name"):
        for x in g:
            if x.startswith(pat) or pat in x:
                return x
    for pat in ("one-star", "Rating ", "Only "):
        for x in g:
            if pat in x:
                return x
    return g[0] if g else ""


def gap_sentence(r):
    g = main_gap(r)
    m = re.search(r"not a real site \((.+?)\)", r["Gaps"])
    if "Google 'website'" in g or "Website is a free" in g:
        target = m.group(1) if m else "a page that isn't your own site"
        return f"the website button on your Google listing opens {target}, not your own site"
    if "Maps name" in g or "different name" in g:
        return "your name on Google Maps doesn't match your Instagram, so people who find you in one place can't find you in the other"
    m = re.search(r"([\d,]+) one-star (?:reviews )?(?:out )?of ([\d,]+)", g)
    if m:
        return f"{m.group(1)} of your {m.group(2)} Google reviews are one-star, and a calm reply under each one changes how new customers read them"
    m = re.search(r"Rating ([\d.]+): below the ([\d.]+)", g)
    if m:
        return f"your Google rating is {m.group(1)}, just under the {m.group(2)} many people filter by"
    m = re.search(r"Only (\d+) Google reviews", g)
    if m:
        return f"you only have {m.group(1)} Google reviews, so you show up below busier competitors on Maps"
    if "No TikTok" in r["Gaps"]:
        return "you're not on TikTok yet, which is the cheapest place to test video ads"
    if "No website" in r["Gaps"] and ("No Instagram" in r["Gaps"]):
        return "your Google listing has no website and no Instagram or TikTok linked, so people who find you on Maps can't see your work"
    if "No website" in r["Gaps"]:
        return "your Google listing has no website, so people can't see prices or book from there"
    return "your Google listing doesn't show your work"


def poke_for(r, group):
    g = main_gap(r)
    if "Google 'website'" in g or "Website is a free" in g:
        return "Who set up your Google listing, and does anyone check where the links go?"
    if "one-star" in g or "Rating" in g:
        return "Who replies to the bad reviews at the moment?"
    if "Only " in g:
        return "What do you do now to get happy customers to leave a Google review?"
    if group == "product":
        return "How do people who find you on Maps see your products before they come in?"
    return "When someone finds you on Google Maps, how do they get to see your work before they call?"


def verdict(r, me):
    reviews = int(float(r["Reviews"] or 0))
    rating = float(r["Rating"] or 0)
    pres = presence(me) if me else []
    if CHAIN.search(r["Business"]):
        return "PARK", "A chain or multi-branch business. Marketing is decided centrally, not in this branch."
    if len(pres) >= 2 and reviews > 300:
        return "PILOT", f"Already has {joinlist(pres)} and {reviews:,} reviews. Pitch one small test, not a rebuild."
    if rating and rating < 3.8:
        return "PILOT", f"Rated {rating}, so it's struggling and may not pay much. Offer review care only."
    group = GROUP.get(r["Niche"], "clinic")
    dubai = r["Region"].startswith("UAE")
    if group == "realestate" and (dubai or reviews < 5):
        return "PILOT", ("A brokerage with agents and portal budgets; reply odds are low. Offer one landing page for one project." if dubai
                         else f"Only {reviews} reviews; it may be tiny or inactive. Check it's active before you spend time.")
    if dubai and group == "food":
        return "PILOT", "Dubai cafés and restaurants get pitched daily. One free sample, then let it go if there's no reply."
    if dubai and group == "clinic" and len(pres) >= 2:
        return "PILOT", f"Already has {joinlist(pres)}; DHA ad rules apply. Pitch review replies or one TikTok test only."
    if re.search(r"salons|clinics|centers|centres", r["Business"], re.I) and reviews > 300:
        return "PILOT", "The plural name may mean several branches. Ask whether it's one place before pitching."
    if reviews < 15:
        return "GO", f"Small or new ({reviews} reviews), with a small budget. Start with the listing fix and a review plan."
    if dubai:
        return "GO", "Owner-run shop or clinic with a gap you can show in one message."
    return "GO", "Owner-run, single location, with a gap you can point at on the call."


def build_one(i, r, places):
    me = match(r, places)
    group = GROUP.get(r["Niche"], "clinic")
    dubai = r["Region"].startswith("UAE")
    if dubai and group == "clinic":
        pass
    plural = PLURAL.get(r["Niche"], "businesses")
    area = r["Area"].split(" (")[0]
    rv, extra = rival_for(r, me, places)
    reviews = int(float(r["Reviews"] or 0))
    if rv:
        dist = km(me, rv)
        where = "nearby" if dist < 0.6 else f"about {dist:.1f} km away"
        rname = clean_name(rv["title"])
        rfact = f"{rname}, {where}, has {float(rv.get('totalScore') or 0):.1f}★ from {rv['reviewsCount']:,} reviews"
        rfact += f" and links {joinlist(extra)} on Google." if extra else "."
        better_rating = (rv.get("totalScore") or 0) < float(r["Rating"] or 0)
        if extra and better_rating:
            insight_rival = f"{rname} has a lower rating than you ({rv.get('totalScore')} vs {r['Rating']}), but links {joinlist(extra)}, so people comparing on Maps see its work and not yours."
        elif extra:
            insight_rival = f"{rname}, {where}, links {joinlist(extra)} on Google, so people comparing on Maps see its work first."
        elif rv["reviewsCount"] > reviews:
            insight_rival = f"{rname}, {where}, has {rv['reviewsCount']:,} reviews to your {reviews:,}, so it looks like the safer choice on Maps."
        else:
            insight_rival = f"You already have more reviews than {rname} ({reviews:,} vs {rv['reviewsCount']:,}), so you're the one to beat nearby. The listing just needs to show it."
    else:
        rfact = f"No close competitor in the same search had more presence, so lead with the gap itself."
        insight_rival = ""
    v, why = verdict(r, me)
    gs = gap_sentence(r)
    if dubai:
        opener = f"Hi {r['Business'].split(' (')[0]} team, I'm Ismail. I make product visuals and ads for Gulf businesses and run the ads myself. I compared {plural} in {area} on Google this week."
        if group == "product":
            ask = "I made one image of your product as an example (attached). Want 3 more, free, ready for Instagram or WhatsApp?"
        else:
            ask = "Can I send a free one-page audit with the 3 fixes?"
        proof = b1.PROOF_GULF
        no_ask = b1.NO_ASK_GULF if group == "product" else "Would it be a bad idea if I sent you the free audit?"
        route = DUBAI_ROUTE
        when = WHEN["product"]
    else:
        opener = f"Hi, this is Ismail. I work with {plural} in {area}. I compared {plural} near you on Google Maps this week and noticed something about {r['Business'].split(' (')[0]} I think you'd want to know. Can I take 30 seconds?"
        ask = "Can I send you a free 2-minute audit on WhatsApp with the exact fix? Who should I send it to?"
        proof = b1.PROOF_LEADS if group != "food" else b1.PROOF_LAUNCH
        no_ask = b1.NO_ASK
        route = ROUTE.get(group, b1.R_CLINIC)
        when = WHEN.get(group, WHEN["clinic"])
    base = f"{r['Rating']}★ from {reviews:,} reviews is a real base." if reviews >= 100 else f"The people who came rate you {r['Rating']}★."
    insight = f"{base} But {gs}. {insight_rival}".strip()
    them = f"{r['Rating']}★ from {reviews:,} reviews. " + "; ".join(x.strip().rstrip('.') for x in r["Gaps"].split(" • ") if x.strip() and not x.startswith("Product business")) + "."
    check = "Open their Google listing and Instagram on your phone first and confirm the gap is still there."
    if group == "clinic":
        check += " Never use patient photos without written consent."
    if dubai and group == "product":
        check += " Only send an image made from their real product photo; never an invented label."
    return dict(i=i, region=r["Region"], n=int(r["Priority #"]), name=r["Business"], area=r["Area"], niche=r["Niche"],
                phone=r["Phone"], when=when, them=them, rival=rfact, opener=opener, insight=insight,
                poke=poke_for(r, group), questions=QUESTIONS[group], proof=proof, ask=ask, no_ask=no_ask,
                objection=OBJECTION[group], future=FUTURE[group], check=check, v=v, why=why, route=route,
                offer=r["Offer"], deal=r["Deal size"])


def script(b):
    q = "\n".join(f"  - {x}" for x in b["questions"])
    return (f"1 PERMISSION + REASON: {b['opener']}\n\n2 INSIGHT: {b['insight']}\n\n3 POKE (then stop talking): {b['poke']}\n\n"
            f"4 QUALIFY:\n{q}\n\n5 CERTAINTY: {b['proof']}\n\n6 SMALL ASK: {b['ask']}\n   or, no-oriented: {b['no_ask']}\n\n"
            f"7 IF \"{b['objection'][0]}\": {b['objection'][1]}\n\n8 FUTURE: {b['future']}")


def written(b):
    if b["region"].startswith("UAE"):
        return f"{b['opener']} {b['insight']} {b['ask'].replace('Want 3 more, free', 'I can send 3 more, free')} Open to seeing them?" if "image" in b["ask"] else f"{b['opener']} {b['insight']} I wrote a one-page audit with the 3 fixes, free. Open to seeing it?"
    return (f"Hi, this is Ismail. I work with {PLURAL.get(b['niche'], 'businesses')} in {b['area'].split(' (')[0]}. "
            f"I compared listings near you on Google this week. {b['insight']} I wrote a 2-minute audit with the fix, free. Open to seeing it?")


def build(sheets):
    order = b1.ORDER
    md = ["# Batch 2 call sheets: Tier B, 90 businesses (18 Oct 2026)", "",
          "Batch 2 = every Tier B lead: 57 in Egypt (call) and 33 in Dubai (message first). Built like batch 1.",
          "Each lead has a realism rating, a real competitor fact (the strongest same-niche place within 5 km in the 11 Oct Google Maps pull), the 8-step call and a route to the decision-maker.",
          "The playbook, sources and honesty rules are in batch 1. **Check each fact on your phone before you call.**", ""]
    cards = []
    for region in ["Egypt", "UAE (Dubai)"]:
        rs = sorted([s for s in sheets if s["region"] == region], key=lambda s: (order[s["v"]], s["n"]))
        md += [f"## {region} ({len(rs)})", ""]
        for s in rs:
            md += [f"### {s['n']}. {s['name']} [{b1.LABEL[s['v']]}]",
                   f"{s['area']} · {s['niche']} · {s['phone']} · Best time: {s['when']}", "",
                   f"- **Realism:** {s['why']}",
                   f"- **Reaching the decision-maker:** {s['route']}",
                   f"- **Them:** {s['them']}",
                   f"- **Competitor insight:** {s['rival']}",
                   f"- **Open:** \"{s['opener']}\"",
                   f"- **Insight:** \"{s['insight']}\"",
                   f"- **Poke (then stop talking):** \"{s['poke']}\"",
                   "- **Qualify:** " + " / ".join(s["questions"]),
                   f"- **Certainty:** \"{s['proof']}\"",
                   f"- **Small ask:** \"{s['ask']}\" (or: \"{s['no_ask']}\")",
                   f"- **If they say** \"{s['objection'][0]}\" → \"{s['objection'][1]}\"",
                   f"- **Future pace:** \"{s['future']}\"",
                   f"- **Offer and price range:** {s['offer']} · {s['deal']} (first deals: use the pricing menu in reports/pricing-2026-10-17.md)",
                   f"- **Check first:** {s['check']}", ""]
            reg = "egypt" if region == "Egypt" else "dubai"
            e = html.escape
            qs = "".join(f"<li>{e(q)}</li>" for q in s["questions"])
            cards.append(f'''<article class="lead v-{s['v'].lower()}" data-region="{reg}" data-search="{e((s['name']+' '+s['area']+' '+s['niche']+' '+b1.LABEL[s['v']]).lower())}">
  <header><div><span class="badge b-{s['v'].lower()}">{b1.LABEL[s['v']]}</span><h3><span class="num">{s['n']}</span>{e(s['name'])}</h3>
  <p class="meta">{e(s['area'])} · {e(s['niche'])}</p>
  <p class="meta"><span class="phone">{e(s['phone'])}</span> · {e(s['when'])}</p></div></header>
  <dl>
    <div class="real"><dt>Realism</dt><dd>{e(s['why'])}</dd></div>
    <div class="route"><dt>Reaching the decision-maker</dt><dd>{e(s['route'])}</dd></div>
    <div><dt>Them</dt><dd>{e(s['them'])}</dd></div>
    <div class="rival"><dt>Competitor insight</dt><dd>{e(s['rival'])}</dd></div>
  </dl>
  <ol class="steps">
    <li><b>Open</b> “{e(s['opener'])}”</li>
    <li><b>Insight</b> “{e(s['insight'])}”</li>
    <li><b>Poke</b> “{e(s['poke'])}” <i>then stop talking</i></li>
    <li><b>Qualify</b><ul>{qs}</ul></li>
    <li><b>Certainty</b> “{e(s['proof'])}”</li>
    <li><b>Small ask</b> “{e(s['ask'])}”<br><span class="alt-ask">Or: “{e(s['no_ask'])}”</span></li>
    <li><b>If they say</b> “{e(s['objection'][0])}” → “{e(s['objection'][1])}”</li>
    <li><b>Future pace</b> “{e(s['future'])}”</li>
  </ol>
  <p class="check"><b>Check first:</b> {e(s['check'])}</p>
  <div class="actions">
    <button type="button" class="copy" data-target="b2s{s['i']}">Copy call script</button>
    <button type="button" class="copy alt" data-target="b2m{s['i']}">Copy {'DM' if reg == 'dubai' else 'WhatsApp'} version</button>
  </div>
  <pre id="b2s{s['i']}" class="src" hidden>{e(script(s))}</pre>
  <pre id="b2m{s['i']}" class="src" hidden>{e(written(s))}</pre>
</article>''')
    (HERE / "batch2-call-sheets.md").write_text("\n".join(md), encoding="utf-8")
    tpl = (HERE / "batch1-template.html").read_text(encoding="utf-8")
    counts = {k: sum(1 for s in sheets if s["v"] == k) for k in ("GO", "PILOT", "PARK")}
    tpl = tpl.replace("<title>Batch 1 Call Sheets</title>", "<title>Batch 2 Call Sheets</title>")
    tpl = tpl.replace("<h1>Batch 1 Call Sheets</h1>", "<h1>Batch 2 Call Sheets</h1>")
    tpl = re.sub(r'<p class="lede">.*?</p>',
                 '<p class="lede">The 90 Tier B businesses, each rated for realism: <b>{{N_GO}} go now</b>, {{N_PILOT}} pilot only and {{N_PARK}} parked. '
                 'Every approach opens with a real competitor fact: the strongest same-niche place within 5 km in the 11 Oct Google Maps pull. '
                 '<b>Check each fact on your phone before you call.</b> Start with batch 1; this is the next list.</p>', tpl, count=1, flags=re.S)
    page = tpl.replace("{{METHOD}}", b1.method_html()).replace("{{CARDS}}", "\n".join(cards))
    page = page.replace("{{N_GO}}", str(counts["GO"])).replace("{{N_PILOT}}", str(counts["PILOT"])).replace("{{N_PARK}}", str(counts["PARK"]))
    page = page.replace("{{N_EG}}", str(sum(1 for s in sheets if s["region"] == "Egypt"))).replace("{{N_AE}}", str(sum(1 for s in sheets if s["region"] != "Egypt")))
    (HERE / "batch2-call-sheets.html").write_text(page, encoding="utf-8")
    return counts


if __name__ == "__main__":
    leads, places = load()
    sheets = [build_one(i, r, places) for i, r in enumerate(leads)]
    unmatched = [s["name"] for s, r in zip(sheets, leads) if match(r, places) is None]
    counts = build(sheets)
    print(f"{len(sheets)} sheets · {counts} · unmatched: {unmatched}")
