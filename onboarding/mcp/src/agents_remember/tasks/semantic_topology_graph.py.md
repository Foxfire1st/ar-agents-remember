# mcp/src/agents_remember/tasks/semantic_topology_graph.py

## Governing Overview

[Tasks overview](overview.md)

## Purpose

Builds the one deep-immutable, bounded, indexed sprint-graph context from which every candidate's
semantic-topology placement is read.

## Code Commentary

### Logic

`build_semantic_topology_graph_index` compares separately resolved authored and canonical graph
bytes, performs a cheap pre-admission lower-bound check, materializes one immutable snapshot, admits
the complete graph once, and builds node, leaf-placement, and incident-edge indexes. The returned
`SemanticTopologyGraphIndex` exposes candidate and whole-population reads with exact work counters.
Graph validation, snapshot, build, and candidate work are independently accounted under the closed
`MAX_SEMANTIC_TOPOLOGY_GRAPH_WORK` budget; an over-budget population refuses before immutable
admission.

### Conventions

- Indexes preserve authored declaration order wherever deterministic order is observable.
- Published indexes use read-only mappings, and work records expose named exact counters.

### Invariants And Boundaries

- Authored and resolved graph bytes must match before the index is usable.
- The returned bound graph and all indexed collections are recursively immutable.
- Whole-graph admission occurs exactly once per context and candidate reads never rescan the graph.
- The work budget counts scalar bytes as well as collection operations.
- Unknown placements and every mismatch carry typed, actionable refusal status/detail.

### Todos

None.

## Evidence

### Docs References

No external source is needed for this repository-owned graph index.

### Repo-Internal References

- Validation, build, population, and candidate work have separate immutable counters. [1]
- The graph index owns the sole bound graph and candidate slice APIs. [2]
- Construction enforces the lower bound and exact total budget before publishing an index. [3]
- Canonical capture, immutable binding, and indexed node/edge population are one bounded pipeline. [4]

### Cross-Repo References

None.
