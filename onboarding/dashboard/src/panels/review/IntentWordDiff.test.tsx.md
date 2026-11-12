# dashboard/src/panels/review/IntentWordDiff.test.tsx

## Governing Overview

[Owning route overview](overview.md)

## Purpose

Derived successor controls keep authored prose, list alignment and accessible word changes truthful while condition lines open independently.

## Code Commentary

### Logic

- The helper derives one changed field from retained invariant/family operands and mounts SelectedStatement inside IntentWordDiffScope. Its accessible-text reader includes hidden announcements and excludes decorative glyphs; statement, applicability and guarantee changes use del/ins rather than a code editor.
- Existing cases cover one calculation per passage, exact-text alignment with moved/added/removed items, unequal-gap descriptions, coarse 1500-by-1500 lists, selected-revision field rows and three missing-row/moved-in shapes whose one revision still has different text.
- Added, removed, unreadable and unresolved states remain distinct. Identical wording in a successor revision differs from the same recorded revision; differing text in one revision remains changed. Whitespace-only changes preserve exact texts and have no ineffective layout control.
- Each condition is a focusable role=button line carrying its full text and word marks while closed. Clicking, Enter or Space changes only that line; no details or disclosure owns the list. A side-by-side changed line keeps removed words only on before and added words only on after.
- A mostly rewritten condition starts side by side with its ratio explanation, then can open and switch inline without closing. Whole-passage layout choice persists locally, defaults inline when storage reads fail and still changes when storage writes fail.
- When display versions were not carried, the changed-fields label omits raw revision IDs. A joined-only exclusion row remains reported rather than reconstructed into an aligned list, with same-revision text-difference qualification as applicable. Guarantee helper cases retain their separate known-absence and same-revision facts.

### Invariants And Boundaries

These are declared unit/component controls over derived captured operands and synthetic storage failures. They were not executed here; DOM classes and full text presence do not constitute real browser measure/ellipsis geometry.

## Evidence

- Declared check and its fixture assertions. [15]
- Declared check and its fixture assertions. [16]
- Declared check and its fixture assertions. [17]
- Declared check and its fixture assertions. [18]
- Declared check and its fixture assertions. [19]
- Declared check and its fixture assertions. [20]
- Declared check and its fixture assertions. [21]
- Declared check and its fixture assertions. [22]
- Declared check and its fixture assertions. [23]
- Declared check and its fixture assertions. [24]
- Declared check and its fixture assertions. [25]
- Declared check and its fixture assertions. [26]
- Declared check and its fixture assertions. [27]
- Declared check and its fixture assertions. [28]
- Declared check and its fixture assertions. [29]
- Declared check and its fixture assertions. [30]
- Declared check and its fixture assertions. [31]
- Declared check and its fixture assertions. [32]
- Declared check and its fixture assertions. [33]
- Declared check and its fixture assertions. [34]
- Declared check and its fixture assertions. [35]
- Declared check and its fixture assertions. [36]
- Declared check and its fixture assertions. [37]
- Declared check and its fixture assertions. [38]
- Declared check and its fixture assertions. [39]
- Declared check and its fixture assertions. [40]
- Declared check and its fixture assertions. [41]
- Declared check and its fixture assertions. [42]
- Declared check and its fixture assertions. [43]
- Declared check and its fixture assertions. [44]
- Declared check and its fixture assertions. [45]

## Historical predecessor account

The earlier account follows as provenance. Current assertions and removed journeys are described above.

