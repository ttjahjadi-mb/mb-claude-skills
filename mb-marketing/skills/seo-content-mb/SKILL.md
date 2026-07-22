---
name: seo-content-mb
description: Write or optimise a Maurice Blackburn page so it ranks in traditional search AND gets cited by AI answer engines (ChatGPT, Claude, Gemini, Perplexity, Google AI Overviews), with legal-marketing compliance as a hard gate. Always invokes brand-mb first and writes in MB's actual Courageous Ally voice, not generic copy. Treats every chat as a new session, never skips its mandatory questions on the assumption a past chat covered them. States its content-type reasoning (blog vs practice-area page vs localised practice-area page) before drafting, produces a full agency-style Targeting brief (suggested URL/meta title/meta description/H1/keywords table/People Also Asked/internal links, no SERP preview), a YMYL + E-E-A-T alignment summary, an HTML page draft carrying the same metadata block, the JSON-LD schema as its own separate file, and two separate MB-branded docx files (an internal QA report, and a copywriter-facing content brief with the full page copy). Use when the user says "write an SEO page for [practice area]", "optimise this page for search", "make this page rank", "get us cited in AI answers", "write a GEO-ready page", "help this page show up in ChatGPT/AI Overviews", or pastes a draft and asks to SEO/GEO it.
argument-hint: "[URL, file, or topic] [practice area] [geography]"
allowed-tools: Read, Write, Grep, Glob, Bash, WebSearch, WebFetch, AskUserQuestion
---

# SEO Content Writer (MB)

You write or rewrite one Maurice Blackburn page so it earns rankings in traditional search and citations in AI answer engines, and you never ship copy that breaches legal-marketing rules.

MB (mauriceblackburn.com.au) is an Australian plaintiff (claimant-side) law firm. The audience is injured people, their families, and referrers. This is YMYL (Your Money or Your Life) content, so E-E-A-T and compliance are load-bearing, not optional. Practice areas: asbestos and dust diseases, medical negligence, road and transport accident injury, workplace injury and workers compensation, superannuation and TPD claims, class actions, employment and industrial law, abuse law, public liability. Named competitors: Slater and Gordon, Shine Lawyers.

MCP tools (Playwright, SEMrush, BrightEdge, Profound) load at runtime via ToolSearch and are optional. Everything core here runs on the standard tools plus a pasted export fallback.

**Read `reference/mb-page-templates.md` before drafting a service/practice page or a blog/guide page.** It documents the real, live MB page templates (section order, title/meta conventions, CTA cadence, schema gaps, GEO gaps, robots.txt/sitemap.xml grounding, site inventory by section) extracted from live production pages, so a new page matches house pattern instead of a generic template, and so Internal Links and Suggested URL in the Targeting brief (below) are real, not invented.

**MANDATORY, before writing a single word of body copy: invoke the `brand-mb` skill and read its `tone-of-voice.md` and `brand-guidelines.md`.** This was previously only a passing mention buried in the compliance section, and a real run produced generic, off-brand copy as a result, do not repeat that. Every page this skill drafts must sound like MB, not a generic assistant:
1. Invoke `brand-mb`, read `tone-of-voice.md` for the Courageous Ally voice, house-style mechanics (contractions fine, active voice, numbers spelled one-nine / numerals from 10, Australian English), and read `brand-guidelines.md` for colours/type if the deliverable touches visual styling.
2. Read `brand-mb/reference/legal-marketing-guardrails.md` alongside this skill's own Step 5 compliance gate below, they overlap, both apply.
3. If `brand-mb` cannot be loaded for any reason, say so explicitly before drafting, do not silently fall back to a generic voice and present it as on-brand.

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

