# dashboard/src/panels/lifecycle-list/hierarchy.test.tsx

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/lifecycle-list/hierarchy.test.tsx`    |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-07T08:19Z                                           |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f`                  |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
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

## Update History

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the
  hierarchy suite split from `LifecycleList.test.tsx`. Verification pinned to the
  leaf base until closeout stamps the code commit.
