---
name: seo-audit-mb
description: Runs a full technical SEO and structured-data audit of a Maurice Blackburn page or the whole site. Crawls index hygiene first (robots.txt, noindex, canonicals, sitemap membership), then canonicals/hreflang/redirect chains/404s, Core Web Vitals via the free PageSpeed Insights + CrUX API, mobile-HTML parity, an AI-crawler parity check (GPTBot/PerplexityBot/OAI-SearchBot vs Googlebot), and full JSON-LD extraction and validation. Use when the user says "audit this page/site for SEO", "run a technical SEO audit", "check crawlability/indexability", "why isn't this page indexed", "validate the schema / structured data / FAQPage", "check Core Web Vitals", "is this page mobile-friendly", "can AI crawlers see this page", or asks about canonicals, redirects, robots.txt, sitemaps, or rich results.
argument-hint: [URL, sitemap URL, domain, or crawl/GSC export path]
allowed-tools: Read, Write, Grep, Glob, Bash, WebFetch, AskUserQuestion
---

# seo-audit-mb

Full technical SEO and structured-data auditor for the Maurice Blackburn website: it finds what is broken or invisible to search engines and AI answer engines, ranks it by severity, and hands you a fix backlog.

This skill absorbs the old `seo-analyst-mb` schema logic and extends it into a complete technical audit. Playwright MCP browser tools load at runtime via ToolSearch (query `select:mcp__playwright__browser_navigate` and friends). Paid connectors are not needed here; siblings cover keyword, gap, and backlink work.

## When to Activate

- "Audit this page / this site for SEO."
- "Run a technical SEO audit" / "do a site health check."
- "Why isn't this page indexed / showing in Google?"
- "Check crawlability / indexability / robots / canonical / sitemap."
- "Validate the schema / structured data / FAQPage / rich results on this page."
- "Check Core Web Vitals / page speed / LCP / INP / CLS."
- "Is this page mobile-friendly? Are the nav links in the HTML?"
- "Can ChatGPT / Perplexity / AI crawlers actually read this page?"
- "Check the redirects / are there redirect chains or loops?"

## When NOT to Use

Scope this skill to the technical health of pages that already exist. Route elsewhere for:

- On-page content, E-E-A-T, and GEO answer-structure rewriting: `seo-content-mb`.
- Keyword and topic-cluster gaps vs Slater and Gordon / Shine: `seo-gap-mb`.
- Competitor rank tracking and Share-of-Voice / Share-of-Model: `seo-competitor-mb`.
- Backlink and digital-PR / off-site brand-mention analysis: `seo-backlinks-mb`.
- Bulk 404 discovery and ACS redirect management: the existing **"SEO - 404 Checker"** workstream. This skill cross-references its output rather than re-crawling the whole site for dead links.
- Road-injury FAQ schema authoring: the existing **"SEO - Road Injury FAQ Schema"** workstream. This skill validates FAQ schema; that workstream produces it.

## Before You Start

Confirm before auditing. Ask only what is missing:

1. **Scope.** One URL, a set of URLs, a sitemap URL, or the whole domain (mauriceblackburn.com.au)?
2. **Practice area** of the page(s), so severity is judged against YMYL expectations (asbestos, medical negligence, road/transport injury, workers comp, super/TPD, class actions, employment, abuse law, public liability).
3. **Geography.** MB is Australia-only. Any hreflang or non-AU signal is a flag, not a feature.
4. **Inputs available (ask this explicitly, do not assume none exists).** Before running the free-tool checks, ask whether the user has a Screaming Frog crawl export, a Google Search Console (GSC) coverage/index export, an XML sitemap, or a BrightEdge Data Cube / SEMrush Site Audit export for the same page(s). Any of these cross-checks "in the sitemap" vs "actually indexed", or supplements Core Web Vitals with a broader ranking/technical picture, without guessing. Always support the pasted/exported CSV fallback, but ask first rather than defaulting straight to the free-tool-only path.
5. **Cadence.** One-off, or the quarterly recurring audit (see the note at the end)?

