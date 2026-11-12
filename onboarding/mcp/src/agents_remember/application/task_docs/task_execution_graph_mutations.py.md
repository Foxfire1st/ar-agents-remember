# mcp/src/agents_remember/application/task_docs/task_execution_graph_mutations.py

## Governing Overview

[task_docs overview](overview.md)

## Purpose

The one candidate mutation engine for a sprint's execution graph. It holds the typed mutation models of
`author_execution_graph`, the mutable `_GraphDraft` that a batch edits, the handler for each mutation and the
dispatch table, and the batch edge removal that master retirement uses. `task_execution_topology.py` (graph authoring)
and retirement's sprint-edit owner share its edge-deletion operation. It was split
out of `task_execution_topology.py` to keep that file under the repository's size limit; the handlers are unchanged.

## Code Commentary

### Logic

The six mutations are `add_node`, `remove_node`, `add_edge`, `remove_edge`, `move_leaf` and `set_nature`, each a strict
model with an `op` discriminator, collected in `_ExecutionGraphAuthoring`. `_GraphDraft` carries the working node list,
edge list and per-master natures. `_MUTATION_HANDLERS` maps each `op` to its `_apply_*` handler. Judgment-bearing
mutations require a `judgmentId` (`_statically_judgment_bearing`, `_require_mutation_judgment`); a `move_leaf` whose leaf
samples an edge endpoint is refused by `_require_move_does_not_retarget_edge`. `ExecutionTopologyError` is the error
family of this engine.

`_remove_edge_indexes` is the single deletion owner for edges: a named `remove_edge` mutation removes the first matching
edge through it, and `remove_retired_master_edges` removes, in one batch, every edge that touches a retiring master's
nodes. `remove_retired_master_edges` resolves the existing graph once (through the graph's own resolved-edge analysis),
returns the new graph and the list of removed edges, and leaves the nodes in place for the caller to drop.

### Conventions

- The handlers keep the typed refusals (`task-execution-graph-...`) that graph authoring has always raised.
- Names with a leading underscore are shared inside the `task_docs` package, not public API.

### Invariants And Boundaries

- Graph authoring uses this module's draft and mutation handlers; retirement shares its edge-deletion owner.
- Retirement node and membership removal belongs to `task_sprint_candidates._detached_data`, called by
  `task_retirement_sprint_edit` after edge removal; that caller validates the final retirement candidate.

## Evidence

- The draft is the one working copy a batch edits. [1]
- Edge deletion has one owner for a named mutation and for a retirement batch. [2]
- Retirement removes every edge touching the master's nodes in one batch and returns the removed edges. [3]
- A move whose leaf samples an edge endpoint is refused. [4]
