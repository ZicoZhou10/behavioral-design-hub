#!/usr/bin/env python3
"""Generate 5 Category Benchmark Pages for Behavioral Design Hub.

Each page targets high-intent category-level queries like:
  "behavioral design in social media"
  "best UX in e-commerce"

These have higher CPC ($5-15) and lower competition than product-name queries.
"""

import os
import json
from pathlib import Path

BASE_URL = "https://behavioral-design-hub.github.io"
HUB_DIR = Path(__file__).parent

# ── Product Database ──
PRODUCTS = {
    "tiktok":    {"name": "TikTok",    "ca": 10, "cl": 9, "md": 8, "tt": 3, "ea": 2, "total": 32, "pct": 64, "emoji": "🎵"},
    "instagram": {"name": "Instagram", "ca": 8,  "cl": 5, "md": 8, "tt": 3, "ea": 3, "total": 27, "pct": 54, "emoji": "📸"},
    "linkedin":  {"name": "LinkedIn",  "ca": 7,  "cl": 5, "md": 7, "tt": 6, "ea": 5, "total": 30, "pct": 60, "emoji": "💼"},
    "amazon":    {"name": "Amazon",    "ca": 8,  "cl": 6, "md": 9, "tt": 5, "ea": 4, "total": 32, "pct": 64, "emoji": "📦"},
    "shopify":   {"name": "Shopify",   "ca": 9,  "cl": 7, "md": 8, "tt": 7, "ea": 7, "total": 38, "pct": 76, "emoji": "🛒"},
    "airbnb":    {"name": "Airbnb",    "ca": 9,  "cl": 7, "md": 8, "tt": 7, "ea": 6, "total": 37, "pct": 74, "emoji": "🏠"},
    "notion":    {"name": "Notion",    "ca": 7,  "cl": 6, "md": 6, "tt": 8, "ea": 9, "total": 36, "pct": 72, "emoji": "📝"},
    "slack":     {"name": "Slack",     "ca": 7,  "cl": 5, "md": 7, "tt": 7, "ea": 5, "total": 31, "pct": 62, "emoji": "💬"},
    "whatsapp":  {"name": "WhatsApp",  "ca": 7,  "cl": 9, "md": 6, "tt": 7, "ea": 7, "total": 36, "pct": 72, "emoji": "📱"},
    "calm":      {"name": "Calm",      "ca": 7,  "cl": 8, "md": 6, "tt": 8, "ea": 8, "total": 37, "pct": 74, "emoji": "🧘"},
    "chatgpt":   {"name": "ChatGPT",   "ca": 6,  "cl": 7, "md": 8, "tt": 5, "ea": 6, "total": 32, "pct": 64, "emoji": "🤖"},
    "netflix":   {"name": "Netflix",   "ca": 8,  "cl": 6, "md": 7, "tt": 5, "ea": 4, "total": 30, "pct": 60, "emoji": "🎬"},
    "spotify":   {"name": "Spotify",   "ca": 8,  "cl": 7, "md": 7, "tt": 7, "ea": 7, "total": 36, "pct": 72, "emoji": "🎧"},
    "uber":      {"name": "Uber",      "ca": 8,  "cl": 9, "md": 7, "tt": 4, "ea": 5, "total": 33, "pct": 66, "emoji": "🚗"},
    "duolingo":  {"name": "Duolingo",  "ca": 9,  "cl": 8, "md": 9, "tt": 6, "ea": 5, "total": 37, "pct": 74, "emoji": "🦉"},
}

DIMS = [
    ("ca", "Choice Architecture"),
    ("cl", "Cognitive Load Mgmt"),
    ("md", "Motivation Design"),
    ("tt", "Trust & Transparency"),
    ("ea", "Ethical Alignment"),
]

