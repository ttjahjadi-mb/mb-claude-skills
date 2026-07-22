# MB Page Templates (grounded in live pages, 2026-07-12)

Source of truth for `seo-content-mb`. Extracted from 7 live mauriceblackburn.com.au pages: 4 service/practice pages, 3 blog guides. Real findings only, no assumptions. Update this file if the live pattern changes.

Analyzed:
- Service pages: TPD claims (Melbourne), car accident claims (Melbourne), workers' compensation (Melbourne), submitting a WorkCover claim (VIC how-to)
- Blog guides: TAC claims guide, searching for a will, 7 things before a road injury claim

Note: MB's CDN can serve a stale/mismatched cached page under concurrent fetches. Always fetch pages one at a time and verify the returned `<title>`/canonical matches the requested URL before trusting the content.

## Site inventory: robots.txt and sitemap.xml (verified 2026-07-22)

- **robots.txt**: `https://www.mauriceblackburn.com.au/robots.txt` (canonical is `www`, bare domain 301s to it). A wildcard `User-agent: *` / `Allow: /`, no bot-specific rules, so AI crawlers (GPTBot, ClaudeBot, PerplexityBot, Google-Extended) are allowed by default, do not flag a missing per-bot line as a gap. Disallows: a handful of legacy language paths (`/es/`, `/ar/`, `/fa/`, `/it/`, `/vi/`, `/zh_cn/`, `/el/`), two specific PDFs, and `/partnerships/`. Lists two `Sitemap:` lines, `sitemap.xml` and `mb.sitemap.xml`, the second 301s to the first, there is only one real sitemap.
- **sitemap.xml**: `https://www.mauriceblackburn.com.au/sitemap.xml`, a flat `urlset` (not a sitemap index), ~1,443 URLs. Rough shape by top-level path: `/blog` (586, the largest section), `/our-lawyers` (291, lawyer bio pages), `/media-centre` (198), `/class-actions` (140), `/injury-illness` (87, the practice/service pages this skill's templates above are drawn from), `/our-offices` (35), `/our-people` (18), `/wills` (13), `/campaign` (13), `/employment-issues` (12), `/social-justice` (8), `/insurance-claims-disputes` (7), `/free-claim-check` (6).
- **Legacy URL pattern found, do not copy it.** A small number of `/personal-injury-lawyers-{vic,qld,wa}/...` URLs also exist in the sitemap (8 total), a different, older pattern than the `/injury-illness/{pillar}/{keyword}-{location}/` structure documented above. Treat these as legacy, not a second valid template.

---

## 1. Service / practice-area page template

**URL pattern:** `/injury-illness/{pillar}/{keyword}-{location}/`, trailing slash, self-canonical. `{pillar}` is one of `road-injury`, `work-injury`, `superannuation-insurance-claims`, etc.

**Title:** `{Service} {Location} | {Maurice Blackburn or value-prop}`. Real range 45-63 chars, aim ≤60.

**Meta description:** 142-158 chars. Benefit-led, opens with "Our expert/Melbourne lawyers..." or a scenario ("If your life was altered..."). Closes with the branded string **"Free Online Claim Check ✓"** on every page except how-to guides.

**H1:** exactly one, `{service} {location}`. (Live bug found on the TPD page: a stray second H1 "Take your free claim check today" existed alongside the real one. Do not replicate. Enforce single H1.)

**Section skeleton (consistent order across all 4 pages):**
1. Breadcrumb (Home > pillar > sub-pillar > page), also emitted as JSON-LD
2. Hero: H1 + short intro + primary CTA button + phone
3. "What's on this page" jump-nav (in-page anchors)
4. Intro / value proposition H2 ("Expert legal support for X in {location}")
5. Trust strip: 3 repeating H3 cards ("No Win, No Fee claims", "Client-focused support", "Offices across Victoria")
6. Educational body: "What is X?", "Who is eligible?", "Your rights and entitlements", "Types of claims covered", "Benefits/compensation"
7. Process block: H2 "The X claim process" with numbered H3 steps (1. Find out if you have a claim -> 2. We manage it -> 3. Receive payment/treatment)
8. Why Maurice Blackburn / track record
9. FAQ: H2 "Frequently Asked Questions about X", 5-13 question-form H3s
10. Client story (named case study, e.g. Teresa's story)
11. Reviews strip: "over 3,000 five-star reviews" (present on 3 of 4)
12. Related practice links back to pillar pages
13. Primary end CTA block
14. Local-office selector: "Select your state below"

**Body length:** ~3,700-5,400 words of real content.

**CTA pattern:**
- Primary: **"Free Online Claim Check"** linking to a practice-scoped funnel `/free-claim-check/{pillar}/`. Repeated 8-22x per page.
- Phone: national `1800 111 222` + a practice-specific number, 7-12 `tel:` links per page.
- Morry live chat wired in throughout (~20 refs per page).
- 3 forms per page: claim-check, contact, office-locator.
- Cadence: hero, mid-page after process, dedicated end block, office selector. Top/middle/bottom, not just one CTA.

**Internal linking:** the full practice-area mega-menu renders on every page (~167-171 `/injury-illness/` links, ~83 unique), sitewide siloing to all pillars, not just the current one. Contextual related-practice cards link up to the parent pillar.

**Schema shipped today (the gap to close):**
- All 4: `BreadcrumbList` only, as the baseline.
- 1 of 4 (car accident page): adds `FAQPage`.
- **Missing on every page despite the content existing:** `FAQPage` (3 of 4 have a visible FAQ with no schema), `LegalService`/`LocalBusiness` (despite location targeting + office data), `AggregateRating` (despite the "3,000 five-star reviews" claim), `Person`/author.
- When writing a new or updated service page: always ship `BreadcrumbList` + `FAQPage` (if there's an FAQ section) + `LegalService`/`LocalBusiness` + `AggregateRating` if a real review count is sourced. Never invent a rating number, use the real, current figure.

**GEO readiness (real gaps found):**
- Direct-answer opening: partial. 3 of 4 pages open the body with a scenario-then-answer paragraph. One page (workers' comp) opens with literally "Table of content" as the first line of body text after H1, no answer at all. Never do this: always open with one direct-answer sentence.
- Question-based headings: strong already (FAQ + several body H3s are natural questions). Keep this.
- Jurisdiction in body: strong already (Victoria/VIC/Melbourne/Australia all stated 9-61x per page). Keep this.
- Named stats/sources: weak. Only one or two numeric claims across all 4 pages ("over 100 years", one `$160,000` figure), no cited external sources, no legislation citations, no dates. This is the single biggest GEO opportunity: add 2-3 cited, dated stats or legislation references per page (Princeton GEO paper: citing sources/stats/quotes lifts AI-citation ~30-40%).
- E-E-A-T: weak. No "last updated"/"reviewed by" date on any service page, no author byline, no "Accredited Specialist" mention. Lawyer name-cards where present are thin (name only, no credential). Add a dated "Reviewed by {lawyer name}, {credential}" line near the top.

---

## 2. Blog / guide page template

**URL pattern:** `/blog/{practice-topic}/{descriptive-kebab-slug}/`, trailing slash, topic segment matches the blog taxonomy (`road-injury`, `wills-estates`, etc). No dates or IDs in the slug.

**Title:** `{Descriptive headline} | Maurice Blackburn [Lawyers]`. Real range 52-77 chars.

**Meta description:** 143-149 chars, benefit/question-led ("Learn how...", "Searching for a Will? Discover where to look...").

**H1:** present, may legitimately differ in wording from the `<title>` tag (one real example: title says "Searching for a Will? Where to Start in Australia", H1 says "Searching for a Will? Here's where to start"). This divergence is acceptable house style, keep it intentional not accidental.

**Byline (E-E-A-T, done well here, unlike service pages):** "By {Named lawyer}, {Role}" linking to their `/our-lawyers/{slug}/` bio, plus "Last updated {D Month YYYY}" visible near the top. This is the one place MB already does author E-E-A-T right, replicate this pattern on service pages too.

**Section skeleton:**
1. Breadcrumb (also JSON-LD)
2. H1
3. Author byline + last-updated date
4. H2 "In summary": answer-first TL;DR, always the first section, with inline links to the relevant service/practice page
5. Body H2 topic sections with H3 sub-steps (how-to guides use step H3s, listicles use numbered H3s: "1. ... " through "7. ...")
6. Soft-conversion section mid/late ("Need help with...", "We're here to help")
7. FAQ section (present on 2 of 3 analyzed, both road-injury topics; absent on the wills piece): H2 "Frequently asked questions [about X]", 5 question-form H3s
8. Lead-gen contact block: "We're here to help, get in touch" form + phone + state selector
9. Related articles: 4 sibling-blog cards under the same `/blog/{topic}/` hub

**Lists/tables:** heavy use of bullet lists (60-65 per page including nav), some numbered lists, **zero tables found across all 3 pages**. Comparison data (e.g. "what's covered vs not covered") is currently written as prose/lists, not tables. Adding a genuine comparison table where the content is naturally tabular is a real GEO opportunity, not currently done.

**Internal linking / funnel:** two distinct link types: in-body conversion links from "In summary" and body prose pointing to the matching service/practice page (e.g. `/injury-illness/road-injury/tac-claims-lawyers.html`) and sitewide `/free-claim-check/` + `/get-in-touch/`; plus related-content links to sibling blogs. This is how blog content funnels into the conversion pages above, always include at least one in-body link to the matching practice page.

**Word count:** roughly 1,000-2,000 words. Listicles and how-to guides land shorter (~1,000-1,200), narrative guides longer (~1,200-2,000).

**Schema shipped today (the gap to close):** **all 3 pages ship exactly one JSON-LD block, `BreadcrumbList`. Nothing else.** Specifically missing despite the content existing: `Article`/`BlogPosting`, `FAQPage` (even on the 2 pages with a visible FAQ section), `Person` author (author only exists as a visible byline, not in schema), `datePublished`/`dateModified` in schema (dates exist only in a JS data layer and as visible text, not machine-readable). `og:type` is `website`, should be `article` for blog posts.

When writing or updating a blog/guide page: always ship `BreadcrumbList` + `BlogPosting` (with `author` as a `Person` matching the visible byline, and `datePublished`/`dateModified`) + `FAQPage` if there's an FAQ section.

**GEO readiness (real gaps found):**
- Direct-answer opening: strong already, every page opens with "In summary". Keep this, and consider bringing it to service pages too.
- Question-based headings: strong already.
- Standalone-answerable chunks: strong already, H3 sub-sections are self-contained ~120-180 words.
- Jurisdiction in body: strong already.
- Named authors with role + bio link: strong already (the best E-E-A-T signal MB has, visible-only though, not in schema).
- Named stats/sources: weak, same gap as service pages. Content is explanatory, not citation-backed. No external sources, no dated statistics.
- No comparison tables: real gap, tabular content is more extractable by both search and AI than prose lists.

---

## 3. Cross-cutting rules for `seo-content-mb` to apply on every draft

1. **Ship the schema that matches what's already on the page.** The single biggest, cheapest lift across both templates is: if there's a visible FAQ section, ship `FAQPage`. If it's a blog post, ship `BlogPosting` with `Person` author + real dates. If it's a service page, ship `LegalService`/`LocalBusiness`. None of these require new content, only marking up what's already there.
2. **Add 2-3 cited, dated stats or legislation references** per page, this is the single biggest content-side GEO gap on both templates and the one the Princeton GEO paper (arxiv 2311.09735) validates as a 30-40% citation lift.
3. **Add a dated "Reviewed by {lawyer}, {credential}" line** on service pages (blogs already do this via the byline, replicate it there).
4. **Every section opens with one direct-answer sentence.** Never open a page or section with structural text like "Table of content" and nothing else.
5. **Never invent a stat, rating count, or credential.** If the real figure (review count, years of experience, settlement figure) isn't provided, flag it as missing rather than guessing.
6. **Single H1 per page.** Check for the double-H1 bug pattern before shipping.
7. Where the content is naturally tabular (coverage comparisons, eligibility criteria, timelines), use a real `<table>`, not another bullet list.
