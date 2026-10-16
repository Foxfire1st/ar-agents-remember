# mcp/test_support/agents_remember_test_support/code_quality/projection_types.py

## Governing Overview

[overview](../../../overview.md)

## Purpose

Generate persisted and served dashboard TypeScript contracts from the Python wire schemas.

## Code Commentary

`NAMED_VOCABULARIES` now names only attention severity/lane and process fact/health vocabularies. Ordinary model interfaces emit every declared property; there is no lifecycle state partition, metrics bucket inheritance/factory or duplicate subtask-row alias. Regeneration uses the active environment's `python`.

Nullable serialized properties become optional after null variants are removed. `_without_null` preserves non-null unions and annotations, retains multiple surviving alternatives, and refuses an all-null field. There is no `NULL_PRESERVING_MODELS` special case. Supported runtime refinements are `maxItems`, `maxLength`, `minLength`, `minimum` and `pattern`; they remain exact in schema and deterministic property comments. `maximum` and the retired terminal-observer-health payload are not current declarations.

The served-only definition set must still equal `DEFINITION_RENAMES` exactly. A new served payload requires an explicit declaration and regeneration; unknown or shape-inapplicable schema keywords fail closed with the model/property path. Named PEP 695 local enum references and inline enum shapes each render one vocabulary; missing/external/non-enum references refuse. Generated-file drift is named by the check rather than silently accepted. These are static generator semantics, not an execution result.

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
