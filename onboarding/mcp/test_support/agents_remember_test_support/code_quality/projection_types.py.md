# mcp/test_support/agents_remember_test_support/code_quality/projection_types.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/test_support/agents_remember_test_support/code_quality/projection_types.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T20:42+02:00 |
| lastVerifiedCommitHash | `e9678c56e7f441371584ad8a18e2b9380cb38cf0`|
| lastVerifiedCommitDate | 2026-09-15T20:50:53+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview](../../../overview.md)

## Purpose

Generate the dashboard projection contract from the Python wire schemas.

## Code Commentary

L23 makes projection regeneration invoke `python` through the active environment instead of deriving a checkout-adjacent virtualenv path, so the clean executor controls interpreter resolution.

### Logic

Module-level surface (ranges re-derived against the current candidate):

- `ProjectionTypeGenerationError` (class, lines 82-84) — A Python schema shape cannot be represented by this generator.
- `workspace_projection_schema` (function, lines 86-89) — The canonical projection schema, copied so callers may safely mutate fixtures.
- `served_projection_schema` (function, lines 91-94) — The declared HTTP/SSE snapshot schema, including its serve-time tail.
- `schema_json` (function, lines 96-100) — Stable bytes for the committed JSON Schema artifact.
- `_object` (102-106) · `_objects` (108-112) · `_strings` (114-118) · `_definitions` (120-122) · `_properties` (124-126) · `_definition_ref_name` (128-133) · `_ref_name` (135-138) · `_nullable_variants` (140-143) · `_is_null` (145-147) · `_is_nullable` (149-152) · `_json_literal` (154-163) · `_enum_values` (165-168)
- `_property_enum` (170-189) · `_named_vocabulary_definitions` (191-201) — the two canonical CPython 3.13 named-literal shapes and the one-definition-per-vocabulary pass.
- `_schema_allowed_keywords` (203-236) · `_refinement_schema` (238-258) · `_refinement_comment` (260-272) — the keyword allowlist per schema shape and the deterministic refinement rendering.
- `_schema_children` (274-306) · `_validate_schema_node` (308-327) · `_validate_schema` (329-341) — the fail-closed walk over every node.
- `_array_type` (343-349) · `_object_type` (351-361) · `_schema_type` (363-395) · `_without_null` (397-410) · `_property_line` (412-425) · `_model_interface` (427-444)
- `_state_count_field` (446-449) · `_state_partition` (451-466) · `_metric_bucket_fields` (468-471) · `_vocabulary` (473-480) · `_tuple_constant` (482-485) · `_vocabulary_block` (487-567) — the derived state partition and closed TypeScript vocabularies.
- `render_typescript` (569-601) — Render the public projection module from emitted Pydantic schemas, folding the served projection's own definitions into the same output.
- `typescript_text` (603-608) · `generated_files` (610-612) · `stale_generated_files` (614-621) · `sync_generated_files` (623-625) — the drift-checked publication path used by `scripts/sync-projection-types.py --check`.

Two module-level declaration sets are contract, not configuration: `DEFINITION_RENAMES` (35-38) and `NAMED_VOCABULARIES` (40-46) name what the generated TypeScript calls each folded definition, and `NULL_PRESERVING_MODELS` (48-49) names the models whose nullable properties stay REQUIRED `T | null` because they are serialized without `exclude_none`. `SCHEMA_ANNOTATION_KEYWORDS` (51), `SCHEMA_REFINEMENT_KEYWORDS` (52-59) and `SCHEMA_KEYWORDS` (61-65) are the whole keyword vocabulary the renderer understands.

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module. Line ranges in this card are derived from the current source rather than carried forward.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.
- **The served schema's extra `$defs` are asserted exhaustively**: `render_typescript` requires the served schema's folded definitions to equal `DEFINITION_RENAMES` exactly, so extending `ServedWorkspaceProjection` with a new payload model forces a declaration here AND a regeneration of `dashboard/src/types/projection.ts`. Drift is a hard gate, not a warning.
- A schema keyword the renderer does not understand fails closed with the exact model/property path; the allowlist is never widened to make a document render.
- A refinement TypeScript cannot enforce structurally is emitted beside its property as deterministic `JSON Schema refinements` documentation, so the generated contract never silently drops schema truth.

### Todos

None.

## Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact current source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| The fail-closed generation error raised for an unrepresentable schema shape. | `ProjectionTypeGenerationError` | mcp/test_support/agents_remember_test_support/code_quality/projection_types.py:82-84 |
| The persisted projection schema, copied for safe mutation. | `workspace_projection_schema` | mcp/test_support/agents_remember_test_support/code_quality/projection_types.py:86-89 |
| The declared HTTP/SSE snapshot schema, including its serve-time tail. | `served_projection_schema` | mcp/test_support/agents_remember_test_support/code_quality/projection_types.py:91-94 |
| Stable bytes for the committed JSON Schema artifact. | `schema_json` | mcp/test_support/agents_remember_test_support/code_quality/projection_types.py:96-100 |
| The exact declaration sets the renderer folds into TypeScript, including the served projection's payload rename. | `DEFINITION_RENAMES`; `NAMED_VOCABULARIES` | mcp/test_support/agents_remember_test_support/code_quality/projection_types.py:35-38; mcp/test_support/agents_remember_test_support/code_quality/projection_types.py:40-46 |
| The models whose nulls are MEANINGFUL and therefore stay required `T \| null` on the output contract. | `NULL_PRESERVING_MODELS` | mcp/test_support/agents_remember_test_support/code_quality/projection_types.py:48-49 |
| The one vocabulary for runtime-only JSON Schema refinements, `maximum` included, and the shape each refinement may attach to. | `SCHEMA_REFINEMENT_KEYWORDS`; `_schema_allowed_keywords` | mcp/test_support/agents_remember_test_support/code_quality/projection_types.py:52-59; mcp/test_support/agents_remember_test_support/code_quality/projection_types.py:203-236 |
| Refinements are serialized deterministically beside their property instead of being dropped. | `_refinement_schema`; `_refinement_comment` | mcp/test_support/agents_remember_test_support/code_quality/projection_types.py:238-258; mcp/test_support/agents_remember_test_support/code_quality/projection_types.py:260-272 |
| The recursive, fail-closed schema walk that refuses any unknown or shape-inapplicable keyword. | `_schema_children`; `_validate_schema_node`; `_validate_schema` | mcp/test_support/agents_remember_test_support/code_quality/projection_types.py:274-306; mcp/test_support/agents_remember_test_support/code_quality/projection_types.py:308-327; mcp/test_support/agents_remember_test_support/code_quality/projection_types.py:329-341 |
| The derived state partition and the closed TypeScript vocabulary blocks. | `_state_partition`; `_vocabulary_block` | mcp/test_support/agents_remember_test_support/code_quality/projection_types.py:451-466; mcp/test_support/agents_remember_test_support/code_quality/projection_types.py:487-567 |
| The served projection's own definitions are folded into the same generated module, and the definition set is compared exactly. | `render_typescript` | mcp/test_support/agents_remember_test_support/code_quality/projection_types.py:569-601 |
| The drift check the repository gates on: a stale generated artifact is named rather than regenerated silently. | `stale_generated_files`; `sync_generated_files` | mcp/test_support/agents_remember_test_support/code_quality/projection_types.py:614-621; mcp/test_support/agents_remember_test_support/code_quality/projection_types.py:623-625 |

## 260821-CLIVE-L2 Nullable Union Preservation

Nullable-field normalization now removes only null variants. A non-null union is returned intact,
a nullable single variant keeps outer annotations, and a nullable multi-variant union keeps both
its annotations and remaining `anyOf` alternatives. An all-null field still refuses generation.
This lets the lifecycle-operation status schema remain a closed multi-variant union instead of
being flattened or rejected.

| Finding | Anchor | Source |
| --- | --- | --- |
| `_without_null` distinguishes non-null unions, one surviving variant, multiple surviving variants, and the invalid all-null case. | `_without_null` | mcp/test_support/agents_remember_test_support/code_quality/projection_types.py:397-410 |

## 260821-CLIVE Exact Runtime Refinements

The generator has one explicit vocabulary for runtime-only JSON Schema refinements:
`maxItems`, `maximum`, `minimum`, `pattern`, `minLength`, and `maxLength`. Every supported
refinement remains byte-exact in the generated schema and is emitted beside its TypeScript property
as deterministic `JSON Schema refinements` documentation because TypeScript cannot enforce those
constraints structurally. Nested item refinements are preserved recursively.

`_schema_allowed_keywords()` admits a refinement only for the schema shape that can own it — an
integer or number node may now carry `maximum` as well as `minimum`, which is what lets a bounded
counter state its ceiling. `_refinement_schema()` and `_refinement_comment()` select and
deterministically serialize it. Unknown or shape-inapplicable keywords still fail closed with the
exact model/property path and remediation. The generator never silently drops schema truth, and this
is not a compatibility reader or fallback around canonical schema validation.

## Python 3.13 Named Literal Vocabularies

