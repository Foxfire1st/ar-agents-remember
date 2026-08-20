# dashboard/src/panels/sprint-graph/SprintGraphPage.test.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/sprint-graph/SprintGraphPage.test.tsx` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-20T10:45+02:00                           |
| lastVerifiedCommitHash | `b7f2c8e2c7020642780e2c9b997ffb035a782e62`       |
| lastVerifiedCommitDate | 2026-08-20T10:42:29+02:00                        |
| governingOverview      | `overview.md`                                    |

## Governing Overview

[sprint-graph overview](overview.md)

## Purpose

Shell-level reachability proof (260815-DAG-L12 R5): the sprint page must mount the graph
view AND the CloseoutQueue panel, so a panel that is exported but unmounted fails this test
instead of passing silently. The test renders the real `DetailPanel` surface (the sprint
page in the Operations viewport), not the panel in isolation.

## Code Commentary

### Logic

`describe("sprint page shell (L12-R5)")` seeds a sprint task document carrying an
`executionGraphView` plus a `CloseoutQueueNode`, renders `DetailPanel` selected at the
sprint, and asserts the wave-grid graph (`sprint-graph`, `Wave 1`) and the scoped closeout
queue (`closeout-queue`, `rev 3 · graph abababab` revision meta) are both mounted. A second
case proves the queue is scoped to the viewed sprint: another sprint's queue (`rev 9`)
does not render.

### Invariants And Boundaries

- Shell-level: the assertion is on the mounted sprint page, closing the
  exported-but-unmounted dead-panel class of defect (L8 R2-F2/F3).
- The queue scoping follows `sameTaskDocumentRef` equality against the viewed sprint ref.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The shell-level reachability suite. | "sprint page shell (L12-R5)" | dashboard/src/panels/sprint-graph/SprintGraphPage.test.tsx:52-100 |
| The real sprint page surface rendered. | `DetailPanel` | dashboard/src/panels/detail-panel/DetailPanel.tsx:75-75 |
| The section that mounts view + queue. | `SprintGraphSection` | dashboard/src/panels/detail-panel/taskReader.tsx:220-233 |
| The sprint-scoped queue implementation. | `CloseoutQueueImpl` | dashboard/src/panels/CloseoutQueue.tsx:69-82 |

## Cross-Repo References

No cross-repository implementation source governs this file.

## Update History

- 2026-08-20T10:45+02:00 — Created for 260815-DAG-L12 (R5): the sprint-page shell test —

graph view + scoped CloseoutQueue mounted on the real DetailPanel, with queue scoping

pinned. Verified at code commit b7f2c8e2.



- 2026-08-20T10:45+02:00 — Created for 260815-DAG-L12 (R5): the sprint-page shell test —
  graph view + scoped CloseoutQueue mounted on the real DetailPanel, with queue scoping
  pinned. Verified at code commit b7f2c8e2.
