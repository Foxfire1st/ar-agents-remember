# useReviewCatalogue.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/useReviewCatalogue.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-26T19:49:05Z |
| lastVerifiedCommitHash | `43b247d5bf30d4191f8fd5eb4dea9cfd72e4258d`|
| lastVerifiedCommitDate | 2026-09-27T00:14:33+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview.md](overview.md)

## Purpose

Own the recorded-subject catalogue read shared by the task entry and the review workspace.

## Code Commentary

### Logic

The hook calls intentReviewEntries for the repository, master and leaf. It carries the complete recorded subjects and supplied totals, known-empty state, refusal or transport failure. Request sequence and mount guards reject obsolete completions. The returned targetKey must match the current task before any rows are exposed. Refresh increments the same read cycle; projection facts indicate staleness.

### Conventions

Use the existing owner interfaces and exact recorded identities; keep transient task evidence outside durable onboarding.

### Invariants And Boundaries

A pending read for another task exposes no old rows. Catalogue membership and counts come from the read owner; this hook selects no database and creates no family or invariant.

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
| `useReviewCatalogue` owns the behavior described above. | `useReviewCatalogue` | dashboard/src/data/useReviewCatalogue.ts:63-110 |
| `catalogueAnswer` owns the behavior described above. | `catalogueAnswer` | dashboard/src/data/useReviewCatalogue.ts:26-61 |

## Cross-Repo References

No independent cross-repository interface is introduced by this source.

| Finding | Anchor | Source |
| --- | --- | --- |
| No additional cross-repository evidence is required. | — | — |

## Update History

- 2026-09-26T19:49:05Z — Created the shared catalogue reader card and documented target-bound pending reads.
