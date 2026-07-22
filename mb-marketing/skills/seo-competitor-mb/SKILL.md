---
name: seo-competitor-mb
description: Compare Maurice Blackburn's SEO and GEO (generative engine / AI-answer) standing against named competitors, default Slater and Gordon and Shine Lawyers. Produces a competitor scorecard, a keyword-gap opportunity list, and both traditional Share of Voice and Share of Model (AI-answer visibility) bars. Use when the user asks "how do we rank vs Slater and Gordon", "SEO competitor analysis", "who wins on [practice area] search", "are we showing up in ChatGPT/Perplexity/AI Overviews vs competitors", "keyword gap vs Shine", "share of voice", or "share of model / AI visibility". Reuses the competitor framework from acquisition-dashboard-mb and brand-analyst-mb rather than forking it, and adds the SEO/GEO-specific measurement layer on top.
argument-hint: [MB page/domain + competitor(s) + practice area/geography, or a paid-tool export path]
allowed-tools: Read, Write, Grep, Glob, Bash, WebSearch, WebFetch, AskUserQuestion
---

# MB SEO/GEO Competitor Analyst

Compare Maurice Blackburn's search and AI-answer standing against named competitors on a practice area or the domain as a whole, then report a scored teardown a marketing lead can act on. Default competitors: Slater and Gordon, Shine Lawyers. Accept any others the user names.

MCP tools (SEMrush, BrightEdge, Profound, DataForSEO, Playwright) are not in `allowed-tools` above because they load at runtime via ToolSearch. Fetch a tool's schema with `ToolSearch` (e.g. `select:mcp__playwright__browser_navigate`) before calling it. Everything still works without them via the CSV/export fallback, which you must always support.

## When to Activate

- "How do we rank against Slater and Gordon / Shine on [practice area]."
- "SEO competitor analysis" / "keyword gap vs [competitor]."
- "Share of Voice" for a topic or practice area across the plaintiff-law market.
- "Share of Model", "AI visibility", "are we cited in ChatGPT / Gemini / Perplexity / Claude / Google AI Overviews vs competitors."
- "Content teardown vs [competitor]" / "who has better pages on [topic]."
- "Technical / Core Web Vitals comparison" across the firms.

## When NOT to Use

- Full acquisition due-diligence, a saved scored dashboard across nine pillars, an Excel workbook, or a leadership deck: that is `acquisition-dashboard-mb`. This skill is the SEO/GEO-specific layer, not a replacement.
- A brand-only read (positioning, tone, visual identity, reputation): that is `brand-analyst-mb`. Borrow its competitor-research method, but stay in SEO/GEO here.
- Auditing MB's own schema / JSON-LD / rich-result eligibility on a single page: that is `seo-analyst-mb`.
- Turning the resulting opportunity list into an on-page content plan for one MB page: hand off to `seo-gap-mb`, which this skill feeds (see Output).
- Writing or grading the actual social/marketing copy: `post-writer-mb` / `post-grader-mb`.

## Relationship to the existing competitor framework (reuse, do not fork)

`acquisition-dashboard-mb` and `brand-analyst-mb` already own MB's competitor-comparison framework: how a competitor is researched, how MB's own side is sourced (`brand-mb`), and the 1-5 scored-pillar teardown format. Do not rebuild that.

- **What those skills own:** the acquisition/due-diligence scoring across all pillars (`acquisition-dashboard-mb`) and the brand/positioning/tone read (`brand-analyst-mb`).
- **What this skill adds:** the SEO/GEO measurement layer that sits inside the "SEO / digital visibility" pillar of that framework: keyword gap, traditional Share of Voice, Share of Model (AI-answer visibility), content depth/format teardown, and a technical + Core Web Vitals comparison.
- **In practice:** when a run here is part of a bigger acquisition or brand review, produce the scorecard below and tell the user it drops straight into the SEO pillar of `acquisition-dashboard-mb`.

