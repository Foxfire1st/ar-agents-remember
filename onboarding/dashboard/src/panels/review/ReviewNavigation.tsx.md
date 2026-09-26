# ReviewNavigation.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/ReviewNavigation.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-26T19:49:05Z |
| lastVerifiedCommitHash | `43b247d5bf30d4191f8fd5eb4dea9cfd72e4258d`|
| lastVerifiedCommitDate | 2026-09-27T00:14:33+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[overview.md](../overview.md)

## Purpose

Navigate all recorded families and invariants from inside the review workspace using the shared catalogue.

## Code Commentary

### Logic

useReviewNavigation preserves an explicit subject from the incoming target. Otherwise it chooses the first recorded family, then the first available invariant. A deliberate All source changes choice remains source-only when the catalogue refreshes. CatalogueFamilies substitutes the loaded family subtree once among the remaining recorded family buttons; all invariant subjects stay reachable in their disclosure. Refusal details remain available and do not fabricate an empty family.

### Conventions

Use the existing owner interfaces and exact recorded identities; keep transient task evidence outside durable onboarding.

### Invariants And Boundaries

Catalogue identity and comparison-specific family content have different owners. Loading, unreadable, confirmed empty and explicit source-only selection remain distinct. This module authors no knowledge or assessment.

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
| `useReviewNavigation` owns the behavior described above. | `useReviewNavigation` | dashboard/src/panels/review/ReviewNavigation.tsx:130-145 |
| `initialSubject` owns the behavior described above. | `initialSubject` | dashboard/src/panels/review/ReviewNavigation.tsx:154-162 |
| `ReviewNavigation` owns the behavior described above. | `ReviewNavigation` | dashboard/src/panels/review/ReviewNavigation.tsx:70-127 |
| `CatalogueFamilies` owns the behavior described above. | `CatalogueFamilies` | dashboard/src/panels/review/ReviewNavigation.tsx:164-197 |

## Cross-Repo References

No independent cross-repository interface is introduced by this source.

| Finding | Anchor | Source |
| --- | --- | --- |
| No additional cross-repository evidence is required. | — | — |

## Update History

- 2026-09-26T19:49:05Z — Created the in-review catalogue navigation card.