# ── Category Definitions ──
CATEGORIES = [
    {
        "slug": "social-media",
        "title": "Social Media",
        "emoji": "📱",
        "products": ["tiktok", "instagram", "linkedin"],
        "meta_desc": "How do social media platforms score on behavioral design? TikTok, Instagram, and LinkedIn ranked across 5 research-backed dimensions. Data-driven analysis of engagement patterns, dark patterns, and ethical design in social media.",
        "hero_tagline": "Social media platforms master engagement — but at what ethical cost? We scored TikTok, Instagram, and LinkedIn across 5 behavioral science dimensions to find out.",
        "overview": """<p>Social media is where behavioral design has its most visible — and most controversial — impact. These platforms serve billions of daily active users, making every design choice a behavioral experiment at unprecedented scale.</p>
<p>Our analysis reveals a stark pattern: <strong>social media platforms excel at Choice Architecture and Motivation Design but consistently score lowest on Trust &amp; Ethical Alignment.</strong> The category average for ethics (3.3/10) is the lowest of any industry we've analyzed — nearly half the all-product average of 5.5/10.</p>
<p>This isn't accidental. Social media's advertising business model creates structural incentives to maximize engagement time, which frequently conflicts with user wellbeing. The question isn't whether these products use behavioral science — it's whether they use it <em>for</em> or <em>against</em> the user.</p>""",
        "pattern_title": "The Engagement-Ethics Inversion",
        "pattern_text": """<p>Across all three social platforms, we observe what we call the <strong>"Engagement-Ethics Inversion"</strong>: the more sophisticated the engagement mechanics, the lower the ethical alignment score. TikTok has the highest Choice Architecture score of any product we've analyzed (10/10) — and the lowest Ethics score (2/10).</p>
<p>This pattern suggests that current social media behavioral design optimizes a single variable (time-on-platform) at the expense of user-aligned outcomes. LinkedIn partially escapes this trap because its professional context creates natural boundaries on engagement optimization — users have a clear "job to be done" that limits infinite-scroll dynamics.</p>
<p><strong>The opportunity for social platforms:</strong> Calm (74%) proves that engagement and ethics aren't inherently opposed. A social platform that applied Calm's trust-first approach could differentiate dramatically in a market where users increasingly distrust engagement-maximizing design.</p>""",
        "faqs": [
            {
                "q": "Which social media platform has the best behavioral design?",
                "a": "TikTok leads with 32/50 (64%), followed by LinkedIn at 30/50 (60%) and Instagram at 27/50 (54%). However, TikTok's lead comes primarily from perfect Choice Architecture (10/10) — its Ethics score (2/10) is the lowest of any product analyzed. LinkedIn has the most balanced social media scores across all 5 dimensions."
            },
            {
                "q": "Do social media apps use dark patterns?",
                "a": "Our analysis finds that social media platforms score an average of 3.3/10 on Ethical Alignment — the lowest of any industry category. Specific dark patterns identified include: infinite scroll with no stopping cues (TikTok, Instagram), misleading notification badges that conflate social and promotional content (LinkedIn, Instagram), and variable-ratio reinforcement schedules designed to create compulsive checking behavior (all three platforms)."
            },
            {
                "q": "How does TikTok's behavioral design compare to Instagram?",
                "a": "TikTok scores 32/50 vs Instagram's 27/50. TikTok's advantage comes from superior Choice Architecture (10 vs 8) and Cognitive Load Management (9 vs 5). TikTok's single-video-at-a-time interface eliminates decision paralysis, while Instagram's multi-format feed (posts, stories, reels, shop) fragments attention. Both score poorly on Trust (3/10) and Ethics (TikTok 2/10, Instagram 3/10)."
            }
        ]
    },
    {
        "slug": "e-commerce",
        "title": "E-Commerce & Marketplace",
        "emoji": "🛍️",
        "products": ["shopify", "airbnb", "amazon"],
        "meta_desc": "Behavioral design rankings for e-commerce: Shopify, Airbnb, and Amazon scored across 5 research-backed dimensions. Which marketplace has the best UX? Data-driven analysis of choice architecture, trust signals, and conversion patterns.",
        "hero_tagline": "E-commerce platforms live or die by conversion — making behavioral design a core business function, not a UX nice-to-have. We scored Shopify, Airbnb, and Amazon to see who does it best.",
        "overview": """<p>E-commerce is the industry where behavioral design has the most direct, measurable revenue impact. Every friction point costs money. Every trust signal converts. This makes e-commerce platforms the most commercially motivated behavioral designers in tech.</p>
<p>Our analysis shows that <strong>e-commerce leads all categories in overall behavioral design quality</strong>, with a category average of 35.7/50 (71.3%) — significantly above the all-product average of 33.1/50. The key driver: commercial alignment. When the platform's revenue depends on the user successfully completing a transaction, the incentives naturally align toward reducing friction and building trust.</p>
<p>Shopify leads at 76% — the highest score of any product in our entire database — because it's a platform that helps <em>merchants</em> convert <em>their</em> customers. This double-alignment (Shopify succeeds when merchants succeed when buyers succeed) creates uniquely strong behavioral design incentives.</p>""",
        "pattern_title": "Commercial Alignment as Behavioral Design Advantage",
        "pattern_text": """<p>The standout pattern in e-commerce: <strong>transaction-based business models produce better behavioral design than advertising-based models.</strong> When revenue comes from completed purchases (not time-on-platform), the platform is incentivized to help users make good decisions quickly — the opposite of engagement-maximizing social media.</p>
<p>Shopify (76%) and Airbnb (74%) both score 7/10 on Trust — dramatically higher than social media's average of 4/10. This isn't altruism; it's economics. A user who trusts the platform buys more. Amazon (64%) scores lower partly because its marketplace model creates trust ambiguity — is this sold by Amazon or a third party? — that Shopify avoids by design.</p>
<p><strong>The Motivation Design divergence is revealing:</strong> Amazon scores 9/10 on Motivation (urgency timers, "only 3 left", social proof badges) while Shopify scores 8/10 — but Amazon's aggressive tactics cost it on Ethics (4/10 vs Shopify's 7/10). The lesson: you can drive motivation without manipulating.</p>""",
        "faqs": [
            {
                "q": "Which e-commerce platform has the best behavioral design?",
                "a": "Shopify leads with 38/50 (76%) — the highest score of any product in our database. Airbnb follows at 37/50 (74%) and Amazon at 32/50 (64%). Shopify's advantage comes from its double-aligned business model: it succeeds when merchants succeed when buyers succeed, creating natural incentives for user-centered behavioral design."
            },
            {
                "q": "How does Amazon's UX compare to Shopify?",
                "a": "Amazon scores 32/50 vs Shopify's 38/50. Amazon leads on Motivation Design (9 vs 8) through urgency tactics and social proof, but Shopify wins on Choice Architecture (9 vs 8), Trust (7 vs 5), and Ethics (7 vs 4). Amazon's marketplace complexity creates cognitive load (6/10) that Shopify's cleaner merchant-focused interface avoids (7/10). The key difference: Shopify optimizes for merchant success; Amazon optimizes for purchase completion."
            },
            {
                "q": "Does Airbnb use behavioral science in its design?",
                "a": "Airbnb scores 37/50 (74%), ranking 2nd in e-commerce. Its strongest behavioral design elements include: urgency signals based on real booking data (not manufactured scarcity), trust-building through host verification and review transparency (Trust: 7/10), and progressive disclosure in its booking flow that reduces cognitive load (7/10). Airbnb's photo-first search results are a masterclass in Choice Architecture (9/10)."
            }
        ]
    },
    {
        "slug": "productivity",
        "title": "Productivity & Collaboration",
        "emoji": "⚡",
        "products": ["notion", "slack"],
        "meta_desc": "Behavioral design in productivity tools: Notion vs Slack scored across 5 research-backed dimensions. Which collaboration tool has better UX? Analysis of cognitive load, ethical design, and motivation patterns in workplace software.",
        "hero_tagline": "Productivity tools face a unique behavioral design challenge: they must drive engagement without creating distraction. We scored Notion and Slack to see who navigates this paradox best.",
        "overview": """<p>Productivity software occupies a unique position in the behavioral design landscape. Unlike social media or entertainment, these tools must <em>reduce</em> time-on-platform while <em>increasing</em> output. The behavioral design challenge isn't "how do we keep users engaged?" — it's "how do we help users accomplish their goal and leave?"</p>
<p>This fundamental difference produces a distinctive scoring pattern. <strong>Productivity tools score highest on Ethical Alignment</strong> (category average 7.0/10 vs all-product average 5.5/10) but lowest on Motivation Design (category average 6.5/10). This is the right trade-off: a productivity tool that maximizes engagement is, by definition, failing at its job.</p>
<p>Notion leads at 72% with the highest single-dimension Ethics score of any product (9/10), suggesting that ethical design and business success are complementary in the productivity category — users choose tools they trust with their most valuable asset: attention.</p>""",
        "pattern_title": "The Utility-First Behavioral Design Model",
        "pattern_text": """<p>Both Notion and Slack embody what we call <strong>"Utility-First" behavioral design</strong>: design decisions prioritize task completion over engagement metrics. This manifests differently in each product:</p>
<p><strong>Notion</strong> maximizes user agency. Its block-based architecture gives users architectural control over their workspace — the opposite of algorithmic content feeds. This "blank canvas" approach scores lower on Choice Architecture (7/10) because it requires more upfront decisions, but it produces the highest Trust (8/10) and Ethics (9/10) scores of any product. Users feel like collaborators, not targets.</p>
<p><strong>Slack</strong> faces a harder behavioral design challenge: it must facilitate communication without enabling notification overload. Its Cognitive Load score (5/10) reflects this tension — the same feature that ensures you don't miss important messages (persistent notifications) is the feature that fragments deep work. Slack's Do Not Disturb and scheduled messages are behavioral design countermeasures against its own engagement mechanics.</p>
<p><strong>The lesson:</strong> Productivity tools prove that behavioral design quality correlates with ethical alignment when the business model rewards user outcomes, not user attention.</p>""",
        "faqs": [
            {
                "q": "Which productivity tool has better behavioral design — Notion or Slack?",
                "a": "Notion leads with 36/50 (72%) vs Slack's 31/50 (62%). Notion's advantage comes from superior Ethical Alignment (9 vs 5) and Trust (8 vs 7). Notion's block-based design gives users control over their workspace — its behavioral design serves user goals. Slack scores higher on equal terms for Choice Architecture (both 7/10) but struggles with Cognitive Load (5/10) due to notification overload patterns."
            },
            {
                "q": "Does Slack use dark patterns?",
                "a": "Slack scores 5/10 on Ethical Alignment. While it avoids overt dark patterns, several design choices prioritize engagement over user wellbeing: notification defaults that interrupt deep work, the unread badge that creates anxiety about missing messages, and channel proliferation that fragments attention. Slack's behavioral design challenge is structural — the same features that make it useful for communication make it harmful for focus."
            },
            {
                "q": "What makes Notion's UX design ethical?",
                "a": "Notion scores 9/10 on Ethical Alignment — the highest of any product analyzed. Key factors: no algorithmic feed (users choose what to see), no engagement-maximizing notifications (minimal by default), transparent data handling, and a business model (subscription) that aligns with user success rather than attention extraction. Notion proves that tool utility and ethical design are complementary, not competing."
            }
        ]
    },
    {
        "slug": "communication-utility",
        "title": "Communication & Utility",
        "emoji": "🔧",
        "products": ["whatsapp", "calm", "chatgpt"],
        "meta_desc": "Behavioral design in communication and utility apps: WhatsApp, Calm, and ChatGPT scored across 5 research-backed dimensions. Analysis of cognitive load management, trust signals, and ethical design in everyday-use applications.",
        "hero_tagline": "Communication and utility apps are the invisible infrastructure of daily life. We scored WhatsApp, Calm, and ChatGPT to see how behavioral science shapes the tools you use every day.",
        "overview": """<p>This category spans apps that serve fundamentally different purposes — messaging, wellness, and AI assistance — but share a common trait: they're used daily by hundreds of millions of people as part of core routines, not for entertainment or productivity. Their behavioral design has outsized impact because users rarely evaluate alternatives.</p>
<p><strong>Communication &amp; Utility apps score highest on Cognitive Load Management</strong> (category average 8.0/10) — significantly above the all-product average of 6.9/10. This makes intuitive sense: these tools succeed when they're invisible. WhatsApp's interface hasn't meaningfully changed in a decade because its behavioral design was right from the start: zero learning curve, zero cognitive overhead.</p>
<p>Calm leads at 74% and demonstrates that <strong>a wellness app can achieve both high engagement and high ethics</strong> — a combination that social media platforms have failed to achieve. The key: Calm's business model (subscription) aligns its incentives with user outcomes (feeling calmer), not user attention.</p>""",
        "pattern_title": "Invisible Design as Behavioral Excellence",
        "pattern_text": """<p>The strongest pattern across Communication &amp; Utility apps is what we call <strong>"Invisible Design"</strong>: the best behavioral design in this category is the design you don't notice. WhatsApp scores 9/10 on Cognitive Load Management because its interface requires near-zero mental effort — there's nothing to learn, nothing to configure, nothing to optimize.</p>
<p>This contrasts sharply with ChatGPT (7/10 on Cognitive Load), which faces the opposite challenge: its blank-prompt interface is cognitively demanding because users must generate the input, not just respond to it. ChatGPT's strongest dimension is Motivation Design (8/10) — the dopamine hit of getting a useful AI response creates a powerful variable-reward loop.</p>
<p><strong>Calm's position is strategically instructive:</strong> it proves that subscription-based apps can achieve 74% behavioral design scores with 8/10 Trust and 8/10 Ethics. In a market where "freemium engagement trap" is the default model, Calm's success shows that users will pay for behavioral design that serves their interests. This is the model other categories should study.</p>""",
        "faqs": [
            {
                "q": "Which communication app has the best behavioral design?",
                "a": "Calm leads with 37/50 (74%), followed by WhatsApp at 36/50 (72%) and ChatGPT at 32/50 (64%). Calm's advantage comes from industry-leading Trust (8/10) and Ethics (8/10) scores. WhatsApp excels at Cognitive Load Management (9/10) — its decade-stable interface is a masterclass in invisible design. ChatGPT scores highest on Motivation Design (8/10) due to its variable-reward response loop."
            },
            {
                "q": "How does ChatGPT's UX compare to traditional apps?",
                "a": "ChatGPT scores 32/50 (64%) — below category average. Its unique challenge: a blank-prompt interface is high cognitive load (users generate input instead of selecting from options). ChatGPT compensates with strong Motivation Design (8/10) — the dopamine response from useful AI outputs. Its weakest area is Trust (5/10), reflecting user uncertainty about data usage and response accuracy. As AI interfaces mature, expect ChatGPT's Choice Architecture (currently 6/10) to improve significantly."
            },
            {
                "q": "Is WhatsApp well-designed from a behavioral science perspective?",
                "a": "WhatsApp scores 36/50 (72%), with its standout being Cognitive Load Management at 9/10 — the second-highest of any product analyzed. WhatsApp's behavioral design philosophy is 'invisible design': zero learning curve, minimal settings, decade-stable interface. Its Trust score (7/10) benefits from end-to-end encryption messaging. The weakest areas are Choice Architecture (7/10) and Motivation Design (6/10) — WhatsApp deliberately avoids engagement-maximizing features like stories algorithms."
            }
        ]
    },
    {
        "slug": "entertainment-learning",
        "title": "Entertainment & Learning",
        "emoji": "🎯",
        "products": ["duolingo", "spotify", "netflix", "uber"],
        "meta_desc": "Behavioral design in entertainment and learning: Duolingo, Spotify, Netflix, and Uber scored across 5 dimensions. Which entertainment app has the best UX? Data-driven analysis of habit formation, motivation design, and ethical engagement.",
        "hero_tagline": "Entertainment and learning apps compete for discretionary time — making behavioral design their primary competitive weapon. We scored Duolingo, Spotify, Netflix, and Uber to see who wields it best.",
        "overview": """<p>Entertainment &amp; Learning apps compete in the most crowded market in tech: human leisure time. Every minute on Spotify is a minute not on Netflix. Every Duolingo session competes with every Uber ride's in-app time. This zero-sum competition for attention makes behavioral design the decisive differentiator.</p>
<p>The category average is 34.0/50 (68%), close to the all-product mean, but the <strong>variance within the category is high</strong> — from Duolingo's 74% to Netflix's 60%. This spread reflects fundamentally different behavioral design philosophies: Duolingo builds habits through active participation, while Netflix optimizes for passive consumption.</p>
<p>The most striking finding: <strong>Duolingo, the only education product in this category, has the highest overall score (74%)</strong>. Its gamification mechanics (streaks, XP, leagues) are the most sophisticated motivation system we've analyzed — scoring 9/10 on both Choice Architecture and Motivation Design. But its Ethics score (5/10) reveals the cost: the same mechanics that make learning addictive can also prioritize app engagement over actual language acquisition.</p>""",
        "pattern_title": "Active vs. Passive Engagement Models",
        "pattern_text": """<p>This category reveals two fundamentally different behavioral design models:</p>
<p><strong>Active Engagement (Duolingo, Uber):</strong> Users make continuous decisions. Duolingo's lesson selection, streak tracking, and league competition require active participation. Uber's ride-hailing flow demands real-time decision-making. Both score high on Choice Architecture (9/10, 8/10) because they structure decisions well.</p>
<p><strong>Passive Engagement (Netflix, Spotify):</strong> The algorithm decides; the user consumes. Netflix's autoplay and Spotify's algorithmic playlists minimize decision effort. Both have lower Choice Architecture scores (8/10, 8/10) but Netflix's passive model produces lower overall scores (60%) because passive consumption has fewer opportunities to build trust or demonstrate ethical intent.</p>
<p><strong>Spotify occupies the ideal middle ground</strong> at 72% — it offers both algorithmic curation (Discover Weekly) and user-directed browsing, letting users choose their engagement mode. Its balanced scores across all 5 dimensions (no score below 7/10) make it the most consistently well-designed product in this category. The lesson: give users agency over <em>how</em> they engage, not just <em>what</em> they engage with.</p>""",
        "faqs": [
            {
                "q": "Which entertainment app has the best behavioral design?",
                "a": "Duolingo leads with 37/50 (74%), followed by Spotify at 36/50 (72%), Uber at 33/50 (66%), and Netflix at 30/50 (60%). Duolingo's gamification mechanics (streaks, XP, leagues) produce the highest Motivation Design score in the category (9/10). Spotify has the most balanced scores — no dimension below 7/10. Netflix's passive consumption model limits its behavioral design ceiling."
            },
            {
                "q": "How does Netflix use behavioral design?",
                "a": "Netflix scores 30/50 (60%), ranking last in Entertainment & Learning. Its behavioral design centers on choice reduction: algorithmic recommendations reduce browsing time, autoplay removes the 'should I watch another episode?' decision, and personalized thumbnails optimize click-through rates. Netflix excels at Choice Architecture (8/10) but scores low on Trust (5/10) and Ethics (4/10) — its 'skip intro' and autoplay features prioritize binge-watching over user-controlled consumption."
            },
            {
                "q": "Is Duolingo's gamification effective behavioral design?",
                "a": "Duolingo scores 37/50 (74%) with perfect-near scores on Choice Architecture (9/10) and Motivation Design (9/10). Its gamification is extremely effective at driving daily engagement — streaks leverage loss aversion, XP provides variable-ratio reinforcement, and leagues add social competition. However, its Ethics score (5/10) reflects a known concern: the streak mechanic can prioritize 'opening the app' over 'learning the language.' Effective behavioral design? Yes. Perfectly aligned with user goals? Not always."
            }
        ]
    }
]


