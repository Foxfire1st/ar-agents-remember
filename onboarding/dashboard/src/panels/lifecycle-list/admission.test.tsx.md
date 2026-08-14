# dashboard/src/panels/lifecycle-list/admission.test.tsx

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/lifecycle-list/admission.test.tsx`    |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-07T08:19Z                                           |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`                  |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `../overview.md`                                            |

## Governing Overview

[panels/ overview](../overview.md)

## Purpose

The row-admission suite split from `LifecycleList.test.tsx` by the 260731-EFA-L8
test split (22-name set reconciled item-for-item). Pins which task labels admit rows
into the Operations list.

## Code Commentary

### Logic

Seeds projections with mixed lifecycle/doc kinds and asserts the admitted rows and
their labels per the admission rule.

### Invariants And Boundaries

Assertions preserved from the monolithic suite; shared cleanup from
`test-utils.tsx`.

### Todos

None recorded.

## Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant domain documentation was found. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The row-admission suite. | `describe` | dashboard/src/panels/lifecycle-list/admission.test.tsx:18-575 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the
  admission suite split from `LifecycleList.test.tsx`. Verification pinned to the
  leaf base until closeout stamps the code commit.
