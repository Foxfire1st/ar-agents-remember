# dashboard/src/panels/detail-panel/taskReader.tsx

## Governing Overview

[panels/ overview](../overview.md)

## Purpose

The task-document reader grammar of the DetailPanel, extracted from `DetailPanel.tsx`
by the 260731-EFA-L8 split. Owns `TaskContent`, the master overview/step rendering
(`MasterOverview`, `MasterSection`, `TaskReader`), the sub-task index with cross-series
jumps (`SubTaskIndex`), the slice list, spine lane, section/bullets/step-list
primitives, skipped dispositions, code examples, and the on-demand task-body notice.


## 260831-CCR-L23 Task-Requirement Boundary

L23 mounts a `TaskRequirementBoundary` around both `MasterOverview` and
`TaskReader`. The boundary renders a `TaskRequirementLinksProvider`
(`grammar/TaskRequirementLinks.tsx`) scoped to the viewed task document
(`repo=doc.repository`, `master=dirName(doc.docPath)`,
`document=taskDocumentRefForDoc(doc)?.path`) and forwards the panel's
`onOpenNotes` as its `onOpenArtifact`. Task prose and the mounted
`TaskNotes` surface therefore see the registered requirement listing and can
open requirement packets through the internal reader. Non-requirement rendering is
unchanged.

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

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

- The reader entry and master overview mount optional graph content and the independently scoped queue. [1]
- The sub-task index composes rows in received order. [2]
- The slice list orders and opens authored task documents. [3]
- StepList renders implementation steps, nested substeps, and explicit skip dispositions. [4]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.


## 260815-DAG-L12 Sprint Graph Section

`MasterOverview` mounts optional `SprintGraphSection` graph content and, independently, this sprint's
scoped `CloseoutQueue` (`sprintRef` = the viewed doc's ref). Graph absence is valid for a reviewed
atomic-sequential sprint and does not hide scheduling state. A non-sprint master still omits both
sprint-only surfaces.

## 260821-CLIVE Discard Audit And Graph-Less Scheduling

`DiscardedSubTaskHistory` renders discarded number/name, reason, `discardedAt`, and proof fingerprint
in a separate `Discarded before start` section. It is audit history, not part of the live sub-task list
or completion count. The queue mount is outside the optional graph branch so a graph-less sprint can
still show exact-current scheduling projection state. `MasterOverviewHeader` is a behavior-preserving
extraction of the existing kind/title/status header, body notice, change-set bar, and token summary;
it keeps `MasterOverview` within the function-size gate without changing render order or conditions.
