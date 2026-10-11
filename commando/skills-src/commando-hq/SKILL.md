---
name: "commando-hq"
description: "Coordinator and entry point for the founder's whole marketing ecosystem. Understands a request, picks which skills to run and in what order (all 29 marketing skills), passes handoff cards, and keeps the user approving at each gate. Use for broad marketing requests (\"plan next month\", \"launch this\", \"start the week\") or when it's unclear which marketing skill fits."
---

# Commando HQ

Routes work; doesn't duplicate what other skills do.

## Routing table
| Need | Skill |
|---|---|
| Facts about a brand, create/update profile | commando-profiles |
| Is there demand / pricing / trends in a market | market-research |
| Who competitors are and what they do | competitor-scanner |
| Who exactly we're talking to | avatar-creator |
| What to post, where, when, how often | strategy-partner |
| Turn an idea into something original | twist-lab |
| Upgrade an idea that feels cliché | idea-elevator |
| Voice, look, personality | brand-persona |
| Hooks, script, shots, editing | commando-content-studio |
| One piece → many formats/platforms | repurposing |
| Product drops, event promotions, offers | launch-planner |
| Comments, DMs, community | community-manager |
| Quality check before publishing | senior-reviewer |
| Remove cringe, AI-sounding or try-hard lines | cringe-filter |
| Approved English → natural Egyptian Arabic | egyptian-voice |
| Results, reports, improvements | performance-tracker |
| Paste-ready hooks, captions, ad copy, WhatsApp messages | copy-engine |
| What's trending now (global + Egypt), worth riding or not | trend-radar |
| Platform specs, sizes, safe zones, which format where | platform-playbook |
| Carousels, static posts, thumbnails, covers, ad images | commando-design-studio |
| Motion graphics, brand films, captions over footage | commando-motion-studio |
| Bios, handles, highlights, covers, WhatsApp Business | social-profile-optimizer |
| Briefs/production packs for Adam, Anas, editors, collaborators | production-docs |
| Real live numbers for any account (followers, views, outliers, rhythm) | social-auditor |
| Benchmark creators + competitors list, what works, mechanics → ideas with personality | reference-bank |
| Retention curves, drop-offs, rewatch spikes, traffic sources, algorithm state | retention-lab |
| Brand colours (theory, validation, picking a palette) | color-system |
| Logo design, testing and the logo suite | logo-system |
| One-page brand board / branding scheme (like the Nova PDF) | brand-board |
| Finding clients for freelance services | lead-finder (separate from marketing) |

## Standard pipelines
- **New brand / quarterly reset:** profiles → market-research → reference-bank (list) → social-auditor (live data) → competitor-scanner → avatar-creator → brand-persona (Mode A) → color-system → logo-system → brand-board → social-profile-optimizer → strategy-partner
- **Monthly plan:** social-auditor (refresh references + own accounts) → retention-lab (drop-off library review) → performance-tracker (monthly report) → reference-bank (new outliers → mechanics) → trend-radar (monthly scan) → strategy-partner (calendar)
- **After every published video (48–72 h):** retention-lab (curve + traffic sources) → performance-tracker log → rules back to commando-content-studio
- **Each piece:** idea-elevator (if the idea feels familiar) or twist-lab (if it needs a new concept) → brand-persona (Mode B) → commando-content-studio (video) / copy-engine + commando-design-studio (carousel, static) / commando-motion-studio (motion film) → cringe-filter → senior-reviewer → (approve English) → egyptian-voice → publish → repurposing
- **Fast lane (daily posts, stories, replies, small captions):** copy-engine → cringe-filter → founder approves → publish. Use the full "each piece" pipeline only for hero pieces, launches, series openers and ads.
- **Collaborator handover:** after approval → production-docs (Plan Overview / Production Pack)
- **Launch/event:** launch-planner → pieces through the "each piece" pipeline
- **Weekly rhythm:** Monday plan the week's pieces; batch-film day; Friday performance-tracker weekly report + community-manager digest

## How to run
1. Restate the request in one line and show the pipeline you'll follow (with steps that can be skipped because outputs already exist).
2. Run one skill at a time. At each gate, show the output compactly and ask the user to approve, edit, or skip. Never publish, send, or post anything without explicit approval.
3. Pass a handoff card between skills:
```
HANDOFF → [skill]
Brand | Goal | Platform | Avatar | Pillar/Format | Face/Faceless | Deadline
Inputs ready: [docs] | Decisions so far: … | Open questions: …
```

## Where outputs live
Before running a skill, look for its saved output by exact title in Claude Docs (`[Brand] — Avatar Pack`, `— Market Brief`, `— Competitor Scan`, `— Strategy Plan`, `— Performance Log`; rule in `commando-profiles`). Reuse it if it exists; update that same doc instead of making a new one. Brand facts live only in `commando-profiles`.

## Staying within context and cost
- Keep long outputs (avatar packs, plans, logs) in documents, not in the chat; reload only the section a task needs.
- For big jobs (a full month of scripts), work in batches of 3–5 pieces and suggest a fresh chat per batch, starting from the handoff card and the saved docs.
- At the end of a session, write a short "session summary" (decisions, finished pieces, next steps) the user can paste into the next chat or save to their Project.