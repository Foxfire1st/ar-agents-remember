# dashboard/src/panels/sprint-graph/SprintGraphPage.test.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/sprint-graph/SprintGraphPage.test.tsx` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-24T12:59+02:00                           |
| lastVerifiedCommitHash | `f95487ec993b58d34911bba0206a7fa6ef9684eb`       |
| lastVerifiedCommitDate | 2026-08-24T15:28:18+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[sprint-graph overview](overview.md)

## Purpose

Shell-level reachability and scenario-reset proof for the real sprint `DetailPanel` surface in the
Operations viewport. The suite pins graph-plus-queue mounting, sprint scoping, graphless queue
reachability, and the dev/test canonical reset clearing both authoritative closeout-queue state and
its mounted derived view. A panel that is exported but unmounted, a stale queue hidden only by
filtering, or a reset that leaves shared queue state behind therefore fails directly.

## Code Commentary

### Logic

`describe("sprint page shell (L12-R5)")` uses typed sprint and queue builders, selects a real sprint
through `DetailPanel`, and exercises four boundaries:

- the wave-grid graph (`sprint-graph`, `Wave 1`) and sprint-scoped closeout queue mount together;
- another sprint's queue does not render;
- a legal graphless atomic-sequential sprint still exposes its closeout queue; and
- a unique nonempty queue is visible through the mounted real surface before
  `dashboardStore.getState().reset()` runs inside React `act`, after which the unfiltered store is
  exactly empty and the queue container, candidate path, and revision/source metadata are absent.

The final case keeps `DetailPanel` mounted and never hand-clears `closeoutQueues`, so it complements
the direct store regression without manufacturing a broader `ScenarioPlayer` fixture.

### Conventions

Use the shared `taskDoc`/`seedTaskDocuments` helpers and a typed `CloseoutQueueNode` builder. Seed
unique visible markers before asserting their absence, and wrap the synchronous store transition in
React `act` so subscriber-driven UI updates settle through the normal mounted boundary.

### Invariants And Boundaries

- Shell-level: the assertion is on the mounted sprint page, closing the
  exported-but-unmounted dead-panel class of defect (L8 R2-F2/F3).
- The queue scoping follows `sameTaskDocumentRef` equality against the viewed sprint ref.
- Reset proof pairs an unfiltered authoritative-store assertion with mounted UI assertions. Sprint
  filtering or task-surface disappearance cannot hide stale queue state and satisfy the contract.
- The canonical reset is dev/test scenario infrastructure. The suite does not change or specify
  production snapshot/delta ingestion, queue ordering/filtering, scheduling, or lifecycle authority.

### Todos

No file-local todos.

## Docs References

No Domain Documentation entries are configured for this repository, and no external library fact
is needed to explain this repository-local mounted regression.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation source is configured for this repository-local test contract. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The shell-level suite pins graph/queue reachability, sprint scoping, graphless queue reachability, and mounted canonical-reset clearance. | "sprint page shell (L12-R5)" | dashboard/src/panels/sprint-graph/SprintGraphPage.test.tsx:53-174 |
| The real sprint page surface rendered. | `DetailPanel` | dashboard/src/panels/detail-panel/DetailPanel.tsx:75-75 |
| The master reader mounts the queue independently of the optional graph section. | `SprintGraphSection`; `CloseoutQueue` | dashboard/src/panels/detail-panel/taskReader.tsx:191-193; dashboard/src/panels/detail-panel/taskReader.tsx:224-233 |
| The sprint-scoped queue implementation reads the authoritative store and renders nothing when no matching queue remains. | `CloseoutQueueImpl` | dashboard/src/panels/CloseoutQueue.tsx:69-83 |
| The canonical store reset clears all scenario projections, including `closeoutQueues`, in one transaction. | `reset` | dashboard/src/data/store.ts:382-400 |

## Cross-Repo References

No cross-repository implementation source governs this file.

## Update History

- 2026-08-24T12:59+02:00 — 260821-DAGQC-L3 curator: extended this card with the forcing mounted
  regression: seed a visible unique queue through the real `DetailPanel`, run the canonical reset
  while mounted, and prove both authoritative store state and queue-derived UI residue disappear.
  Recorded that this is dev/test scenario infrastructure and production queue behavior remains
  unchanged. Verification metadata remains pinned until governed closeout stamps the code commit.

- 2026-08-20T10:45+02:00 — Created for 260815-DAG-L12 (R5): the sprint-page shell test —

graph view + scoped CloseoutQueue mounted on the real DetailPanel, with queue scoping

pinned. Verified at code commit b7f2c8e2.



- 2026-08-20T10:45+02:00 — Created for 260815-DAG-L12 (R5): the sprint-page shell test —
  graph view + scoped CloseoutQueue mounted on the real DetailPanel, with queue scoping
  pinned. Verified at code commit b7f2c8e2.
