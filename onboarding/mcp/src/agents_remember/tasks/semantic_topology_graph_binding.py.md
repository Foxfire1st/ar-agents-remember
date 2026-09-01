# mcp/src/agents_remember/tasks/semantic_topology_graph_binding.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/tasks/semantic_topology_graph_binding.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-01T03:58+02:00 |
| lastVerifiedCommitHash |  `47c8d102c2430d5337dbe207d4601efb4844fec0`|
| lastVerifiedCommitDate |  2026-09-01T08:53:56+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Tasks overview](overview.md)

## Purpose

Materializes canonical sprint graph bytes as the recursively immutable runtime graph used by the
semantic-topology context while preserving the persisted wire shape.

## Code Commentary

### Logic

Private frozen Pydantic subclasses replace mutable node, edge, endpoint, and collection members.
The graph retains canonical whole-graph admission; only missing or ambiguous endpoint checks are
deferred until candidate-population binding supplies the complete live leaf population.
`immutable_semantic_topology_graph` is the single construction boundary.

### Conventions

- Private frozen subclasses preserve the public persisted models and their serialized wire shape.

### Invariants And Boundaries

- Persisted task documents remain ordinary mutable authoring models.
- Only an already captured semantic-topology context receives the frozen representation.
- Serialization remains identical to the canonical authored graph bytes.
- Recursive mutation after binding is impossible.

### Todos

None.

## Docs References

No external source is needed for this runtime binding.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Frozen endpoint, node, edge, and graph subclasses preserve the schema while sealing collections. | `_ImmutableSprintExecutionEndpoint`; `_ImmutableSprintExecutionNode`; `_ImmutableSprintExecutionEdge`; `_ImmutableSprintExecutionGraph` | mcp/src/agents_remember/tasks/semantic_topology_graph_binding.py:26-89 |
| Canonical bytes are the only input to immutable materialization. | `immutable_semantic_topology_graph` | mcp/src/agents_remember/tasks/semantic_topology_graph_binding.py:91-102 |

## Cross-Repo References

None.

## Update History

- 2026-09-01T03:58+02:00 — 260831-CCR-L01 Attempt 8: created the deep-immutable graph-binding card.
  Verification remains closeout-owned.
