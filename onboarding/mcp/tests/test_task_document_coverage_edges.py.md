# mcp/tests/test_task_document_coverage_edges.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_task_document_coverage_edges.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-01T08:13+02:00 |
| lastVerifiedCommitHash |  `47c8d102c2430d5337dbe207d4601efb4844fec0`|
| lastVerifiedCommitDate |  2026-09-01T08:53:56+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Forces defensive task-document graph, field-taxonomy, and composite leaf-binding branches while
preserving the canonical production owners.

## Code Commentary

### Logic

The suite proves the compatibility cycle wrapper still translates indexed validation failure and
that indexed cycle discovery excludes an independent node while accounting exact wave, residual,
and cycle work. It refuses unknown taxonomy models and lost lookups, projects mappings, enum wire
values, and classified subclasses deterministically, then exercises invalid parent/leaf shapes,
split and stem-only identities, and the defensive successful composite-binding path.

### Conventions

- Tests call the production graph, taxonomy, and binding helpers directly with canonical models.
- Defensive cases assert exact typed status/detail or exact operation counts.

### Invariants And Boundaries

- Indexed cycle reporting remains deterministic and names only the actual cycle members.
- Taxonomy lookup cannot infer an unknown model, while supported mappings, enums, and inheritance
  retain canonical projection behavior.
- Composite leaf identity requires the full parent-row/ref/id/stem agreement; no stem fallback is
  accepted.
- This is ordinary `unit-regression` evidence, not durable requirement acceptance evidence.

### Todos

None.

## Docs References

No configured external source is needed for these repository-owned regressions.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The compatibility wrapper translates indexed endpoint failure, and cycle discovery reports exact residual members and work. | `test_cycle_compatibility_wrapper_translates_indexed_validation_error`; `test_indexed_cycle_search_covers_empty_and_multi_residual_paths` | mcp/tests/test_task_document_coverage_edges.py:55-102 |
| Unknown/lost taxonomy models refuse while mappings, enum values, and classified subclasses project canonically. | `test_taxonomy_refuses_unknown_models_and_defensive_lookup_loss`; `test_taxonomy_projects_mapping_enum_and_classified_base_model` | mcp/tests/test_task_document_coverage_edges.py:103-183 |
| Invalid parent and leaf shapes preserve exact binding refusals. | `test_leaf_binding_rejects_invalid_document_and_parent_shapes` | mcp/tests/test_task_document_coverage_edges.py:184-239 |
| Split and stem-only identities refuse while the complete defensive binding path succeeds. | `test_leaf_binding_detects_split_stem_and_keeps_defensive_success_path` | mcp/tests/test_task_document_coverage_edges.py:240-296 |

## Cross-Repo References

None.

## Update History

- 2026-09-01T08:13+02:00 — Created for the final CCR-R01 candidate's task-document coverage
  edges. The delivery-attempt delta is test-only; production semantics and verification ownership
  remain unchanged and closeout-owned.
