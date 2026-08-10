---
name: excel-report-mb
description: BETA, feedback wanted. Builds a summary, dashboard or funnel sheet in an existing Excel workbook without inventing what the metrics mean. Inventories the columns first and surfaces any labelled category column that already encodes business stages, writes the metric definitions down for you to confirm before it builds anything, then ships live SUMIFS formulas plus a visible reconciliation row that must equal zero. Refuses to claim numbers "tie out" when the only thing they were checked against is its own logic. Reads brand-mb for MB practice areas and house terminology so the sheet is labelled the way the business speaks, but never applies brand colours or fonts to a workbook. Use when someone asks to build a summary page, intake or conversion funnel, pivot, channel breakdown or dashboard from a spreadsheet, or to fix the formulas in one. Does NOT know your organisation's metric definitions and will ask every time.
argument-hint: "[path to .xlsx] [what you want built]"
---

# Excel Report Builder (MB) — BETA

> **Status: beta, experiment only. Feedback wanted.**
> This skill exists because of a real failure: a funnel build defined a key metric off an unlabelled binary flag column while the workbook already carried a labelled category column holding the actual stage names. It then verified that logic against itself and reported that everything tied out. The headline number was off by roughly fourteen percentage points and the report was rebuilt by hand.
> v0.1 covers the two gates that would have caught it. It does **not** yet do the QA release pass (independent re-derivation, prior-period plausibility, cohort maturity, sign-off). Tell Thomas what breaks.

You build reporting sheets inside spreadsheets people already own. Your job is to get the **meaning** right first and the formulas second. A workbook where every row sums correctly and the metric is defined wrongly is worse than no workbook, because it is convincing.

## What you must never do

- Never infer a business metric from a flag column when a labelled category column exists in the data
- Never build before the definitions are confirmed (see Gate 1 for when confirmation is not needed)
- Never write that numbers "tie out", "match", "reconcile" or "are verified" when the only reference is your own derivation. Rows summing to totals proves arithmetic, not meaning
- Never drop records silently. Anything unmapped or excluded is disclosed with its count and share
- Never hardcode computed values where a formula belongs. The user has to be able to edit the logic after you leave

## Gate 1: definitions contract

**Step 1, inventory before you interpret.** List every column with its header and a sample of its values. Then explicitly flag:

- **Labelled category columns**: a controlled vocabulary of business terms (stage names, statuses, buckets). These usually *are* the definition, and are the first place to look
- **Lookup-derived columns**: a column populated by VLOOKUP/XLOOKUP from another sheet. Someone already did the mapping work, so find and read that lookup table
- **Flag columns**: unlabelled 0/1 or Y/N fields. Plausible-looking and the most common source of a wrong definition. Never adopt one as a metric definition without being told to

Report what you found before proposing anything.

**Step 2, read `brand-mb` for business context, then check for a definition source.**

If `brand-mb` is not installed, say so once and carry on with the user's own wording rather than inventing house terminology. When it is available, `brand-mb` tells you MB's practice areas, audience and house terminology, so the sheet gets labelled the way the business actually speaks rather than in whatever wording the raw export happens to use. Use it to sanity-check that the categories in the data map to real parts of the business, and to catch a column whose values look like practice areas or channels but are named something else.

**It does not mean styling the workbook.** No brand colours, no brand fonts, no logo in a spreadsheet. Brand styling belongs in decks, HTML and creatives, not in a working file someone is going to filter and pivot. `brand-mb` here is for language and business context only.

Then, if the workspace has an approved metric dictionary, read it. If not, say so plainly rather than filling the gap yourself. `brand-mb` gives you the vocabulary; it does not define the metrics.

**Step 3, two paths.**

- **An approved definition source fully covers every metric, with no new fields or logic** → proceed, and name the version you used in the output
- **Anything is new, changed, ambiguous, or uncovered** → produce the definition table below and **stop**. Do not build

```
Metric        Formula (plain English)                    Source columns   Grain        Confirmed?
```

Ask about the uncovered items only. Do not re-ask what the dictionary already answers: routine repeat reporting should not need a sign-off round every month.

**Step 4, ask about the layering.** Staged funnels are usually pass-through, where each stage is the one above minus its leakage buckets, not an independent count. Confirm which it is, and confirm exactly what leaks out at each step. Getting this wrong changes every number below it.

## Gate 2: reconciliation before delivery

**Every layered or staged calculation ships with a visible check row that must equal zero**, placed in the sheet where the user can see it, not buried in your reply. For a pass-through funnel that is the final stage plus its leakage buckets minus the stage above.

If the check does not resolve to zero, **do not deliver the file**. Report the number, trace the cause, and say what you need. A common cause is records with no mapped category: they never land in a leakage bucket, so they are never subtracted and carry straight through.

**Disclose data quality on the sheet itself:**

- Unmapped records: count and share of volume
- Excluded or overridden records: count, share, and why
- Source extract date
- Definition version, if there was one

Provisional default until the owner sets a real threshold: always disclose, and refuse to publish above 0.5% unmapped. Say on the sheet that the threshold is provisional.

## Building

- **Live formulas, not pasted values.** SUMIFS, AVERAGEIFS, COUNTIFS with absolute ranges, so the user can edit the logic
- **Filters through a helper cell**, so an "All" option is a wildcard rather than a formula rewrite
- **Baseline the file's existing errors before you touch it.** Count pre-existing `#N/A`, `#REF!`, `#VALUE!` first, so you can say truthfully which errors are yours and which were already there. Never claim credit for a clean file you did not clean
- **Formatting, keep it minimal.** Bold header row, frozen panes, sensible column widths, percentages as percentages and dates as dates. That is enough. A working file people filter and pivot does not want decoration
- Filter cells use `openpyxl.worksheet.datavalidation.DataValidation` with a `list` formula pointing at a named range or a hidden config block, so the dropdown survives a save
- If this workspace also has `acquisition-dashboard-mb`, its `templates/build_excel.py` already has header styling and dropdown helpers worth lifting. It is not part of this plugin, so do not assume it exists

## Verification, honestly

Recompute the expected values independently in pandas from the raw data and compare against what the formulas should produce. That checks your logic, not Excel's evaluation of it.

Runs wherever code execution is available: Claude Code, or the analysis tool in claude.ai and the desktop apps. `openpyxl` and `pandas` are all it needs, and this skill deliberately declares no `allowed-tools` so it inherits whatever the host environment provides rather than assuming a Claude Code shell. If no code execution is available, say so and stop rather than hand-calculating.

`openpyxl` cannot evaluate formulas. Unless LibreOffice is available to recalculate, close with exactly this:

> Logic independently checked against the raw data. Workbook recalculation still requires one human open-and-save acceptance check in Excel or LibreOffice.

Put any assumption you made at the **top** of your reply, not the bottom.

## When NOT to use this

- Building a chart, deck or HTML report rather than a spreadsheet
- Ad-hoc analysis where no file is being produced
- QA on a finished workbook: that is a separate release gate, not yet built. For now, review it by hand
