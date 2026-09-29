# mcp/src/agents_remember/tasks/document_field_effects.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/tasks/document_field_effects.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T17:20:02+02:00|
| lastVerifiedCommitHash |  `46ca74302e76cf40fb6370ea9ece16d8fa719f00`|
| lastVerifiedCommitDate |  2026-09-30T00:07:49+02:00|
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

Since 260831-LOCR-L33 `Step` carries a `note` field (`tasks/document.py`), classified here as
`AUDIT`: free prose about one unit is an operational-audit fact, so an audit-only edit can never
invalidate a closeout projection. Nothing else about the taxonomy changed — the point of recording
the classification is that the taxonomy is **exhaustive and fails closed**, so adding a persisted
field without a classification refuses before write rather than silently widening an effect plane.

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
  The L33 `Step.note` addition is the worked example: it was classified `AUDIT` in the same change that
  declared the field, because leaving it unclassified refuses the write.
- One field may belong to multiple effects, but no persisted field may have an empty classification.
- Projection selects schema-owned semantic fields; it does not decide queue policy or delivery state.
- `TaskDocument.id` and `TaskDocument.kind` are each explicitly classified as both normative and
  structural; there is no second leaf-identity table beside the shared taxonomy.
- Every persisted field must resolve to a mutation class through `FIELD_EFFECT_MUTATION_CLASSES`;
  missing or stale mappings refuse classification before write.
- `invalidates_projection` is a derived fact of the classified delta: topology/intent/completion
  changes invalidate, acceptance-evidence and operational-audit changes alone never do.
- **`knowledgeMaintenanceScope` is `LIFECYCLE` (MIK-R08, architect ruling 4).** Like `lifecycleId`, it
  records how the leaf is run, not what it intends: classifying it `NORMATIVE` would require a
  `task-intent/v1` schema change, because `_validate_allowlisted_classifications` refuses a normative slot
  outside the intent. As a `LIFECYCLE` field, a change to it is an `operational-audit` mutation and never
  invalidates a closeout projection.
- **`expectedKnowledgeEffects` is `NORMATIVE` (MIK-R11 rule 1: `NORMATIVE_INTENT`).** Unlike
  `knowledgeMaintenanceScope`, a leaf's declared knowledge effects are part of what it intends, so the field
  and the three fields of `ExpectedKnowledgeEffect` (`subject`, `effect`, `requirementRef`) are classified
  `NORMATIVE`, and MIK-R11 adds the matching optional slot to `task-intent/v1` (`task_intent.py`), which keeps
  `_validate_allowlisted_classifications` symmetric. A change to it is an `intent` mutation.

### Todos

None.

## Docs References

No external Domain Documentation source is configured; the schema taxonomy and mutation
classification are repository-owned. The governing CCR-R04@v1 packet is the task authority for
the classification and invalidation semantics this file implements:
`ar-coordination/tasks/agents-remember/260831_closeout-certification-reform/requirements/CCR-R04-v1-mutation-classified-projection-invalidation.md`.
It is an authority link, not a resolved dependency-version source; current behavior is
evidenced by the repository-owned references below.

