# dashboard/src/panels/review/changeTriage.test.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/changeTriage.test.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T22:21:58+02:00 |
| lastVerifiedCommitHash | `3dc2ab0cf59cdc87ec478f6563d4ac6696871076`|
| lastVerifiedCommitDate | 2026-09-30T23:11:04+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**The pure triage rules over the store-authored comparison's served bodies** (`triage.family`, `triage.familyPage`,
`triage.familyContinued`, `triage.shared`; the world `mcp/tests/test_review_change_kinds.py` asserts the facts of). 12
cases check that the tree orders, counts and merges the delivered facts and never decides one.

## Code Commentary

### Logic

- **Family triage (5):** counts by delivered primary kind; a partial page scoped to its returned members with the total
  named; a complete-looking family whose total is unknown scoped as "(total unknown)" and weighing at least `unknown`
  (SYNTHETIC: no total; review R1 F2); a family weighed by its own revised guarantee (SYNTHETIC: every member
  unchanged; mutation R-C3); the total said to be unknown rather than invented.
- **Tree order (5):** changes first by weight then authored position, every sibling kept; pure authored order is the
  family record's `members` list; families by their highest member or guarantee weight, then context order; a partial
  family above a complete unchanged one (SYNTHETIC facts); a dataset review (no facts) in its landed order.
- **Roster walk (2):** `mergeFamilyContinuation` keeps the facts of every member the walk returned (strengthened with a
  SYNTHETIC gap after the walk-merge mutation first survived); two deliveries unioned with the newer family facts.

### Conventions

Vitest over captured JSON read from the test's own directory; SYNTHETIC variations are labelled in the case names.

### Invariants And Boundaries

Proves part of the candidate invariant recorded on `changeTriage.ts.md` (order never hides siblings; partial pages scoped).

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
| The suite's statement and its bodies. | "These tests"; "check that the tree orders, counts and merges the delivered facts and never decides one." | dashboard/src/panels/review/changeTriage.test.ts:1-26 |
| Family triage: counts, partial and scoped breakdowns, the guarantee's weight. | "scopes a partial page to the members it returned and names the total"; "scopes a complete-looking family whose total is unknown (SYNTHETIC: no total)" | dashboard/src/panels/review/changeTriage.test.ts:35-118 |
| Tree order: changes first with every sibling kept, pure authored order, families by weight, a dataset review untouched. | "lists changes first by weight then authored position, keeping every sibling"; "leaves a dataset review (no change facts) in its landed order" | dashboard/src/panels/review/changeTriage.test.ts:120-209 |
| The roster walk keeps every returned member's facts. | "keeps the facts of every member the walk has returned" | dashboard/src/panels/review/changeTriage.test.ts:211-246 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T22:21:58+02:00 — 260928-MIK-L33 curator (staged change set on `ar/260928-mik-l33`, code base `c052b2593b85d9baf425cc1d5c46f384b13fc9ea`; review R1 changes-required, R2 and R3 pass-with-notes, each followed by a fix round, with the merge round after MIK-L34): created this card for the new triage-rules test (12 cases), recording review R1 F2 and F3's cases. The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