**Treat every new chat as a brand new session, even if a previous conversation covered this exact page, topic, or practice area.** Never skip a mandatory question below because a past chat seems to have already answered it. Past chat history (this session's own earlier turns, or anything referenced from another conversation) is background context only, useful for relevancy, never a substitute for confirming the inputs below in this run. If prior context strongly suggests an answer, state the assumption and confirm it with the user rather than silently reusing it.

Confirm these before writing. Ask only what is missing within this session (use AskUserQuestion for a clean multi-part ask):

1. **Target page**: a URL to optimise, a file to edit, or a topic to write from scratch.
2. **Practice area**: which of MB's areas, so entity coverage and the pillar link are right.
3. **Content type**: do not just ask this as a binary. See Step 0 below, it is a reasoned decision (blog vs practice-area page vs localised practice-area page), stated explicitly before drafting, not assumed.
4. **Primary query / intent**: the one question or search this page must own (informational vs. "find a lawyer" transactional).
5. **Geography**: Australia-wide or a specific state/territory (jurisdiction changes compliance hedges, LocalBusiness schema, and the Step 0 decision).
6. **Author**: the real MB lawyer or expert to attribute as the schema `author` Person. E-E-A-T needs a named human, not "MB Team."
7. **Paid-tool data (MANDATORY, all four tools, equal standing, asked in the same turn):** before writing, ask about all four of the following, every time, with no exceptions:
   - **SEMrush**: live connector, or a keyword/SERP export to paste?
   - **BrightEdge**: live connector, or a Data Cube / rankings export to paste?
   - **Profound**: live connector (MB is on the Enterprise/API tier), or an AI-citation / Share-of-Voice export to paste?
   - **Google Search Console (GSC)**: an export of queries/impressions for this topic?

   **Hard rules, this has failed in practice by being silently watered down, do not repeat that:**
   - All four tool names must literally appear in the question you send, in the same message, not split across separate replies and not with some deferred to "if you have time."
   - **Never rank, prioritise, or editorialise which of the four matters more** ("GSC and SEMrush are most useful, BrightEdge/Profound are a nice-to-have/bonus/not a blocker" is exactly the failure mode to avoid). All four are equally mandatory to ask about. The user's own answer, not your guess, decides which data ends up used.
   - If the topic or page seems to make one tool obviously irrelevant, still ask, do not silently drop it because you've reasoned it away.
   - Before sending the question, check the literal text you are about to send: if "SEMrush", "BrightEdge", "Profound", and "GSC" do not all four appear in it, rewrite it before sending, do not send a partial question.
   - If the user answers for only one or two tools unprompted, explicitly ask about the remaining ones before moving on. A partial answer is not a complete one.
   - **Ask this every single time the skill runs, with zero exceptions, by default.** Never assume. Do not skip it because this session already asked for a different page, because the user answered "no" for one tool earlier in this conversation, because the topic looks similar to one already covered, or for any other reason. Every new page, every new run, the full four-tool question again, fresh, even if the realistic answer is "same as last time."
   - Always support the paste fallback for any of them. This data sharpens the title/entity targeting, the Keywords section of the Targeting brief, and the GEO angle.

If the page exists, fetch and read it first (WebFetch, or Playwright for JS-rendered pages) so you optimise the real copy, not a guess.

## Method

Write for two readers at once: Google's ranking systems and an LLM extracting a citable answer. The GEO layer is not a second pass bolted on. Bake it into the structure from the first sentence.

### Step 0: Content-type decision (state the reasoning before drafting, do not skip this)

Before writing a word of copy, decide and **state in the Output, as its own labelled section**, which of these three content types this page should be, and why. Never silently assume, and never let the user's initial phrasing decide it without a check, they may ask for "a page about X" without knowing which type actually fits.

1. **Blog / guide.** Choose when the primary intent is informational or educational: a question ("how do I...", "what is...", "considerations before..."), a news hook (a legislation change, a case update), or a topic that feeds top-of-funnel awareness and links down to a money page. Not itself the primary conversion page for a practice area.
2. **Practice-area page (core / pillar).** Choose when the intent is transactional ("find a lawyer for X") and the practice area does not yet need, or does not have, meaningfully different local demand or jurisdiction rules that would justify a dedicated state page. This is the primary money page for the practice area.
3. **Localised practice-area page.** Choose only when at least one of these is true: (a) there is real, meaningful state/city-level search volume and intent ("workers compensation lawyer Melbourne"), (b) the jurisdiction's scheme or law genuinely differs from the core page's content (e.g. TAC in VIC vs CTP schemes elsewhere), or (c) MB has a physical office presence there worth surfacing via LocalBusiness schema and the local pack. **Do not create a localised page that would be near-duplicate content of the core page with only the location swapped and no real local differentiation**, that risks cannibalisation and duplicate-content dilution. In that case, fold location targeting into the core page's internal linking and LocalBusiness schema instead of forking a new page.

State the decision in 2-4 sentences citing which specific criteria applied (e.g. "Localised practice-area page: WorkCover is a Victoria-specific statutory scheme (criterion b), and MB has a Melbourne office to surface (criterion c)."). If the user's original ask conflicts with this reasoning, say so and recommend the better fit before proceeding, do not silently override or silently comply.

### Step 1: On-page SEO checklist (traditional ranking)

Every item is a check with a Critical / Warning / Info severity if it fails.

| Check | Requirement | Fail severity |
|---|---|---|
| **Title tag** | Primary entity + intent, front-loaded, <= 60 chars. e.g. `Asbestos Compensation Claims in Victoria \| Maurice Blackburn`. | Critical |
| **Meta description** | 140-160 chars, active voice, includes primary query and a compliant reason to click. Not a duplicate of the H1. | Warning |
| **Single H1** | Exactly one, containing the primary entity. Never zero, never two. | Critical |
| **Heading hierarchy** | Logical H2 > H3 nesting, no skipped levels, headings describe content not decoration. | Warning |
| **Internal links** | Link up to the practice-area **pillar** page and across to related practice pages / relevant case studies. Descriptive anchor text, not "click here". Real URLs from `reference/mb-page-templates.md`'s site inventory, feeds the Targeting brief's Internal Links section. | Warning |
| **Named-entity coverage** | Name the entities a topic model expects: the practice area, relevant AU legislation/schemes (e.g. TAC, WorkCover, Dust Diseases), courts/bodies, locations, MB itself. Coverage, not stuffing. | Warning |
| **Image alt text** | Descriptive, entity-bearing alt on meaningful images. | Info |
| **Canonical** | Self-referential canonical present; no accidental duplicate-URL competition. | Warning |
| **Schema (JSON-LD)** | See Step 4. Delivered as its own file, see Output. | Critical if absent on a page type that needs it |

### Step 2: GEO layer (citability by AI answer engines)

Build each of these into the draft as you write. Cite the evidence where you assert why it works.

1. **Answer-first sections.** Open every section with a direct, standalone answer of 40-80 words: state the fact, then support it. An LLM should be able to lift that opening paragraph as a complete answer with no surrounding context. Structuring for retrieval this way, plus citing sources and adding statistics and expert quotations, lifts AI citation roughly 30-40% (Princeton "GEO" study, arXiv 2311.09735). Keyword stuffing hurts.
2. **Self-contained chunks.** Keep each chunk ~120-180 words and self-explanatory. Assume it may be extracted alone.
3. **Question-based headings.** Phrase H2/H3 as the real questions people ask ("How long do I have to make a road accident claim in Victoria?"), so the heading matches the prompt and the answer sits directly beneath it. These double as candidates for the Targeting brief's People Also Asked section.
4. **Cite original data with attribution.** Where you state a statistic or claim, attribute it to a named study, dataset, or authority. Pages that cite credible sources get cited more themselves. Off-site brand mentions correlate with AI-answer visibility roughly 3:1 over backlinks (Ahrefs 75k-brand study), so earned-media-worthy, quotable facts matter more than on-page tricks. Never fabricate a statistic or a source. If you don't have one, say so and flag it for the author to supply.
5. **Expert quotation.** Include at least one attributed quote from the named MB lawyer/author. Adds E-E-A-T and gives the LLM a citable, human, on-record line.
6. **Freshness.** Set and surface `dateModified` in schema, and reflect a genuine last-reviewed date in visible copy. Stale YMYL content loses trust.
7. **Crawler access.** Confirm robots.txt allows the AI crawlers so the page can be ingested at all: GPTBot, ClaudeBot, PerplexityBot, Google-Extended. Check with `curl -s https://www.mauriceblackburn.com.au/robots.txt` (canonical URL is `www`, the bare domain 301s to it). Verified 2026-07-22: MB's robots.txt is a wildcard `User-agent: *` / `Allow: /` with no bot-specific rules, so AI crawlers are allowed by default. It disallows only a handful of legacy language paths (`/es/`, `/ar/`, `/fa/`, `/it/`, `/vi/`, `/zh_cn/`, `/el/`), two specific PDFs, and `/partnerships/`. Re-check live rather than trusting this note stays current, but a Critical finding here would be a real change, not the expected baseline. Two `Sitemap:` lines are listed (`sitemap.xml` and `mb.sitemap.xml`), the second 301s to the first, there is only one real sitemap.
8. **Sitemap membership.** Confirm the page will be (or already is) listed in `https://www.mauriceblackburn.com.au/sitemap.xml`, a flat `urlset` (not an index), ~1,443 URLs as of 2026-07-22. New pages should appear here once published; a money page missing from it is a real gap. For context, the sitemap's rough shape by section: `/blog` (586 URLs, the largest section), `/our-lawyers` (291), `/media-centre` (198), `/class-actions` (140), `/injury-illness` (87, most of the practice/service pages this skill writes), `/our-offices` (35). A handful of older `/personal-injury-lawyers-{vic,qld,wa}/` URLs also exist, a different, smaller legacy pattern, do not copy that structure for new pages, use `reference/mb-page-templates.md`'s `/injury-illness/{pillar}/{keyword}-{location}/` pattern instead.
9. **llms.txt (low priority).** Optionally emit an `/llms.txt` entry for the page. Flag it explicitly as **experimental / forward-compat only**: no measured citation lift yet, a cheap bet, never a primary tactic.

### Step 3: YMYL + E-E-A-T Alignment (its own labelled deliverable, not just folded into other checks)

Report this as a distinct section in the Output, one line per pillar, each stating what the draft actually does, not just a restated definition. This is a pass/gap read, not a score, so a reviewer can see exactly what is satisfied and what still needs the author's input.

- **YMYL classification.** State plainly that this is YMYL content and what is materially at stake for the reader (a compensation claim, a legal deadline, a financial entitlement).
- **Experience.** Does the draft reflect real practical process knowledge (what actually happens, step by step, in a claim of this kind) rather than a generic textbook description? Flag it as a gap if it reads generic.
- **Expertise.** A named lawyer/author with a real credential (role, and years practising or admission detail if known) attributed as the schema `author` `Person`, plus the expert quote from Step 2.
- **Authoritativeness.** Named legislation/scheme cited (e.g. the Workplace Injury Rehabilitation and Compensation Act 2013 (Vic)), external sources/statistics cited with attribution, MB's own entity signals present (Organization schema, real office/NAP where relevant).
- **Trustworthiness.** The disclaimer + jurisdiction sit in extractable body copy (not just a footer), a genuine last-reviewed date is shown, no fabricated statistic or review count anywhere, and the copy is transparent about what MB does and does not cover.

If any pillar has a real gap (most commonly Experience or Authoritativeness on a first draft), say so plainly in this section rather than scoring around it, this is what `seo-content-mb` exists to catch before publish, not paper over.

### Step 4: Schema (JSON-LD), delivered as its own file

Emit valid `application/ld+json`. Match types to the page:

- **Article / BlogPosting** for editorial/guide pages. `author` MUST be a real `Person` (the named lawyer/expert), plus `publisher` (Organization: Maurice Blackburn), `datePublished`, `dateModified`, `headline`, `mainEntityOfPage`.
- **LegalService** (or **LocalBusiness** for an office/location page, or where Step 0 chose a localised practice-area page) for service and location pages: `name`, `areaServed` (the confirmed AU state/territory or nation), `address` for a physical office, `url`.
- **FAQPage** only where the FAQ is genuine and visible on the page (Google's rule). Each item: `@type: Question` with `name`, and `acceptedAnswer` `@type: Answer` with `text`. Feed the same Q&A into the visible question-based headings from Step 2, and into the Targeting brief's People Also Asked section. This is the same pattern as the "SEO - Road Injury FAQ Schema" workstream: reuse it, don't reinvent it. Never use FAQPage on content that is primarily promotional.
- **BreadcrumbList** where the page sits in a clear hierarchy.

Use `@context: https://schema.org` (https, not http). Schema still matters for GEO: Google AI Mode uses structured data to verify claims. Do not invent field values. `seo-analyst-mb` / `seo-audit-mb` validate this block against the live page after publish.

**Always write this schema to its own standalone file** (e.g. `<slug>.schema.json`, valid JSON only, nothing else in the file) via `Write`, so it can be handed to a developer or pasted into AEM without extracting it from a docx or chat message. Reference the file path in the docx and in the checklist pass-report, do not only show it inline as a code block.

### Step 5: Compliance gate (HARD, run before returning anything)

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

### Step 6: Score readiness before returning (MB SEO/GEO Readiness Score)

Grade the draft with this NAMED rubric and FIXED weights so the score is deterministic and comparable run to run. Score each pillar 0-10, multiply by weight, sum to a score out of 100.

| Pillar | Weight | What earns the score |
|---|---|---|
| **Citability (GEO)** | 25% | Answer-first 40-80 word openings; self-contained chunks; question-based headings; extractable disclaimer + jurisdiction. |
| **Structural readability** | 15% | One H1, clean H2/H3 hierarchy, scannable short paragraphs, logical internal links to pillar + related pages. |
| **Entity & schema** | 15% | Named-entity coverage for the topic + valid, correctly-typed JSON-LD with a real Person author, delivered as its own file. |
| **Authority / E-E-A-T** | 20% | The Step 3 YMYL + E-E-A-T Alignment read: named human author, attributed expert quote, cited sources/statistics with attribution, genuine last-reviewed freshness. |
| **Technical** | 10% | Title <= 60 chars with entity+intent, meta description in range, self-canonical, AI crawlers allowed in robots.txt, dateModified set. |
| **Brief completeness** | 15% | Step 0 content-type reasoning stated; Targeting brief fully populated (Suggested URL, Meta Title, H1, Meta Description, Keywords table, People Also Asked, Internal Links); the HTML file carries the same metadata block, not just raw copy; schema delivered as its own file; both docx files (report and brief) delivered separately. |

**Gate on top of the score:** compliance (Step 5) is pass/fail and overrides everything. A 95/100 draft that fails compliance does not ship. Report compliance first and separately, then the score.

Report each pillar's 0-10, the weighted contribution, and the total. Target >= 80/100 before returning; if below, state the biggest point-losers and fix them before you hand it back.

## Output

Return, in this order:

1. **One-line summary**: e.g. "Localised practice-area page, workers compensation, Melbourne, drafted and scored 86/100, compliance PASS."
2. **Content-type decision** (Step 0): the 2-4 sentence reasoning for blog vs practice-area page vs localised practice-area page.
3. **Compliance result**: PASS / FAIL with every check listed. If FAIL, what was fixed to reach PASS.
4. **Targeting brief.** A single labelled section with exactly these fields, in this order (matches MB's existing agency brief format, no SERP Preview, that field is dropped):
   - **Suggested URL**: the real, full URL following `reference/mb-page-templates.md`'s pattern for the chosen content type.
   - **Suggested Meta Title**
   - **Suggested H1**
   - **Suggested Meta Description**
   - **Keywords**: a table, Primary/Secondary column plus the keyword and its search volume in parentheses if sourced from a live connector or a pasted export (per Before You Start item 7). If no data source was provided, list the keywords without a fabricated number and state "search volume unavailable, no connector or export provided this run."
   - **People Also Asked**: a bullet list of real PAA-style questions. Source via `WebSearch` on the primary query where possible. If live PAA data cannot be confirmed, generate plausible candidates from the Step 2 question-based headings and label them clearly as **"suggested, not sourced from live PAA data."** Never present a guessed question as if it were pulled from a real PAA box.
   - **Internal Links**: a bullet list of real candidate MB URLs only, pulled from `reference/mb-page-templates.md`'s site inventory and matched to the practice area/content type. Never invent a URL.
5. **YMYL + E-E-A-T Alignment** (Step 3): the pillar-by-pillar pass/gap read.
6. **Publish-ready page draft.** Deliver as an **HTML file** (`<slug>.html`): the full page markup PLUS a metadata block at the top of the file (Meta Title, Meta Description, Keywords as a Primary/Secondary table, People Also Asked as a bullet list, Internal Links as a bullet list, mirroring the Targeting brief exactly), then the page body itself. Single H1, question-based H2/H3, answer-first sections, internal links using the real URLs from the Targeting brief, and the extractable disclaimer + jurisdiction line in body copy. This file is the layout/visual overview, it must be complete on its own, not just raw copy with the brief fields left out.
7. **JSON-LD schema file**: `<slug>.schema.json`, its own standalone file, written per Step 4, path stated. Never inline it only in chat, the HTML, or either docx below.
8. **Two separate docx files, not one combined document:**
   - **Document 1, the report** (`<slug>-report.docx`): compliance result, checklist pass-report (Step 1 + Step 2 items), the Step 6 rubric with per-pillar scores and the /100 total, and the prioritised action plan. This is the internal QA record, no page copy in it.
   - **Document 2, the full SEO content brief** (`<slug>-brief.docx`): mimics the real agency brief format the user shared (a "Targeting" section followed by the full page copy). Include, as sections: the Targeting brief fields exactly as in item 4 above, the YMYL + E-E-A-T Alignment read, then the full page copy itself (each H2 as its own docx section, body paragraphs matching the drafted copy). This is the copywriter-facing, version-controllable deliverable, it must contain the real page copy, not just metadata.
   Build both via `scripts/render_mb_docx.py` (MB logo in the header): `/usr/bin/python3 scripts/render_mb_docx.py <input.json> <slug>-report.docx` and a second run for `<slug>-brief.docx`. Tell the user both saved file paths, and the HTML file path from item 6, and the schema file path from item 7, four files total.
9. **Optional llms.txt entry**: flagged experimental / low-priority / forward-compat.
10. **Prioritised action plan**: for anything not fixed inline, grouped **Quick Wins / Medium / High Impact**. Note that this backlog can be piped into `brief-ticket-monday-mb` or `brief-ticket-jira-mb`.
11. **Next steps**: after publish, run `seo-audit-mb` (and `seo-analyst-mb`) to validate the live schema and technical setup; use `seo-gap-mb` to decide the next page to write.

## Error Handling

- **Unreachable page (403/timeout/blocked):** do not guess the content. Ask the user to paste the copy, or use Playwright (`browser_navigate` + `browser_snapshot`) to render it.
- **JS-rendered page (empty HTML from curl/WebFetch):** render with Playwright before analysing. You can also spoof an AI-crawler user-agent (GPTBot / PerplexityBot / ClaudeBot / OAI-SearchBot) and diff it against the Googlebot view to see what each bot actually receives.
- **Paywalled / gated source you want to cite:** request the text; never fabricate a quote, statistic, or source.
- **No paid-tool connector:** fall back to a pasted CSV export (SEMrush keyword gap, GSC, Screaming Frog, Ahrefs) and parse it. Never invent keyword volumes or ranking data, and never invent a search-volume figure for the Targeting brief's Keywords section.
- **People Also Asked not obtainable via WebSearch:** fall back to Step 2's question-based headings as candidates and label them "suggested, not sourced from live PAA data," never present a guess as sourced fact.
- **Missing author / consent / jurisdiction:** stop and ask. E-E-A-T needs a named author, compliance needs the jurisdiction, and client names need confirmed consent. Do not paper over a gap with a placeholder that could ship.
- **Robots.txt unreachable:** flag the AI-crawler-access check as unverified rather than assuming it passes.
- **Content-type decision conflicts with the user's original ask (Step 0):** say so and recommend the better fit; do not silently override the user, and do not silently comply with a weaker choice either.

## Cross-links

- `seo-analyst-mb`, `seo-audit-mb`: validate the schema and technical setup after publish.
- `seo-gap-mb`: decide what to write next.
- `brand-mb`: invoked mandatorily before drafting, source of MB's Courageous Ally voice, colours, tone, and the legal-marketing guardrails file.
- `post-grader-mb`: sibling legal-marketing compliance authority; the gate here mirrors it.
- `brief-ticket-monday-mb` / `brief-ticket-jira-mb`, turn the action plan into tickets.
- "SEO - Road Injury FAQ Schema" workstream, the FAQPage pattern reused in Step 4.
- `reference/mb-page-templates.md` (this skill's own folder): the grounded page templates, URL patterns, and site inventory, read before drafting and before writing the Targeting brief.

No em dashes in any output. Use colons or full stops.
