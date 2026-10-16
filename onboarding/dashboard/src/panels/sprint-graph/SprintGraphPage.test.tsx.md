# dashboard/src/panels/sprint-graph/SprintGraphPage.test.tsx

## Governing Overview

[sprint-graph overview](overview.md)

## Purpose

Shell-level reachability and scenario-reset proof for the real sprint `DetailPanel` surface in the
Operations viewport. The suite pins inline Order rows plus queue and graph-link reachability, sprint scoping, graphless queue
reachability, and the dev/test canonical reset clearing both authoritative closeout-queue state and
its mounted derived view. A panel that is exported but unmounted, a stale queue hidden only by
filtering, or a reset that leaves shared queue state behind therefore fails directly.

## Code Commentary

### Logic

`describe("sprint page shell (L12-R5)")` uses typed sprint and queue builders, selects a real sprint
through `DetailPanel`, and exercises four boundaries:

- producer-ordered master rows and the sprint-scoped closeout queue are on the page; clicking
  `order-graph-link` then reaches the complete wave grid (`sprint-graph`, `Wave 1`);
- another sprint's queue does not render;
- a legal graphless atomic-sequential sprint has no Order rows or graph link but still exposes
  its closeout queue; and
- a unique nonempty queue is visible through the mounted real surface before
  `dashboardStore.getState().reset()` runs inside React `act`, after which the unfiltered store is
  exactly empty and the queue container, candidate path, and revision/source metadata are absent.

The final case keeps `DetailPanel` mounted and never hand-clears `closeoutQueues`, so it complements
the direct store regression without manufacturing a broader `ScenarioPlayer` fixture.

### Conventions

Use shared taskEntry/taskSummary/seedTaskEntries fixtures and a typed CloseoutQueueNode builder. DetailPanel selects the native sprint’s qualified key; no lifecycle/document projection seed is required. Keep unique visible queue markers and wrap canonical reset in React act so mounted store updates settle normally.

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

## Evidence

### Docs References

No Domain Documentation entries are configured for this repository, and no external library fact
is needed to explain this repository-local mounted regression.

No relevant external documentation source is configured for this repository-local test contract.

### Repo-Internal References

- The shell-level suite pins graph/queue reachability, sprint scoping, graphless queue reachability, and mounted canonical-reset clearance. [1]
- The real sprint page surface rendered. [2]
- The master reader mounts the queue independently of the optional graph section. [3]
- The sprint-scoped queue implementation reads the authoritative store and renders nothing when no matching queue remains. [4]
- The canonical store reset clears all scenario projections, including `closeoutQueues`, in one transaction. [5]

### Cross-Repo References

No cross-repository implementation source governs this file.
