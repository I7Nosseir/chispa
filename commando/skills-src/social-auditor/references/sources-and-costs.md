# Sources, workarounds and costs (Oct 2026)

## Open-source collectors (free; run on GitHub Actions)
| Platform | Tool | Status | Limits & workarounds |
|---|---|---|---|
| Instagram | instaloader ≥4.15 (~13K★) | works; frequent 401/429 | public profiles without login; 5–12 s random delays (built in); datacenter IPs (GitHub runners) get blocked more → fall back to Apify |
| Instagram (official) | Graph API Business Discovery | stable | needs your own IG professional account + Meta app; gives followers/bio/media count of other professional accounts |
| TikTok | yt-dlp profile URL; TikTokApi (davidteather, ~6.3K★, Playwright) | intermittent | TikTok often needs browser cookies for full profile listing; blocks datacenter IPs |
| YouTube | yt-dlp; YouTube Data API v3 (free quota 10K units/day) | stable | yt-dlp also returns the public **"most replayed" heatmap** (retention proxy) |
| Facebook | yt-dlp (page videos); facebook-scraper (kevinzg, stale since 2024) | weak | use Apify for posts |
| X | twscrape / Scweet | works with your own X sessions | burner accounts get banned; Nitter is dead |
| Any page | Crawl4AI (~66–71K★) | active | websites, reviews, press |

## Apify (managed, residential proxies included in per-result actors)
Plans (Jul 2026): Free $0 incl. $5 usage · Starter $29 (incl. $29 usage) · Scale $199 · Business $999. Credits expire monthly.

| Actor | Users / rating | Price per 1,000 results |
|---|---|---|
| apify/instagram-scraper | 388K / 4.70★ | $2.70 Free · $2.30 Bronze/Starter · $1.90 Silver · $1.50 Gold (verified 7 Oct 2026) |
| clockworks/tiktok-scraper | 275K / 4.76★ | $3.70 Free · $3.00 Bronze/Starter · $2.30 Silver · $1.70 Gold, + $0.001 per run; comments +$1.25/1K, transcripts $0.048/min (verified 7 Oct 2026) |
| apify/facebook-posts-scraper | 107K / 4.64★ | ≈ $2.00 |
| streamers/youtube-scraper | — | ≈ $2–5 (check before large runs) |
| YouTube most-replayed (heatmap) actors | — | small, per video |
| Comments scrapers (IG/TikTok) | — | ≈ $1–2.50 per 1,000 comments |

## Cost at scale (results = posts + profile records + comments)
| Scenario | Monthly volume | Est. cost | Plan |
|---|---|---|---|
| **Rakha only**: 5 accounts × 30 posts, weekly | ≈ 600–800 | ≈ $2–3 | Free ($5) — real test: 91 results = $0.28 |
| **Rakha deep**: + 10 more benchmarks, + 50 comments on top 10 posts each, weekly | ≈ 4,000–5,000 | ≈ $9–12 | Starter $29 (covers it) |
| **All Commando brands** (Sparq, Ignite, Nova, founder, Adam & Anas, Rakha): 8 references × 2 platforms × 30 posts, weekly | ≈ 13,000–14,000 | ≈ $35–40 at Starter prices | Starter $29 + ~$10 overage |
| **War-room**: all brands, daily tracking + comments + heatmaps | ≈ 50,000–70,000 | ≈ $100–150 | Starter + pay-as-you-go, or Scale $199 at higher volumes |
Rule: weekly beats daily for strategy; go daily only during launches.

## Jev (TypeSafe AI) — post labelling at scale
- Decision model (no text): returns a **choice**, a **score**, or a **yes/no probability**.
- $0.042 per million input tokens, output free; 64K context (state ≤32K); 70–500 ms. Early-access waitlist (typesafe.ai), keys at console.typesafe.ai.
- One endpoint: `POST https://api.typesafe.ai/v1/systemone`, Bearer key, body `{model: "jev-latest", state: <post text/metadata>, questions: {hook_type: {...choices...}, virality: {...score...}, is_sales_post: {...yes/no...}}}`. Confirm the exact question schema in the docs when the key arrives.
- Cost example: 10,000 posts × ~400 tokens = 4M tokens ≈ $0.17.

## Legal posture (founder's own use)
Public data, logged-out collection, no private individuals, no resale. US case law (Meta v. Bright Data 2024; hiQ v. LinkedIn) supports logged-out scraping of public data; Egypt has no equivalent ruling — keep it internal.

## Sources
scrapfly.io/blog/posts/best-open-source-instagram-scrapers · github.com/davidteather/TikTok-Api · instaloader.github.io/troubleshooting.html · use-apify.com/docs/best-apify-actors/best-social-media-scrapers · scrapegraphai.com/blog/apify-pricing · eesel.ai/blog/typesafe-jev-pricing · marktechpost.com/2026/09/19/typesafe-ai-releases-jev/ · fbm.com (Meta v. Bright Data)
