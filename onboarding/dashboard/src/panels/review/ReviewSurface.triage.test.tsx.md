# dashboard/src/panels/review/ReviewSurface.triage.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/ReviewSurface.triage.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T22:21:58+02:00 |
| lastVerifiedCommitHash | `3dc2ab0cf59cdc87ec478f6563d4ac6696871076`|
| lastVerifiedCommitDate | 2026-09-30T23:11:04+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

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

## Docs References

No domain documentation source is configured; the requirement packet `MIK-R33@v1` (adopting `ICR-R32@v1`) and the architect's rulings in `33_review-triage-order-and-change-kind-badges.json` live outside the code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The suite's statement and its stubbed reads. | "is the real component and only"; "is stubbed" | dashboard/src/panels/review/ReviewSurface.triage.test.tsx:1-58 |
| The one case: the move, the kept context, focus and workspace, and the centre's order. | "moves the selection to the next change and keeps family context, focus and workspace" | dashboard/src/panels/review/ReviewSurface.triage.test.tsx:64-122 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T22:21:58+02:00 — 260928-MIK-L33 curator (staged change set on `ar/260928-mik-l33`, code base `c052b2593b85d9baf425cc1d5c46f384b13fc9ea`; review R1 changes-required, R2 and R3 pass-with-notes, each followed by a fix round, with the merge round after MIK-L34): created this card for the new mounted-surface triage test (1 case), recording the review R1 note that the centre follows the tree. The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
