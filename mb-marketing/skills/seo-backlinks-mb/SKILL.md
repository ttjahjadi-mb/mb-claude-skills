---
name: seo-backlinks-mb
description: Audit Maurice Blackburn's backlink profile, flag toxic links, find the competitor link gap, and build a prioritised outreach list. Produces a backlink health report scored by Domain Rating tiers, a reviewed disavow-candidate list (always held for human sign-off, never auto-submitted), and a ranked outreach prospect list. Use when the user asks "audit our backlinks / backlink profile", "how healthy is our link profile", "do we have toxic / spammy / bad links", "should we disavow", "build a disavow file", "who links to Slater and Gordon / Shine but not us", "backlink gap analysis", "find link-building / outreach targets", or "digital PR prospect list". Default competitors: Slater and Gordon, Shine Lawyers.
argument-hint: [MB domain + competitor(s), plus a backlink CSV export path if available (Ahrefs/SEMrush/BrightEdge)]
allowed-tools: Read, Write, Grep, Glob, Bash, WebFetch, AskUserQuestion
---

# MB Backlink Profile Auditor

Audit Maurice Blackburn's off-site link profile, separate the healthy links from the toxic ones, find the domains linking to competitors but not to MB, and turn all of it into a defensible disavow-candidate list and a ranked outreach plan. Default competitors: Slater and Gordon, Shine Lawyers. Accept any others the user names. Backlinks are a YMYL trust signal for MB, so this is a quarterly audit, not a one-off.

MCP tools (SEMrush, DataForSEO, Playwright) are not in `allowed-tools` above because they load at runtime via ToolSearch. Fetch a tool's schema with `ToolSearch` (e.g. `select:mcp__playwright__browser_navigate`) before calling it. This job usually needs a human-provided backlink CSV export: parse that as the default path (see Before You Start and Data sourcing).

## When to Activate

- "Audit our backlinks" / "how healthy is our backlink profile" / "backlink health report."
- "Do we have toxic / spammy / bad / low-quality links" / "is our profile clean."
- "Should we disavow anything" / "build a disavow file" / "review our disavow list."
- "Who links to Slater and Gordon / Shine but not us" / "backlink gap" / "link intersect."
- "Find link-building targets" / "outreach / digital PR prospect list" / "who should we pitch."

## When NOT to Use

