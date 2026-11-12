# mcp/src/agents_remember/tasks/execution_graph_validation.py

## Governing Overview

[Tasks overview](overview.md)

## Purpose

Implements the task schema's one-pass intrinsic sprint-execution-graph admission algorithm. One
endpoint index and one resolved-edge population serve uniqueness, ownership, DAG, wave, and cycle
checks while exposing exact operation counts.

## Code Commentary

### Logic

`validate_execution_graph` builds indexed node/ref/leaf endpoint lookups, resolves every edge once,
checks duplicate nodes and resolved edges, lump/segment ownership, leaf ownership, self-edges, and
endpoint ambiguity, then derives deterministic topological waves. A cyclic graph returns the exact
cycle members. `ExecutionGraphValidationWork` counts each collection operation and accompanies both
successful `ExecutionGraphAnalysis` and typed `ExecutionGraphValidationError` refusal. The minimum
successful-work function supplies a pre-admission lower bound without traversing the population.

### Conventions

- Integer indexes retain authored declaration order for deterministic output.
- Work fields use exact operation names and counts; they never stand in for elapsed-time timing.

### Invariants And Boundaries

- Admission is linear in the indexed node/leaf/edge population; public endpoint scans are not used.
- One resolved-edge population feeds validation, waves, and cycle analysis.
- Declaration order determines deterministic wave and cycle ordering.
- This is an internal schema algorithm; public task-document models translate its refusal to their
  existing `ValueError` validation surface.

### Todos

None.

## Evidence

### Docs References

No external source is needed for this repository-owned graph admission algorithm.

### Repo-Internal References

- Exact intrinsic work is a first-class immutable result. [1]
- Canonical admission and the cheap successful-work lower bound share one operation vocabulary. [2]
- Indexed endpoint resolution visits each edge once. [3]
- Wave and cycle derivation consume the resolved adjacency without rescanning endpoints. [4]

### Cross-Repo References

None.
