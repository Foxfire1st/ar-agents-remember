# mcp/tests/test_closeout_queue_graph.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_closeout_queue_graph.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-15T13:18+02:00 |
| lastVerifiedCommitHash | `17987fa66a642306eb8d20fa9a4bff2b881550d2` |
| lastVerifiedCommitDate | 2026-08-15T14:36:30+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Owns bounded graph-context resolution and deterministic predecessor projection for the closeout
queue.

## Code Commentary

### Logic

The suite translates task/sprint topology errors, requires explicit graph migration, enforces node,
edge, and leaf capacity limits, and proves incomplete predecessor output follows canonical graph
order.

### Invariants And Boundaries

- The queue accepts only an explicit valid execution graph.
- Capacity bounds are checked at the queue boundary.
- Graph mechanics do not introduce scheduling judgment.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Resolution errors retain queue-specific diagnostics. | `test_graph_context_translates_sprint_and_topology_resolution_errors` | mcp/tests/test_closeout_queue_graph.py:31-43 |
| Every queue graph capacity limit is forced. | `test_graph_context_requires_migration_and_enforces_all_capacity_bounds` | mcp/tests/test_closeout_queue_graph.py:44-93 |
| Predecessors preserve canonical node order. | `test_incomplete_predecessor_map_preserves_graph_order` | mcp/tests/test_closeout_queue_graph.py:90-96 |

## Update History

- 2026-08-15T13:18+02:00 — No content impact: repository Ruff formatting changed only layout;
  bounded graph cases and predecessor ordering are identical.
- 2026-08-15T12:53+02:00 — Created for the focused L3 graph mechanics and admission-cap suite.