> # dashboard/src/panels/review/IntentWordDiff.test.tsx
>
> ## Governing Overview
>
> [dashboard/src/panels route overview](overview.md)
>
> ## Purpose
>
> **MIK-R35's rendering cases (28 test declarations, including one three-shape `it.each`), with accessible-text assertions.** The knowledge pane and member rows start from
> the real served invariant review of the converted scratch leaf (`gitTrees.invariant.captured.json`, a tree
> comparison `review:trees:1`), and the family cases from `gitTrees.family.captured.json`; `review()` derives the
> second revision by changing exactly the field each case is about, as `statementWording.test.tsx` does, and mounts
> the real `SelectedStatement` inside `IntentWordDiffScope`. Assertions read what assistive technology reads
> (`spoken`: visually hidden announcements included, `aria-hidden` glyphs excluded), not only the styling.
>
> ## Code Commentary
>
> ### Logic
>
> - **A tree comparison statement (20 declarations):**
>   - each text passage computed once for layout choice and drawing;
>   - unequal list gaps shown as removed and added rows with an accessible explanation;
>   - 1500-by-1500 lists shown without alignment, with the coarse explanation, 3000 rows and no changed row;
>   - the statement marked in place in one passage, read as "…links is removed: refused added: rejected and reported
>     with…", with `<del>` / `<ins>` elements and no `diff-pane`;
>   - a condition-only revision: the changed condition marked in place and the statement once;
>   - R2-1: a paired condition whose only change is whitespace offers no layout control;
>   - conditions and exclusions aligned by exact text (unchanged, moved, added, removed), with no control;
>   - a changed applicability as its own passage;
>   - **ruling Q4:** only the selected revisions' field rows are read in the captured comparison scope (another
>     record's `applicability` row is ignored, the subject's own row is read);
>   - **review R1 F1**, three probe cases: one revision whose texts differ when the after row is not on the page, the
>     before row is not on the page, or the member is listed on the after side only (moved in, wording touched) —
>     each reads "Changed statement · revision r2 → r2 · the same revision on both sides; its text differs", no
>     "unchanged" testid, and the marked comma;
>   - F4's X9/X10: one revision with identical text reads "Statement unchanged · same recorded revision", with or
>     without rows;
>   - F4's X11: an applicability recorded on one side only reads as a known absence, with no diff and no control;
>   - F4's X13: a list the comparison only reported joined is shown as reported, never aligned;
>   - F4's X19: a whitespace change inside a changed passage is drawn as `·` / `··` and announced "removed: 1 space
>     added: 2 spaces";
>   - "Wording unchanged" kept for a new revision whose every field is identical;
>   - the same revision with different text diffed and labelled (ruling Q1);
>   - the boundary example: a trailing space renders once as "whitespace-only change" with both exact texts disclosed;
>   - a rewrite shown side by side with its reason, and "Show inline" switching that passage;
>   - the toggle switching every passage and writing `review.intent-diff.layout.v1`;
>   - inline when storage throws on read, and a throwing `setItem` still switching.
> - **One-sided and unavailable statements (3 declarations):** added and removed statements with the known-absent line;
>   an unreadable side named as unreadable and never diffed against; no diff for an unresolved selection.
> - **The family guarantee (4):** a changed guarantee word-diffed with compact revision metadata and a control; one
>   revision with different text diffed (and `guaranteeTextChange` null for identical text or a missing side); no
>   control for a whitespace-only guarantee; a one-sided guarantee labelled a known absence only when the other side is
>   `not_recorded`.
> - **Labels of one revision whose texts differ (one surviving helper case; historical R1 F2 subject):** `guaranteeFact` returns `same_revision_text_changed` for differing bytes and `unchanged_revision` for identical captured bytes. The navigator guarantee and member-tag rendering cases were removed.
>
> ### Conventions
>
> - `afterEach` resets the preference store to inline and clears `localStorage`, so no case leaks its layout.
> - The successor revision id and the display versions `r2`/`r3` are the derivation's own values; the `rows` option
>   shapes the member rows per side (`MemberSides`) or `'none'` so the pane and its field rows answer.
>
> ### Invariants And Boundaries
>
> - Retained unit-level cases cover selected-side statement sourcing, prose diff and guarantee rendering, plus the narrow `guaranteeFact` helper classification. The earlier worker/reviewer mutation accounts are historical run records for their named source trees, not a claim that the removed navigator-label tests still execute or that those probes were rerun here.
>
> ### Todos
>
> No additional work is asserted by this card.
>
> ## Evidence
>
> ### Docs References
>
> No domain documentation source is configured; the requirement packets `MIK-R35@v1` / `ICR-R35@v1`, the leaf's rulings
> and the reviewer's probes (`notes/reports/260928-MIK-L35-review-R1-checks/`) live outside the repositories, so they
> are named here and not cited as rows.
>
> No configured live documentation source was available for this pass.
>
> ### Repo-Internal References
>
> - The real bodies the cases start from, and the accessible-text reader. (historical reference 1)
> - The conforming example, condition-only, R2-1, list alignment and applicability cases. (historical reference 3)
> - F4's cases and the same-revision label. (historical reference 5)
> - Whitespace-only, the rewrite and the preference. (historical reference 6)
> - The family guarantee. (historical reference 8)
>
> ### Cross-Repo References
>
> No cross-repo boundary is crossed by this file.
> - Base statement fixture for diff passages (historical reference 10)
> - Review mount helper with scope and revision options (historical reference 11)
> - Tree scope fixture for comparison passages (historical reference 12)
> - Layout persistence assertions across passages (historical reference 13)
>
> - The review helper derives a successor, supplies per-side member rows and mounts SelectedStatement in the captured payload's IntentWordDiffScope. (historical reference 2)
> - Selected-revision field sourcing in the captured comparison scope and the retained three-shape same-revision differing-text table. (historical reference 4)
> - Three declarations cover known-absent added/removed statements, unreadable sides and unresolved revision selection; no dataset or ambiguous-selection case remains. (historical reference 7)
> - The retained center-details guaranteeFact helper case classifies differing text as same_revision_text_changed and identical captured text as unchanged_revision. Navigator guarantee/member-tag tests and the dataset-path helper expectation are absent. (historical reference 9)
> - Three added declarations assert single computation per passage, accessible descriptions on unequal-gap rows and coarse rendering of 1500-by-1500 lists. (historical reference 14)
