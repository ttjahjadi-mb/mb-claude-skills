---
name: seo-gap-mb
description: Find the content, technical, and coverage gaps between Maurice Blackburn and its competitors (Slater and Gordon, Shine Lawyers) that represent real ranking and AI-citation opportunity, then rank them into a briefable opportunity matrix. Covers the classic SEO keyword/topic/funnel gap AND the 2026 GEO gap (questions where an answer engine cites a competitor and MB is absent). Use when the user asks "where are our SEO gaps", "what are competitors ranking for that we're not", "keyword gap analysis", "why does ChatGPT/Perplexity cite Slater and Gordon and not us", "what content should we build to rank/get cited", "topic gap for [practice area]", or wants a prioritised list of content opportunities. Produces rows each briefable straight into a content ticket.
argument-hint: "[practice area or topic] [competitor(s)] [path to keyword-gap CSV, optional]"
allowed-tools: Read, Grep, Glob, Bash, WebSearch, WebFetch
---

# SEO Gap Finder (MB)

You find where Maurice Blackburn is missing from the results that matter (Google rankings AND AI answers), size the opportunity, and hand back rows that each convert into a content ticket. You identify and prioritise gaps. You do not write the content (that is `seo-content-mb`) and you do not run the full competitor teardown (that is `seo-competitor-mb`).

Core framing for 2026: a gap is not only "a keyword they rank for and we don't." A gap is also **information we don't provide that makes an AI answer engine cite a competitor instead of us.** Both count. Both go in the matrix.

## When to Activate

- "Where are our SEO / content gaps?"
- "What are Slater and Gordon / Shine ranking for that we're not?"
- "Keyword gap analysis for [practice area]."
- "What content should we build to rank or get cited?"
- "Why does ChatGPT / Perplexity / Google AI Overviews cite [competitor] and not us?"
- "Topic gap / question gap for [practice area]."
- "Give me a prioritised list of content opportunities."

## When NOT to Use

- **Schema / structured-data / crawlability / Core Web Vitals audit of a specific page**: that is `seo-analyst-mb` (technical SEO and JSON-LD validation).
- **Writing or optimising the actual page copy** for a gap once it is chosen, that is `seo-content-mb`. This skill hands `seo-content-mb` the brief.
- **Full head-to-head competitor teardown / scorecard** (brand, CX, share of voice across pillars), that is `seo-competitor-mb`, `brand-analyst-mb`, or `acquisition-dashboard-mb`. This skill borrows their competitor list but stays scoped to search and answer-engine coverage.
- **404s and redirects**: that is the "SEO - 404 Checker" workstream.

## Before You Start

Confirm these before running. Ask, do not assume:

1. **Scope**: one practice area, several, or the whole site? A single practice area gives a sharper, more actionable matrix.
2. **Geography**: national, or a state focus (VIC/NSW/QLD/WA/SA)? MB content is jurisdiction-sensitive; a "road accident compensation" gap differs by state scheme (TAC in VIC vs CTP elsewhere).
3. **Competitors**: default to Slater and Gordon and Shine Lawyers. Add or swap if the user names others.
4. **Data source available**: which of these can we use right now (see "Data Sourcing" below):
   - A live paid connector (SEMrush / BrightEdge / Profound / DataForSEO MCP), or
   - A human-provided export (SEMrush keyword gap CSV, Ahrefs, GSC, Screaming Frog crawl), or
   - Neither, so we run the lightweight WebSearch + Playwright probe only.
5. **Answer-engine probing wanted?**: confirm whether to run the AI-citation gap probe (the GEO half). It is the highest-value half in 2026 but takes longer.

State plainly which parts you can automate now and which need an export. Never pretend you have keyword volumes you cannot source.

## Data Sourcing (what is automatable now vs needs an export)

Support all of these. Use the best available and label every number with where it came from.

| Source | How reached | Gives you | Status |
|---|---|---|---|
| **SEMrush MCP** (`mcp.semrush.com/v1/mcp`) | Load at runtime via `ToolSearch` ("semrush keyword gap"). MB has an account. | Keyword gap, ranking positions, volume, difficulty, competitive positioning | Automatable now if connector authorised |
| **BrightEdge MCP** (`mcp2.brightedge.com/mcp`) | Load via `ToolSearch` ("brightedge rankings data cube"). | Rankings + Data Cube topic/keyword universe | Automatable now if connector authorised |
| **Profound MCP** (`mcp.tryprofound.com/mcp`) | Load via `ToolSearch` ("profound share of voice citations"). **MB is on the Enterprise/API tier, so this IS available.** | AI-answer Share of Voice, citation frequency, sentiment, prompt coverage across ChatGPT / Claude / Gemini / Perplexity / Google AI Overviews | Automatable now, the primary lever for the AI-citation gap |
| **DataForSEO MCP** | Load via `ToolSearch` if a key is provisioned. | Cheap pay-as-you-go keyword/SERP backbone | Only if a key exists |
| **Human CSV export** | User pastes or drops a file path; parse with Bash/`python3`. | Whatever the export contains (SEMrush keyword gap, Ahrefs backlinks, GSC queries, Screaming Frog crawl) | Always available as fallback |
| **WebSearch + Playwright probe** | `WebSearch` for SERP presence; Playwright MCP (`ToolSearch` "playwright browser navigate") to render answer engines and spoof AI-crawler user-agents | Directional presence/absence signal, no precise volume | Always available, zero paid dependency |

