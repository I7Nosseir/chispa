#!/usr/bin/env python3
"""Builds the Command Center page (index.html) and the Business Directory (directory.md)
from commando/leads/all-leads-2026-10-11.csv plus report.md and approach.md.

Run: python3 build.py   (needs `pip install markdown`)
"""
import csv, json, os, re, html
import markdown

HERE = os.path.dirname(os.path.abspath(__file__))
LEADS = os.path.join(HERE, '..', 'leads', 'all-leads-2026-10-11.csv')

PLURAL = {'Dental': 'dental clinics', 'Gym': 'gyms', 'Beauty': 'salons', 'Restaurant': 'restaurants',
          'Dermatology': 'skin clinics', 'Physio': 'physio clinics', 'Real estate': 'real estate brokers',
          'Abaya': 'abaya brands', 'Perfume': 'perfume brands', 'Aesthetic': 'aesthetic clinics',
          'Fitness': 'fitness studios', 'Coffee': 'cafés', 'Jewelry': 'jewelry brands', 'Skincare': 'skincare brands',
          'Padel': 'padel clubs', 'Cafe': 'cafés', 'Clinic': 'clinics'}
PRODUCT = {'Perfume', 'Abaya', 'Jewelry', 'Skincare'}
SKIP = ('Product business', 'Has a site', 'Big review base')


def gaps_of(x):
    return [g.strip().rstrip('.') for g in x['Gaps'].split(' • ') if g.strip() and not g.startswith(SKIP)]


def rank(g):
    if g.startswith("Google 'website'") and 'not a real site' not in g:
        return 0
    if 'different name' in g or 'Two names' in g or 'Maps name' in g or 'shares the same phone' in g or 'personal' in g:
        return 0
    if 'Website is a free' in g or 'not a real site' in g:
        return 1
    if 'one-star' in g:
        return 2
    if 'Rating' in g:
        return 2
    if g.startswith('No website'):
        return 3
    if g.startswith('No Instagram'):
        return 4
    return 5


def best_gap(x):
    gs = sorted(gaps_of(x), key=rank)
    return gs[0] if gs else ''


def to_you(g):
    """Turn an audit note about 'their' listing into a sentence addressed to the owner."""
    m = re.match(r"(\d[\d,]*) one-star (?:reviews )?(?:out )?of ([\d,]+)", g)
    if m:
        return f"{m.group(1)} of your {m.group(2)} Google reviews are one-star, and a short reply to each changes how new customers read them"
    m = re.match(r"Only (\d+) Google reviews", g)
    if m:
        return f"you only have {m.group(1)} Google reviews, so you show up below competitors on Maps"
    m = re.match(r"Rating ([\d.]+): below the ([\d.]+)", g)
    if m:
        return f"your Google rating is {m.group(1)}, just under the {m.group(2)} many people filter by"
    m = re.match(r"Google 'website' is not a real site \((.+)\)", g)
    if m:
        return f"the website button on your Google listing opens {m.group(1)}, not a website"
    if g.startswith('No website on'):
        return "your Google Maps listing has no website, so people can't see prices or book from there"
    if g.startswith('No Instagram/Facebook/TikTok'):
        return "your Google listing doesn't link to any Instagram, Facebook or TikTok, so people who find you on Maps can't see your work"
    if g.startswith('No Instagram/TikTok'):
        return "your Google listing doesn't link to an Instagram or TikTok, so people who find you on Maps can't see your work"
    if g.startswith('No TikTok'):
        return "you're not on TikTok yet, which is the cheapest place to test video ads"
    s = g.replace("Google 'website'", "the website button on your Google listing")
    s = re.sub(r'\btheir\b', 'your', s)
    s = re.sub(r'\bthe site\b', 'your site', s)
    return s[0].lower() + s[1:]