def score_color(score):
    """Return CSS color based on score."""
    if score >= 8: return "var(--green)"
    if score >= 6: return "var(--yellow)"
    return "var(--red)"

def pct_color(pct):
    if pct >= 70: return "var(--green)"
    if pct >= 60: return "var(--yellow)"
    return "var(--red)"


def generate_category_page(cat):
    """Generate a complete HTML page for a category."""
    slug = cat["slug"]
    title = cat["title"]
    products = [PRODUCTS[p] for p in cat["products"]]
    products_sorted = sorted(products, key=lambda p: p["total"], reverse=True)

    # Category averages
    n = len(products)
    avg_total = sum(p["total"] for p in products) / n
    avg_pct = avg_total / 50 * 100
    dim_avgs = {}
    for key, label in DIMS:
        dim_avgs[key] = sum(p[key] for p in products) / n

    winner = products_sorted[0]

    # Product slugs for links
    product_slugs = {p["name"]: s for s, p in PRODUCTS.items()}

    # Build rankings rows
    ranking_rows = ""
    for i, p in enumerate(products_sorted, 1):
        medal = ["🥇","🥈","🥉","4️⃣","5️⃣"][i-1] if i <= 5 else f"{i}."
        p_slug = product_slugs[p["name"]]
        dim_cells = ""
        for key, label in DIMS:
            sc = p[key]
            dim_cells += f'<td style="color:{score_color(sc)};font-weight:600">{sc}/10</td>\n'
        ranking_rows += f"""<tr>
<td style="font-size:1.2rem">{medal}</td>
<td><a href="{BASE_URL}/teardowns/{p_slug}/" style="color:var(--accent-light);text-decoration:none;font-weight:600">{p["emoji"]} {p["name"]}</a></td>
<td style="color:{pct_color(p['pct'])};font-weight:700">{p["total"]}/50 ({p["pct"]}%)</td>
{dim_cells}
</tr>
"""

    # Dimension average rows
    dim_avg_rows = ""
    for key, label in DIMS:
        avg = dim_avgs[key]
        dim_avg_rows += f"""<div class="dim-bar">
<span class="dim-name">{label}</span>
<span class="dim-track"><span class="dim-fill" style="width:{avg*10}%;background:{score_color(int(round(avg)))}"></span></span>
<span class="dim-score">{avg:.1f}/10</span>
</div>
"""

    # Comparison links
    comp_links = ""
    slugs = cat["products"]
    for i in range(len(slugs)):
        for j in range(i+1, len(slugs)):
            a, b = sorted([slugs[i], slugs[j]])
            na = PRODUCTS[a]["name"]
            nb = PRODUCTS[b]["name"]
            comp_links += f'<a href="{BASE_URL}/compare/{a}-vs-{b}/" class="cmp-link">{na} vs {nb} →</a>\n'

    # FAQ HTML + JSON-LD
    faq_html = ""
    faq_jsonld_items = []
    for faq in cat["faqs"]:
        faq_html += f"""<div class="faq-item">
<h3 class="faq-q">{faq["q"]}</h3>
<p class="faq-a">{faq["a"]}</p>
</div>
"""
        faq_jsonld_items.append({
            "@type": "Question",
            "name": faq["q"],
            "acceptedAnswer": {
                "@type": "Answer",
                "text": faq["a"]
            }
        })

    faq_jsonld = json.dumps({
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": faq_jsonld_items
    }, indent=2, ensure_ascii=False)

    # ItemList JSON-LD
    itemlist_items = []
    for i, p in enumerate(products_sorted, 1):
        p_slug = product_slugs[p["name"]]
        itemlist_items.append({
            "@type": "ListItem",
            "position": i,
            "name": p["name"],
            "url": f"{BASE_URL}/teardowns/{p_slug}/",
            "description": f"{p['pct']}% ({p['total']}/50) — Behavioral Design Score"
        })

    itemlist_jsonld = json.dumps({
        "@context": "https://schema.org",
        "@type": "ItemList",
        "name": f"Behavioral Design Rankings: {title}",
        "description": cat["meta_desc"],
        "url": f"{BASE_URL}/categories/{slug}/",
        "numberOfItems": len(products),
        "itemListOrder": "https://schema.org/ItemListOrderDescending",
        "itemListElement": itemlist_items
    }, indent=2, ensure_ascii=False)

    # Article JSON-LD
    article_jsonld = json.dumps({
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": f"Behavioral Design in {title} — Rankings & Analysis",
        "description": cat["meta_desc"],
        "url": f"{BASE_URL}/categories/{slug}/",
        "datePublished": "2026-04-11",
        "dateModified": "2026-04-11",
        "author": {
            "@type": "Organization",
            "name": "Behavioral Design Hub",
            "url": BASE_URL
        },
        "publisher": {
            "@type": "Organization",
            "name": "Behavioral Design Hub",
            "url": BASE_URL
        },
        "mainEntityOfPage": f"{BASE_URL}/categories/{slug}/",
        "keywords": f"behavioral design {slug.replace('-', ' ')}, UX {slug.replace('-', ' ')}, behavioral science {slug.replace('-', ' ')}, product design analysis"
    }, indent=2, ensure_ascii=False)

    product_names = ", ".join(p["name"] for p in products_sorted)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Behavioral Design in {title} — {product_names} Ranked</title>
