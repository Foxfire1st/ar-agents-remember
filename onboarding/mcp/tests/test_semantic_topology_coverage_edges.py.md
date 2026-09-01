# mcp/tests/test_semantic_topology_coverage_edges.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_semantic_topology_coverage_edges.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-01T08:13+02:00 |
| lastVerifiedCommitHash |  `47c8d102c2430d5337dbe207d4601efb4844fec0`|
| lastVerifiedCommitDate |  2026-09-01T08:53:56+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Forces the remaining fail-closed branches of `semantic-topology/v2` projection and its bounded
immutable graph index.

## Code Commentary

### Logic

The suite rejects a DAG index supplied to graphless atomic mode, an unknown canonical-binding
status, an incompletely consumed indexed projection, taxonomy and projected-shape failures, and an
ambiguous candidate placement. It separately preserves taxonomy failure through graph-index
construction, forces both post-capture work-budget guards, counts a self-incident edge once, and
rejects a blank immutable leaf id.

### Conventions

- Each case changes one internal contract fact and asserts the exact public typed refusal.
- Work-budget assertions use exact named counts, never elapsed-time thresholds.

### Invariants And Boundaries

- Unknown classifications, versions, binding statuses, shapes, or placements fail closed.
- Graphless and DAG contexts cannot be mixed.
- Both lower-bound and exact work-budget enforcement remain active after capture.
- This is ordinary `unit-regression` evidence, not durable requirement acceptance evidence.

### Todos

None.

## Docs References

No configured external source is needed for these repository-owned regressions.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Graphless mode rejects a supplied DAG context, and unknown binding status fails closed. | `test_graphless_projection_rejects_a_dag_context`; `test_unknown_leaf_binding_status_is_not_translated_by_default` | mcp/tests/test_semantic_topology_coverage_edges.py:65-107 |
| Indexed placement must be fully consumed, structurally valid, and unambiguous. | `test_invalid_indexed_projection_is_a_typed_schema_refusal`; `test_structural_projection_translates_taxonomy_and_shape_failures`; `test_candidate_slice_refuses_ambiguous_index_membership` | mcp/tests/test_semantic_topology_coverage_edges.py:108-179 |
| Graph-index taxonomy failure and both work-budget guards preserve exact typed refusal. | `test_graph_index_translates_taxonomy_failure`; `test_both_post_capture_work_budget_guards_refuse` | mcp/tests/test_semantic_topology_coverage_edges.py:180-246 |
| Self-incident attachment is unique and immutable leaf ids cannot be blank. | `test_self_incident_edge_attaches_once_and_blank_leaf_refuses` | mcp/tests/test_semantic_topology_coverage_edges.py:247-253 |

## Cross-Repo References

None.

## Update History

- 2026-09-01T08:13+02:00 — Created for the final CCR-R01 candidate's semantic-topology coverage
  edges. The delivery-attempt delta is test-only; production semantics and verification ownership
  remain unchanged and closeout-owned.
