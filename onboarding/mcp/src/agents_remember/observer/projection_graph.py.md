# mcp/src/agents_remember/observer/projection_graph.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/observer/projection_graph.py` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-24T13:43+02:00                           |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d`       |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
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

## Docs References

No Domain Documentation sources are configured for this repository-internal projection seam.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation was available after checking the configured source registry. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The structural title protocol requires master-qualified leaf keys. | `GraphNodeLike`; `GraphTitlesLike` | mcp/src/agents_remember/observer/projection_graph.py:35-44; mcp/src/agents_remember/observer/projection_graph.py:47-54 |
| `_node_view` projects titles only through `(node.ref, leaf_id)` and retains local raw-id fallback. | `_node_view` | mcp/src/agents_remember/observer/projection_graph.py:188-225 |
| Public projection forcing proves duplicate local numbers retain the owning master's title. | `TaskDocumentsGraphViewProjectionTests` | mcp/tests/test_task_documents_graph_projection.py:34-272 |
| Builder tests consume the qualified title mapping through the same serving-style walk. | `ExecutionGraphViewBuilderTests` | mcp/tests/test_execution_graph_view.py:129-269 |

## Cross-Repo References

No cross-repository implementation dependency governs this file.

## Update History

- 2026-08-24T13:43+02:00 — DAGQC L1: the primitives-only title protocol and `_node_view`
  now retain `(owning master ref, local leaf id)` through projection, preventing cross-master
  same-number title overwrite. Verification metadata remains pinned until closeout.

- 2026-08-20T10:45+02:00 — Created for 260815-DAG-L12 (R4): the primitives-only render-ready

sprint graph view builder — per-node kind/title/leaf/wave/frontier/nature/predecessor

projection, mechanical frontier derivation, stable node identity. Verified at code commit

b7f2c8e2.



- 2026-08-20T10:45+02:00 — Created for 260815-DAG-L12 (R4): the primitives-only render-ready
  sprint graph view builder — per-node kind/title/leaf/wave/frontier/nature/predecessor
  projection, mechanical frontier derivation, stable node identity. Verified at code commit
  b7f2c8e2.