If given a bare URL and no other context, begin immediately and note the assumptions you made.

## The Audit: run the checks in this order

Index hygiene comes first. A perfectly structured page that is blocked, noindexed, or canonicalised away is worth zero, so there is no point validating its schema until you know it can rank at all.

### 1. Crawl and index hygiene (do this first)

1. **robots.txt.** `curl -s https://mauriceblackburn.com.au/robots.txt`. Confirm the audited path is not `Disallow`ed. Confirm search bots (`Googlebot`, `bingbot`) are allowed, and that AI crawlers are explicitly allowed: `GPTBot`, `ClaudeBot`, `PerplexityBot`, `Google-Extended`. A path blocked in robots.txt cannot be crawled: **Critical**.
2. **Meta robots / X-Robots-Tag.** Fetch the page and check for `<meta name="robots" content="noindex...">` in the HTML head and for an `X-Robots-Tag` response header:
   `curl -sI https://mauriceblackburn.com.au/<path> | grep -i x-robots-tag`.
   An unintended `noindex` on a page you want ranked is **Critical**.
3. **Canonical target.** Extract `<link rel="canonical">`. The value should be an absolute HTTPS URL. If a page points its canonical at a different URL, note where it sends authority (see check 2).
4. **Sitemap membership vs reality.** Pull the XML sitemap(s): `curl -s https://mauriceblackburn.com.au/sitemap.xml`. Cross-check:
   - Page you want indexed but missing from the sitemap: **Warning**.
   - Page in the sitemap but `noindex`/canonicalised elsewhere/redirecting (mixed signals): **Critical**, sitemaps should list only indexable, canonical, 200-status URLs.
   - If a GSC coverage export is provided, diff "submitted in sitemap" against "indexed" to catch pages Google is choosing not to index. Never assert indexation status without either GSC data or a `site:` check; if you have neither, say so.

### 2. Canonicals, hreflang, redirects, 404s

1. **Self-referential canonical.** Each indexable page should canonical to itself. Missing or cross-pointing canonical on a page that should stand alone: **Warning** (or **Critical** if it silently deindexes a money page).
2. **No canonical chains or conflicts.** If A canonicals to B and B canonicals to C, that is a chain: **Critical**. A page carrying two conflicting canonical signals (e.g. one in HTML, one in the HTTP header) is also **Critical**.
3. **hreflang.** MB is AU-only. There should be no hreflang cluster. Any stray `hreflang` tag (e.g. an `en-us`/`en-gb` alternate, or a self-referential `en-au` with no counterparts) is a flag: **Warning**, remove it unless a real localised counterpart exists.
4. **Redirect chains and loops.** Trace the hop chain: `curl -sIL https://mauriceblackburn.com.au/<path> | grep -iE '^(HTTP|location)'`. One hop is fine. Two or more hops to the destination is a chain (**Warning**, wastes crawl budget and leaks a little authority per hop). A loop is **Critical**. Prefer a single 301 to the final URL.
5. **404s.** Do not re-crawl the whole site for broken links here. Cross-reference the **"SEO - 404 Checker"** workstream's latest output and flag any audited URL that appears there, or any internal link on the audited page that returns 404/410. Route new broken-link discovery and ACS redirect fixes back to that workstream.

### 3. Core Web Vitals (free PageSpeed Insights v5 + CrUX API)

Use the free PSI v5 endpoint, which returns both **lab** (Lighthouse) and **field** (CrUX, real-user) data. No API key is required for low volume; add `&key=YOUR_KEY` if a key is provisioned and you hit rate limits. Measure mobile and desktop separately, and lead with mobile (mobile-first indexing).

Exact call shape (mobile):

