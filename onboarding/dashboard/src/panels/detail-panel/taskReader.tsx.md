# dashboard/src/panels/detail-panel/taskReader.tsx

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/detail-panel/taskReader.tsx`          |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-20T10:45+02:00                                        |
| lastVerifiedCommitHash | `b7f2c8e2c7020642780e2c9b997ffb035a782e62`                  |
| lastVerifiedCommitDate | 2026-08-20T10:42:29+02:00|
| governingOverview      | `../overview.md`                                            |

## Governing Overview

[panels/ overview](../overview.md)

## Purpose

The task-document reader grammar of the DetailPanel, extracted from `DetailPanel.tsx`
by the 260731-EFA-L8 split. Owns `TaskContent`, the master overview/step rendering
(`MasterOverview`, `MasterSection`, `TaskReader`), the sub-task index with cross-series
jumps (`SubTaskIndex`), the slice list, spine lane, section/bullets/step-list
primitives, skipped dispositions, code examples, and the on-demand task-body notice.

## Code Commentary

### Logic

Since 260815-DAG-L14 `SubTaskIndex` also renders typed sprint rows: a row carrying a
`masterRef` (with a projected target via `docPathForRef`) opens the commanded master document
directly through `MasterRefIndexRow` (the `⇒` master link — the sprint → master leg of the
drill-down); an unprojected `masterRef` target falls through to the older slice/static behaviors.

`TaskReaderSections` walks the task document sections; `SubTaskIndex` renders rows and
guards the `linkedLifecycleId` cross-series jump; `TaskBodyNotice` reflects the
on-demand body state; the small primitives (`Section`, `Bullets`, `StepList`,
`CodeExample`) render markdown-model content without a markdown renderer.

### Conventions

Presentational grammar; the panel owns data wiring.

### Invariants And Boundaries

The reader renders `TaskDocNode`/`SeriesNode` content only and never mutates it.

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
| The reader entry and master overview (since 260815-DAG-L12 the master overview also mounts the sprint execution graph section). | `TaskContent`; `MasterOverview`; `TaskReader` | dashboard/src/panels/detail-panel/taskReader.tsx:84-136; dashboard/src/panels/detail-panel/taskReader.tsx:591-603 |
| The sub-task index and section primitives. | `SubTaskIndex`; `SliceList`; `StepList` | dashboard/src/panels/detail-panel/taskReader.tsx:395-433; dashboard/src/panels/detail-panel/taskReader.tsx:436-472; dashboard/src/panels/detail-panel/taskReader.tsx:642-666 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |


## 260815-DAG-L12 Sprint Graph Section

`MasterOverview` now mounts `SprintGraphSection` (L12-R5): for a doc carrying the render-ready `executionGraphView`, the sprint page shows the `Execution graph` section (`SprintGraphView` wave-grid) plus this sprint's scoped `CloseoutQueue` (`sprintRef` = the viewed doc's ref). A non-sprint master returns nothing, so ordinary master reading is unchanged.

## Update History
- 2026-08-20T10:45+02:00 — 260815-DAG-L12: `MasterOverview` now mounts `SprintGraphSection` (the sprint execution graph wave-grid view plus this sprint's CloseoutQueue — L12-R5); claim re-read, citation ranges regenerated, stamp advanced to code commit b7f2c8e2.


- 2026-08-20T04:32+02:00 — 260815-DAG-L14: `SubTaskIndex` renders typed `masterRef` rows as
  `MasterRefIndexRow` (opens the commanded master document directly; unprojected targets fall
  through to older behaviors), and `docPathForRef` is threaded through `TaskContent`,
  `MasterOverview`, `MasterSection`, and `SubTaskIndex`. Verified at code commit 9c3180c1.


- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the reader
  grammar module extracted from `DetailPanel.tsx`. Verification pinned to the leaf
  base until closeout stamps the code commit.
