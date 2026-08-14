# dashboard/src/panels/detail-panel/masterSeries.test.tsx

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/detail-panel/masterSeries.test.tsx`   |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-07T08:19Z                                           |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`                  |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `../overview.md`                                            |

## Governing Overview

[panels/ overview](../overview.md)

## Purpose

The master/series navigation suite split from `DetailPanel.test.tsx` by the
260731-EFA-L8 test split. Pins the 6g master overview, sub-task index, drill-in, and
cross-series navigation behavior of the detail reader.

## Code Commentary

### Logic

Seeds a master with sub-task refs and a linked series; asserts the index rows, the
in-panel drill-in, and the `linkedLifecycleId` cross-series jump.

### Invariants And Boundaries

Uses the shared `test-utils.tsx` seeds (`seedSeriesOrdering`, `seedTaskDocuments`);
assertions preserved from the monolithic suite.

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
| The master-series navigation suite. | `describe` | dashboard/src/panels/detail-panel/masterSeries.test.tsx:15-411 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the
  master-series suite split from `DetailPanel.test.tsx`. Verification pinned to the
  leaf base until closeout stamps the code commit.