<meta name="description" content="{cat['meta_desc']}">
<meta property="og:title" content="Behavioral Design in {title} — Industry Rankings">
<meta property="og:description" content="{cat['meta_desc'][:200]}">
<meta property="og:type" content="article">
<meta property="og:url" content="{BASE_URL}/categories/{slug}/">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Behavioral Design in {title} — Rankings">
<meta name="twitter:description" content="{cat['meta_desc'][:200]}">
<link rel="canonical" href="{BASE_URL}/categories/{slug}/">

<script type="application/ld+json">
{article_jsonld}
</script>
<script type="application/ld+json">
{itemlist_jsonld}
</script>
<script type="application/ld+json">
{faq_jsonld}
</script>

<style>
*{{margin:0;padding:0;box-sizing:border-box}}
:root{{
  --bg:#0a0a0f;--surface:#12121a;--card:#1a1a28;--border:#2a2a3a;
  --text:#e8e8f0;--text-muted:#8888a0;--accent:#6c5ce7;--accent-light:#a29bfe;
  --green:#00b894;--yellow:#fdcb6e;--red:#e17055;--blue:#74b9ff;
  --gradient:linear-gradient(135deg,#6c5ce7,#a29bfe,#74b9ff);
}}
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;background:var(--bg);color:var(--text);line-height:1.6;min-height:100vh}}
.ct{{max-width:900px;margin:0 auto;padding:32px 20px}}