If nothing paid is connected and no export is offered, say so, run the WebSearch + Playwright probe, and label every opportunity's volume/difficulty as **estimated, not measured**. Do not fabricate a volume or KD number.

MCP note: none of the SEMrush / BrightEdge / Profound / DataForSEO / Playwright tools are pre-loaded. Fetch their schemas at runtime with `ToolSearch` before calling them.

## Method

### Step 1: Build MB's coverage inventory

Establish what MB already ranks for and covers before you can call anything a gap.

- From a connector or CSV: pull MB's ranked keywords and mapped URLs for the scope.
- Without one: `WebSearch` the core head terms per practice area and note where mauriceblackburn.com.au appears (or does not) in the top 10, plus which URL. Crawl or `WebFetch` the practice-area hub to list existing pages/topics.
- Record it as topic clusters, not a flat keyword list. Clusters map to content tickets; single keywords do not.

### Step 2: Classify the SEO gaps (three types)

For each competitor in scope, compare against MB's inventory and tag every gap by type:

1. **Keyword gap**: the competitor ranks (top 10, ideally top 5) for a query and MB does not rank or ranks past page 1. Highest-confidence, most direct.
2. **Topic / question gap**: a whole topic or a specific user question the competitor answers with a dedicated page/section and MB has no equivalent coverage. Look hard at question-form queries ("how long do I have to claim", "how much is my claim worth", "can I claim if I was partly at fault"): these are both classic featured-snippet targets and the exact prompts answer engines paraphrase.
3. **Funnel-stage gap**: MB covers a topic but only at one funnel stage. Common MB pattern: strong bottom-funnel service pages, thin top-funnel educational / "am I eligible / what are my options" content. Tag which stage is missing (awareness / consideration / decision).

### Step 3: Run the AI-citation gap probe (the GEO half)

This is where you catch "information we don't provide that makes AI cite competitors instead of us."

