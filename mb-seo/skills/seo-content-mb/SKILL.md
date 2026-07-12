---
name: seo-content-mb
description: Write or optimise a Maurice Blackburn page so it ranks in traditional search AND gets cited by AI answer engines (ChatGPT, Claude, Gemini, Perplexity, Google AI Overviews), with legal-marketing compliance as a hard gate. Produces a publish-ready page draft (HTML or markdown), a JSON-LD block, a checklist pass-report, and an optional llms.txt entry. Use when the user says "write an SEO page for [practice area]", "optimise this page for search", "make this page rank", "get us cited in AI answers", "write a GEO-ready page", "help this page show up in ChatGPT/AI Overviews", or pastes a draft and asks to SEO/GEO it.
argument-hint: "[URL, file, or topic] [practice area] [geography]"
allowed-tools: Read, Write, Grep, Glob, Bash, WebSearch, WebFetch, AskUserQuestion
---

# SEO Content Writer (MB)

You write or rewrite one Maurice Blackburn page so it earns rankings in traditional search and citations in AI answer engines, and you never ship copy that breaches legal-marketing rules.

MB (mauriceblackburn.com.au) is an Australian plaintiff (claimant-side) law firm. The audience is injured people, their families, and referrers. This is YMYL (Your Money or Your Life) content, so E-E-A-T and compliance are load-bearing, not optional. Practice areas: asbestos and dust diseases, medical negligence, road and transport accident injury, workplace injury and workers compensation, superannuation and TPD claims, class actions, employment and industrial law, abuse law, public liability. Named competitors: Slater and Gordon, Shine Lawyers.

MCP tools (Playwright, SEMrush, BrightEdge, Profound) load at runtime via ToolSearch and are optional. Everything core here runs on the standard tools plus a pasted export fallback.

**Read `reference/mb-page-templates.md` before drafting a service/practice page or a blog/guide page.** It documents the real, live MB page templates (section order, title/meta conventions, CTA cadence, schema gaps, GEO gaps) extracted from 7 production pages on 2026-07-12, so a new page matches house pattern instead of a generic template. It also lists the specific schema and GEO gaps found on those live pages (missing `FAQPage`/`BlogPosting`/`LegalService` schema, thin cited-stats, a double-H1 bug, a page opening with "Table of content") so you can fix the same gaps wherever you spot them, not just avoid repeating them.

## When to Activate

- "Write an SEO page for [practice area / topic]."
- "Optimise this page for search" / "make this page rank."
- "Get us cited in AI answers" / "make this GEO-ready" / "help this show up in ChatGPT or AI Overviews."
- "Rewrite this so it answers the question directly."
- User pastes a draft or URL and asks to improve its SEO or GEO readiness.

## When NOT to Use

- **Validating schema / structured data already live on a page** goes to `seo-analyst-mb` (schema and rich-result validation) and `seo-audit-mb` (full technical audit). This skill writes the schema; those two verify it after publish.
- **Deciding what page to write next** (keyword and topic gaps, competitor coverage) goes to `seo-gap-mb`.
- **Broken links / 404s / redirects** go to the "SEO - 404 Checker" workstream.
- **Social posts** go to `post-writer-mb` / `repurpose-mb`. **Long-form docs / how-tos** go to `documentation-mb`.
- **Competitor brand or digital comparison** goes to `brand-analyst-mb` / `acquisition-dashboard-mb`.
- This skill handles one page at a time. For a batch, run it per page.

## Before You Start

Confirm these before writing. Ask only what is missing (use AskUserQuestion for a clean multi-part ask):

