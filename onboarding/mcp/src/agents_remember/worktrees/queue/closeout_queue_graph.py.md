# mcp/src/agents_remember/worktrees/queue/closeout_queue_graph.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/queue/closeout_queue_graph.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:43+02:00 |
| lastVerifiedCommitHash | `f95487ec993b58d34911bba0206a7fa6ef9684eb` |
| lastVerifiedCommitDate | 2026-08-24T15:28:18+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[MCP overview](../../../overview.md)

## Purpose

Builds the bounded immutable sprint-graph/index/order view used by closeout-projection construction,
including leaf-to-node resolution, predecessor reasons, and deterministic member ordering.

## Code Commentary

### Logic

`graph_context` resolves and validates bounded sprint topology, accepts task-document overrides for
preview, computes node/leaf indexes and incomplete predecessors once, and carries canonical
planning authorities. A reviewed graph-less sprint is the valid atomic-sequential default rather
than an error; graph-backed membership and order remain strict when a graph exists.
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
  refuse.
- Graph revision changes when execution structure or a master's execution nature changes.
- Predecessor completion is a mechanistic fact, not a priority judgment.
- No acquisition or in-flight lane facts are owned here.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Graph construction validates/caps topology and derives the exact queue revision and indexes, with the strict/tolerant register split. | `graph_context` | mcp/src/agents_remember/worktrees/queue/closeout_queue_graph.py:79-161 |
| Incomplete predecessors are built in one bounded adjacency pass with master-granular completion. | `incomplete_predecessor_map` | mcp/src/agents_remember/worktrees/queue/closeout_queue_graph.py:279-305 |
| Leaf-aware candidate lookups resolve a candidate to its lump or segment node. | `candidate_node`; `candidate_predecessors` | mcp/src/agents_remember/worktrees/queue/closeout_queue_graph.py:204-211; mcp/src/agents_remember/worktrees/queue/closeout_queue_graph.py:214-227 |
| The queue's sort key and waiting reasons consume the candidate's own node. | `ready_sort_key`; `predecessor_waiting_reasons` | mcp/src/agents_remember/worktrees/queue/closeout_queue_graph.py:237-244; mcp/src/agents_remember/worktrees/queue/closeout_queue_graph.py:247-263 |

## Cross-Repo References

No meaningful cross-repository reference applies.

## 260821-CLIVE-L2 Graph Failure-Surface Redaction

Sprint resolution, execution-topology validation, and planning-register failures now translate
through the shared bounded queue evidence API. The graph service retains stable refusal statuses
without exposing task contents or lower-level topology details. Its lifecycle-shaped queue state
remains transitional until L3's waiting-only projection rewrite.

| Finding | Source |
| --- | --- |
| Graph construction bounds failures at sprint, topology, and planning-register stages. | mcp/src/agents_remember/worktrees/queue/closeout_queue_graph.py:89-171 |

## 260821-CLIVE Projection Ordering Only

The graph module still owns bounded sprint DAG/index/order and accepts task-document overrides for
preview. It now orders `CloseoutProjectionMember` values and has no mutable-state acquisition facts.
Ready order remains effective priority rank, graph declaration order, then leaf identity. A reviewed
graph-less atomic-sequential sprint is valid; the graph never owns in-flight lane state.

## Update History

- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: reduced graph responsibility to bounded projection ordering and preview. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-24T00:51+02:00 — 260821-CLIVE-L2: reconciled bounded graph and planning-register failures. Verified at code commit `1d446724`.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: source moved to `mcp/src/agents_remember/worktrees/queue/closeout_queue_graph.py` (new package route); the citation fixer repointed in-body references; import paths updated inside the module. Verified at code commit e5cb139f.


- 2026-08-19T22:32+02:00 — 260815-DAG-L13: added `acquisition_facts` (in-flight organizational
  leafs reported at blocker acquisition), the `strict_registers` parameter splitting mutation-strict
  from read-tolerant register parsing, recovery-named register errors, and the graph-less refusal
  now names the atomic-sequential default plus the `author_execution_graph` bootstrap. Verification
  remains closeout-owned.

- 2026-08-19T08:55+02:00 — 260815-DAG-L11: the queue graph projection is leaf-aware — node-keyed
  order and incomplete-predecessor maps, the leaf→node index with derived-placement facts, and the
  extracted `candidate_node`/`candidate_predecessors`/`predecessor_waiting_reasons`/
  `ready_sort_key`/`master_incomplete_predecessors` helpers (moved here from `closeout_queue.py`
  under the file-size rail). Verification remains closeout-owned.

- 2026-08-15T09:10+02:00 — Created for L3's bounded immutable queue graph projection; verification remains closeout-owned.
