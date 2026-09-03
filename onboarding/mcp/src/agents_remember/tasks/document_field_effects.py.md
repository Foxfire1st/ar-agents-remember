# mcp/src/agents_remember/tasks/document_field_effects.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/tasks/document_field_effects.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash |  `3e276f2b2052b641afbee180a472259f21b500df`|
| lastVerifiedCommitDate |  2026-09-02T14:46:34+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Tasks overview](overview.md)

## Purpose

Owns the exhaustive, schema-derived classification of every persisted task-document field by the
state planes it may affect, and the mutation-class derivation that decides whether one exact
accepted/candidate task delta invalidates disposable closeout projections. It prevents a reader
from using whole-document bytes as a proxy for one semantic concern and refuses schema growth
until the new field is classified.

## Code Commentary

### Logic

`TaskDocumentFieldEffect` defines the closed planes: structural topology, normative intent,
completion readiness, progress, evidence, lifecycle, and prose audit. `TASK_DOCUMENT_FIELD_EFFECTS`
classifies every field on `TaskDocument` and all nested persisted models. Validation recursively
discovers the live Pydantic schema and refuses missing models, missing or stale fields, and empty
effect memberships. `TaskDocumentFieldEffectProjector` validates the runtime model before projecting
only fields carrying one requested effect; nested models and containers are projected recursively.

The mutation half maps each effect plane to exactly one `TaskDocumentMutationClass`:
`STRUCTURAL_TOPOLOGY` to `topology`, `NORMATIVE_INTENT` to `intent`,
`COMPLETION_READINESS`/`PROGRESS` to `completion-readiness`, `EVIDENCE` to `acceptance-evidence`, and
`LIFECYCLE`/`PROSE_AUDIT` to `operational-audit`
(`FIELD_EFFECT_MUTATION_CLASSES`). `classify_task_document_mutation` validates both sides of the
exact before/candidate pair, walks every changed leaf value through recursive
`_changed_*_effects` helpers (nested models, mappings, lists, present-vs-None), and returns a frozen
`TaskDocumentMutationClassification` set. `invalidates_projection` is true exactly when the union
touches topology, intent, or completion-readiness, so evidence/audit-only edits publish task truth
without task-driven queue refresh. `validate_task_document_mutation_classes` refuses an effect
vocabulary change without a corresponding mutation class, and unclassified schema models refuse
before write.

### Conventions

- Effect wire values use stable kebab-case names.
- Taxonomy keys are Pydantic model classes and canonical field names, never aliases.
- Mutation classes are derived only from schema-owned effect planes; no operation-name
  special-casing (for example `record_route_review`) exists.

### Invariants And Boundaries

- The live persisted schema and taxonomy must match exactly; future nested schema changes fail closed.
- One field may belong to multiple effects, but no persisted field may have an empty classification.
- Projection selects schema-owned semantic fields; it does not decide queue policy or delivery state.
- `TaskDocument.id` and `TaskDocument.kind` are each explicitly classified as both normative and
  structural; there is no second leaf-identity table beside the shared taxonomy.
- Every persisted field must resolve to a mutation class through `FIELD_EFFECT_MUTATION_CLASSES`;
  missing or stale mappings refuse classification before write.
- `invalidates_projection` is a derived fact of the classified delta: topology/intent/completion
  changes invalidate, acceptance-evidence and operational-audit changes alone never do.

### Todos

None.

## Docs References

No external Domain Documentation source is configured; the schema taxonomy and mutation
classification are repository-owned. The governing CCR-R04@v1 packet names the classification
and invalidation semantics this file implements.

| Finding | Anchor | Source |
| --- | --- | --- |
| The R04 packet requires exhaustive mutation classification (topology/intent/completion/evidence/audit) and task-first publication with no queue authority. | "Required Behavior"; "Ownership And Authority" | ar-coordination/tasks/agents-remember/260831_closeout-certification-reform/requirements/CCR-R04-v1-mutation-classified-projection-invalidation.md:25-72 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The closed effect vocabulary and projector are declared together. | `TaskDocumentFieldEffect`; `TaskDocumentFieldEffectProjector` | mcp/src/agents_remember/tasks/document_field_effects.py:50-59; mcp/src/agents_remember/tasks/document_field_effects.py:101-122 |
| The taxonomy explicitly covers the root and every nested persisted model, including evidence-dependency and task-intent contracts. | `TASK_DOCUMENT_FIELD_EFFECTS` | mcp/src/agents_remember/tasks/document_field_effects.py:140-303 |
| The effect-to-mutation-class map and the exact before/candidate classifier drive projection invalidation decisions. | `FIELD_EFFECT_MUTATION_CLASSES`; `classify_task_document_mutation`; `TaskDocumentMutationClassification` | mcp/src/agents_remember/tasks/document_field_effects.py:306-314; mcp/src/agents_remember/tasks/document_field_effects.py:317-330; mcp/src/agents_remember/tasks/document_field_effects.py:80-95 |
| Missing or stale mutation mappings and unclassified models refuse before write. | `validate_task_document_mutation_classes`; `_changed_model_effects` | mcp/src/agents_remember/tasks/document_field_effects.py:333-343; mcp/src/agents_remember/tasks/document_field_effects.py:346-366 |
| Runtime schema discovery refuses missing, stale, or empty classifications. | `task_document_schema_models`; `validate_task_document_field_effects` | mcp/src/agents_remember/tasks/document_field_effects.py:442-456; mcp/src/agents_remember/tasks/document_field_effects.py:459-474 |
| Effect projection retains only fields classified for the requested plane. | `fields_with_effect`; `project_model_field_effect` | mcp/src/agents_remember/tasks/document_field_effects.py:490-500; mcp/src/agents_remember/tasks/document_field_effects.py:503-514 |

## Cross-Repo References

None; this is the task-schema authority inside agents-remember.

## Update History

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for
  3e276f2b2052b641afbee180a472259f21b500df (CCR-R04@v1/L04): recorded the mutation-classification
  half added by L04 — `TaskDocumentMutationClass`,
  `TaskDocumentMutationClassification`, `FIELD_EFFECT_MUTATION_CLASSES`,
  `classify_task_document_mutation`, `validate_task_document_mutation_classes`, and the recursive
  changed-value helpers — and extended the taxonomy account to the evidence-dependency and
  task-intent contracts it now covers. Verification is pinned to the owning commit.

- 2026-09-01T08:13+02:00 — Corrected the leaf-identity boundary to the implemented dual
  classification of `TaskDocument.id` and `TaskDocument.kind`; no nonexistent parallel identity
  constant is implied. Verification remains closeout-owned.

- 2026-09-01T03:58+02:00 — 260831-CCR-L01 Attempt 8: created the file card for the exhaustive
  task-document field-effect taxonomy. Verification remains closeout-owned.