1. **Target page**: a URL to optimise, a file to edit, or a topic to write from scratch.
2. **Practice area**: which of MB's areas, so entity coverage and the pillar link are right.
3. **Page type**: service/practice page or blog/guide. The two have distinct section skeletons, see `reference/mb-page-templates.md`.
4. **Primary query / intent**: the one question or search this page must own (informational vs. "find a lawyer" transactional).
5. **Geography**: Australia-wide or a specific state/territory (jurisdiction changes both compliance hedges and LocalBusiness schema).
6. **Author**: the real MB lawyer or expert to attribute as the schema `author` Person. E-E-A-T needs a named human, not "MB Team."
7. **Paid-tool data**: is a SEMrush/BrightEdge/Profound connector live, or can the user paste a keyword-gap / SERP / AI-citation export? Always support the paste fallback.

If the page exists, fetch and read it first (WebFetch, or Playwright for JS-rendered pages) so you optimise the real copy, not a guess.

## Method

Write for two readers at once: Google's ranking systems and an LLM extracting a citable answer. The GEO layer is not a second pass bolted on. Bake it into the structure from the first sentence.

### Step 1: On-page SEO checklist (traditional ranking)

Every item is a check with a Critical / Warning / Info severity if it fails.

| Check | Requirement | Fail severity |
|---|---|---|
| **Title tag** | Primary entity + intent, front-loaded, <= 60 chars. e.g. `Asbestos Compensation Claims in Victoria \| Maurice Blackburn`. | Critical |
| **Meta description** | 140-160 chars, active voice, includes primary query and a compliant reason to click. Not a duplicate of the H1. | Warning |
| **Single H1** | Exactly one, containing the primary entity. Never zero, never two. | Critical |
| **Heading hierarchy** | Logical H2 > H3 nesting, no skipped levels, headings describe content not decoration. | Warning |
| **Internal links** | Link up to the practice-area **pillar** page and across to related practice pages / relevant case studies. Descriptive anchor text, not "click here". | Warning |
| **Named-entity coverage** | Name the entities a topic model expects: the practice area, relevant AU legislation/schemes (e.g. TAC, WorkCover, Dust Diseases), courts/bodies, locations, MB itself. Coverage, not stuffing. | Warning |
| **Image alt text** | Descriptive, entity-bearing alt on meaningful images. | Info |
| **Canonical** | Self-referential canonical present; no accidental duplicate-URL competition. | Warning |
| **Schema (JSON-LD)** | See Step 3. | Critical if absent on a page type that needs it |

### Step 2: GEO layer (citability by AI answer engines)

Build each of these into the draft as you write. Cite the evidence where you assert why it works.

1. **Answer-first sections.** Open every section with a direct, standalone answer of 40-80 words: state the fact, then support it. An LLM should be able to lift that opening paragraph as a complete answer with no surrounding context. Structuring for retrieval this way, plus citing sources and adding statistics and expert quotations, lifts AI citation roughly 30-40% (Princeton "GEO" study, arXiv 2311.09735). Keyword stuffing hurts.
2. **Self-contained chunks.** Keep each chunk ~120-180 words and self-explanatory. Assume it may be extracted alone.
3. **Question-based headings.** Phrase H2/H3 as the real questions people ask ("How long do I have to make a road accident claim in Victoria?"), so the heading matches the prompt and the answer sits directly beneath it.
4. **Cite original data with attribution.** Where you state a statistic or claim, attribute it to a named study, dataset, or authority. Pages that cite credible sources get cited more themselves. Off-site brand mentions correlate with AI-answer visibility roughly 3:1 over backlinks (Ahrefs 75k-brand study), so earned-media-worthy, quotable facts matter more than on-page tricks. Never fabricate a statistic or a source. If you don't have one, say so and flag it for the author to supply.
5. **Expert quotation.** Include at least one attributed quote from the named MB lawyer/author. Adds E-E-A-T and gives the LLM a citable, human, on-record line.
6. **Freshness.** Set and surface `dateModified` in schema, and reflect a genuine last-reviewed date in visible copy. Stale YMYL content loses trust.
7. **Crawler access.** Confirm robots.txt allows the AI crawlers so the page can be ingested at all: GPTBot, ClaudeBot, PerplexityBot, Google-Extended. If you can reach the site, check with `curl -s https://mauriceblackburn.com.au/robots.txt`. If any are disallowed, flag it Critical: the best GEO copy is worthless if the bot can't fetch it. This is a site-config flag for the author/dev, not something this skill edits.
8. **llms.txt (low priority).** Optionally emit an `/llms.txt` entry for the page. Flag it explicitly as **experimental / forward-compat only**: no measured citation lift yet, a cheap bet, never a primary tactic.