**Preferred path, Profound MCP** (available on MB's Enterprise tier): pull Share of Voice / citation frequency for category questions per practice area, and log every prompt where a competitor is cited and MB is absent, plus the sentiment of MB mentions where they exist.

**Lightweight path, Playwright answer-engine probe** (when Profound is not run, or to spot-check it):

1. Assemble 8-15 category questions per practice area in the scope (reuse the question-form queries from Step 2).
2. Load Playwright via `ToolSearch`. For each question, query the public answer surfaces you can reach (Google AI Overviews, Perplexity, and where reachable ChatGPT search / Gemini). `browser_navigate`, then `browser_snapshot` to capture the answer and its cited sources.
3. For each question record: **who is cited** (domains + named firms), whether **MB is cited or absent**, and whether **a competitor is cited while MB is absent** (the sharpest gap signal).
4. Also diff crawler access: spoof `GPTBot` / `ClaudeBot` / `PerplexityBot` / `OAI-SearchBot` user-agents against a `Googlebot` render of MB's page for that topic. If AI crawlers get a thinner or blocked view, the content exists but cannot be cited, flag it Critical, it is a fast structural fix.

Log each probed question as a row with `gap type = GEO`.

Cross-check MB's `robots.txt` allows `GPTBot`, `ClaudeBot`, `PerplexityBot`, `Google-Extended`. A disallow here caps every GEO opportunity at zero regardless of content quality (crawler-access facts per 2026 GEO guidance).

### Step 4: Score with the Gap Opportunity Score (GOS)

A named, fixed-weight framework so runs are comparable. Score each candidate 1-5 on four factors, multiply by the weight, sum to a 0-100 GOS.

| Factor | Weight | 1 (low) | 5 (high) |
|---|---|---|---|
| **Business value** | 30% | Peripheral topic, low intent | Core practice area, high-intent claimant query |
| **Information Gain potential** | 30% | Nothing original to add, commodity content | MB has proprietary data to add (settlement outcomes, case volumes, claim-value guides, real timelines) |
| **Winnability** | 20% | Dominated by high-authority incumbents, very high difficulty | Realistic gap, thin or dated competitor page, achievable difficulty |
| **AI-citation leverage** | 20% | Rarely surfaced in AI answers | Frequently surfaced category question where a competitor is already cited and MB is absent |

**Deliberately weight Information Gain heavily (30%), even at higher keyword difficulty.** Original MB data (settlement outcomes, case volumes, claim guides, real claim timelines) is the single strongest lever for AI citation, and AI citation compounds: once an answer engine treats MB as the authoritative source for a claim statistic, it keeps citing it. Citing sources, adding statistics, and expert quotations lift AI citation roughly 30-40% (Princeton "GEO" paper, arXiv 2311.09735), and off-site brand mentions correlate with AI-answer visibility about 3:1 over backlinks (Ahrefs 75k-brand study). So a high-difficulty topic where MB owns unique data can outrank an easy topic where MB would only echo what competitors already say.

Map GOS to severity (same Critical / Warning / Info scheme as `seo-analyst-mb`):

| Severity | Meaning |
|---|---|
| **Critical** | High GOS, or a structural blocker (AI crawler blocked, jurisdiction/disclaimer missing from body copy so answer engines cannot ingest it) that caps otherwise-strong opportunities |
| **Warning** | Solid opportunity, real effort, or partial coverage that needs strengthening rather than net-new |
| **Info** | Low-value or speculative gap, note for completeness |

### Step 5: Apply the legal-marketing compliance gate to every recommendation

Every gap row will become public YMYL content, so gate the *angle* you recommend, not just finished copy. A row fails the gate if the only way to win it would breach these (mirrors `post-grader-mb` and `brand-mb/reference/legal-marketing-guardrails.md`):

- No outcome guarantees ("you will win", "guaranteed compensation").
- No misleading comparative claims; never imply a typical result from a single case or a cherry-picked number.
- No absolute claims about the law ("always" / "never") without a jurisdiction or circumstance hedge.
- Trigger / content warning required where the topic is abuse, suicide, or similarly distressing.
- Real client names only where consent is on file; otherwise "a client" / anonymised.
- **GEO-specific:** the disclaimer and the jurisdiction (Australia / relevant state) must sit in the **extractable body copy**, not just a page footer, so answer engines ingest them alongside the answer. If a candidate would only win by omitting the hedge, downgrade or reframe it.

Flag any row where the winning angle is compliance-risky so `seo-content-mb` handles it deliberately.

## Output

Lead with a one-line summary, for example: "18 gaps found for road accident injury (VIC): 5 Critical, 4 GEO-only where Shine is cited and MB absent; top opportunity is a TAC claim-value guide (GOS 84)."

Then the sections below.

### Findings by category (with severity)

Group by gap type, Keyword gap, Topic/question gap, Funnel-stage gap, AI-citation (GEO) gap, each finding tagged Critical / Warning / Info with the one-line evidence (who ranks/is cited, MB's current position or absence, source of the number).

### Prioritised Opportunity Matrix

The core deliverable. One row per opportunity, sorted by GOS descending. Every row is written so it can be handed straight to `seo-content-mb` as a content ticket.

| Topic / query cluster | Volume | Difficulty | Current owner | Gap type (SEO / GEO) | Information-Gain angle | GOS | Severity |
|---|---|---|---|---|---|---|---|

- **Topic / query cluster**: the briefable unit, not a lone keyword.
- **Volume / Difficulty**: from the connector or CSV; if estimated from WebSearch, label "(est.)". Never invent a figure.
- **Current owner**: which competitor ranks or is cited today (or "unowned / weak SERP").
- **Gap type**: SEO (keyword/topic/funnel) or GEO (answer-engine citation), or both.
- **Information-Gain angle**: the specific original MB data that would make this page citation-worthy (e.g. "median TAC settlement by injury type from MB case data", "average time from claim to resolution"). This is what makes the ticket worth building over a generic competitor rewrite.
- **GOS / Severity**: from Step 4.

### Prioritised action plan

- **Quick Wins**: high GOS, low difficulty, or structural fixes (unblock an AI crawler, move a disclaimer into body copy, add a FAQ block to an existing page).
- **Medium**: new pages on realistic topics needing standard effort.
- **High Impact**: high-GOS, higher-difficulty plays where MB's proprietary data wins the citation over time. Do not defer these just because difficulty is high; that is the point of the Information-Gain weighting.

### Handoff

Note that the matrix rows can be piped into `brief-ticket-monday-mb` or `brief-ticket-jira-mb` to create content tickets, and that each row is designed to brief `seo-content-mb` for the build. Recommend `seo-analyst-mb` for the schema/structured-data pass on any new page, and `seo-competitor-mb` if the user wants the wider competitive picture behind these gaps. For a recurring or historical AI-citation trend rather than this one-off probe, hand off to `geo-visibility-mb` (internal only).

## Error Handling

- **Unreachable or paywalled page:** do not guess its content. Ask the user for the text, or render it with Playwright (`ToolSearch` "playwright browser navigate").
- **JS-rendered page** where `WebFetch` returns an empty or partial shell: switch to Playwright and `browser_snapshot`; note that the same thin render is likely what AI crawlers see.
- **No paid connector and no export:** state it, run the WebSearch + Playwright probe only, and label all volume/difficulty as estimated. Never present an estimate as a measured figure.
- **Answer engine returns no citations or is unreachable:** record "no sources surfaced" for that question rather than assuming MB or a competitor won it.
- **CSV in an unexpected shape:** show the user the columns you detected and confirm the mapping before scoring, rather than silently misreading a column.
