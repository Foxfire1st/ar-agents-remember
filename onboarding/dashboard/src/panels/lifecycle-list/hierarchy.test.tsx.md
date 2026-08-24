# dashboard/src/panels/lifecycle-list/hierarchy.test.tsx

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/lifecycle-list/hierarchy.test.tsx`    |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-24T15:04+02:00                                      |
| lastVerifiedCommitHash | `f95487ec993b58d34911bba0206a7fa6ef9684eb`                  |
| lastVerifiedCommitDate | 2026-08-24T15:28:18+02:00|
| governingOverview      | `../overview.md`                                            |

## Governing Overview

[panels/ overview](../overview.md)

## Purpose

The hierarchy/phase-grouping suite split from `LifecycleList.test.tsx` by the
260731-EFA-L8 test split. Pins row grouping, phase ordering, and collapsible
hierarchy behavior of the Operations list.

## Code Commentary

### Logic

Seeds the collapsible hierarchy projection and asserts group headers, phase
ordering, and re-show behavior.

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
| The hierarchy/grouping suite. | `describe` | dashboard/src/panels/lifecycle-list/hierarchy.test.tsx:19-321 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## 260821-CLIVE Discarded Progress Proof

The suite now proves that a planning master with one live leaf and one discarded-before-start entry
renders `0/1 · 1 discarded`, explicitly not `1/1`. This preserves the distinction between audited
removal and completed execution while leaving hierarchy, phase grouping, collapse behavior, and
long-title coverage unchanged.

## Update History

- 2026-08-24T15:04+02:00 — Added the regression that discarded work is shown separately and does
  not increase completion.

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the
  hierarchy suite split from `LifecycleList.test.tsx`. Verification pinned to the
  leaf base until closeout stamps the code commit.