```bash
curl -s "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=https://mauriceblackburn.com.au/<path>&strategy=mobile&category=performance" \
  | python3 -c 'import sys,json; d=json.load(sys.stdin); \
    le=d.get("loadingExperience",{}).get("metrics",{}); \
    print("LCP_ms", le.get("LARGEST_CONTENTFUL_PAINT_MS",{}).get("percentile")); \
    print("INP_ms", le.get("INTERACTION_TO_NEXT_PAINT",{}).get("percentile")); \
    print("CLS_x100", le.get("CUMULATIVE_LAYOUT_SHIFT_SCORE",{}).get("percentile"))'
```

Re-run with `&strategy=desktop` for the desktop figure. The `loadingExperience` block is CrUX field data (what real users get); `lighthouseResult.audits` holds the lab diagnostics (what to fix). CLS percentile comes back multiplied by 100 (e.g. `10` means 0.10).

Grade each against Google's "good" thresholds:

| Metric | Good | Needs work | Poor |
|---|---|---|---|
| LCP (Largest Contentful Paint) | < 2.5s | 2.5-4.0s | > 4.0s |
| INP (Interaction to Next Paint) | < 200ms | 200-500ms | > 500ms |
| CLS (Cumulative Layout Shift) | < 0.1 | 0.1-0.25 | > 0.25 |

Any metric in "Poor" on mobile is **Critical**; "Needs work" is **Warning**. If CrUX returns no field data (low-traffic URL), say so and fall back to the Lighthouse lab score, labelling it as lab-only. Pull the top opportunities from `lighthouseResult.audits` (e.g. render-blocking resources, unsized images causing CLS) so the fix is actionable, not just a number.

### 4. Mobile: nav links in raw HTML, not click-injected

MB is mobile-first indexed. Googlebot must find navigation and key internal links in the server-rendered HTML, not behind a JS click.

1. Fetch raw HTML with `curl -s` (no JS execution) and grep for the primary nav and key practice-area links. If the main nav `<a href>` targets are present in raw HTML, good.
2. If the raw HTML has an empty nav shell and links only appear after JS/click, that is a crawl risk: **Warning** (or **Critical** if primary practice-area links are entirely JS-injected). Confirm by comparing the `curl` HTML against the Playwright-rendered DOM in check 5.
3. Also confirm a mobile viewport meta tag is present and tap targets are not obviously broken (report only what the HTML/CWV data shows; do not guess visual layout).

### 5. AI-crawler parity check (2026)

AI answer engines increasingly fetch pages with their own user-agents, and some do not execute JavaScript the way Googlebot's rendering service does. If MB's content only exists after client-side JS, an AI crawler may see an empty page, and MB gets left out of AI answers. Check parity.

1. Load Playwright MCP at runtime: `ToolSearch` with `select:mcp__playwright__browser_navigate,mcp__playwright__browser_evaluate,mcp__playwright__browser_snapshot`.
2. For each key URL, re-fetch under different user-agents and capture the rendered/main text:
   - Googlebot baseline: `Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)`
   - `GPTBot` (OpenAI training/crawl): `Mozilla/5.0 (compatible; GPTBot/1.1; +https://openai.com/gptbot)`
   - `OAI-SearchBot` (ChatGPT search): `Mozilla/5.0 (compatible; OAI-SearchBot/1.0; +https://openai.com/searchbot)`
   - `PerplexityBot`: `Mozilla/5.0 (compatible; PerplexityBot/1.0; +https://perplexity.ai/perplexitybot)`
   - `ClaudeBot`: `Mozilla/5.0 (compatible; ClaudeBot/1.0; +claudebot@anthropic.com)`
   Set the UA via Playwright, navigate, then extract main body text (`browser_evaluate` returning `document.querySelector('main')?.innerText` or the article container).
3. Diff each AI-crawler view against the Googlebot view and the raw `curl` HTML. Substantial missing body copy, headings, disclaimers, or the answer itself under an AI-crawler UA is **Critical** for GEO: the page is effectively invisible to that engine. Also confirm the compliance-critical text (jurisdiction, disclaimers) survives in the extractable body, not just a footer, per the compliance gate below.
4. If a bot UA is served a block/challenge page, cross-check robots.txt (check 1) and note whether it is a deliberate block or an accidental one.

