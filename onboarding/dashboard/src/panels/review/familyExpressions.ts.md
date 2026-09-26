# familyExpressions.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/familyExpressions.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-26T19:49:05Z |
| lastVerifiedCommitHash | `43b247d5bf30d4191f8fd5eb4dea9cfd72e4258d`|
| lastVerifiedCommitDate | 2026-09-27T00:14:33+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[overview.md](../overview.md)

## Purpose

Group carried family realization claims into deduplicated expression summaries without changing their recorded identity.

## Code Commentary

### Logic

carriedMembership preserves before and after membership rows. familyExpressionExcerpts first counts changed, resolved and unmeasured realization outcomes, groups changed claims by path plus recorded source identity, then attaches all per-side readings for those keys. Observed identities are readings, never part of the grouping key. Occurrences retain exact revision IDs and sides; deterministic ordering stabilizes the presentation.

### Conventions

Use the existing owner interfaces and exact recorded identities; keep transient task evidence outside durable onboarding.

### Invariants And Boundaries

Different recorded blobs at the same path remain distinct. A path resolved on one side and mismatched on the other remains one expression with both readings. These realization-resolution counts are not the measured source-change inventory and imply no semantic assessment.

### Todos

No additional work is asserted by this card.

## Docs References

No Domain Documentation source is configured. The implementation-specific account is grounded in the repository source below.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain source could be checked. | — | — |

## Repo-Internal References

The named constructs own this behavior; reads and validation use their existing callers and models.

| Finding | Anchor | Source |
| --- | --- | --- |
| `carriedMembership` owns the behavior described above. | `carriedMembership` | dashboard/src/panels/review/familyExpressions.ts:21-26 |
| `familyExpressionExcerpts` owns the behavior described above. | `familyExpressionExcerpts` | dashboard/src/panels/review/familyExpressions.ts:185-202 |
| `excerptKey` owns the behavior described above. | `excerptKey` | dashboard/src/panels/review/familyExpressions.ts:64-66 |
| `recordSideReadings` owns the behavior described above. | `recordSideReadings` | dashboard/src/panels/review/familyExpressions.ts:147-168 |

## Cross-Repo References

No independent cross-repository interface is introduced by this source.

| Finding | Anchor | Source |
| --- | --- | --- |
| No additional cross-repository evidence is required. | — | — |

## Update History

- 2026-09-26T19:49:05Z — Moved the existing pure family-expression grouping account from the center to its extracted owner.
