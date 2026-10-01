# mcp/src/agents_remember/observer/projection_graph.py

## Governing Overview

[observer overview](overview.md)

## Purpose

The render-ready sprint execution graph projection builder (260815-DAG-L12 R4). The
persisted `executionGraph` ships raw refs and leaf ids; this module turns it into the
per-node view the dashboard renders directly — node kind, master ref + title, leaf ids +
titles, derived wave index, mechanically derived frontier state, execution nature, and
predecessors with their recorded reasons. The frontend never joins raw paths or re-derives
waves/state.

## Code Commentary

### Logic

Layer contract: the `observer` package must not import the `tasks` package, so this module
is **primitives-only**. The serving layer (which may import `tasks`) walks the persisted
graph — derived waves, resolved edge endpoints, joined titles, per-master status/nature
facts — and feeds this builder plain data. The structural protocols (`GraphNodeLike`,
`GraphTitlesLike`) declare exactly the surface the builder consumes; the concrete types
live in `agents_remember.tasks`.

- `TaskExecutionPredecessorNode` / `TaskExecutionNodeView` / `TaskExecutionGraphView`
  (`extra="forbid"`): the served per-node model. `nodeId` is a stable semantic identity — a
  lump's master ref key, or the ref key plus a segment ordinal for a segmented master
  (`node_identity`). `waveIndex` is the 1-based derived wave.
- `MasterGraphFacts`: primitives-only per-master facts (task status, execution nature,
  per-leaf declared statuses) the frontier derivation needs; missing entries project a
  conservative frontier state (never landed, never in-flight).
- `GraphPredecessorFacts`: one resolved predecessor edge — the predecessor node plus its
  recorded reason and optional judgment id.
- `GraphTitlesLike` keeps leaf-title identity as `(TaskDocumentRef, leaf id)`. `_node_view`
  performs that qualified lookup for every segment leaf, so a same-numbered row in another master
  cannot overwrite the projected title; an absent qualified key falls back only to the local raw
  leaf id.
- `_frontier_state`: mechanical precedence — landed (master `Completed`, or every sampled
  leaf `Completed`) → waiting (any predecessor not landed) → in-flight (master or any
  sampled leaf `inProgress`/`blocked`) → ready. Reads statuses and edges only; never
  invents priority/reason judgment.
- `build_execution_graph_view`: takes `nodes` in declaration order, `waves` ordered by
  derived wave (nodes within a wave in declaration order), `predecessor_edges` keyed by
  successor node, per-master facts, and joined titles; emits the view ordered by derived
  wave then node order, so a re-render with an unchanged graph is byte-stable.

### Conventions

- Missing masters project ref-key/leaf-id fallback labels and a conservative frontier.
- A missing-master frontier falls back to `ready` (never landed, never in-flight) — the
  optimistic-mechanical default, documented and test-pinned (reviewer finding F6).

### Invariants And Boundaries

- The observer package never imports `tasks`; the serving seam does the tasks-domain walk.
- The builder is pure: no writes, no scheduler interpretation, no judgment synthesis.
- The dashboard renders projected facts verbatim and never joins raw refs.
- Projection never performs a flat leaf-number title lookup; owning-master identity is retained
  through the structural protocol.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation sources are configured for this repository-internal projection seam.

No relevant external documentation was available after checking the configured source registry.

### Repo-Internal References

- The structural title protocol requires master-qualified leaf keys. [1]
- `_node_view` projects titles only through `(node.ref, leaf_id)` and retains local raw-id fallback. [2]
- Public projection forcing proves duplicate local numbers retain the owning master's title. [3]

### Cross-Repo References

No cross-repository implementation dependency governs this file.
