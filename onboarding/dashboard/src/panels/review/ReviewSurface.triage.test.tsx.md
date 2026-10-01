# dashboard/src/panels/review/ReviewSurface.triage.test.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**`j` in the mounted reviewer** over the store-authored bodies (`triage.family`, `triage.memberA`, `triage.memberH`,
`triage.entries`); `ReviewSurface` is the real component and only `fetch` is stubbed. 1 case.

## Code Commentary

### Logic

- A `j` move selects the next change's subject exactly as a click does (the member review read for that subject) and
  keeps the family context, the focus on the moved-to node and the mounted workspace node (ICR-R32 rule 6, ICR-L48).
- The centre's member list follows the tree's displayed order, in triage and in authored order (review R1 note;
  `FamilyReviewCenter.FamilyCenter`).
- The cold first render waits up to 5 s (one run exceeded the 1 s default under load).

### Conventions

Vitest with Testing Library; tree-view and source-content reads answer a typed refusal because they are outside this check.

### Invariants And Boundaries

Selection moves keep family context, focus and the mounted workspace.

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured; the requirement packet `MIK-R33@v1` (adopting `ICR-R32@v1`) and the architect's rulings in `33_review-triage-order-and-change-kind-badges.json` live outside the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The suite's statement and its stubbed reads. [1]
- The one case: the move, the kept context, focus and workspace, and the centre's order. [2]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