**MANDATORY, every run, not just acquisition/brand reviews: pull MB's brand/voice/positioning side from `brand-mb` first** (`brand-guidelines.md`, `brand-history.md`), the same way `brand-analyst-mb` does, rather than re-researching or assuming it. A competitor comparison is only meaningful measured against MB's actual documented position, not a guess.

## Before You Start

**Treat every new chat as a brand new session, even if a previous conversation covered this exact scope or competitor set.** Never skip a question below because a past chat seems to have already answered it, past chat history is background context only, not a substitute for confirming inputs in this run.

Confirm, briefly, before running:

1. **Scope:** whole domain (mauriceblackburn.com.au) or a specific practice area / page? Practice areas: asbestos & dust diseases, medical negligence, road/transport accident injury, workplace injury & workers compensation, superannuation & TPD claims, class actions, employment & industrial law, abuse law, public liability.
2. **Competitors:** default Slater and Gordon (slatergordon.com.au) and Shine Lawyers (shine.com.au). Confirm or add others.
3. **Geography:** national, or a state/city (matters for local pack and "near me" intent).
4. **Data available (MANDATORY, all four, equal standing, asked in the same turn):** before running anything, ask about all of the following, every time, no exceptions:
   - **SEMrush**: live connector, or a keyword-gap / ranking export to paste?
   - **BrightEdge**: live connector, or a Data Cube / rankings export to paste?
   - **Profound**: live connector (MB is on the Enterprise/API tier), or an AI-citation / Share-of-Model export to paste?
   - **GSC / Ahrefs / Screaming Frog**: any export covering this scope?

   **Hard rules, this has failed in practice by being silently watered down, do not repeat that:** all names must appear in the one question you send, in the same message. **Never rank or editorialise which matters more** ("GSC and SEMrush are most useful, BrightEdge/Profound are a bonus" is exactly the failure mode to avoid), the user's answer decides, not your guess. Check the literal text before sending, rewrite it if any tool is missing. If the user only answers for one or two, ask about the rest before proceeding, a partial answer is not a complete one. **Ask this every single time the skill runs, with zero exceptions, by default. Never assume.** Do not skip it because this session already asked for a different scope or competitor set, or because the topic looks similar to one already covered. State which parts you can automate now vs which need an export before you begin, so expectations are set.

## Method

Run the parts relevant to the ask. Each part is scored on the same 1-5 scale used by `acquisition-dashboard-mb` (1 = MB clearly behind, 3 = par, 5 = MB clearly ahead) so runs are comparable over time. Findings within a part carry a **Critical / Warning / Info** severity (same scheme as `seo-analyst-mb`).

### Data-sourcing legend (state this per part in the output)

- **Automatable now:** doable with Bash/curl/Playwright/WebSearch or a live MCP connector.
- **Needs export:** requires a paid-tool CSV the user pastes, or a connector that is not currently provisioned.

### Part 1: Keyword gap and traditional Share of Voice (weight 30%)

Traditional Share of Voice = a domain's estimated share of total organic clicks/visibility for the topic keyword set, expressed as a percent per domain (all tracked domains sum to ~100%).

1. Assemble the keyword set for the scope (practice-area seed terms + their long-tail and "near me" variants).
2. **Automatable now** (live connector): pull ranking positions and volumes via SEMrush MCP (`mcp.semrush.com/v1/mcp`) or BrightEdge MCP (`mcp2.brightedge.com/mcp`); DataForSEO MCP is a cheap pay-as-you-go backbone if a key is provisioned. **Needs export** otherwise: parse a SEMrush "Keyword Gap" or Ahrefs "Content Gap" CSV the user provides.
3. Bucket keywords: MB ranks and leads, MB ranks but a competitor outranks, competitor ranks and MB is absent (the gap), nobody ranks well (open field).
4. Compute traditional SoV per domain: sum a CTR-weighted visibility score by position across the keyword set, then express each domain as a percent of the total. State the CTR curve assumption (e.g. position 1 ~30%, tapering) so the number is reproducible.
5. Score: MB SoV clearly above both competitors = 5; roughly level = 3; clearly below = 1.

### Part 2: Share of Model (AI-answer visibility) (weight 25%)