/* Nav */
.nv{{display:flex;justify-content:space-between;align-items:center;margin-bottom:40px;padding-bottom:16px;border-bottom:1px solid var(--border);flex-wrap:wrap;gap:8px}}
.nv a{{color:var(--accent-light);text-decoration:none;font-size:.88rem;font-weight:500}}
.nb{{font-weight:700;font-size:.95rem}}
.nav-links{{display:flex;gap:16px;flex-wrap:wrap}}
.nav-links a{{font-size:.82rem}}

/* Hero */
.hero{{text-align:center;padding:20px 0 40px}}
.hero-emoji{{font-size:3.5rem;margin-bottom:16px}}
.cat-badge{{display:inline-block;background:rgba(108,92,231,0.15);color:var(--accent-light);padding:6px 16px;border-radius:20px;font-size:0.82rem;font-weight:600;margin-bottom:16px;border:1px solid rgba(108,92,231,0.3)}}
.hero h1{{font-size:clamp(1.6rem,4vw,2.4rem);font-weight:800;margin-bottom:12px;line-height:1.2}}
.hero .tagline{{color:var(--text-muted);font-size:1rem;max-width:650px;margin:0 auto;line-height:1.7}}

/* Stats bar */
.stats-bar{{display:flex;justify-content:center;gap:32px;margin:24px 0;flex-wrap:wrap}}
.stat{{text-align:center}}
.stat-num{{font-size:1.6rem;font-weight:800;display:block}}
.stat-label{{font-size:0.72rem;color:var(--text-muted);text-transform:uppercase;letter-spacing:1px}}

