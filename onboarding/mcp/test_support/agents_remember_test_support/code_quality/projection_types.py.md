# mcp/test_support/agents_remember_test_support/code_quality/projection_types.py

## Governing Overview

[overview](../../../overview.md)

## Purpose

Generate persisted and served dashboard TypeScript contracts from the Python wire schemas.

## Code Commentary

`NAMED_VOCABULARIES` names the attention severity, lane and item-class vocabularies together with the process fact/health vocabularies, and the attention item class is emitted as its own `ATTENTION_ITEM_CLASSES` block. Ordinary model interfaces emit every declared property; there is no lifecycle state partition, metrics bucket inheritance/factory or duplicate subtask-row alias. Regeneration uses the active environment's `python`.

Nullable serialized properties become optional after null variants are removed. `_without_null` preserves non-null unions and annotations, retains multiple surviving alternatives, and refuses an all-null field. There is no `NULL_PRESERVING_MODELS` special case. Supported runtime refinements are `maxItems`, `maxLength`, `minLength`, `minimum`, `pattern` and `format`, each held in the exact definition set; a `format` of `date-time` keeps its date-time meaning in the generated type instead of degrading to a bare string. An unknown keyword, one the string shape cannot carry, or a definition set that differs from the exact one still fails closed. `maximum` is not a supported refinement.

The served-only definition set must still equal `DEFINITION_RENAMES` exactly; it declares four served renames, `BuildCurrentnessPayload`, `CheckoutBindingPayload`, `ServingBuildPayload` and `WatcherHealthPayload`, each emitted without its `Payload` suffix. A new served payload requires an explicit declaration and regeneration; unknown or shape-inapplicable schema keywords fail closed with the model/property path. Named PEP 695 local enum references and inline enum shapes each render one vocabulary; missing/external/non-enum references refuse. Generated-file drift is named by the check rather than silently accepted. These are static generator semantics, not an execution result.


## Evidence

- The fail-closed generation error raised for an unrepresentable schema shape. [1]
- The persisted projection schema, copied for safe mutation. [2]
- The declared HTTP/SSE snapshot schema, including its serve-time tail. [3]
- Stable bytes for the committed JSON Schema artifact. [4]

- The exact declaration sets the renderer folds into TypeScript: four served payload renames and five named vocabularies. [5]

- The served build-currentness payload is folded as `BuildCurrentness`. [18]

- Refinements are serialized deterministically beside their property instead of being dropped. [8]
- The recursive, fail-closed schema walk that refuses any unknown or shape-inapplicable keyword. [9]

- The served projection's own definitions are folded into the same generated module, and the definition set is compared exactly. [11]

- The drift check the repository gates on: a stale generated artifact is named rather than regenerated silently. [12]
- `_without_null` distinguishes non-null unions, one surviving variant, multiple surviving variants, and the invalid all-null case. [13]


- Only the attention and process vocabularies are emitted. [14]

- Every model property emits directly, without lifecycle metrics inheritance. [15]
- Nullable properties become optional after null removal. [16]

- Runtime refinements are shape-checked and unsupported keywords refuse. [17]