Share of Model = the AI equivalent of Share of Voice: the percent of AI answers, across ChatGPT, Gemini, Perplexity, Claude, and Google AI Overviews, that mention (or cite) each firm for a set of buyer-intent prompts. This is the load-bearing GEO metric.

1. Build a prompt set that mirrors how an injured person would actually ask (e.g. "best asbestos compensation lawyer in Victoria", "how do I claim TPD superannuation", "who runs class actions in Australia"). Cover each in-scope practice area and geography.
2. **Automatable now (preferred, MB is on the Profound Enterprise/API tier):** use Profound MCP (`mcp.tryprofound.com/mcp`) for Share of Voice across models, citation frequency, prompt coverage, and sentiment per firm. This is the cleanest source.
3. **Automatable now (fallback / cross-check):** answer-engine probes via Playwright MCP (load its tools with ToolSearch). Run each prompt through the public answer engines, capture the rendered answer text and any citations, and tally which firms are named. Note this is a point-in-time sample, not a stable metric, so record the date and prompt count.
4. Compute Share of Model per firm = (prompts where the firm is mentioned or cited) / (total prompts), per engine and blended. Also record citation frequency (how often MB's own domain is the cited source) and answer sentiment.
5. Cross-check crawler access (feeds this metric): fetch `mauriceblackburn.com.au/robots.txt` and each competitor's, and confirm GPTBot, ClaudeBot, PerplexityBot, and Google-Extended are allowed. A firm that blocks AI crawlers cannot be cited. **Automatable now** via curl.
6. Score: MB Share of Model clearly above both competitors = 5; level = 3; below = 1.

Why this matters, cite when you assert it: off-site brand mentions correlate with AI-answer visibility roughly 3:1 over backlinks (Ahrefs 75k-brand study), and citing sources, statistics, and expert quotations lifts AI citation ~30-40% (Princeton "GEO" paper, arxiv 2311.09735). So a Share-of-Model gap is usually a digital-PR / earned-media and content-structure gap, not an on-page-keyword gap.

### Part 3: Content depth and format teardown (weight 25%)

For the top MB page and each competitor's equivalent page on the in-scope topic:

1. Fetch each page (WebFetch; if JS-rendered or blocked, use Playwright, never guess). Compare: word count and topic coverage, whether sections open with a direct 40-80 word standalone answer, chunk size (~120-180 words, self-contained), question-based H2/H3, explicit FAQ/Q&A blocks, statistics and cited sources, named expert authorship (a real `Person`), and `dateModified` freshness. These are the retrieval-structure signals AI engines reward.
2. Check schema present per page (defer the deep JSON-LD validation to `seo-analyst-mb`): law-firm-relevant types are LegalService, Attorney, LocalBusiness, FAQPage, Review, Article/BlogPosting with a real Person author.
3. **Compliance gate on anything you recommend MB publish** (hard gate, embedded): no outcome guarantees ("you will win", "guaranteed compensation"); no misleading comparative claims or implying a typical result from one case; no absolute claims about the law ("always"/"never") without a jurisdiction/circumstance hedge; a trigger/content warning on abuse, suicide, or distressing subject matter; real client names only where consent is on file, otherwise "a client"/anonymised. For GEO specifically: the disclaimer and jurisdiction (Australia / relevant state) must sit in the extractable body copy, not just a footer, so answer engines ingest them with the answer. If a recommendation would breach any of these, do not make it; this mirrors the `post-grader-mb` compliance gate and `brand-mb`'s `reference/legal-marketing-guardrails.md`.
4. Score: MB pages deeper and better-structured for retrieval than both competitors = 5; level = 3; behind = 1. **Automatable now.**

### Part 4: Technical and Core Web Vitals comparison (weight 20%)

1. **Automatable now, free:** run the Google PageSpeed Insights + CrUX API (PSI v5, no key-cost issues) via curl for MB and each competitor's key page. Capture field CrUX (real-user LCP, INP, CLS) and lab scores. Example: `curl "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=<encoded-url>&strategy=mobile"`.
2. Compare crawlability/indexability signals: robots.txt (reuse Part 2 step 5), sitemap presence and health, canonical hygiene, HTTPS, mobile-friendliness.
3. Flag each finding with severity: Critical (failing CWV thresholds or blocking indexation), Warning (near threshold or risky config), Info (best-practice nudge).
4. Score: MB clearly faster/cleaner than both competitors = 5; level = 3; behind = 1.

### Composite score

Weighted composite (1-5) = 0.30·Part1 + 0.25·Part2 + 0.25·Part3 + 0.20·Part4. Report the composite plus each part's score so the movement is legible. These weights are fixed so runs are comparable; do not retune per run.

## Output

Deliver in the conversation (offer to save a copy if the run is large):

1. **One-line summary:** e.g. "MB leads on organic SoV (42%) but trails Shine on Share of Model (MB 18% vs Shine 34%); composite 3.4/5, biggest gap is AI-answer visibility on TPD."
2. **Competitor scorecard:** a table, one row per firm, columns for each part's 1-5 score, the composite, and the data-source note (automatable-now vs export-based) per part so the reader knows how solid each number is.
3. **Traditional Share of Voice bars:** percent per domain (text bars are fine, e.g. `MB ████████ 42%`), with the CTR-curve assumption stated.
4. **Share of Model bars:** percent of AI answers mentioning/citing each firm, per engine and blended, with the date and prompt count, and citation frequency + sentiment noted.
5. **Findings by category** (keyword gap, Share of Model, content, technical), each with **Critical / Warning / Info** severity and the exact fix.
6. **Keyword-gap opportunity list:** the competitor-ranks-MB-absent and open-field buckets, ranked by volume × winnability, each tagged with the target practice area and intent.
7. **Prioritised action plan:** Quick Wins / Medium / High Impact. GEO fixes (earned-media brand mentions, adding cited statistics and expert quotes, opening sections with standalone answers, jurisdiction disclaimers in body copy) usually sit in High Impact given the 3:1 mentions-over-backlinks and 30-40% citation-lift evidence above. Note that `llms.txt` is a low-priority, experimental, forward-compat bet with no measured citation lift yet, never a primary tactic.
8. **Handoff notes:** the opportunity list feeds `seo-gap-mb` for on-page execution on a specific MB page; the scorecard drops into the SEO pillar of `acquisition-dashboard-mb`; and the whole backlog can be piped into `brief-ticket-monday-mb` or `brief-ticket-jira-mb` (MBLS) as tickets.
9. **MB-branded docx:** always also export the scorecard as a `.docx` with the MB logo in the page header. Build a JSON object matching the shape at the top of `scripts/render_mb_docx.py` (title, subtitle = scope/competitors, date, sections for the summary, scorecard table, SoV/Share-of-Model bars as text, and the action plan), write it with `Write`, then run `/usr/bin/python3 scripts/render_mb_docx.py <input.json> <output-name>.docx`. Use system Python (`/usr/bin/python3`), it has `python-docx` installed. Tell the user the saved file path.

## Error Handling

- **Unreachable or paywalled page:** ask the user for the page text or an export; do not guess or fabricate metrics.
- **JS-rendered page** (thin/empty via WebFetch): re-fetch with Playwright MCP (load its tools with ToolSearch) before concluding content is missing.
- **No live MCP connector:** fall back to the CSV/export path and say so, clearly, per affected part. Never present export-dependent numbers as if they were pulled live.
- **Answer-engine probe variance:** Share of Model from Playwright probes is a point-in-time sample. Always stamp it with date and prompt count, and prefer Profound MCP as the stable source where available.
- **Missing MB-side brand/voice inputs:** pull from `brand-mb` as `brand-analyst-mb` does; treat documented gaps as real gaps, do not invent MB positioning to pad the comparison.

**For a recurring or historical Share of Model trend, or the full Profound feature set (sentiment, citation sources, AI-referred traffic), hand off to `geo-visibility-mb` (internal only)** rather than re-running this Part 2 repeatedly. This skill's Part 2 is for a single-conversation, point-in-time comparison inside a wider competitor teardown.
