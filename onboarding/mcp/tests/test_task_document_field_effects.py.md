# mcp/tests/test_task_document_field_effects.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_task_document_field_effects.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-01T08:13+02:00 |
| lastVerifiedCommitHash |  `47c8d102c2430d5337dbe207d4601efb4844fec0`|
| lastVerifiedCommitDate |  2026-09-01T08:53:56+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Pins exhaustive task-document field-effect coverage, the explicit structural-plus-normative
classification of leaf identity facts, and refusal of stale or empty taxonomy memberships.

## Code Commentary

### Logic

The tests compare the live recursive schema with the taxonomy, inject a future nested field to
prove refusal, assert that `TaskDocument.id` and `TaskDocument.kind` are both normative and
structural, then monkeypatch stale and empty entries to require typed failure.

### Conventions

- Tests derive coverage from the live production schema and canonical taxonomy owner.
- Assertions require exact structural membership and typed stale/empty refusal details.

### Invariants And Boundaries

- The live schema, not a hand-maintained model count, determines completeness.
- These are ordinary schema regressions, not durable task evidence.

### Todos

None.

## Docs References

No configured external source is needed for these repository-owned regressions.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Recursive schema coverage refuses an unclassified future nested field. | `test_taxonomy_covers_current_schema_and_refuses_a_future_nested_field` | mcp/tests/test_task_document_field_effects.py:16-27 |
| Leaf identity is explicit and stale/empty taxonomy entries refuse. | `test_leaf_identity_shape_stays_normative_and_is_explicitly_structural`; `test_taxonomy_refuses_stale_and_empty_memberships` | mcp/tests/test_task_document_field_effects.py:29-46 |

## Cross-Repo References

None.

## Update History

- 2026-09-01T08:13+02:00 — Clarified that the suite pins dual taxonomy membership for
  `TaskDocument.id` and `TaskDocument.kind`, not a separate leaf-identity table. Verification
  remains closeout-owned.

- 2026-09-01T03:58+02:00 — 260831-CCR-L01 Attempt 8: created the field-effect taxonomy test card.
  Verification remains closeout-owned.
