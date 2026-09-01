# mcp/src/agents_remember/tasks/document_field_effects.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/tasks/document_field_effects.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-01T08:13+02:00 |
| lastVerifiedCommitHash |  `47c8d102c2430d5337dbe207d4601efb4844fec0`|
| lastVerifiedCommitDate |  2026-09-01T08:53:56+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Tasks overview](overview.md)

## Purpose

Owns the exhaustive, schema-derived classification of every persisted task-document field by the
state planes it may affect. It prevents a reader from using whole-document bytes as a proxy for one
semantic concern and refuses schema growth until the new field is classified.

## Code Commentary

### Logic

`TaskDocumentFieldEffect` defines the closed planes: structural topology, normative intent,
completion readiness, progress, evidence, lifecycle, and prose audit. `TASK_DOCUMENT_FIELD_EFFECTS`
classifies every field on `TaskDocument` and all nested persisted models. Validation recursively
discovers the live Pydantic schema and refuses missing models, missing or stale fields, and empty
effect memberships. `TaskDocumentFieldEffectProjector` validates the runtime model before projecting
only fields carrying one requested effect; nested models and containers are projected recursively.

### Conventions

- Effect wire values use stable kebab-case names.
- Taxonomy keys are Pydantic model classes and canonical field names, never aliases.

### Invariants And Boundaries

- The live persisted schema and taxonomy must match exactly; future nested schema changes fail closed.
- One field may belong to multiple effects, but no persisted field may have an empty classification.
- Projection selects schema-owned semantic fields; it does not decide queue policy or delivery state.
- `TaskDocument.id` and `TaskDocument.kind` are each explicitly classified as both normative and
  structural; there is no second leaf-identity table beside the shared taxonomy.

### Todos

None.

## Docs References

No external source is needed for this repository-owned schema taxonomy.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The closed effect vocabulary and projector are declared together. | `TaskDocumentFieldEffect`; `TaskDocumentFieldEffectProjector` | mcp/src/agents_remember/tasks/document_field_effects.py:39-79 |
| The taxonomy explicitly covers the root and every nested persisted model. | `TASK_DOCUMENT_FIELD_EFFECTS` | mcp/src/agents_remember/tasks/document_field_effects.py:87-228 |
| Runtime schema discovery refuses missing, stale, or empty classifications. | `task_document_schema_models`; `validate_task_document_field_effects` | mcp/src/agents_remember/tasks/document_field_effects.py:230-276 |
| Effect projection retains only fields classified for the requested plane. | `fields_with_effect`; `project_model_field_effect` | mcp/src/agents_remember/tasks/document_field_effects.py:278-365 |

## Cross-Repo References

None; this is the task-schema authority inside agents-remember.

## Update History

- 2026-09-01T08:13+02:00 — Corrected the leaf-identity boundary to the implemented dual
  classification of `TaskDocument.id` and `TaskDocument.kind`; no nonexistent parallel identity
  constant is implied. Verification remains closeout-owned.

- 2026-09-01T03:58+02:00 — 260831-CCR-L01 Attempt 8: created the file card for the exhaustive
  task-document field-effect taxonomy. Verification remains closeout-owned.