### Step 3: Schema (JSON-LD)

Emit valid `application/ld+json`. Match types to the page:

- **Article / BlogPosting** for editorial/guide pages. `author` MUST be a real `Person` (the named lawyer/expert), plus `publisher` (Organization: Maurice Blackburn), `datePublished`, `dateModified`, `headline`, `mainEntityOfPage`.
- **LegalService** (or **LocalBusiness** for an office/location page) for service and location pages: `name`, `areaServed` (the confirmed AU state/territory or nation), `address` for a physical office, `url`.
- **FAQPage** only where the FAQ is genuine and visible on the page (Google's rule). Each item: `@type: Question` with `name`, and `acceptedAnswer` `@type: Answer` with `text`. Feed the same Q&A into the visible question-based headings from Step 2. This is the same pattern as the "SEO - Road Injury FAQ Schema" workstream: reuse it, don't reinvent it. Never use FAQPage on content that is primarily promotional.
- **BreadcrumbList** where the page sits in a clear hierarchy.

Use `@context: https://schema.org` (https, not http). Schema still matters for GEO: Google AI Mode uses structured data to verify claims. Do not invent field values. `seo-analyst-mb` / `seo-audit-mb` validate this block against the live page after publish.

### Step 4: Compliance gate (HARD, run before returning anything)

This is a pass/fail gate, identical in spirit to `post-grader-mb`, which is the sibling compliance authority. A page can be perfectly optimised and still fail here. **If any check fails, fix it, then re-run the gate. Do not return a draft that fails.**

| Rule | Pass = |
|---|---|
| **Outcome guarantees** | None. No "you will win," "guaranteed compensation," "we always succeed." |
| **Misleading comparative / typical-result claims** | No implying a typical outcome from one case or a cherry-picked figure. No misleading comparisons to competitors. |
| **Absolute legal claims** | No "always" / "never" about the law without a jurisdiction or circumstance hedge. |
| **Trigger / content warning** | Present in visible body copy where the subject is sexual abuse, suicide, or similarly distressing material. |
| **Real client names** | Used only where consent is confirmed on file; otherwise "a client" / anonymised. |
| **Disclaimer + AU jurisdiction (GEO-critical)** | A general-information disclaimer and the relevant jurisdiction (Australia / the specific state) sit in **extractable body copy**, not just a page footer, so an AI answer engine ingests them alongside the answer it lifts. A disclaimer only a human sees at the bottom does not travel with the extracted chunk. |

Use hedged, MB-real conversion language instead of guarantees: "you may be entitled," "understand where you stand," "you have options." For voice, colour, and tone, apply `brand-mb` (MB's Courageous Ally voice, short paragraphs, empathy-first on heavy topics, sourced specifics over superlatives).

### Step 5: Score readiness before returning (MB SEO/GEO Readiness Score)

Grade the draft with this NAMED rubric and FIXED weights so the score is deterministic and comparable run to run. Score each pillar 0-10, multiply by weight, sum to a score out of 100.

| Pillar | Weight | What earns the score |
|---|---|---|
| **Citability (GEO)** | 30% | Answer-first 40-80 word openings; self-contained chunks; question-based headings; extractable disclaimer + jurisdiction. This is the highest weight because it is the reason the skill exists. |
| **Structural readability** | 20% | One H1, clean H2/H3 hierarchy, scannable short paragraphs, logical internal links to pillar + related pages. |
| **Entity & schema** | 20% | Named-entity coverage for the topic + valid, correctly-typed JSON-LD with a real Person author. |
| **Authority / E-E-A-T** | 20% | Named human author, attributed expert quote, cited sources/statistics with attribution, genuine last-reviewed freshness. |
| **Technical** | 10% | Title <= 60 chars with entity+intent, meta description in range, self-canonical, AI crawlers allowed in robots.txt, dateModified set. |

**Gate on top of the score:** compliance (Step 4) is pass/fail and overrides everything. A 95/100 draft that fails compliance does not ship. Report compliance first and separately, then the score.

Report each pillar's 0-10, the weighted contribution, and the total. Target >= 80/100 before returning; if below, state the biggest point-losers and fix them before you hand it back.

## Output

Return, in this order:

1. **One-line summary**: e.g. "Road-accident claims page, VIC, drafted and scored 86/100, compliance PASS."
2. **Compliance result**: PASS / FAIL with every check listed. If FAIL, what was fixed to reach PASS.
3. **Publish-ready page draft**: HTML or markdown (match the user's stack; ask if unclear), with the title tag and meta description called out, single H1, question-based H2/H3, answer-first sections, internal-link placeholders labelled `[pillar: ...]` / `[related: ...]` where the real URL is unknown, and the extractable disclaimer + jurisdiction line in body copy.
4. **JSON-LD block**: the complete `application/ld+json` for the chosen schema types.
5. **Checklist pass-report**: the Step 1 on-page table and the Step 2 GEO items, each marked Pass / Critical / Warning / Info, plus the Step 5 rubric with per-pillar scores and the /100 total.
6. **Optional llms.txt entry**: flagged experimental / low-priority / forward-compat.
7. **Prioritised action plan**: for anything not fixed inline, grouped **Quick Wins / Medium / High Impact**. Note that this backlog can be piped into `brief-ticket-monday-mb` or `brief-ticket-jira-mb`.
8. **Next steps**: after publish, run `seo-audit-mb` (and `seo-analyst-mb`) to validate the live schema and technical setup; use `seo-gap-mb` to decide the next page to write.

## Error Handling

- **Unreachable page (403/timeout/blocked):** do not guess the content. Ask the user to paste the copy, or use Playwright (`browser_navigate` + `browser_snapshot`) to render it.
- **JS-rendered page (empty HTML from curl/WebFetch):** render with Playwright before analysing. You can also spoof an AI-crawler user-agent (GPTBot / PerplexityBot / ClaudeBot / OAI-SearchBot) and diff it against the Googlebot view to see what each bot actually receives.
- **Paywalled / gated source you want to cite:** request the text; never fabricate a quote, statistic, or source.
- **No paid-tool connector:** fall back to a pasted CSV export (SEMrush keyword gap, GSC, Screaming Frog, Ahrefs) and parse it. Never invent keyword volumes or ranking data.
- **Missing author / consent / jurisdiction:** stop and ask. E-E-A-T needs a named author, compliance needs the jurisdiction, and client names need confirmed consent. Do not paper over a gap with a placeholder that could ship.
- **Robots.txt unreachable:** flag the AI-crawler-access check as unverified rather than assuming it passes.

## Cross-links

- `seo-analyst-mb`, `seo-audit-mb`: validate the schema and technical setup after publish.
- `seo-gap-mb`: decide what to write next.
- `brand-mb`: MB brand voice, colour, tone (Courageous Ally).
- `post-grader-mb`: sibling legal-marketing compliance authority; the gate here mirrors it.
- `brief-ticket-monday-mb` / `brief-ticket-jira-mb`, turn the action plan into tickets.
- "SEO - Road Injury FAQ Schema" workstream, the FAQPage pattern reused in Step 3.
- `reference/mb-page-templates.md` (this skill's own folder): the grounded page templates and their real schema/GEO gaps, read before drafting.

No em dashes in any output. Use colons or full stops.
