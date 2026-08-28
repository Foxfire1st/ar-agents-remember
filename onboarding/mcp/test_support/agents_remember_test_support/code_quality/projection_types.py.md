# mcp/test_support/agents_remember_test_support/code_quality/projection_types.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/test_support/agents_remember_test_support/code_quality/projection_types.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-28T07:20+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[overview](../../../overview.md)

## Purpose

Generate the dashboard projection contract from the Python wire schemas.

## Code Commentary

L23 makes projection regeneration invoke `python` through the active environment instead of deriving a checkout-adjacent virtualenv path, so the clean executor controls interpreter resolution.

### Logic

Module-level surface:

- `ProjectionTypeGenerationError` (class, lines 55-56) — A Python schema shape cannot be represented by this generator.
- `workspace_projection_schema` (function, lines 59-61) — The canonical projection schema, copied so callers may safely mutate fixtures.
- `served_projection_schema` (function, lines 64-66) — The declared HTTP/SSE snapshot schema, including its serve-time tail.
- `schema_json` (function, lines 69-72) — Stable bytes for the committed JSON Schema artifact.
- `_object` (function, lines 75-78)
- `_objects` (function, lines 81-84)
- `_strings` (function, lines 87-90)
- `_definitions` (function, lines 93-94)
- `_properties` (function, lines 97-98)
- `_ref_name` (function, lines 101-105)
- `_nullable_variants` (function, lines 108-110)
- `_is_null` (function, lines 113-114)
- `_is_nullable` (function, lines 117-119)
- `_json_literal` (function, lines 122-130)
- `_enum_values` (function, lines 133-135)
- `_schema_allowed_keywords` (function, lines 138-166)
- `_schema_children` (function, lines 169-200)
- `_validate_schema_node` (function, lines 203-221)
- `_validate_schema` (function, lines 224-235)
- `_array_type` (function, lines 238-243)
- `_object_type` (function, lines 246-255)
- `_schema_type` (function, lines 258-289)
- `_without_null` (function, lines 292-301)
- `_property_line` (function, lines 304-313)
- `_model_interface` (function, lines 316-332)
- `_state_count_field` (function, lines 335-337)
- `_state_partition` (function, lines 340-356)
- `_metric_bucket_fields` (function, lines 359-361)
- `_vocabulary` (function, lines 364-374)
- `_tuple_constant` (function, lines 377-379)
- `_vocabulary_block` (function, lines 382-421)
- `render_typescript` (function, lines 467-495) — Render the public projection module from emitted Pydantic schemas.
- `typescript_text` (function, lines 498-502) — Generate TypeScript from parsed deterministic schema bytes.
- `generated_files` (function, lines 505-506)
- `stale_generated_files` (function, lines 509-515)
- `sync_generated_files` (function, lines 518-522)

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.

### Todos

None.

## Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the class `ProjectionTypeGenerationError` (lines 55-56) — A Python schema shape cannot be represented by this generator.. | `ProjectionTypeGenerationError` | mcp/test_support/agents_remember_test_support/code_quality/projection_types.py:62-63 |
| Defines the function `workspace_projection_schema` (lines 59-61) — The canonical projection schema, copied so callers may safely mutate fixtures.. | `workspace_projection_schema` | mcp/test_support/agents_remember_test_support/code_quality/projection_types.py:66-68 |
| Defines the function `served_projection_schema` (lines 64-66) — The declared HTTP/SSE snapshot schema, including its serve-time tail.. | `served_projection_schema` | mcp/test_support/agents_remember_test_support/code_quality/projection_types.py:71-73 |
| Defines the function `schema_json` (lines 69-72) — Stable bytes for the committed JSON Schema artifact.. | `schema_json` | mcp/test_support/agents_remember_test_support/code_quality/projection_types.py:76-79 |
| Defines the function `_object` (lines 75-78). | `_object` | mcp/test_support/agents_remember_test_support/code_quality/projection_types.py:82-85 |
| Defines the function `_objects` (lines 81-84). | `_objects` | mcp/test_support/agents_remember_test_support/code_quality/projection_types.py:88-91 |
| Defines the function `_strings` (lines 87-90). | `_strings` | mcp/test_support/agents_remember_test_support/code_quality/projection_types.py:94-97 |
| Defines the function `_definitions` (lines 93-94). | `_definitions` | mcp/test_support/agents_remember_test_support/code_quality/projection_types.py:100-101 |
| Defines the function `_properties` (lines 97-98). | `_properties` | mcp/test_support/agents_remember_test_support/code_quality/projection_types.py:104-105 |
| Defines the function `_ref_name` (lines 101-105). | `_ref_name` | mcp/test_support/agents_remember_test_support/code_quality/projection_types.py:108-112 |
| Defines the function `_nullable_variants` (lines 108-110). | `_nullable_variants` | mcp/test_support/agents_remember_test_support/code_quality/projection_types.py:115-117 |
| Defines the function `_is_null` (lines 113-114). | `_is_null` | mcp/test_support/agents_remember_test_support/code_quality/projection_types.py:120-121 |
| Defines the function `_is_nullable` (lines 117-119). | `_is_nullable` | mcp/test_support/agents_remember_test_support/code_quality/projection_types.py:124-126 |
| Defines the function `_json_literal` (lines 122-130). | `_json_literal` | mcp/test_support/agents_remember_test_support/code_quality/projection_types.py:122-130 |
| Defines the function `_enum_values` (lines 133-135). | `_enum_values` | mcp/test_support/agents_remember_test_support/code_quality/projection_types.py:140-142 |
| Defines the function `_schema_allowed_keywords` (lines 138-166). | `_schema_allowed_keywords` | mcp/test_support/agents_remember_test_support/code_quality/projection_types.py:138-166 |
| Defines the function `_schema_children` (lines 169-200). | `_schema_children` | mcp/test_support/agents_remember_test_support/code_quality/projection_types.py:216-247 |
| Defines the function `_validate_schema_node` (lines 203-221). | `_validate_schema_node` | mcp/test_support/agents_remember_test_support/code_quality/projection_types.py:250-268 |
| Defines the function `_validate_schema` (lines 224-235). | `_validate_schema` | mcp/test_support/agents_remember_test_support/code_quality/projection_types.py:271-282 |
| Defines the function `_array_type` (lines 238-243). | `_array_type` | mcp/test_support/agents_remember_test_support/code_quality/projection_types.py:285-290 |
| Defines the function `_object_type` (lines 246-255). | `_object_type` | mcp/test_support/agents_remember_test_support/code_quality/projection_types.py:293-302 |
| Defines the function `_schema_type` (lines 258-289). | `_schema_type` | mcp/test_support/agents_remember_test_support/code_quality/projection_types.py:258-289 |
| Defines the function `_without_null` (lines 292-301). | `_without_null` | mcp/test_support/agents_remember_test_support/code_quality/projection_types.py:339-351 |
| Defines the function `_property_line` (lines 304-313). | `_property_line` | mcp/test_support/agents_remember_test_support/code_quality/projection_types.py:354-366 |
| Defines the function `_model_interface` (lines 316-332). | `_model_interface` | mcp/test_support/agents_remember_test_support/code_quality/projection_types.py:369-385 |
| Defines the function `_state_count_field` (lines 335-337). | `_state_count_field` | mcp/test_support/agents_remember_test_support/code_quality/projection_types.py:388-390 |
| Defines the function `_state_partition` (lines 340-356). | `_state_partition` | mcp/test_support/agents_remember_test_support/code_quality/projection_types.py:393-409 |
| Defines the function `_metric_bucket_fields` (lines 359-361). | `_metric_bucket_fields` | mcp/test_support/agents_remember_test_support/code_quality/projection_types.py:412-414 |
| Defines the function `_vocabulary` (lines 364-374). | `_vocabulary` | mcp/test_support/agents_remember_test_support/code_quality/projection_types.py:417-427 |
| Defines the function `_tuple_constant` (lines 377-379). | `_tuple_constant` | mcp/test_support/agents_remember_test_support/code_quality/projection_types.py:430-432 |

## 260821-CLIVE-L2 Nullable Union Preservation

Nullable-field normalization now removes only null variants. A non-null union is returned intact,
a nullable single variant keeps outer annotations, and a nullable multi-variant union keeps both
its annotations and remaining `anyOf` alternatives. An all-null field still refuses generation.
This lets the lifecycle-operation status schema remain a closed multi-variant union instead of
being flattened or rejected.

| Finding | Anchor | Source |
| --- | --- | --- |
| `_without_null` distinguishes non-null unions, one surviving variant, multiple surviving variants, and the invalid all-null case. | `_without_null` | mcp/test_support/agents_remember_test_support/code_quality/projection_types.py:339-351 |

## 260821-CLIVE Exact Runtime Refinements

The generator has one explicit vocabulary for runtime-only JSON Schema refinements:
`maxItems`, `minimum`, `pattern`, `minLength`, and `maxLength`. Every supported refinement remains
byte-exact in the generated schema and is emitted beside its TypeScript property as deterministic
`JSON Schema refinements` documentation because TypeScript cannot enforce those constraints
structurally. Nested item refinements are preserved recursively.

`_schema_allowed_keywords()` admits a refinement only for the schema shape that can own it;
`_refinement_schema()` and `_refinement_comment()` select and deterministically serialize it.
Unknown or shape-inapplicable keywords still fail closed with the exact model/property path and
remediation. The generator never silently drops schema truth, and this is not a compatibility reader
or fallback around canonical schema validation.

## Update History

- 2026-08-24T15:04+02:00 — Cumulative CLIVE/DAGQC reconciliation: expanded the earlier
  `maxItems` account to the exact supported refinement vocabulary and its fail-closed rendering
  boundary. Timestamp is the curator host's Europe/Berlin system time; verification remains
  closeout-owned.

- 2026-08-24T00:51+02:00 — 260821-CLIVE-L2: reconciled nullable multi-variant union preservation. Verified at code commit `1d446724`.

- 2026-08-12T15:56+02:00 — 260731-EFA-L23 curator body review: reconciled this card with the exact current source delta described above; verification provenance remains closeout-owned.

- 2026-08-08T22:10+02:00 — 260713-TES-L1 completion round 2 (curator): No content impact: the supervisor -> agent-notifier rename does not change the behavior this sidecar documents; reviewed current against the changed source. Verification metadata pinned until closeout stamps the 260713-TES-L1 commit.
- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
