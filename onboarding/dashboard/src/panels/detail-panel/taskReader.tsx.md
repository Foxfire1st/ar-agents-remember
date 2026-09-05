# dashboard/src/panels/detail-panel/taskReader.tsx

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/detail-panel/taskReader.tsx`          |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-09-04T01:06+02:00 |
| lastVerifiedCommitHash | `1993dd25bdf8331a2c1e28171dff2bf92ea090e2` |
| lastVerifiedCommitDate | 2026-09-04T00:57:29+02:00 |
| governingOverview      | `../overview.md`                                            |

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

## Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant domain documentation was found. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The reader entry and master overview mount optional graph content and the independently scoped queue. | `TaskContent`; `MasterOverview`; `TaskReader` | dashboard/src/panels/detail-panel/taskReader.tsx:85-132; dashboard/src/panels/detail-panel/taskReader.tsx:167-242; dashboard/src/panels/detail-panel/taskReader.tsx:614-648 |
| The sub-task index composes rows in received order. | "export function SubTaskIndex({" | dashboard/src/panels/detail-panel/taskReader.tsx:464-502 |
| The slice list orders and opens authored task documents. | "export function SliceList({" | dashboard/src/panels/detail-panel/taskReader.tsx:505-541 |
| StepList renders implementation steps, nested substeps, and explicit skip dispositions. | "export function StepList({" | dashboard/src/panels/detail-panel/taskReader.tsx:726-750 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |


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

## Update History

- 2026-09-05T06:38:58+00:00 — CCR L31 dashboard citation curation: re-read the scoped claims against frozen source `ea35964985f30080488270e71ac81657ac40682b`, split pooled evidence and corrected current source boundaries. Historical claims retain their recorded provenance. This is scoped claim review; existing whole-file verification metadata is unchanged.

- 2026-09-04T01:06+02:00 — 260831-CCR-L23 Gate-5 memory pass: recorded the `TaskRequirementBoundary` provider mount around `MasterOverview`/`TaskReader` (requirement listing scoped to the viewed task document, forwarded `onOpenNotes`).

- 2026-08-24T15:04+02:00 — Added separate discard-before-start audit rendering, corrected the
  sprint surface contract (optional graph, independent scoped projection), and recorded the
  behavior-preserving `MasterOverviewHeader` extraction made during commit-hook closure.
- 2026-08-20T10:45+02:00 — 260815-DAG-L12: `MasterOverview` now mounts `SprintGraphSection` (the sprint execution graph wave-grid view plus this sprint's CloseoutQueue — L12-R5); claim re-read, citation ranges regenerated, stamp advanced to code commit b7f2c8e2.


- 2026-08-20T04:32+02:00 — 260815-DAG-L14: `SubTaskIndex` renders typed `masterRef` rows as
  `MasterRefIndexRow` (opens the commanded master document directly; unprojected targets fall
  through to older behaviors), and `docPathForRef` is threaded through `TaskContent`,
  `MasterOverview`, `MasterSection`, and `SubTaskIndex`. Verified at code commit 9c3180c1.


- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the reader
  grammar module extracted from `DetailPanel.tsx`. Verification pinned to the leaf
  base until closeout stamps the code commit.
