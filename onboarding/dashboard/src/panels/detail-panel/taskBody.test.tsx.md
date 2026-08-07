# dashboard/src/panels/detail-panel/taskBody.test.tsx

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/detail-panel/taskBody.test.tsx`       |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-07T08:19Z                                           |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f`                  |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
| governingOverview      | `../overview.md`                                            |

## Governing Overview

[panels/ overview](../overview.md)

## Purpose

The on-demand task-body suite split from `DetailPanel.test.tsx` by the
260731-EFA-L8 test split. Pins the task-11 on-demand body loading, states, and the
`TaskBodyNotice`.

## Code Commentary

### Logic

Mounts the reader with a task document whose body loads on demand and asserts the
loading/error/settled states and the notice surface.

### Invariants And Boundaries

Assertions preserved from the monolithic suite.

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
| The on-demand task-body suite. | `describe` | dashboard/src/panels/detail-panel/taskBody.test.tsx:11-253 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the
  task-body suite split from `DetailPanel.test.tsx`. Verification pinned to the leaf
  base until closeout stamps the code commit.
