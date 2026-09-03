# mcp/tests/test_task_document_field_effects.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_task_document_field_effects.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash |  `3e276f2b2052b641afbee180a472259f21b500df`|
| lastVerifiedCommitDate |  2026-09-02T14:46:34+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Pins exhaustive task-document field-effect coverage, the explicit structural-plus-normative
classification of leaf identity facts, refusal of stale or empty taxonomy memberships, and the
exact before/candidate mutation-class derivation that decides projection invalidation.

## Code Commentary

### Logic

The tests compare the live recursive schema with the taxonomy, inject a future nested field to
prove refusal, assert that `TaskDocument.id` and `TaskDocument.kind` are both normative and
structural, then monkeypatch stale and empty entries to require typed failure.

The L04 mutation-classification half drives the exact delta matrix: top-level id/title/status/
references/statusNote edits map to the canonical classes (topology+intent, intent,
completion-readiness, acceptance-evidence, operational-audit), nested step changes classify by the
changed leaf field rather than the container, a new document classifies as exhaustive, a missing
effect-to-mutation mapping refuses, incompatible or unclassified nested models refuse with the
persisted-model identity, and mapping/model union variants preserve all owned effects.

### Conventions

- Tests derive coverage from the live production schema and canonical taxonomy owner.
- Assertions require exact structural membership and typed stale/empty refusal details.
- Mutation assertions require the classification's full class set and the derived
  `invalidates_projection` boolean.

### Invariants And Boundaries

- The live schema, not a hand-maintained model count, determines completeness.
- These are ordinary schema regressions, not durable task evidence.
- An evidence/audit-only delta must never claim projection invalidation; a completion delta must.

### Todos

None.

## Docs References

No configured external source is needed for these repository-owned regressions.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Recursive schema coverage refuses an unclassified future nested field. | `test_taxonomy_covers_current_schema_and_refuses_a_future_nested_field` | mcp/tests/test_task_document_field_effects.py:36-46 |
| Leaf identity is explicit and stale/empty taxonomy entries refuse. | `test_leaf_identity_shape_stays_normative_and_is_explicitly_structural`; `test_taxonomy_refuses_stale_and_empty_memberships` | mcp/tests/test_task_document_field_effects.py:49-57; mcp/tests/test_task_document_field_effects.py:85-93 |
| The canonical top-level delta matrix maps to exact mutation classes and invalidation. | `test_exact_top_level_delta_maps_to_canonical_mutation_classes` | mcp/tests/test_task_document_field_effects.py:136-154 |
| Nested deltas classify by the changed leaf field; new/refused/exhaustive variants are forced. | `test_nested_delta_uses_changed_leaf_field_instead_of_container_name`; `test_new_document_and_effect_mapping_are_exhaustive`; `test_missing_effect_to_mutation_mapping_refuses_classification` | mcp/tests/test_task_document_field_effects.py:156-184; mcp/tests/test_task_document_field_effects.py:185-194; mcp/tests/test_task_document_field_effects.py:195-205 |
| Unknown and incompatible nested schema types refuse classification with exact identity. | `test_nested_model_refusals_cover_unknown_and_incompatible_schema_types` | mcp/tests/test_task_document_field_effects.py:207-238 |
| Mapping and model union variants preserve every owned effect for one delta. | `test_nested_mapping_and_model_union_variants_preserve_all_owned_effects` | mcp/tests/test_task_document_field_effects.py:240-268 |

## Cross-Repo References

None.

## Update History

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for
  3e276f2b2052b641afbee180a472259f21b500df (CCR-R04@v1/L04): recorded the L04 mutation-class
  forcing matrix (exact top-level deltas, nested leaf-field classification, exhaustive mapping,
  missing-mapping refusal, nested-model refusals, union variants) added to this suite.
  Verification is pinned to the owning commit.

- 2026-09-01T08:13+02:00 — Clarified that the suite pins dual taxonomy membership for
  `TaskDocument.id` and `TaskDocument.kind`, not a separate leaf-identity table. Verification
  remains closeout-owned.

- 2026-09-01T03:58+02:00 — 260831-CCR-L01 Attempt 8: created the field-effect taxonomy test card.
  Verification remains closeout-owned.