| Finding | Anchor | Source |
| --- | --- | --- |
| R04's exhaustive mutation taxonomy and task-first projection boundary are implemented by the closed effect map and canonical scope resolver. | `TASK_DOCUMENT_FIELD_EFFECTS`; "def classify_task_document_mutation("; `resolve_projection_scope_union` | mcp/src/agents_remember/tasks/document_field_effects.py:145-340; mcp/src/agents_remember/tasks/document_field_effects.py:347-347; mcp/src/agents_remember/tasks/document_field_effects.py:345-358; mcp/src/agents_remember/application/task_docs/task_doc_queue_scope.py:38-86 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| MIK-R08's task-document field is classified with the lifecycle plane. | "knowledgeMaintenanceScope" | mcp/src/agents_remember/tasks/document_field_effects.py:166-166 |
| MIK-R11's declaration and its nested fields are classified normative. | "expectedKnowledgeEffects"; `ExpectedKnowledgeEffect` | mcp/src/agents_remember/tasks/document_field_effects.py:167-167; mcp/src/agents_remember/tasks/document_field_effects.py:270-274 |
| The closed effect vocabulary and projector are declared together. | `TaskDocumentFieldEffect`; `TaskDocumentFieldEffectProjector` | mcp/src/agents_remember/tasks/document_field_effects.py:55-64; mcp/src/agents_remember/tasks/document_field_effects.py:106-127 |
| The taxonomy explicitly covers the root and every nested persisted model, including evidence-dependency and task-intent contracts. | `TASK_DOCUMENT_FIELD_EFFECTS` | mcp/src/agents_remember/tasks/document_field_effects.py:145-340 |
| The effect-to-mutation-class map and the exact before/candidate classifier drive projection invalidation decisions. | `FIELD_EFFECT_MUTATION_CLASSES`; `classify_task_document_mutation`; `TaskDocumentMutationClassification` | mcp/src/agents_remember/tasks/document_field_effects.py:85-100; mcp/src/agents_remember/tasks/document_field_effects.py:354-367; mcp/src/agents_remember/tasks/document_field_effects.py:343-351 |
| Missing or stale mutation mappings and unclassified models refuse before write. | `validate_task_document_mutation_classes`; `_changed_model_effects` | mcp/src/agents_remember/tasks/document_field_effects.py:370-380; mcp/src/agents_remember/tasks/document_field_effects.py:383-403 |
| Runtime schema discovery refuses missing, stale, or empty classifications. | `task_document_schema_models`; `validate_task_document_field_effects` | mcp/src/agents_remember/tasks/document_field_effects.py:442-456; mcp/src/agents_remember/tasks/document_field_effects.py:479-493; mcp/src/agents_remember/tasks/document_field_effects.py:496-511 |
| Effect projection retains only fields classified for the requested plane. | `fields_with_effect`; `project_model_field_effect` | mcp/src/agents_remember/tasks/document_field_effects.py:527-537; mcp/src/agents_remember/tasks/document_field_effects.py:540-551 |

## Cross-Repo References

None; this is the task-schema authority inside agents-remember.

## Update History

- 2026-09-29T23:27:43+02:00 — 260928-MIK-L11 curator (uncommitted change set on `ar/260928-mik-l11`, code base `2c6f170ef07bf6767d582f76c9f9dd06bbdd06a4` plus the staged delta): **body updated for MIK-R11.** Added the Invariants bullet on `expectedKnowledgeEffects` and `ExpectedKnowledgeEffect` classified `NORMATIVE` (the packet's `NORMATIVE_INTENT`), with the matching optional intent slot. One row added; L08's row re-pointed by the exact +1 line shift; other rows re-pointed by the installed fixer. No verification stamp was advanced.
- 2026-09-29T17:20:02+02:00 — 260928-MIK-L08 curator (uncommitted change set on `ar/260928-mik-l08`, code base `e49ba07865b3848cd36759cea6b37bba7d0d51c3` plus the working-tree delta and untracked files): **body updated for MIK-R08.** Invariants records the new `TaskDocument.knowledgeMaintenanceScope` classification (`LIFECYCLE`, architect ruling 4, hence `operational-audit` and outside the intent digest), with a citation row.
- 2026-09-13T00:40+02:00 — 260831-LOCR-L33 curator: recorded the classification of the new persisted
  `Step.note` field as `AUDIT`, and used it as the worked example of the taxonomy's exhaustive,
  fail-closed rule (a persisted field without a classification refuses before write). No mutation-class
  mapping or projection policy changed, because `AUDIT` already maps to `operational-audit`.
  Verification metadata remains closeout-owned; no acceptance claim.

- 2026-09-09T14:45+02:00 — CCR-L42 curator reconciliation: re-read affected claims against the frozen current source and corrected only their source anchors/ranges; verification stamps remain closeout-owned.

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