def short_topic(g):
    if 'one-star' in g: return 'your one-star reviews'
    if 'Google reviews' in g: return 'your Google reviews'
    if 'Rating' in g: return 'your Google rating'
    if "website" in g.lower() and ('not a real' in g or "Google 'website'" in g or 'free' in g): return 'the website button on your Google listing'
    if g.startswith('No website'): return 'the missing website on your Google listing'
    if g.startswith('No Instagram') or g.startswith('No TikTok'): return 'linking your Instagram/TikTok to Google'
    if 'name' in g.lower(): return 'your business name across Google and Instagram'
    return 'your Google listing'


def area_short(a):
    return re.sub(r'\s*\(.*\)', '', a).strip()


def lead(x, i):
    egypt = x['Region'] == 'Egypt'
    g = best_gap(x)
    you = to_you(g) if g else 'your online presence is thin compared to your reputation'
    topic = short_topic(g) if g else 'your Google listing'
    try:
        rv, nr = float(x['Rating'] or 0), int(float(x['Reviews'] or 0))
    except ValueError:
        rv, nr = 0, 0
    if rv >= 4.3 and nr >= 50:
        praise = f"{x['Rating']}★ from {x['Reviews']} reviews is strong"
    elif nr >= 50:
        praise = f"{x['Reviews']} reviews shows a lot of people know you"
    elif rv >= 4.5:
        praise = f"a {x['Rating']}★ rating is a great start"
    else:
        praise = "people clearly know you"
    product = not egypt and x['Niche'] in PRODUCT
    niche = PLURAL.get(x['Niche'], x['Niche'].lower())
    place = area_short(x['Area']) + ('' if egypt else ', Dubai')
    name = x['Business']
    short = re.sub(r'\s*\(.*\)', '', name).strip()
    copies = []
    if not product:
        copies.append(('Warm note (WhatsApp / Instagram DM)',
            f"Hi {short} team, I'm Ismail. I work on marketing for {niche} in {area_short(x['Area']) if egypt else 'Dubai'}. "
            f"I was looking at your Google page: {praise}. One thing I noticed: {you}. "
            f"I wrote a short note on how to fix it. It takes about 10 minutes on your side and it's free. Should I send it here?"))
    else:
        copies.append(('Sample-first message (WhatsApp / Instagram DM)',
            f"Hi {short} team, I'm Ismail, a performance marketer and AI content producer. I made this image of your "
            f"[product name] as a quick example of what we can do without a studio shoot (attached). I make product visuals "
            f"and UGC-style video ads for Gulf brands and run the ads too. Want me to send 3 more for free so you can test them in your ads?"))
    copies.append(('Warm call opener (only after they reply)',
        ("Hi, this is Ismail. I sent you the image of your product. Did you like it? " if product else
         f"Hi, this is Ismail. I sent you a note about {topic}. Did it make sense? ") +
        (f"Who looks after your ads and content at {short}? I'd like 10 minutes to show you 3 more versions." if product else
         f"Who looks after your marketing at {short}? I'd like 10 minutes to show you the fix on your phone.")))
    copies.append(('Follow-up (day 3)',
        "Hi, just checking you saw the image of your product. Happy to send the 3 free versions this week. Which product should I use? Ismail" if product else
        f"Hi, just checking you saw my note about {topic}. Happy to send the fix, no cost and no commitment. Ismail"))
    copies.append(('Last note (day 8)',
        "Last note from me. If product visuals or ad creatives become a priority, I'm here. Portfolio: [link]. Ismail" if product else
        f"Last message from me. If you ever want the fix for {topic}, or help with {('content and bookings' if egypt else 'ad creatives')}, I'm here. Ismail"))
    copies.append(('AI prompt: one-page audit (paste into Claude)',
        f"Load social-auditor and lead-finder. Using the Apify connector, audit {name} ({x['Niche']}, {x['Area']}, {x['Region']}). "
        f"Google Maps: {x['Google Maps']}\n"
        f"1) Pull the Google listing: rating, review count, the 20 newest reviews (note unanswered 1★), website button, hours.\n"
        f"2) Search their name on Instagram, TikTok and Facebook; scrape the last 30 posts of any account you find.\n"
        f"Known gaps from our list: {x['Gaps']}\n"
        f"Return a one-page audit in plain English: 3 strengths, the 3 gaps that cost them the most customers (with the number behind each), "
        f"one fix I can do for free this week, and a 3-line WhatsApp message offering that fix. Every number must come from the data; never invent. "
        f"Keep it under 250 words and run it through cringe-filter."))
    if product:
        copies.append(('AI prompt: product sample image (paste into Claude)',
            f"Load ai-video-prompt-engineering. I'm making a spec sample for {name} ({x['Niche']}, {x['Area']}, Dubai). "
            f"I'll attach their real product photo from Google Maps or Instagram as @product. Write one Mode B commercial-hero image prompt "
            f"(Nano Banana) with props from their brand story, product lock (exact shape, cap/label, colour), and run prompt_lint.py. "
            f"If I don't have a clear real product photo, tell me to skip this brand. Never invent a product."))
    return {
        'id': i, 'region': 'Egypt' if egypt else 'Dubai', 'tier': x['Tier'][0], 'tierLabel': x['Tier'],
        'name': name, 'niche': x['Niche'], 'area': x['Area'], 'phone': x['Phone'], 'wa': x['WhatsApp link'],
        'maps': x['Google Maps'], 'rating': x['Rating'], 'reviews': x['Reviews'], 'fact': g or x['Gaps'],
        'gaps': x['Gaps'], 'offer': x['Offer'], 'deal': x['Deal size'], 'why': x['Why you'],
        'how': x['How to contact'], 'copies': [{'label': a, 'text': b} for a, b in copies]}


