# mcp/tests/test_closeout_projection_coverage_edges.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_closeout_projection_coverage_edges.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-01T08:13+02:00 |
| lastVerifiedCommitHash |  `47c8d102c2430d5337dbe207d4601efb4844fec0`|
| lastVerifiedCommitDate |  2026-09-01T08:53:56+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Forces the typed error adapters at the closeout-projection, semantic graph-index, and lifecycle
leaf-binding boundaries without changing their production policy.

## Code Commentary

### Logic

The suite makes a field-effect taxonomy failure retain its exact task address and become one
complete unreadable task-source problem. A planning-register refusal becomes one complete invalid
source problem. A semantic graph-index refusal crosses the queue adapter with its exact status and
detail intact. The lifecycle leaf resolver likewise preserves a task-domain binding refusal and
rejects a canonical task source that escapes the repository task root.

### Conventions

- Cases patch one lower-level production boundary at a time and assert the public typed shape.
- Temporary files are used only for the real canonical leaf-source confinement boundary.

### Invariants And Boundaries

- Source problems retain a bounded, complete public shape rather than leaking backend exception
  text or silently dropping the affected source.
- Queue and lifecycle adapters preserve exact typed status/detail and never invent a fallback.
- This is ordinary `unit-regression` evidence, not durable requirement acceptance evidence.

### Todos

None.

## Docs References

No configured external source is needed for these repository-owned regressions.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Field-effect failure retains the task address and yields the complete unreadable source-problem shape. | `test_task_source_error_retains_address_and_projects_as_unreadable` | mcp/tests/test_closeout_projection_coverage_edges.py:53-87 |
| Planning failure yields one complete invalid source-problem shape. | `test_planning_error_projects_as_one_typed_source_problem` | mcp/tests/test_closeout_projection_coverage_edges.py:88-122 |
| The queue graph adapter preserves semantic-index refusal status and detail. | `test_queue_graph_translates_semantic_index_refusal` | mcp/tests/test_closeout_projection_coverage_edges.py:123-147 |
| Lifecycle binding preserves domain refusal identity and rejects an escaped source. | `test_leaf_binding_translates_domain_error_and_refuses_escaped_source` | mcp/tests/test_closeout_projection_coverage_edges.py:148-204 |

## Cross-Repo References

None.

## Update History

- 2026-09-01T08:13+02:00 — Created for the final CCR-R01 candidate's closeout-projection coverage
  edges. The delivery-attempt delta is test-only; production semantics and verification ownership
  remain unchanged and closeout-owned.