### 6. Structured data: full JSON-LD extraction and validation

This carries over the `seo-analyst-mb` logic verbatim in spirit. Extract every `<script type="application/ld+json">` block and validate each.

General rules for every block:

1. JSON is well-formed and parseable. Malformed JSON-LD is **Critical** (the whole block is ignored).
2. `@context` is `https://schema.org` (not `http://`).
3. `@type` matches the intended rich-result type.
4. Required fields for the type are present and non-empty.
5. Flag duplicate entities, missing values, typo'd field names, truncated text, and content that violates Google's guidelines (promotional or misleading answers). Note if schema is injected via GTM or another tag manager rather than server-rendered.

Law-firm types to expect and their rules (use only where genuine, never fabricate a type the page does not support):

- **Article / BlogPosting** (news, case updates, guides): require `headline`, `datePublished`, and `dateModified`, and an `author` that is a real `Person` (name, ideally a `url` to the author bio), not the org as author and not a bare string. Missing author-as-Person or missing dates is a **Warning** (weakens E-E-A-T on YMYL content); missing `headline` is **Critical**.
- **LegalService / LocalBusiness / Attorney** (office and practice pages): require `name`, `address` (`PostalAddress`), and `areaServed`. Include `url` and `telephone`. A LocalBusiness/LegalService block with no real NAP is **Warning**. Do not stamp LegalService on a generic blog post.
- **FAQPage** (genuine Q&A only): each item is `@type: Question` with `name` (the question) and an `acceptedAnswer` of `@type: Answer` with `text`. Questions must be genuine user questions, not ads; answers factual; the FAQ content must be visible on the page (not hidden). Anchor links in answer `text` are allowed. Flag duplicate questions, missing answers, truncated text. FAQPage on content that is primarily promotional is **Critical** (guideline violation). Route FAQ authoring to the "SEO - Road Injury FAQ Schema" workstream; validate here.
- **BreadcrumbList**: `itemListElement` with ordered `position`, `name`, `item`. Broken position order or missing items is **Warning**.
- **Review / AggregateRating**: only where MB has real, on-file review data. Self-serving or fabricated ratings are **Critical** (guideline violation and legal-marketing risk).

### Severity scheme (same as seo-analyst-mb)

| Level | Meaning |
|---|---|
| Critical | The page cannot rank/be indexed, will fail validation or rich-result eligibility, is invisible to a crawler, has a "Poor" mobile CWV, or violates a Google/legal guideline. Fix now. |
| Warning | Works but risks being ignored, flagged, or degraded (mixed signals, redirect chains, weak E-E-A-T schema, "Needs work" CWV). Fix soon. |
| Info | Best-practice suggestion, no immediate impact. |

## Legal-marketing compliance gate

This skill mostly reads, but wherever it recommends copy or schema changes to public pages, enforce these (MB is a plaintiff law firm, YMYL content). A recommendation that breaches any of these must be reworded before it ships. This mirrors the `post-grader-mb` gate and `brand-mb`'s `reference/legal-marketing-guardrails.md`.

- No outcome guarantees ("you will win", "guaranteed compensation").
- No misleading comparative claims; do not imply a typical result from one case.
- No absolute claims about the law ("always"/"never") without a jurisdiction or circumstance hedge.
- Include a trigger/content warning for abuse, suicide, or distressing subject matter.
- Real client names only where consent is on file; otherwise "a client"/anonymised.
- For AI answer engines: disclaimers and jurisdiction (Australia / relevant state) must sit in the extractable body copy so AI crawlers ingest them with the answer, not hidden in a footer. Check this during the parity check (step 5).

## Output

Deliver a severity-ranked audit plus a fix backlog:

