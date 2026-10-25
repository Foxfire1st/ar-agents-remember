# dashboard/src/panels/sprint-graph/SprintGraphView.tsx

## Governing Overview

[sprint-graph overview](overview.md)

## Purpose

The sprint execution graph wave-grid view (260815-DAG-L12 R2/R6). The backend projects a
render-ready per-node model (`executionGraphView`) — kind, master ref + title, leaf ids +
titles, derived wave index, frontier state, execution nature, and predecessors with
reasons. Those remain graph facts; each box separately resolves its qualified master reference in the existing task-entry store for the shared task-state word and tone. The component does not derive graph waves or task stage/activity.

## Code Commentary

### Logic

`SprintGraphViewImpl` groups the supplied nodes into ordered wave rows and renders one GraphBox per supplied unit. GraphBox subscribes to its exact taskReferenceKey in the existing dashboard store. taskStatusKey/statusLabel/StatusWord supply the task-state text, tone and accessible label, so an entry change updates the box even when the graph object is unchanged. A missing entry renders no task-status badge and its accessible label says task unavailable; it does not borrow landed/in-flight/abandoned as a task state.

The separate dependency annotation is ready or waiting, with cycle taking precedence. Graph-supplied membership, leaf lists, lump presentation and Markdown predecessor reasons remain. Complete-graph membership is not filtered to unfinished tasks. Memoization does not introduce a cache, poll or second task-state producer.

### Shared marking and Markdown edges

useRestHighlight waits GRAPH_REST_MS (180ms) before pointer marking, preserves the old mark while
resting on a neighbor and marks keyboard focus immediately. The whole graph also supports a pinned
node surviving blur. relatedGraphNodes includes the selected master's segments, its predecessors and
its dependents by qualified references. Both helpers are shared by the inline sprint Order rows.
useReducedMotion disables the fade, not the rest. Unmount clears the outstanding timer.
GraphPredecessors renders the edge reason through inline Markdown, preserving actual links.
These interactions do not replace graph wave/readiness authority or the task-entry state owner, and introduce no second graph model.

### Conventions

- Deterministic render: nodes arrive ordered; the component preserves that order.
- Test-surface attributes (`data-testid`, `data-node`, `data-readiness`) are part of the
  component contract for the L12-R7 mounted-UI proof.

### Invariants And Boundaries

- Graph titles and wave/readiness facts remain supplied; qualified reference lookup is only for the native task entry and its shared status presentation.
- A node without predecessors renders no label list (zero-edge graphs show independent
  boxes).

### Todos

None.


**L184 — INV-XZYGEB.** This view is one of the named places that show one task's word. The obligation this leaf records for this place is stated in the invariant named here; the card's earlier account of this file stands, and this paragraph adds what the change made true.

## Evidence

### Repo-Internal References


- The wave-grid component and box renderer. [1]

- The wire model consumed. [2]

- The responsive grid/leaf contracts. [3]


- The component forcing suite. [4]

- The sprint Order own view mounts this complete graph rather than a second inline wave-grid list. [5]

### Cross-Repo References

No cross-repository implementation source governs this file.
