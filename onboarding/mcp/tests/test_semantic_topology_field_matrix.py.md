# mcp/tests/test_semantic_topology_field_matrix.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_semantic_topology_field_matrix.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-01T03:58+02:00 |
| lastVerifiedCommitHash |  `47c8d102c2430d5337dbe207d4601efb4844fec0`|
| lastVerifiedCommitDate |  2026-09-01T08:53:56+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Exhaustively verifies that each candidate-relevant persisted field affects the topology fingerprint
exactly when the schema taxonomy classifies it as structural.

## Code Commentary

### Logic

Parameterized mutations cover every field on the parent row, task-document ref, graph node, edge,
endpoint, and graph container. Each case compares the canonical taxonomy effect with the observed
v2 fingerprint change, including canonical ordering and candidate-applicability boundaries.

### Conventions

- Cases mutate canonical production models and take expected effects from the production taxonomy.
- Assertions compare exact v2 fingerprint behavior for one persisted field at a time.

### Invariants And Boundaries

- The expected effect comes from the schema-owned taxonomy, not a duplicated test allowlist.
- These are ordinary regression tests, not durable acceptance evidence.

### Todos

None.

## Docs References

No configured external source is needed for these repository-owned regressions.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Parent-row and ref fields are checked one by one against taxonomy. | `test_every_parent_row_field_uses_its_canonical_taxonomy_effect`; `test_every_task_document_ref_field_uses_its_canonical_taxonomy_effect` | mcp/tests/test_semantic_topology_field_matrix.py:101-170 |
| Node, edge, endpoint, and graph-container fields receive the same exhaustive treatment. | `test_every_candidate_graph_node_field_uses_its_canonical_taxonomy_effect`; `test_every_relevant_edge_field_uses_its_canonical_taxonomy_effect`; `test_every_relevant_endpoint_field_uses_its_canonical_taxonomy_effect`; `test_every_graph_container_field_uses_its_canonical_taxonomy_effect` | mcp/tests/test_semantic_topology_field_matrix.py:172-282 |

## Cross-Repo References

None.

## Update History

- 2026-09-01T03:58+02:00 — 260831-CCR-L01 Attempt 8: created the exhaustive topology field-matrix
  regression card. Verification remains closeout-owned.
