# Changelog

Release notes for the **mb-marketing** plugin. Each version is also an annotated git tag (`vX.Y.Z`). Installing the plugin doesn't auto-update, remove and re-add it (or `/plugin update` in Claude Code) to pick up a new version.

## v0.4.0 - 2026-08-11
- **New skill: `excel-report-mb` (BETA, experiment only, feedback wanted).** Builds a summary, funnel or dashboard sheet inside an existing workbook without inventing what the metrics mean. Written after a real build defined a key metric off an unlabelled binary flag column while the workbook already carried a labelled category column holding the actual stage names, then verified that logic against itself and reported that everything tied out.
- **Gate 1, definitions contract.** Inventories every column and explicitly surfaces labelled category columns and lookup-derived columns *before* any flag column, then writes the metric definitions into a table and stops for confirmation. Skips the sign-off round when an approved definition source already covers the request, so routine repeat reporting is not slowed down.
- **Gate 2, reconciliation.** Ships live SUMIFS rather than pasted values, plus a visible check row that must equal zero, and refuses to deliver the file if it does not resolve. Discloses unmapped and excluded records with counts and share, and baselines the workbook's pre-existing errors so it can say truthfully which are its own.
- Forbidden from writing that numbers "tie out" or "match" when the only reference is its own derivation. States plainly that `openpyxl` cannot evaluate formulas, so a human still needs one open-and-save check.
- Not yet included: the QA release pass (independent re-derivation, prior-period plausibility, cohort maturity, named sign-off). Coming once the thresholds are agreed.
- Plugin goes from 12 to 13 skills. README, plugin and marketplace manifests updated to match.

## v0.3.7 - 2026-08-09
- `seo-content-mb`: the "How we can help" close now offers MB's real **contact channel mix**, phone 1800 111 222 (as a `tel:` link), the free claim check, and "get in touch", not a single CTA.

## v0.3.6 - 2026-08-09
- `seo-content-mb`: standard **section order** now ends on "How we can help" after the FAQ, then Sources. Added a required **"Related articles"** section (link-checked cards) and guidance to use **content tables** where a section is comparative/structured.

## v0.3.5 - 2026-08-09
- `seo-content-mb`: added SEO/GEO best-practice brief elements, a **key-takeaways / "In summary"** box, a **featured-snippet target**, a light pre-draft **SERP read** (deep gap work stays with `seo-gap-mb`), an **inbound internal-link plan**, a **measurement** line, a **media/image plan**, a fuller **author-authority** by-line, and **two CTA placements**.

## v0.3.4 - 2026-08-09
- `seo-content-mb`: MB-branded **docx** now has a clear **Heading 1/2/3 hierarchy**, real **clickable hyperlinks**, **FAQ questions as Heading 3**, and a relevant **client-story cross-reference**. "No Win, No Fee" always links to the fees page.

## v0.3.3 - 2026-08-09
- `seo-content-mb`: new **Content QA** step, HTTP-checks every link (no invented URLs), verifies the docx copy matches the HTML, and confirms internal links are real. Targeting brief switched to the agency **"Townsville" table** format.

## v0.3.2 - 2026-08-09
- `brand-mb`: blog voice reference gained a **Content genres** section (the six MB blog templates); the writer now picks the genre before drafting. Built from ~140 real MB blogs.

## v0.3.1 - 2026-08-09
- `brand-mb`: blog voice reference gained **per-practice-area language + CTA models** (e.g. TAC vs WorkCover vs TPD vs Fair Work; employment uses a paid consult, super uses a free super claim check).

## v0.3.0 - 2026-08-09
- `seo-content-mb`: major rework from reviewer feedback. New **blog voice reference** built from real MB blogs + a **mandatory voice pass** (rewrites off-brand copy), **mandatory visible citations** with a Sources list, a **data-recency** rule, **statement headings** (questions reserved for the FAQ), **no auto general disclaimer** (content warnings only for confirmed sensitive topics), and a hard **85/100 readiness gate**.

## v0.2.0 - 2026-08-09
- New skill **`qa-creative-mb` (QA Creative Agent)**: WCAG 2.2 AA + visual QA on a drafted Canva creative (contrast, size, alt text, thumbnail read), auto-fixes the safe issues as a before/after you approve; brand colours always win on contrast. Auto-invoked by the social skills. Plugin now has 12 skills.

## v0.1.3 - 2026-08-08
- `post-writer-mb` / `repurpose-mb`: class-action posts offer three MB class-action templates (Image / No Image / Quote); refreshed to Canva's current editing tools (`read-design` + `edit-design`).

## v0.1.2 - 2026-08-08
- `post-writer-mb` / `repurpose-mb`: witness-ad requests offer all four MB witness templates with a graceful fallback; every Canva creative is named `PRACTICE AREA - REQUEST - DDMMYYYY`.

## v0.1.1 - 2026-08-08
- `post-writer-mb` / `repurpose-mb`: the skill now confirms the Canva template with you before building, always asking when more than one fits.

## v0.1.0 - 2026-08-08
- First tagged release. `post-writer-mb` / `repurpose-mb` select Canva templates by the live `MB -` title-prefix (MB's brand-template naming scheme), replacing a hardcoded ID list.