def main():
    rows = list(csv.DictReader(open(LEADS, encoding='utf-8-sig')))
    leads = [lead(x, i + 1) for i, x in enumerate(rows)]
    clients = [
        {'name': 'Mr Mohamed Rakha', 'kind': 'Client (free)', 'niche': 'IGCSE Business & Economics teacher', 'area': 'Egypt: own center + online',
         'fact': "Sparq Study's first teacher. Full brand (Whisky Lounge palette, signet logo) and Shoot Day 1 pack ready; waiting on his approvals."},
        {'name': 'La Margrita', 'kind': 'Prospect (free month offered)', 'niche': 'Neapolitan pizza & pasta', 'area': 'Hadayek al Ahram, 3rd Gate (Fayoum Rd)',
         'fact': '175K TikTok followers but ~7K views per recent video; one clip hit 13.7M. 4.6★ on Google. Four different names and a broken phone number in one post.'},
    ]
    general = [
        ('New chat starter', "Load commando-profiles and commando-hq. Read commando/HANDOFF.md on branch claude/elegant-brown-yt0vko of I7Nosseir/chispa first. "
         "I'm the founder of The Commando (Sparq Study, Ignite Uni, Nova). I don't code. Apify is connected. Keep everything documented in HANDOFF.md and the client folders. "
         "Today I want to: [task]."),
        ('Log my calls (paste notes after a calling session)', "Load lead-finder. Here are today's call notes: [paste]. Update commando/leads/all-leads-2026-10-11.csv and the matching xlsx "
         "(Status, Notes, Follow-up date), draft the follow-up WhatsApp for each person who replied, and tell me which 5 businesses to warm up tomorrow (same niche)."),
        ('La Margrita meeting page', "Load commando-profiles (La Margrita). Call notes: [paste]. Build a one-page meeting page in English and Egyptian Arabic: "
         "their numbers (175K vs ~7K, 13.7M clip, 4.6★), the 3 quick fixes, the free-month scope and what they provide, and the retainer options. Keep it calm, no hype."),
        ('Who are you? (say it)', "I'm Ismail. I've run marketing for Grapes Holiday and Rihla Travel, and I build my own businesses: Ignite Uni and Sparq Study. "
         "I'm local, I do the work myself, and you deal with me directly, not an account manager."),
        ('"We already have a social media person"', "Great, that's half the work. Do they also handle the website, the Google Maps listing and the review replies? "
         "Most social media people don't. Let me send the free note anyway: if your person is doing great, it'll confirm it; if not, you'll know what to ask them for."),
        ('"How much?"', "It depends on what you need. Websites start around 12K EGP, social media from 6K a month. Let me send the free note first so you know if it's even worth it. "
         "(Proposed ranges: approve before quoting.)"),
        ('Gulf: job application cover', "I'm a performance marketer who also produces ad creative with AI. As Marketing Director at Grapes Holiday I cut ad spend by 62.5% while generating "
         "2.5× the leads (3,000+ qualified leads). At Rihla Travel's launch we made 350K+ EGP in the first two weeks. I build the landing pages and AI creatives myself, "
         "so tests ship fast. Portfolio: [link]. I'm in Cairo and available [full-time/part-time] remotely."),
        ('Meeting checklist (ask before any work)', "1) Your goal in one sentence and how you measure it today. 2) Orders/bookings per week now. 3) What you spend on marketing. "
         "4) Who approves content. 5) What you tried before. 6) Logo, colours, photos, menu/price list. Then: signed scope, deposit first, admin/partner access (no passwords), "
         "permission to use results as a case study."),
    ]
    def md(f):
        lines, out = open(os.path.join(HERE, f)).read().split('\n'), []
        for ln in lines:
            ln = re.sub(r'^   (- )', r'    \1', ln)  # nested bullets need 4 spaces
            is_list = re.match(r'\s*(- |\d+\. )', ln)
            if is_list and not ln.startswith(' ') and out and out[-1].strip() and not re.match(r'\s*(- |\d+\. )', out[-1]):
                out.append('')  # a list needs a blank line before it
            out.append(ln)
        return markdown.markdown('\n'.join(out), extensions=['tables'])
    data = {'leads': leads, 'clients': clients, 'general': [{'label': a, 'text': b} for a, b in general],
            'report': md('report.md'), 'approach': md('approach.md')}
    tpl = open(os.path.join(HERE, 'template.html')).read()
    payload = json.dumps(data, ensure_ascii=False).replace('</', '<\\/')
    open(os.path.join(HERE, 'index.html'), 'w').write(tpl.replace('/*@@DATA@@*/null', payload))

    # Business Directory (markdown → PDF elsewhere)
    out = ['# Business Directory (17 Oct 2026)', '',
           f'{len(leads)} leads ({sum(l["region"]=="Egypt" for l in leads)} Egypt, {sum(l["region"]=="Dubai" for l in leads)} Dubai) plus 2 clients. '
           'Key fact = the most specific verified gap on their Google listing (Apify, 11 Oct). Check it on your phone before contacting.', '',
           '## Clients and prospects']
    for c in clients:
        out.append(f"- **{c['name']}** ({c['kind']}) · {c['area']} · {c['niche']}. {c['fact']}")
    for reg in ('Egypt', 'Dubai'):
        for t, lab in (('A', 'Tier A: high-paying'), ('B', 'Tier B: mid'), ('C', 'Tier C: quick wins')):
            ls = [l for l in leads if l['region'] == reg and l['tier'] == t]
            if not ls: continue
            out += ['', f'## {reg}: {lab} ({len(ls)})']
            for l in ls:
                r = f"{l['rating']}★/{l['reviews']}" if l['rating'] else ''
                out.append(f"- **{l['name']}** · {l['area']} · {l['niche']} · {r} · {l['phone']}. {l['fact']}.")
    open(os.path.join(HERE, 'directory.md'), 'w').write('\n'.join(out) + '\n')
    print(f'built index.html ({len(leads)} leads) and directory.md')


if __name__ == '__main__':
    main()
