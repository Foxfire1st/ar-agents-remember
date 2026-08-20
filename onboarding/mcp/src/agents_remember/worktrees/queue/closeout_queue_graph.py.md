# mcp/src/agents_remember/worktrees/queue/closeout_queue_graph.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/queue/closeout_queue_graph.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-21T00:45+02:00 |
| lastVerifiedCommitHash | `e5cb139f66abbd6502d4dcc4be883eb5f49770fe` |
| lastVerifiedCommitDate | 2026-08-21T00:28:23+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[MCP overview](../../../overview.md)

## Purpose

Builds the bounded immutable sprint-graph projection consumed by every queue decision, and — since
260815-DAG-L11 — owns the leaf-aware lookups: the leaf-to-node index, candidate-node resolution,
leaf-aware predecessor/waiting-reason/sort-key helpers. Since 260815-DAG-L13 it also owns the
blocker `acquisition_facts` report and the strict/tolerant register-read split.

## Code Commentary

### Logic

`graph_context` resolves and validates the canonical sprint graph, caps masters/edges/leaves,
computes a revision over the graph plus execution natures, indexes node order (keyed on
`SprintExecutionNode`), computes incomplete predecessors once, and parses the canonical planning
authorities. A graph-less sprint refusal now names the atomic-sequential default and the
`task_doc.author_execution_graph` bootstrap. `strict_registers` (default `True`) guards mutations:
a malformed canonical planning register refuses with the `task_doc.set_section` repair named;
the read path (L13-R4) passes `False` so a malformed register degrades the projection instead of
failing it. `acquisition_facts` (L13-R3) reports the in-flight organizational leafs observed at
blocker acquisition — facts only, so the start-anyway decision stays judgment.
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

The queue's repeated scheduling work consumes this precomputed projection; the inherited task
topology validator remains the canonical reference-integrity authority.

### Invariants And Boundaries

- Missing or over-capacity graphs refuse before queue admission; the refusal names the
  atomic-sequential default and the graph-authoring bootstrap.
- Graph revision changes when execution structure or a master's execution nature changes.
- Predecessor completion is a mechanistic fact, not a priority judgment.
- Register malformation is strict for mutations and tolerant for reads; the tolerant read carries
  the malformed detail as register facts.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Graph construction validates/caps topology and derives the exact queue revision and indexes, with the strict/tolerant register split. | `graph_context` | mcp/src/agents_remember/worktrees/queue/closeout_queue_graph.py:79-161 |
| Blocker acquisition reports in-flight organizational leafs as facts only. | `acquisition_facts` | mcp/src/agents_remember/worktrees/queue/closeout_queue_graph.py:36-58 |
| Incomplete predecessors are built in one bounded adjacency pass with master-granular completion. | `incomplete_predecessor_map` | mcp/src/agents_remember/worktrees/queue/closeout_queue_graph.py:279-305 |
| Leaf-aware candidate lookups resolve a candidate to its lump or segment node. | `candidate_node`; `candidate_predecessors` | mcp/src/agents_remember/worktrees/queue/closeout_queue_graph.py:204-211; mcp/src/agents_remember/worktrees/queue/closeout_queue_graph.py:214-227 |
| The queue's sort key and waiting reasons consume the candidate's own node. | `ready_sort_key`; `predecessor_waiting_reasons` | mcp/src/agents_remember/worktrees/queue/closeout_queue_graph.py:237-244; mcp/src/agents_remember/worktrees/queue/closeout_queue_graph.py:247-263 |

## Cross-Repo References

No meaningful cross-repository reference applies.

## Update History

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