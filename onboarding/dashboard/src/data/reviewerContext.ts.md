# dashboard/src/data/reviewerContext.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/reviewerContext.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-31T07:35+02:00 |
| lastVerifiedCommitHash | `f2b7c648f540efb9d64ceea22e11e651cb5cc914` |
| lastVerifiedCommitDate |  2026-08-31T15:32:32+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[data overview](overview.md)

## Purpose

Defines the dashboard's shared reviewer-parent validator and the altitude-aware labels rendered for
live reviewer seats.

## Code Commentary

### Logic

`reviewerParentMatches` accepts a reviewer only when its generation-bound structural parent matches
the selected leaf, master, or sprint ownership plane. `reviewerContextLabel` projects the same parent
identity as leaf, master, plan, or super reviewer copy.

### Conventions

Reviewer role alone is insufficient identity; task-document parent plus parent role selects the
review plane.

### Invariants And Boundaries

- Leaf reviewers belong to the owning master manager.
- Master reviewers belong to that master's manager.
- Sprint reviewers retain either architect or orchestrator ownership without collapsing the two.
- Missing or mismatched parent stamps are invalid rather than guessed.

### Todos

None.

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Reviewer ownership is checked at all three topology altitudes. | `reviewerParentMatches` | dashboard/src/data/reviewerContext.ts:11-24 |
| UI labels retain the sprint ownership plane. | `reviewerContextLabel` | dashboard/src/data/reviewerContext.ts:26-36 |

## Cross-Repo References

No cross-repository implementation dependency governs this file.

## Update History

- 2026-08-31T07:35+02:00 — Created for 260821-ARSPAWN-L5 independent-review repair. Verification remains closeout-owned.