/* Sections */
.section{{margin-bottom:40px}}
.section-title{{font-size:1.2rem;font-weight:700;margin-bottom:20px;padding-bottom:10px;border-bottom:1px solid var(--border)}}

/* Overview */
.overview{{background:var(--card);border:1px solid var(--border);border-radius:16px;padding:28px 24px;margin-bottom:32px}}
.overview p{{color:var(--text-muted);font-size:0.92rem;line-height:1.7;margin-bottom:14px}}
.overview p:last-child{{margin-bottom:0}}
.overview strong{{color:var(--text)}}

/* Ranking Table */
.tbl-wrap{{overflow-x:auto;margin-bottom:24px}}
table{{width:100%;border-collapse:collapse;font-size:.88rem}}
th{{text-align:left;padding:10px 8px;border-bottom:2px solid var(--border);color:var(--text-muted);font-size:.75rem;text-transform:uppercase;letter-spacing:1px;white-space:nowrap}}
td{{padding:12px 8px;border-bottom:1px solid var(--border)}}
tr:hover{{background:rgba(108,92,231,0.05)}}

/* Dim averages */
.dim-bar{{display:flex;align-items:center;gap:12px;margin-bottom:10px}}
.dim-name{{width:150px;font-size:.82rem;color:var(--text-muted);text-align:right;flex-shrink:0}}
.dim-track{{flex:1;height:7px;background:var(--surface);border-radius:7px;overflow:hidden}}
.dim-fill{{height:100%;border-radius:7px}}
.dim-score{{width:50px;font-size:.82rem;font-weight:600;text-align:right}}

/* Pattern */
.pattern{{background:var(--card);border:1px solid var(--border);border-radius:16px;padding:28px 24px;margin-bottom:32px;border-left:4px solid var(--accent)}}
.pattern h3{{font-size:1.1rem;font-weight:700;margin-bottom:16px;color:var(--accent-light)}}
.pattern p{{color:var(--text-muted);font-size:0.9rem;line-height:1.7;margin-bottom:14px}}
.pattern p:last-child{{margin-bottom:0}}
.pattern strong{{color:var(--text)}}

/* Compare links */
.cmp-grid{{display:flex;flex-wrap:wrap;gap:10px;margin-bottom:16px}}
.cmp-link{{background:var(--card);border:1px solid var(--border);padding:10px 16px;border-radius:10px;color:var(--accent-light);text-decoration:none;font-size:.85rem;font-weight:500;transition:all .2s}}
.cmp-link:hover{{border-color:var(--accent);background:rgba(108,92,231,0.1)}}

/* FAQ */
.faq-item{{background:var(--card);border:1px solid var(--border);border-radius:14px;padding:24px 22px;margin-bottom:16px}}
.faq-q{{font-size:1rem;font-weight:700;margin-bottom:10px}}
.faq-a{{color:var(--text-muted);font-size:0.9rem;line-height:1.7}}

