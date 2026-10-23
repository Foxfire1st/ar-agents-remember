# mcp/test_support/agents_remember_test_support/code_quality/projection_types.py

## Governing Overview

[overview](../../../overview.md)

## Purpose

Generate persisted and served dashboard TypeScript contracts from the Python wire schemas.

## Code Commentary

`NAMED_VOCABULARIES` names the attention severity, lane and item-class vocabularies together with the process fact/health vocabularies, and the attention item class is emitted as its own `ATTENTION_ITEM_CLASSES` block. Ordinary model interfaces emit every declared property; there is no lifecycle state partition, metrics bucket inheritance/factory or duplicate subtask-row alias. Regeneration uses the active environment's `python`.

Nullable serialized properties become optional after null variants are removed. `_without_null` preserves non-null unions and annotations, retains multiple surviving alternatives, and refuses an all-null field. There is no `NULL_PRESERVING_MODELS` special case. Supported runtime refinements are `maxItems`, `maxLength`, `minLength`, `minimum`, `pattern` and `format`, each held in the exact definition set; a `format` of `date-time` keeps its date-time meaning in the generated type instead of degrading to a bare string. An unknown keyword, one the string shape cannot carry, or a definition set that differs from the exact one still fails closed. `maximum` and the retired terminal-observer-health payload are not current declarations.

The served-only definition set must still equal `DEFINITION_RENAMES` exactly. A new served payload requires an explicit declaration and regeneration; unknown or shape-inapplicable schema keywords fail closed with the model/property path. Named PEP 695 local enum references and inline enum shapes each render one vocabulary; missing/external/non-enum references refuse. Generated-file drift is named by the check rather than silently accepted. These are static generator semantics, not an execution result.

No current `METRICS_FACTORY` emits a verification-age histogram; the former lifecycle-derived metrics factory is removed rather than restored.

<details>
<summary>Local predecessor generator inventory; superseded names and ranges are historical</summary>

`METRICS_FACTORY` returns `lifecycleCount` and the spread `lifecycleStateCounts(lifecycles)`; it no longer emits an empty `stalenessHistogram`.

### Logic

Module-level surface (ranges re-derived against the current candidate):

- `ProjectionTypeGenerationError` (class, lines 82-83) — A Python schema shape cannot be represented by this generator.
- `workspace_projection_schema` (function, lines 86-88) — The canonical projection schema, copied so callers may safely mutate fixtures.
- `served_projection_schema` (function, lines 91-93) — The declared HTTP/SSE snapshot schema, including its serve-time tail.
- `schema_json` (function, lines 96-99) — Stable bytes for the committed JSON Schema artifact.
- `_object` (102-105) · `_objects` (108-111) · `_strings` (114-117) · `_definitions` (120-121) · `_properties` (124-125) · `_definition_ref_name` (128-132) · `_ref_name` (135-137) · `_nullable_variants` (140-142) · `_is_null` (145-146) · `_is_nullable` (149-151) · `_json_literal` (154-162) · `_enum_values` (165-167)
- `_property_enum` (170-188) · `_named_vocabulary_definitions` (191-200) — the two canonical CPython 3.14 named-literal shapes and the one-definition-per-vocabulary pass.
- `_schema_allowed_keywords` (203-235) · `_refinement_schema` (238-257) · `_refinement_comment` (260-271) — the keyword allowlist per schema shape and the deterministic refinement rendering.
- `_schema_children` (274-305) · `_validate_schema_node` (308-326) · `_validate_schema` (329-340) — the fail-closed walk over every node.
- `_array_type` (343-348) · `_object_type` (351-360) · `_schema_type` (363-394) · `_without_null` (397-409) · `_property_line` (412-424) · `_model_interface` (427-443)
- `_state_count_field` · `_vocabulary` · `_tuple_constant` · `_vocabulary_block` — the closed TypeScript vocabularies. The derived state-partition helpers (`_state_partition`, `_metric_bucket_fields`) were removed with the verification-age metrics they served.
- `render_typescript` (567-598) — Render the public projection module from emitted Pydantic schemas, folding the served projection's own definitions into the same output.
- `typescript_text` (601-605) · `generated_files` (608-609) · `stale_generated_files` (612-618) · `sync_generated_files` (621-625) — the drift-checked publication path used by `scripts/sync-projection-types.py --check`.

Two module-level declaration sets are contract, not configuration: `DEFINITION_RENAMES` (35-39) and `NAMED_VOCABULARIES` (40-47) name what the generated TypeScript calls each folded definition, and `NULL_PRESERVING_MODELS` (48-50) names the models whose nullable properties stay REQUIRED `T | null` because they are serialized without `exclude_none`. `SCHEMA_ANNOTATION_KEYWORDS` (51), `SCHEMA_REFINEMENT_KEYWORDS` (52-54) and `SCHEMA_KEYWORDS` (61-76) are the whole keyword vocabulary the renderer understands.

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module. Line ranges in this card are derived from the current source rather than carried forward.

### Invariants And Boundaries

- The card mirrors `mcp/test_support/agents_remember_test_support/code_quality/projection_types.py` one-to-one.
- **The served schema's extra `$defs` are asserted exhaustively**: `render_typescript` requires the served schema's folded definitions to equal `DEFINITION_RENAMES` exactly, so extending `ServedWorkspaceProjection` with a new payload model forces a declaration here AND a regeneration of `dashboard/src/types/projection.ts`. Drift is a hard gate, not a warning.
- A schema keyword the renderer does not understand fails closed with the exact model/property path; the allowlist is never widened to make a document render.
- A refinement TypeScript cannot enforce structurally is emitted beside its property as deterministic `JSON Schema refinements` documentation, so the generated contract never silently drops schema truth.

### Todos

None.

</details>


**L184 — INV-4T6KSE.** The checker's own model of the projection has to include the new fact or it cannot judge it. The obligation this leaf records for this place is stated in the invariant named here; the card's earlier account of this file stands, and this paragraph adds what the change made true.

## Evidence

- The fail-closed generation error raised for an unrepresentable schema shape. [1]
- The persisted projection schema, copied for safe mutation. [2]
- The declared HTTP/SSE snapshot schema, including its serve-time tail. [3]
- Stable bytes for the committed JSON Schema artifact. [4]
- The exact declaration sets the renderer folds into TypeScript, including the served projection's payload rename. [5]
- Refinements are serialized deterministically beside their property instead of being dropped. [8]
- The recursive, fail-closed schema walk that refuses any unknown or shape-inapplicable keyword. [9]
- The served projection's own definitions are folded into the same generated module, and the definition set is compared exactly. [11]
- The drift check the repository gates on: a stale generated artifact is named rather than regenerated silently. [12]
- `_without_null` distinguishes non-null unions, one surviving variant, multiple surviving variants, and the invalid all-null case. [13]

- Only remaining attention and process vocabularies are emitted. [14]
- Every model property emits directly, without lifecycle metrics inheritance. [15]
- Nullable properties become optional after null removal. [16]
- Runtime refinements are shape-checked and unsupported keywords refuse. [17]
