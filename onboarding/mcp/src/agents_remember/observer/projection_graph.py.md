# mcp/src/agents_remember/observer/projection_graph.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/observer/projection_graph.py` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-20T10:45+02:00                           |
| lastVerifiedCommitHash | `b7f2c8e2c7020642780e2c9b997ffb035a782e62`       |
| lastVerifiedCommitDate | 2026-08-20T10:42:29+02:00                        |
| governingOverview      | `overview.md`                                    |

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

### Todos

None.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The render-ready per-node graph view model. | `TaskExecutionGraphView` | mcp/src/agents_remember/observer/projection_graph.py:114-123 |
| The per-node view with derived wave and frontier. | `TaskExecutionNodeView` | mcp/src/agents_remember/observer/projection_graph.py:91-111 |
| The primitives-only builder fed by the serving seam. | `build_execution_graph_view` | mcp/src/agents_remember/observer/projection_graph.py:228-260 |
| Stable lump/segment node identity. | `node_identity` | mcp/src/agents_remember/observer/projection_graph.py:126-136 |
| The serving layer's tasks-domain walk that feeds this builder. | `_execution_graph_view` | mcp/src/agents_remember/serving/projections/snapshots_impl/_task_documents.py:327-367 |
| The wire schema (generated TS mirrors the served models). | `TaskExecutionGraphView` | dashboard/src/types/projection.ts:561-565 |
| The graph-view builder forcing suite. | `ExecutionGraphViewBuilderTests` | mcp/tests/test_execution_graph_view.py:129-265 |

## Cross-Repo References

No cross-repository implementation dependency governs this file.

## Update History

- 2026-08-20T10:45+02:00 — Created for 260815-DAG-L12 (R4): the primitives-only render-ready

sprint graph view builder — per-node kind/title/leaf/wave/frontier/nature/predecessor

projection, mechanical frontier derivation, stable node identity. Verified at code commit

b7f2c8e2.



- 2026-08-20T10:45+02:00 — Created for 260815-DAG-L12 (R4): the primitives-only render-ready
  sprint graph view builder — per-node kind/title/leaf/wave/frontier/nature/predecessor
  projection, mechanical frontier derivation, stable node identity. Verified at code commit
  b7f2c8e2.
