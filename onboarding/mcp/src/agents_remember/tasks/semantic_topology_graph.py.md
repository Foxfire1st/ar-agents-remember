# mcp/src/agents_remember/tasks/semantic_topology_graph.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/tasks/semantic_topology_graph.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-01T03:58+02:00 |
| lastVerifiedCommitHash |  `47c8d102c2430d5337dbe207d4601efb4844fec0`|
| lastVerifiedCommitDate |  2026-09-01T08:53:56+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No external source is needed for this repository-owned graph index.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Validation, build, population, and candidate work have separate immutable counters. | "Exact bounded collection operations performed while building one index." | mcp/src/agents_remember/tasks/semantic_topology_graph.py:44-146 |
| The graph index owns the sole bound graph and candidate slice APIs. | "Immutable canonical graph projections and constant-time placement indexes." | mcp/src/agents_remember/tasks/semantic_topology_graph.py:199-258 |
| Construction enforces the lower bound and exact total budget before publishing an index. | `build_semantic_topology_graph_index`; `_require_minimum_work_budget`; `_require_exact_work_budget` | mcp/src/agents_remember/tasks/semantic_topology_graph.py:264-417 |
| Canonical capture, immutable binding, and indexed node/edge population are one bounded pipeline. | `_canonical_graph_capture`; `_validated_graph_binding`; `_incident_edge_index`; `_node_lookup_indexes` | mcp/src/agents_remember/tasks/semantic_topology_graph.py:419-716 |

## Cross-Repo References

None.

## Update History

- 2026-09-01T03:58+02:00 — Checklist follow-up: re-read the exact work records and graph-index
  definition in the uncommitted new source and retained their current ranges; verification remains
  closeout-owned.

- 2026-09-01T03:58+02:00 — 260831-CCR-L01 Attempt 8: created the bounded immutable semantic graph
  index card. Verification remains closeout-owned.
