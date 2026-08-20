# dashboard/src/panels/detail-panel/model.ts

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/detail-panel/model.ts`                |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-20T10:45+02:00 |
| lastVerifiedCommitHash | `b7f2c8e2c7020642780e2c9b997ffb035a782e62` |
| lastVerifiedCommitDate | 2026-08-20T10:42:29+02:00 |
| governingOverview      | `../overview.md`                                            |

## Governing Overview

[panels/ overview](../overview.md)

## Purpose

The pure document-derivation model of the DetailPanel, extracted from
`DetailPanel.tsx` by the 260731-EFA-L8 split. Owns path/slug helpers, the
displayed-reader-doc resolution, the master-document view assembly
(`seriesAsMasterDoc`, `masterDocWithSeriesTokens`), and sub-task key/label helpers.

## Code Commentary

### Logic

Since 260815-DAG-L14 `docPathForTaskRef` resolves a typed `masterRef` against the FULL
projected task-document pool (a sprint commanded master lives in another folder, so
`sliceDocs` can never answer it); undefined when the target is not projected, which is the
caller signal to fall back to the row older behaviors.

`displayedReaderDoc` / `displayedLeafDoc` resolve which task document the reader
shows for a selection; `seriesAsMasterDoc` builds the master view from a series node
(the path whose rows carry `createdAt` for ordering); `masterDocWithSeriesTokens`
merges series tokens into a master document.

### Conventions

Pure functions only — no React, no stores.

### Invariants And Boundaries

The cross-series `→` jump is reachable only when `linkedLifecycleId` is present on a
`TaskSubTaskRefNode`; this module keeps that guard.

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
| The reader-doc resolution entry points. | `displayedReaderDoc`; `displayedLeafDoc` | dashboard/src/panels/detail-panel/model.ts:89-154 |
| The master/series view assembly. | `seriesAsMasterDoc`; `masterDocWithSeriesTokens`; `subTaskKey` | dashboard/src/panels/detail-panel/model.ts:193-208; dashboard/src/panels/detail-panel/model.ts:211-214; dashboard/src/panels/detail-panel/model.ts:221-223 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |


## 260815-DAG-L12 Execution Graph View

`MasterDocView` (the master-document view assembly) now includes the optional `executionGraphView` field (L12-R4/R5), so the sprint page can render the render-ready wave-grid graph directly from the projected master document.


## Update History


- 2026-08-20T10:45+02:00 — 260815-DAG-L12:   `MasterDocView` includes the optional `executionGraphView` (L12-R4/R5). Verified at code commit b7f2c8e2.

- 2026-08-20T04:34+02:00 — 260815-DAG-L14: added `docPathForTaskRef` — resolves a typed
  `masterRef` against the full projected task-document pool (undefined when unprojected, the
  fallback signal for sprint rows). Verified at code commit 9c3180c1.


- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the pure
  model module extracted from `DetailPanel.tsx`. Verification pinned to the leaf
  base until closeout stamps the code commit.
