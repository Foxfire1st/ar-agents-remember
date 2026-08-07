# dashboard/src/panels/detail-panel/taskReader.tsx

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/detail-panel/taskReader.tsx`          |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-07T08:19Z                                           |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f`                  |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
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
| The reader entry and master overview. | `TaskContent`; `MasterOverview`; `TaskReader` | dashboard/src/panels/detail-panel/taskReader.tsx:77-125; dashboard/src/panels/detail-panel/taskReader.tsx:494-529 |
| The sub-task index and section primitives. | `SubTaskIndex`; `SliceList`; `StepList` | dashboard/src/panels/detail-panel/taskReader.tsx:323-358; dashboard/src/panels/detail-panel/taskReader.tsx:361-397; dashboard/src/panels/detail-panel/taskReader.tsx:567-591 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the reader
  grammar module extracted from `DetailPanel.tsx`. Verification pinned to the leaf
  base until closeout stamps the code commit.
