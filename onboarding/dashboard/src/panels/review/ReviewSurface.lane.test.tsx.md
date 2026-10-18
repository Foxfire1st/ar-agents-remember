# dashboard/src/panels/review/ReviewSurface.lane.test.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**Three R86 destination/worklist cases through the real mounted surface, using the exact leaf-built L37 `l86.*` replies.** These cases exercise the existing comparison viewer, held-lane filter state and a held leaf worklist. The old seven-case MIK-L32 focused-lane/explorer suite is historical, not the current source.

The lane destinations in the mounted reviewer: each destination draws in the lane answer order with its one reason sentence, All keeps working while lane counts are read without guessed buckets, and an unanswered leaf worklist reads as reading in its own view, never as no gate item.
## Code Commentary

### Logic

The imported `serve` in `l86.test-utils.ts` routes captured catalogue, review, trees, source-content and comparison-viewer replies; it can hold the lane or worklist read. These are recorded HTTP bodies replayed through fetch, not a newly started backend.
- **Destination case:** the Changes without an invariant destination reports 167 files; the comparison page's code paths follow the lane answer order, its reason sentence appears once, and changed onboarding is absent in that filter. Unknown attribution reports two code files, every delivered unknown path is present, its reason appears once, and no details are mounted.
- **Held-lane case:** the summary reports `… files without an invariant`; All changes opens the 179-code-file comparison list while the Changes without an invariant and Unknown attribution filters are disabled. All stays enabled, and Changes without an invariant becomes enabled when the held lane resolves.
- **Held-worklist case:** the worklist's own view says it is reading, not that no item names the record; resolving the held response produces the rail label `Worklist 518 open`, an open-item count.

### Conventions

- The component tree is real; the current fetch world comes from `l86.test-utils.ts` and the retained L37 captures.

### Invariants And Boundaries

**Historical pre-R86 card account — superseded, not current assertion evidence.**

> - Proves, through the real surface, the candidate invariant "on tree comparisons, the explorer and the technical
>   details take their attribution from the lane, so no two surfaces disagree" (recorded on
>   `review_unexplained_lane.py.md`), and rule 10's destinations, order, totals and focused diff on real data.
> - Mutations caught: the explorer ignoring the lane (3 cases), the details ignoring the lane or not being handed it
>   (3 each), and a second lane read by the workspace (the one-read assertion of case 1).

### Todos

No additional work is asserted by this card.

The lane fixture feeds the rail and the change-set page, asserting destination order, file counts and the single reason sentence above the list. The held-lane case keeps the All filter usable with disabled destination filters and no invented numbers. The worklist case states the pending view distinctly from an empty measurement.
## Evidence

### Docs References

No domain documentation source is configured; the requirement packet `MIK-R32@v1` and its rulings live outside the code
and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

**Historical pre-R86 card account — superseded, not current assertion evidence.**

> - The real bodies and the scratch leaf they describe. [1]
> - The fetch stub, with a held read. [2]
> - Case 1: destinations after the families, one lane read. [3]
> - Case 2: rows in the server's order and a focused hunk. [4]
> - Case 3: the unknown file with its reason. [5]
> - Case 4: the gate's items still being read. [6]
> - Cases 5 and 6: the explorer labels from the lane, or pending (ruling Q1). [7]
> - Case 7: the technical details from the lane (review F1). [8]

### Cross-Repo References

No cross-repo boundary is crossed by this file.

- The module reads its lane fixture from l86.lane.captured.json. [9]
- The mounted destination case asserts Changes without an invariant with 167 files, lane path order, one reason sentence, and the two-file Unknown attribution destination. [10]
- While the lane read is held, All remains usable, both destination filters are disabled, and Changes without an invariant becomes enabled after release. [11]
- The held worklist view states that it is reading; after release the rail asserts Worklist 518 open. [12]