/* CTA */
.cta-box{{background:var(--card);border:2px solid var(--accent);border-radius:16px;padding:32px 28px;text-align:center;margin-bottom:32px}}
.cta-box h3{{font-size:1.2rem;font-weight:700;margin-bottom:10px}}
.cta-box p{{color:var(--text-muted);font-size:0.9rem;margin-bottom:20px}}
.cta-btn{{display:inline-block;background:var(--accent);color:#fff;padding:12px 32px;border-radius:12px;text-decoration:none;font-weight:700;font-size:1rem;transition:all .25s}}
.cta-btn:hover{{background:var(--accent-light);transform:translateY(-2px);box-shadow:0 8px 32px rgba(108,92,231,0.35)}}

/* Footer */
.footer{{text-align:center;padding:32px 0;border-top:1px solid var(--border);margin-top:40px}}
.footer p{{color:var(--text-muted);font-size:0.8rem;margin-bottom:4px}}
.footer a{{color:var(--accent-light);text-decoration:none}}
</style>
</head>
<body>
<div class="ct">

<!-- Nav -->
<nav class="nv">
<a href="{BASE_URL}/" class="nb">Behavioral Design Hub</a>
<div class="nav-links">
<a href="{BASE_URL}/leaderboard/">Leaderboard</a>
<a href="{BASE_URL}/tools/behavioral-design-score/">Score Tool</a>
<a href="{BASE_URL}/categories/">All Categories</a>
</div>
</nav>

<!-- Hero -->
<div class="hero">
<div class="hero-emoji">{cat["emoji"]}</div>
<div class="cat-badge">Category Benchmark</div>
<h1>Behavioral Design in {title}</h1>
<p class="tagline">{cat["hero_tagline"]}</p>
</div>

<!-- Stats -->
<div class="stats-bar">
<div class="stat">
<span class="stat-num" style="color:{pct_color(int(avg_pct))}">{avg_pct:.0f}%</span>
<span class="stat-label">Category Average</span>
</div>
<div class="stat">
<span class="stat-num" style="color:var(--accent-light)">{n}</span>
<span class="stat-label">Products Analyzed</span>
</div>
<div class="stat">
<span class="stat-num" style="color:var(--green)">{winner["name"]}</span>
<span class="stat-label">Category Leader</span>
</div>
</div>

<!-- Overview -->
<div class="section">
<h2 class="section-title">Industry Overview</h2>
<div class="overview">
{cat["overview"]}
</div>
</div>

<!-- Rankings Table -->
<div class="section">
<h2 class="section-title">Rankings</h2>
<div class="tbl-wrap">
<table>
<thead>
<tr>
<th>#</th>
<th>Product</th>
<th>Score</th>
<th>Choice Arch.</th>
<th>Cog. Load</th>
<th>Motivation</th>
<th>Trust</th>
<th>Ethics</th>
</tr>
</thead>
<tbody>
{ranking_rows}
</tbody>
</table>
</div>
</div>

<!-- Dimension Averages -->
<div class="section">
<h2 class="section-title">Category Dimension Averages</h2>
<div style="background:var(--card);border:1px solid var(--border);border-radius:16px;padding:24px 20px">
{dim_avg_rows}
</div>
</div>

<!-- Cross-Product Pattern -->
<div class="section">
<h2 class="section-title">Cross-Product Pattern Analysis</h2>
<div class="pattern">
<h3>{cat["pattern_title"]}</h3>
{cat["pattern_text"]}
</div>
</div>

<!-- Head-to-Head Comparisons -->
<div class="section">
<h2 class="section-title">Head-to-Head Comparisons</h2>
<div class="cmp-grid">
{comp_links}
</div>
</div>

<!-- FAQ -->
<div class="section">
<h2 class="section-title">Frequently Asked Questions</h2>
{faq_html}
</div>

<!-- CTA -->
<div class="cta-box">
<h3>Score Your Own Product</h3>
<p>Take the free 2-minute Behavioral Design Score assessment and see how your product compares to the {title} category leaders.</p>
<a href="{BASE_URL}/tools/behavioral-design-score/" class="cta-btn">Take the Assessment →</a>
</div>

<!-- Footer -->
<div class="footer">
<p>Part of the <a href="{BASE_URL}/">Behavioral Design Hub</a></p>
<p>Research-backed behavioral science tools for product teams</p>
<p style="margin-top:8px"><a href="{BASE_URL}/leaderboard/">Full Leaderboard</a> · <a href="{BASE_URL}/categories/">All Categories</a></p>
</div>

</div>
</body>
</html>"""

    return html


def generate_category_index():
    """Generate the categories index page."""
    cat_cards = ""
    for cat in CATEGORIES:
        products = [PRODUCTS[p] for p in cat["products"]]
        n = len(products)
        avg = sum(p["total"] for p in products) / n
        avg_pct = avg / 50 * 100
        winner = max(products, key=lambda p: p["total"])
        names = ", ".join(p["name"] for p in sorted(products, key=lambda p: -p["total"]))

        cat_cards += f"""<a href="{BASE_URL}/categories/{cat['slug']}/" class="cat-card">
<div class="cat-emoji">{cat["emoji"]}</div>
<h3>{cat["title"]}</h3>
<p class="cat-avg" style="color:{pct_color(int(avg_pct))}">{avg_pct:.0f}% avg</p>
<p class="cat-products">{names}</p>
<p class="cat-leader">Leader: {winner["name"]} ({winner["pct"]}%)</p>
</a>
"""

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Behavioral Design by Industry — Category Benchmarks</title>
<meta name="description" content="Behavioral design rankings by industry: Social Media, E-Commerce, Productivity, Communication, and Entertainment. See which industries lead on ethics, motivation, and UX design.">
<meta property="og:title" content="Behavioral Design by Industry — Category Benchmarks">
<meta property="og:description" content="15 products scored across 5 industries. Which industry has the best behavioral design? See data-driven category benchmarks.">
<meta property="og:type" content="website">
<meta property="og:url" content="{BASE_URL}/categories/">
<link rel="canonical" href="{BASE_URL}/categories/">

<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "CollectionPage",
  "name": "Behavioral Design by Industry — Category Benchmarks",
  "description": "15 products scored across 5 industries. Data-driven behavioral design benchmarks by category.",
  "url": "{BASE_URL}/categories/",
  "hasPart": [
    {{"@type": "WebPage", "name": "Social Media", "url": "{BASE_URL}/categories/social-media/"}},
    {{"@type": "WebPage", "name": "E-Commerce & Marketplace", "url": "{BASE_URL}/categories/e-commerce/"}},
    {{"@type": "WebPage", "name": "Productivity & Collaboration", "url": "{BASE_URL}/categories/productivity/"}},
    {{"@type": "WebPage", "name": "Communication & Utility", "url": "{BASE_URL}/categories/communication-utility/"}},
    {{"@type": "WebPage", "name": "Entertainment & Learning", "url": "{BASE_URL}/categories/entertainment-learning/"}}
  ]
}}
</script>

<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {{
      "@type": "Question",
      "name": "Which industry has the best behavioral design?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "E-Commerce & Marketplace leads with a 71.3% category average, driven by Shopify (76%) and Airbnb (74%). Transaction-based business models create natural incentives for user-centered design. Social Media ranks lowest at 59.3%, reflecting the tension between engagement-maximizing design and user wellbeing."
      }}
    }},
    {{
      "@type": "Question",
      "name": "Which industry has the most ethical behavioral design?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "Productivity & Collaboration leads on Ethical Alignment with a 7.0/10 category average (Notion: 9/10, Slack: 5/10). Social Media has the lowest ethics average at 3.3/10. The pattern: subscription-based tools that align revenue with user outcomes consistently outperform advertising-based platforms on ethical dimensions."
      }}
    }}
  ]
}}
</script>

<style>
*{{margin:0;padding:0;box-sizing:border-box}}
:root{{
  --bg:#0a0a0f;--surface:#12121a;--card:#1a1a28;--border:#2a2a3a;
  --text:#e8e8f0;--text-muted:#8888a0;--accent:#6c5ce7;--accent-light:#a29bfe;
  --green:#00b894;--yellow:#fdcb6e;--red:#e17055;--blue:#74b9ff;
  --gradient:linear-gradient(135deg,#6c5ce7,#a29bfe,#74b9ff);
}}
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;background:var(--bg);color:var(--text);line-height:1.6;min-height:100vh}}
.ct{{max-width:900px;margin:0 auto;padding:32px 20px}}
.nv{{display:flex;justify-content:space-between;align-items:center;margin-bottom:40px;padding-bottom:16px;border-bottom:1px solid var(--border);flex-wrap:wrap;gap:8px}}
.nv a{{color:var(--accent-light);text-decoration:none;font-size:.88rem;font-weight:500}}
.nb{{font-weight:700;font-size:.95rem}}
.nav-links{{display:flex;gap:16px;flex-wrap:wrap}}
.nav-links a{{font-size:.82rem}}
.hero{{text-align:center;padding:20px 0 40px}}
.hero h1{{font-size:clamp(1.6rem,4vw,2.4rem);font-weight:800;background:var(--gradient);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;margin-bottom:12px;line-height:1.2}}
.hero p{{color:var(--text-muted);font-size:1rem;max-width:600px;margin:0 auto;line-height:1.7}}
.cat-grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:16px;margin-bottom:40px}}
.cat-card{{background:var(--card);border:1px solid var(--border);border-radius:16px;padding:28px 24px;text-decoration:none;color:var(--text);transition:all .2s}}
.cat-card:hover{{border-color:var(--accent);transform:translateY(-2px);box-shadow:0 4px 20px rgba(0,0,0,0.3)}}
.cat-emoji{{font-size:2.5rem;margin-bottom:12px}}
.cat-card h3{{font-size:1.1rem;font-weight:700;margin-bottom:8px}}
.cat-avg{{font-size:1.3rem;font-weight:800;margin-bottom:8px}}
.cat-products{{color:var(--text-muted);font-size:.82rem;margin-bottom:6px}}
.cat-leader{{color:var(--accent-light);font-size:.82rem;font-weight:600}}
.footer{{text-align:center;padding:32px 0;border-top:1px solid var(--border);margin-top:40px}}
.footer p{{color:var(--text-muted);font-size:0.8rem;margin-bottom:4px}}
.footer a{{color:var(--accent-light);text-decoration:none}}
</style>
</head>
<body>
<div class="ct">

<nav class="nv">
<a href="{BASE_URL}/" class="nb">Behavioral Design Hub</a>
<div class="nav-links">
<a href="{BASE_URL}/leaderboard/">Leaderboard</a>
<a href="{BASE_URL}/tools/behavioral-design-score/">Score Tool</a>
</div>
</nav>

<div class="hero">
<h1>Behavioral Design by Industry</h1>
<p>15 products scored across 5 industry categories. Which industry leads on behavioral design? Which has the biggest ethics gap? Explore the data.</p>
</div>

<div class="cat-grid">
{cat_cards}
</div>

<div class="footer">
<p>Part of the <a href="{BASE_URL}/">Behavioral Design Hub</a></p>
<p><a href="{BASE_URL}/leaderboard/">Full Leaderboard (15 Products)</a></p>
</div>

</div>
</body>
</html>"""
    return html


def main():
    # Create categories directory
    cat_dir = HUB_DIR / "categories"
    cat_dir.mkdir(exist_ok=True)

    # Generate index
    index_html = generate_category_index()
    (cat_dir / "index.html").write_text(index_html, encoding="utf-8")
    print(f"✓ categories/index.html")

    # Generate each category page
    for cat in CATEGORIES:
        slug_dir = cat_dir / cat["slug"]
        slug_dir.mkdir(exist_ok=True)
        html = generate_category_page(cat)
        (slug_dir / "index.html").write_text(html, encoding="utf-8")
        print(f"✓ categories/{cat['slug']}/index.html")

    print(f"\nGenerated {len(CATEGORIES)} category pages + 1 index = {len(CATEGORIES)+1} new URLs")


if __name__ == "__main__":
    main()
