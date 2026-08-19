# mcp/tests/test_closeout_queue_graph.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_closeout_queue_graph.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-19T08:55+02:00 |
| lastVerifiedCommitHash | `f2e2f4b9c18d89cc0f5c901f43831e014701aae0` |
| lastVerifiedCommitDate | 2026-08-19T11:32:36+02:00|
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
order. Since 260815-DAG-L11 the suite also forces leaf-awareness: segment-targeted edges block
only that segment's leafs, unplaced/unknown leafs surface as placement facts, candidate
predecessors fall back conservatively to the master's node union when a leaf is unmappable, and
waiting reasons name the segment and its leafs.

### Invariants And Boundaries

- The queue accepts only an explicit valid execution graph.
- Capacity bounds are checked at the queue boundary.
- Graph mechanics do not introduce scheduling judgment.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Resolution errors retain queue-specific diagnostics. | `test_graph_context_translates_sprint_and_topology_resolution_errors` | mcp/tests/test_closeout_queue_graph.py:33-45 |
| Every queue graph capacity limit is forced. | `test_graph_context_requires_migration_and_enforces_all_capacity_bounds` | mcp/tests/test_closeout_queue_graph.py:46-93 |
| Predecessors preserve canonical node order. | `test_incomplete_predecessor_map_preserves_graph_order` | mcp/tests/test_closeout_queue_graph.py:94-101 |
| Leaf-aware queue graph behavior (segment blocking, placement facts, fallback, labels). | `CloseoutQueueSegmentGraphTests` | mcp/tests/test_closeout_queue_graph.py:122-290 |

## Update History

- 2026-08-19T08:55+02:00 — 260815-DAG-L11: added `CloseoutQueueSegmentGraphTests` forcing the
  leaf-aware queue graph (segment-targeted blocking, unplaced/unknown-leaf facts, conservative
  fallback, segment-label waiting reasons). Verification remains closeout-owned.
- 2026-08-15T13:18+02:00 — No content impact: repository Ruff formatting changed only layout;
  bounded graph cases and predecessor ordering are identical.
- 2026-08-15T12:53+02:00 — Created for the focused L3 graph mechanics and admission-cap suite.