CPython 3.13 plus Pydantic emits PEP 695 named `Literal` aliases as local `$defs` references rather
than repeating their enum values at every property. `_property_enum()` accepts exactly the two
canonical shapes: an inline enum or one local definition reference whose target is itself an enum.
`_named_vocabulary_definitions()` removes those already-rendered definitions from the interface
pass, so each closed TypeScript vocabulary remains defined exactly once. A missing, external, or
non-enum target still raises `ProjectionTypeGenerationError`; this is support for the canonical
schema shape, not a fallback to untyped strings.

## 260831-LOCR-L17 Served-Schema Declarations

Extending `ServedWorkspaceProjection` with a serve-time payload is never a one-file edit, because
this module is where the generated contract's completeness is enforced. The leaf added
`terminalObserverHealth` to the served tail, which required three exact declarations here and one
regeneration:

- `DEFINITION_RENAMES` gained `TerminalObserverHealthPayload` → `TerminalObserverHealth`: the served
  schema's folded `$defs` are compared to this set **exactly**, so an undeclared new definition is a
  generation refusal rather than a silently missing interface.
- `NULL_PRESERVING_MODELS` gained the same model, because its nullable properties are serialized
  without `exclude_none`: `activeFailureCategory`/`Type`/`Summary` and both timestamps are REQUIRED
  `T | null` on the output contract, and `lastAttemptAt: null` is itself the served fact that no
  attempt has completed in this serving lifetime.
- `SCHEMA_REFINEMENT_KEYWORDS` (and the integer/number branch of `_schema_allowed_keywords`) gained
  `maximum`, so the record's two serving-lifetime counters can state their unsigned 32-bit ceiling
  (`{"maximum":4294967295,"minimum":0}`) beside the property instead of documenting only a floor the
  generated mirror cannot enforce.

The counter ceiling is the reason the keyword exists: a bounded field declared only in the producer
is a contract the schema does not state. The gate stays closed — an unsupported keyword still fails
the drift check — so this is an extension of the vocabulary, not a loosening of it.

## Update History

- 2026-09-15T20:42+02:00 — 260831-LOCR-L17 curator (uncommitted change set on `ar/260831-locr-l17`,
  base `99534dc5`, `projection_types.py` +30/−11): the generator's declaration sets and refinement
  vocabulary changed, so the body was corrected rather than annotated. Added the
  `## 260831-LOCR-L17 Served-Schema Declarations` section: `DEFINITION_RENAMES` gained
  `TerminalObserverHealthPayload` → `TerminalObserverHealth` (the served `$defs` are compared
  exactly, so an undeclared new definition is a refusal), `NULL_PRESERVING_MODELS` gained the same
  model (its nulls are served facts, so its nullable properties stay required `T | null`), and
  `maximum` joined the supported refinement vocabulary — including the integer/number branch of
  `_schema_allowed_keywords` — so the record's two 32-bit counters state their ceiling in the
  generated contract instead of documenting only a floor. The refinements section now lists
  `maximum` and records why it exists (a bounded field declared only in the producer is a contract
  the schema does not state) and that the drift gate still fails closed on any unsupported keyword.
  Every symbol range on this card was re-derived against the current 625-line source, because the
  previous list and table carried ranges from an earlier revision (`_object` `75-78`/`90-93` →
  `102-106`, `_state_partition` `340-356`/`439-453` → `451-466`, `_vocabulary_block` `382-421` →
  `487-567`, `render_typescript` `467-495` → `569-601`, `stale_generated_files` `509-515` →
  `614-621`). The card's `lastVerifiedCommitHash` is deliberately unchanged: the source is an
  uncommitted candidate and verification metadata remains closeout-owned. No stamp advanced.

- 2026-08-29T19:04+02:00 — Generation-11 repair: taught the generator to resolve Python 3.13's
  local named-literal enum references and to emit those vocabularies exactly once while retaining
  fail-closed behavior for every other reference shape. Verification remains closeout-owned.

- 2026-08-24T15:04+02:00 — Cumulative CLIVE/DAGQC reconciliation: expanded the earlier
  `maxItems` account to the exact supported refinement vocabulary and its fail-closed rendering
  boundary. Timestamp is the curator host's Europe/Berlin system time; verification remains
  closeout-owned.

- 2026-08-24T00:51+02:00 — 260821-CLIVE-L2: reconciled nullable multi-variant union preservation. Verified at code commit `1d446724`.

- 2026-08-12T15:56+02:00 — 260731-EFA-L23 curator body review: reconciled this card with the exact current source delta described above; verification provenance remains closeout-owned.

- 2026-08-08T22:10+02:00 — 260713-TES-L1 completion round 2 (curator): No content impact: the supervisor -> agent-notifier rename does not change the behavior this sidecar documents; reviewed current against the changed source. Verification metadata pinned until closeout stamps the 260713-TES-L1 commit.
- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