1. **One-line summary.** e.g. "Road-accident hub: indexable and schema-valid, but mobile LCP is Poor (4.3s) and the GPTBot view is missing the main body. 2 Critical, 3 Warning, 1 Info."
2. **Findings by category**, in the run order above (Index hygiene, Canonicals/hreflang/redirects/404s, Core Web Vitals, Mobile HTML, AI-crawler parity, Structured data). Each finding: severity tag, what was observed (with the exact value or measurement), and the exact fix.
3. **Prioritised action plan**, grouped by effort vs impact:
   - **Quick Wins** (low effort, high value): e.g. remove a stray hreflang, add `dateModified`, collapse a 2-hop redirect to one 301.
   - **Medium**: e.g. add author-as-Person to BlogPosting across the blog template, fix a canonical chain.
   - **High Impact** (bigger build): e.g. server-render nav/body so AI crawlers and Googlebot see it, fix a site-wide LCP regression.
4. **Backlog handoff.** Each action is written so it can be piped straight into `brief-ticket-monday-mb` (marketing/roadmap) or `brief-ticket-jira-mb` (Deloitte MBLS dev work). State which board each item belongs on. If the audit produced a formal write-up, `documentation-mb` can render it.
5. **MB-branded docx.** Always also export the audit as a `.docx` with the MB logo in the page header, do not leave the final deliverable only in chat. Build a JSON object matching the shape documented at the top of `scripts/render_mb_docx.py` (title, subtitle = the audited URL/scope, date, and a `sections` array covering the summary, findings table, and action plan), write it to a temp file with `Write`, then run:
   `/usr/bin/python3 scripts/render_mb_docx.py <input.json> <output-name>.docx`
   Use system Python (`/usr/bin/python3`), not a Homebrew/pyenv one, it is the interpreter with `python-docx` installed. Tell the user the saved file path.

Cross-link the siblings when a finding falls outside scope: content/E-E-A-T rewrites to `seo-content-mb`, keyword/topic gaps to `seo-gap-mb`, competitor/Share-of-Model tracking to `seo-competitor-mb`, off-site brand mentions and links to `seo-backlinks-mb`, bulk dead links to the "SEO - 404 Checker" workstream.

**Known baseline gaps (from `seo-content-mb`'s `reference/mb-page-templates.md`, extracted from 7 live pages on 2026-07-12):** MB's live service pages ship only `BreadcrumbList` (1 of 4 also has `FAQPage`), and live blog pages ship only `BreadcrumbList` with no `Article`/`BlogPosting`, `FAQPage`, or `Person` author schema, despite most pages having a visible FAQ and every blog having a visible author byline. Treat these as expected Critical/Warning findings on any page of that type until fixed, not a surprise.

## Error Handling

- **Page unreachable / non-200:** report the exact status code and stop analysing that URL. Do not invent content.
- **JS-rendered / empty raw HTML:** switch to Playwright MCP to render, and explicitly flag the client-side-rendering gap (it is itself an AI-crawler-parity finding). Never assume content exists because it "should".
- **Paywalled / auth-gated (e.g. staging behind basic auth):** use the known staging credentials via `curl` (WebFetch fails on basic-auth staging); if still blocked, request the page text from the user rather than guessing.
- **CrUX returns no field data:** state that plainly and fall back to Lighthouse lab data, labelled as lab-only, not real-user.
- **No GSC / sitemap / crawl export:** you can still audit a single page fully, but say clearly that sitemap-vs-indexed reconciliation is unavailable without one of those inputs. Never fabricate indexation status.
- **PSI rate-limited:** add a provisioned `&key=` if available, otherwise space calls out or reduce the URL set.

## Cadence

Run this as a **quarterly** technical audit of MB's priority templates and top-traffic pages, plus ad hoc on any new or substantially changed page before it goes live. Between quarters, the "SEO - 404 Checker" workstream covers ongoing broken-link monitoring, so this audit focuses on regressions in index hygiene, Core Web Vitals, crawler parity, and schema.
