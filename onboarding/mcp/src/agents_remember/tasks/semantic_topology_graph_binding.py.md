# mcp/src/agents_remember/tasks/semantic_topology_graph_binding.py

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

## Evidence

### Docs References

No external source is needed for this runtime binding.

### Repo-Internal References

- Frozen endpoint, node, edge, and graph subclasses preserve the schema while sealing collections. [1]
- Canonical bytes are the only input to immutable materialization. [2]

### Cross-Repo References

None.