- On-page schema / JSON-LD / rich-result validation, crawlability, Core Web Vitals, index hygiene on MB's own pages: that is `seo-audit-mb` (which absorbs the old `seo-analyst-mb` schema logic).
- The keyword / topic / Share-of-Voice / Share-of-Model competitor teardown: that is `seo-competitor-mb`. This skill is the off-site link layer only, not the ranking or AI-visibility layer.
- Turning a link opportunity into on-page content for a specific MB page: `seo-gap-mb` / `seo-content-mb`.
- Writing or grading the outreach email / social copy itself: `post-writer-mb` / `post-grader-mb` (and match the recipient's formality per the workspace email rules).
- A full acquisition due-diligence dashboard: `acquisition-dashboard-mb`. This skill's competitor link gap can drop into its SEO pillar, but it is not a replacement.

## Before You Start

Confirm, briefly, before running:

1. **Scope:** the whole domain (mauriceblackburn.com.au) or a specific section / practice-area path? Practice areas: asbestos & dust diseases, medical negligence, road/transport accident injury, workplace injury & workers compensation, superannuation & TPD claims, class actions, employment & industrial law, abuse law, public liability.
2. **Competitors for the gap:** default Slater and Gordon (slatergordon.com.au) and Shine Lawyers (shine.com.au). Confirm or add others.
3. **Geography:** national, or a state/city focus. This shapes which outreach prospects are relevant (local news, community, legal directories).
4. **Data available (this is the gating question, ask explicitly, do not assume none exists):** backlink data is not free-crawlable at scale, so this job usually needs a paid export. Before running anything, ask directly which the user has:
   - **Live connector:** SEMrush MCP (`mcp.semrush.com/v1/mcp`, backlink + competitive data) or DataForSEO MCP backlink API (if a key is provisioned). Load via ToolSearch.
   - **Default path, an export CSV** the user pastes or points to: Ahrefs (Referring Domains / Backlinks export), SEMrush (Backlink Analytics export), or BrightEdge. State plainly that without one of these, MB's backlink profile cannot be enumerated and you can only do the parts that live crawling supports.

## Data sourcing (state which path each part used)

- **CSV export is the default path.** Assume the user pastes or provides a path to an Ahrefs / SEMrush / BrightEdge backlink CSV. Parse it with Bash/python3: detect the tool by its header row, normalise the columns you need (source URL, source/referring domain, Domain Rating or Authority Score, target URL, anchor text, first-seen/last-seen date, dofollow/nofollow, linking-page organic traffic if present), then run every check below over that parsed table. This is deterministic and does not depend on any connector.
- **Live connector** (SEMrush / DataForSEO MCP): use it to pull the same fields directly and to fetch competitor referring domains for the gap. Load the tool schema with ToolSearch first.
- **Live crawling (free, always available):** curl / WebFetch / Playwright for verifying a specific linking page (does it still exist, is it indexed, is the link still live, how many outbound links on the page), reading robots/sitemap, and verifying an outreach contact. Use this to confirm signals, not to enumerate the whole profile.
- Never present export-dependent numbers as if pulled live, and never fabricate a backlink profile when no data source is available: say what is missing and request the export.

## Method

Run the parts relevant to the ask. Findings carry a **Critical / Warning / Info** severity (same scheme as `seo-analyst-mb` / `seo-audit-mb`).

### Part 1: Profile health by Domain Rating tiers

One strong link outweighs a pile of weak ones. A single DR70+ editorial link from a national masthead or a .gov.au / university page is worth far more than dozens of DR-under-20 directory links. Score the profile on quality distribution, not raw link count.

1. From the parsed data, group referring domains into DR (or Authority Score) tiers: **DR70+**, **DR40-69**, **DR20-39**, **DR<20**. Count referring domains and links per tier. Deduplicate to referring domains for the health read (many links from one domain is one relationship, not many).
2. Read the shape:
   - Healthy = a visible spine of DR40+ editorial and institutional links (news, .gov.au, .edu.au, reputable legal directories), reasonable dofollow/nofollow mix, varied and mostly branded/natural anchors.
   - Unhealthy = the profile is dominated by DR<20 domains, near-100% dofollow, and repetitive exact-match commercial anchors.
3. Report anchor-text distribution: branded, naked URL, generic ("click here"), and exact-match commercial ("compensation lawyer Melbourne"). A high share of exact-match commercial anchors is itself a manipulation signal.
4. **Named framework, fixed for run-to-run comparability. Profile Health Score (0-100):**
   - **Authority spine (40 pts):** share and count of DR40+ referring domains. Reward the presence of DR70+ links heavily. Few or none = low score here.
   - **Anchor naturalness (25 pts):** branded + naked-URL share high and exact-match commercial share low = full marks. Deduct as exact-match commercial climbs.
   - **Link diversity (20 pts):** variety of referring domains, IP blocks, and link types; no single domain or IP block dominating.
   - **Toxicity drag (15 pts):** start at full, subtract as the multi-signal toxic share (Part 2) rises.
   - These weights are fixed. Do not retune per run. Report the four sub-scores plus the total so movement quarter-on-quarter is legible.
5. Severity: a thin authority spine with heavy DR<20 dominance is **Warning**; a spine plus a large multi-signal-toxic cluster is **Critical**; minor anchor skew is **Info**.

### Part 2: Toxic-link flagging (multi-signal, never single-score)

**CRITICAL RULE, read before doing anything here.** Never mass-disavow on a tool's "toxic score" or "spam score" alone. Those scores are noisy and routinely flag legitimate links. A link is only ever a disavow *candidate* when it trips **multiple independent signals**, and even then it is a candidate, not a decision. Disavow is a last resort, applied at **domain level** (`domain:` entries, not individual URLs, in almost all cases), only after manual review, and the resulting file is **always flagged for human sign-off and never auto-submitted** to Google. Google itself says most sites never need a disavow file. When in doubt, leave it in and monitor.

Flag a referring domain as a toxic candidate only when it trips **two or more** of these independent signals:

1. **DR<10 and zero (or near-zero) organic traffic** on the linking domain. A real site that ranks for nothing and has no authority is a red flag, especially in bulk.
2. **Unindexed linking page:** the specific page carrying the link is not in Google's index (verify live: fetch the page, and check indexation, e.g. a `site:` lookup or that it returns a real indexable 200, not a soft-404/parked page). Links from pages Google refuses to index carry no trust and often signal a link farm.
3. **100+ outbound links on the linking page:** link-farm / mass-directory footprint. Verify live by fetching the page and counting outbound external links.
4. **Exact-match commercial anchors** pointing at MB money pages (e.g. "best compensation lawyer", "asbestos claim payout") from low-quality domains. Natural editorial links rarely use exact commercial anchors at volume.
5. **PBN / IP-block clustering:** many linking domains sharing an IP block / C-class subnet, the same hosting fingerprint, near-identical templates, or the same registrant / creation window. This is the strongest signal because it implies a coordinated network, not organic linking.

Process:

1. Compute the multi-signal flags per referring domain from the parsed export, then **verify the borderline candidates live** (curl / WebFetch, or Playwright for JS pages) for the signals that need the current page state: indexation, outbound-link count, and whether the link is even still present. Do not disavow a link that no longer exists.
2. Sort into three buckets: **Toxic candidate** (2+ signals, PBN clustering counts strongly), **Watch** (1 signal, monitor next quarter), **Benign** (0 signals, including legitimate low-DR links like a small community site or a real local directory, which are fine).
3. For each Toxic candidate, record which signals fired and the evidence, so a human can audit the call in seconds.
4. Severity: a confirmed PBN/IP cluster or a large multi-signal toxic share is **Critical**; scattered multi-signal domains are **Warning**; single-signal Watch items are **Info**.

### Part 3: Competitor backlink gap (link intersect)

Find the referring domains that link to competitors but not to MB. These are pre-qualified: the domain already links to a plaintiff law firm in this market, so it is a warmer prospect than a cold target.

1. Get competitor referring domains: via SEMrush / DataForSEO MCP if live, otherwise from a competitor referring-domains CSV the user exports (Ahrefs "Link Intersect" / SEMrush "Backlink Gap" does this directly, ask for that export if available).
2. Compute the set difference: domains linking to Slater and Gordon and/or Shine (bonus weight if they link to **both**, that is a strong topical/market fit) but **not** to mauriceblackburn.com.au.
3. Enrich each gap domain: DR/authority tier, whether it looks editorial vs directory vs PBN (skip anything that would be a toxic candidate under Part 2, do not chase junk links just because a competitor has them), the type of page linking (news article, resource page, directory, community org), and the likely link context (a legal explainer, a "best lawyers" roundup, a community sponsorship).
4. Rank the gap by authority × relevance × attainability. A DR75 national news domain linking to both competitors is a high-value target; a DR15 directory is not worth chasing.

### Part 4: Outreach opportunity list

Turn the gap plus other earned-link angles into a ranked, contactable prospect list.

1. **Warm intros convert far better than cold outreach.** Prioritise, in order: existing MB relationships (journalists MB has worked with, community partners, pro-bono and campaign partners, existing referrers), then link-intersect gap domains (Part 3), then relevant-but-cold targets (legal directories, .gov.au / .edu.au resource pages, community organisations tied to MB's practice areas and social-justice positioning). Flag which tier each prospect sits in.
2. Source angles that fit MB's actual profile: earned media / digital PR (MB's class actions and investigations are genuine newsworthy hooks), expert commentary and data-led pieces, resource-page and directory listings, and community/sponsorship links. This matters beyond rankings: off-site brand mentions correlate with AI-answer visibility roughly 3:1 over backlinks (Ahrefs 75k-brand study), so earned media doubles as GEO fuel. See `seo-competitor-mb` for the Share-of-Model side.
3. **Verify a contact before listing it (live, via WebFetch):** open the prospect domain's contact / about / editorial / staff page and confirm a real, current contact route (named editor/journalist, contact form, or role-based email) rather than guessing an address. If no contact can be verified, mark it "contact unverified, needs manual lookup" instead of inventing one. Never fabricate an email address.
4. For each prospect record: domain, DR/authority tier, warm/gap/cold tier, the link angle, the verified contact route, and a one-line pitch idea.
5. **Compliance gate on any suggested pitch angle or outreach copy (hard gate, embedded):** no outcome guarantees ("you will win", "guaranteed compensation"); no misleading comparative claims or implying a typical result from one case; no absolute claims about the law ("always" / "never") without a jurisdiction/circumstance hedge; a trigger/content warning where a pitch touches abuse, suicide, or distressing subject matter; real client names only where consent is on file, otherwise "a client" / anonymised. This mirrors the `post-grader-mb` gate and `brand-mb`'s `reference/legal-marketing-guardrails.md`. If an angle would breach any of these, do not suggest it.

## Output

Deliver in the conversation (offer to save a copy if the run is large):

1. **One-line summary:** e.g. "Profile Health 68/100, spine is thin (11 DR40+ domains) but mostly clean; 23 multi-signal toxic candidates (one 14-domain PBN cluster) held for your sign-off; 41 warm/gap outreach prospects, top pick is [domain]."
2. **Backlink health report:** the Profile Health Score with its four sub-scores, the DR-tier table (referring domains + links per tier), the anchor-text distribution, and findings by category each tagged **Critical / Warning / Info** with the exact fix. State the data path used (CSV export vs live connector) so the reader knows how solid the numbers are.
3. **Reviewed disavow-candidate list (human sign-off required):** the Toxic candidates only, as `domain:` entries in disavow-file format, each with the signals that fired and the evidence. Head the block with an explicit banner: **"DISAVOW CANDIDATES, FOR HUMAN REVIEW AND SIGN-OFF, NOT AUTO-SUBMITTED. Do not upload to Google without manual verification."** Restate that disavow is a last resort and most profiles never need one. Keep the Watch list separate to monitor next quarter.
4. **Competitor link-gap list:** domains linking to competitors but not MB, ranked by authority × relevance × attainability, junk excluded, tagged with the linking-page type.
5. **Prioritised outreach prospect list:** warm intros first, then gap, then cold; each with DR tier, angle, verified contact route, and a one-line pitch. Note that warm intros convert far better than cold outreach.
6. **Prioritised action plan:** Quick Wins / Medium / High Impact. Disavow review sits under a "defensive" heading and is a last resort; earned-media / digital-PR outreach usually sits in High Impact given the links-plus-AI-visibility payoff.
7. **Handoff notes:** the whole backlog (disavow review task, each outreach prospect, each gap target) can be piped into `brief-ticket-monday-mb` or `brief-ticket-jira-mb` (MBLS) as tickets. The link gap can also drop into the SEO pillar of `acquisition-dashboard-mb`, and complements `seo-competitor-mb`'s Share-of-Model read.
8. **Cadence note:** recommend re-running this audit quarterly, and log the run in the relevant project's `MEMORY.md` Activity Log.
9. **MB-branded docx:** always also export the health report as a `.docx` with the MB logo in the page header (the disavow-candidate list, kept clearly labelled for human sign-off, can go in the same document or a separate one). Build a JSON object matching the shape at the top of `scripts/render_mb_docx.py`, write it with `Write`, then run `/usr/bin/python3 scripts/render_mb_docx.py <input.json> <output-name>.docx`. Use system Python (`/usr/bin/python3`), it has `python-docx` installed. Tell the user the saved file path.

## Error Handling

- **No backlink data source (no CSV, no live connector):** stop and request an Ahrefs / SEMrush / BrightEdge export. Do not fabricate or estimate a backlink profile. Say clearly which parts (competitor gap, toxic flagging, health tiers) are blocked until the export arrives; live-crawl parts (contact verification, page-level toxic signals) can still run on specific URLs.
- **Unrecognised CSV format:** show the detected header row and ask the user to confirm the column mapping before parsing, rather than guessing columns.
- **Unreachable / JS-rendered / paywalled linking or prospect page:** re-fetch with Playwright MCP (load its tools via ToolSearch) before concluding; if still blocked, ask for the text or mark the signal "unverified", never guess indexation, outbound-link count, or a contact.
- **Toxic score from a tool alone:** never sufficient. Require 2+ independent signals per the Part 2 rule, and always route the result to human sign-off.
- **Missing DR / traffic / anchor columns in the export:** run the checks you can, and flag which signals could not be evaluated rather than inferring them.
