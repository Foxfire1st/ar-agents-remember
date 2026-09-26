# subjectReview.family.captured.json

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/subjectReview.family.captured.json` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-26T20:20:54Z |
| lastVerifiedCommitHash | `43b247d5bf30d4191f8fd5eb4dea9cfd72e4258d`|
| lastVerifiedCommitDate | 2026-09-27T00:14:33+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[overview.md](../overview.md)

## Purpose

Retain a captured family-selected response for subject-navigation regressions.

## Code Commentary

### Logic

The family response records its own selected family context and record-channel availability. It is paired with the invariant-selected response to prove a family read cannot establish a member assessment absence. The fixture is test evidence, not a current production dataset or invented authored judgment.

### Conventions

Keep captured provenance and exact input identities intact. Only the test harness selects these fixtures.

### Invariants And Boundaries

This source supplies scoped regression evidence, not semantic approval, execution certification or a replacement for the real mounted workflow.

### Todos

No additional work is asserted by this card.

## Docs References

No Domain Documentation source is configured; the fixture and regression source establish this local test contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain source could be checked. | — | — |

## Repo-Internal References

The named case or selected revision field is the direct source of this test input.

| Finding | Anchor | Source |
| --- | --- | --- |
| The case or fixture preserves its own selected input. | "revision_selection" | dashboard/src/panels/review/subjectReview.family.captured.json:78-83 |

## Cross-Repo References

No independent cross-repository authority is introduced.

| Finding | Anchor | Source |
| --- | --- | --- |
| No additional cross-repository evidence is required. | — | — |

## Update History

- 2026-09-26T20:20:54Z — Created the scoped source/progression or selected-subject regression card.
