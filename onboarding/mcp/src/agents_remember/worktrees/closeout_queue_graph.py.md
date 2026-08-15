# mcp/src/agents_remember/worktrees/closeout_queue_graph.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/closeout_queue_graph.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-15T09:10+02:00 |
| lastVerifiedCommitHash | `17987fa66a642306eb8d20fa9a4bff2b881550d2` |
| lastVerifiedCommitDate | 2026-08-15T14:36:30+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[MCP overview](../../../overview.md)

## Purpose

Builds the bounded immutable sprint-graph projection consumed by every queue decision.

## Code Commentary

### Logic

`graph_context` resolves and validates the canonical sprint graph, caps masters/edges/leaves,
computes a revision over the graph plus execution natures, indexes node order, computes incomplete
predecessors once, and parses the canonical planning authorities. `incomplete_predecessor_map`
uses one adjacency construction and one traversal over graph nodes and edges.

### Conventions

The queue's repeated scheduling work consumes this precomputed projection; the inherited task
topology validator remains the canonical reference-integrity authority.

### Invariants And Boundaries

- Missing or over-capacity graphs refuse before queue admission.
- Graph revision changes when execution structure or a master's execution nature changes.
- Predecessor completion is a mechanistic fact, not a priority judgment.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Graph construction validates/caps topology and derives the exact queue revision and indexes. | `graph_context` | mcp/src/agents_remember/worktrees/closeout_queue_graph.py:39-100 |
| Incomplete predecessors are built in one bounded adjacency pass. | `incomplete_predecessor_map` | mcp/src/agents_remember/worktrees/closeout_queue_graph.py:103-119 |

## Cross-Repo References

No meaningful cross-repository reference applies.

## Update History

- 2026-08-15T09:10+02:00 — Created for L3's bounded immutable queue graph projection; verification remains closeout-owned.
