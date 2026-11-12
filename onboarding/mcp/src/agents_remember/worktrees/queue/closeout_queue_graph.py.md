# mcp/src/agents_remember/worktrees/queue/closeout_queue_graph.py

## Governing Overview

[queue overview](overview.md)

## Purpose

Builds the bounded immutable sprint-graph/index/order view used by closeout-projection construction,
including leaf-to-node resolution, predecessor reasons, and deterministic member ordering.

## Code Commentary

### Logic

`graph_context` resolves and validates bounded sprint topology, accepts task-document overrides for
preview, computes node/leaf indexes and incomplete predecessors once, and carries canonical
planning authorities. A reviewed graph-less sprint is the valid atomic-sequential default rather
than an error; that default describes the sprint's shape — every commanded master executes
atomically — and serializes nothing, so the graph never introduces a dependency between its
masters. Graph-backed membership and order remain strict when a graph exists.
`incomplete_predecessor_map` uses one adjacency construction and one traversal over
graph nodes and edges; completion stays master-granular — a node counts complete when its master
document is `Completed`, so an edge into a segment blocks exactly that segment's leafs until the
predecessor's whole master completes (L11-R3). `_leaf_node_index` folds authored and derived
(L11-R2) leaf placements into one leaf→node index and collects the unplaced/unknown-leaf facts the
queue response reports. `candidate_node` maps one candidate to the lump or its leaf's segment
node; `candidate_predecessors`, `predecessor_waiting_reasons`, `predecessor_label`,
`ready_sort_key` (priority rank, then candidate-node declaration order, then leaf identity), and
`master_incomplete_predecessors` serve the queue and the portfolio loop, with an unmappable leaf
falling back conservatively to the master's node union.

### Conventions

Projection construction consumes this precomputed view; the inherited task
topology validator remains the canonical reference-integrity authority.

### Invariants And Boundaries

- An absent graph is valid atomic-sequential topology; malformed or over-capacity authored graphs
  refuse. The surviving capacity refusals bound graph *shape* only and name their own codes —
  `closeout-queue-master-capacity-exceeded` above `MAX_CLOSEOUT_MASTERS` graph nodes and
  `closeout-queue-edge-capacity-exceeded` above `MAX_CLOSEOUT_GRAPH_EDGES` dependency edges. No
  refusal bounds how many leaves the sprint's masters declare: that candidate ceiling and its
  `closeout-queue-capacity-exceeded` code were removed by 260913-LCA-L6.
- Since 260913-LCA-L7 both refusals raise through `closeout_queue_errors.py`'s
  `MASTER_CAPACITY_EXCEEDED` and `EDGE_CAPACITY_EXCEEDED` constants rather than inline code literals,
  so a rename moves the raiser and the `closeout_projection` classifier together and the projection
  reports a sprint past its graph bound as an invalid source, never as one that could not be read.
- Graph revision changes when execution structure or a master's execution nature changes.
- Predecessor completion is a mechanistic fact, not a priority judgment.
- **Predecessor resolution is terminal, not Completed-only (master abandonment):** the blocking set
  is built with `tasks/readiness.py::master_is_terminal`, so a predecessor master that was
  `abandoned` resolves exactly like a `Completed` one and stops blocking its successors. Leaving
  dependents blocked forever would make abandoning a master worse than doing nothing.
- No acquisition or in-flight lane facts are owned here.
- For a graph-less sprint, the user-facing `task-execution-topology-migration-required` refusal now
  states the ruling: "sprint has no executionGraph; the sprint runs atomic-sequentially by default
  (every commanded master executes atomically and no dependency is declared, so nothing serializes
  the masters)". Series-contract presence is not a lane owner and per-contract activation excludes
  no sibling master.

### Todos

None recorded.

## Evidence

### Docs References

No configured Domain Documentation source applies.

### Repo-Internal References

- Graph construction binds the caller's authored graph to one validated deep-immutable semantic index, then derives the exact queue revision and indexes with the strict/tolerant register split. [1]
- Incomplete predecessors are built in one bounded adjacency pass with master-granular terminal resolution. [2]
- Leaf-aware candidate lookups resolve a candidate to its lump or segment node. [3]
- The queue's sort key and waiting reasons consume the candidate's own node. [4]

### Cross-Repo References

No meaningful cross-repository reference applies.

## 260821-CLIVE-L2 Graph Failure-Surface Redaction

Sprint resolution, execution-topology validation, and planning-register failures now translate
through the shared bounded queue evidence API. The graph service retains stable refusal statuses
without exposing task contents or lower-level topology details. Its lifecycle-shaped queue state
remains transitional until L3's waiting-only projection rewrite.

- Graph construction bounds failures at sprint, semantic topology, and planning-register stages. [5]
- Graph admission refuses only graph-shape capacity (masters, then edges) before topology validation, raising through the constants the errors module declares; the declared-leaf count is no longer summed or bounded. [6]

## 260821-CLIVE Projection Ordering Only

The graph module still owns bounded sprint DAG/index/order and accepts task-document overrides for
preview. It now orders `CloseoutProjectionMember` values and has no mutable-state acquisition facts.
Ready order remains effective priority rank, graph declaration order, then leaf identity. A reviewed
graph-less atomic-sequential sprint is valid; the graph never owns in-flight lane state.
