# mcp/src/agents_remember/code_quality/projection_types.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/code_quality/projection_types.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[overview](../../../overview.md)

## Purpose

Generate the dashboard projection contract from the Python wire schemas.

## Code Commentary

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
| Defines the class `ProjectionTypeGenerationError` (lines 55-56) — A Python schema shape cannot be represented by this generator.. | `ProjectionTypeGenerationError` | mcp/src/agents_remember/code_quality/projection_types.py:55-56 |
| Defines the function `workspace_projection_schema` (lines 59-61) — The canonical projection schema, copied so callers may safely mutate fixtures.. | `workspace_projection_schema` | mcp/src/agents_remember/code_quality/projection_types.py:59-61 |
| Defines the function `served_projection_schema` (lines 64-66) — The declared HTTP/SSE snapshot schema, including its serve-time tail.. | `served_projection_schema` | mcp/src/agents_remember/code_quality/projection_types.py:64-66 |
| Defines the function `schema_json` (lines 69-72) — Stable bytes for the committed JSON Schema artifact.. | `schema_json` | mcp/src/agents_remember/code_quality/projection_types.py:69-72 |
| Defines the function `_object` (lines 75-78). | `_object` | mcp/src/agents_remember/code_quality/projection_types.py:75-78 |
| Defines the function `_objects` (lines 81-84). | `_objects` | mcp/src/agents_remember/code_quality/projection_types.py:81-84 |
| Defines the function `_strings` (lines 87-90). | `_strings` | mcp/src/agents_remember/code_quality/projection_types.py:87-90 |
| Defines the function `_definitions` (lines 93-94). | `_definitions` | mcp/src/agents_remember/code_quality/projection_types.py:93-94 |
| Defines the function `_properties` (lines 97-98). | `_properties` | mcp/src/agents_remember/code_quality/projection_types.py:97-98 |
| Defines the function `_ref_name` (lines 101-105). | `_ref_name` | mcp/src/agents_remember/code_quality/projection_types.py:101-105 |
| Defines the function `_nullable_variants` (lines 108-110). | `_nullable_variants` | mcp/src/agents_remember/code_quality/projection_types.py:108-110 |
| Defines the function `_is_null` (lines 113-114). | `_is_null` | mcp/src/agents_remember/code_quality/projection_types.py:113-114 |
| Defines the function `_is_nullable` (lines 117-119). | `_is_nullable` | mcp/src/agents_remember/code_quality/projection_types.py:117-119 |
| Defines the function `_json_literal` (lines 122-130). | `_json_literal` | mcp/src/agents_remember/code_quality/projection_types.py:122-130 |
| Defines the function `_enum_values` (lines 133-135). | `_enum_values` | mcp/src/agents_remember/code_quality/projection_types.py:133-135 |
| Defines the function `_schema_allowed_keywords` (lines 138-166). | `_schema_allowed_keywords` | mcp/src/agents_remember/code_quality/projection_types.py:138-166 |
| Defines the function `_schema_children` (lines 169-200). | `_schema_children` | mcp/src/agents_remember/code_quality/projection_types.py:169-200 |
| Defines the function `_validate_schema_node` (lines 203-221). | `_validate_schema_node` | mcp/src/agents_remember/code_quality/projection_types.py:203-221 |
| Defines the function `_validate_schema` (lines 224-235). | `_validate_schema` | mcp/src/agents_remember/code_quality/projection_types.py:224-235 |
| Defines the function `_array_type` (lines 238-243). | `_array_type` | mcp/src/agents_remember/code_quality/projection_types.py:238-243 |
| Defines the function `_object_type` (lines 246-255). | `_object_type` | mcp/src/agents_remember/code_quality/projection_types.py:246-255 |
| Defines the function `_schema_type` (lines 258-289). | `_schema_type` | mcp/src/agents_remember/code_quality/projection_types.py:258-289 |
| Defines the function `_without_null` (lines 292-301). | `_without_null` | mcp/src/agents_remember/code_quality/projection_types.py:292-301 |
| Defines the function `_property_line` (lines 304-313). | `_property_line` | mcp/src/agents_remember/code_quality/projection_types.py:304-313 |
| Defines the function `_model_interface` (lines 316-332). | `_model_interface` | mcp/src/agents_remember/code_quality/projection_types.py:316-332 |
| Defines the function `_state_count_field` (lines 335-337). | `_state_count_field` | mcp/src/agents_remember/code_quality/projection_types.py:335-337 |
| Defines the function `_state_partition` (lines 340-356). | `_state_partition` | mcp/src/agents_remember/code_quality/projection_types.py:340-356 |
| Defines the function `_metric_bucket_fields` (lines 359-361). | `_metric_bucket_fields` | mcp/src/agents_remember/code_quality/projection_types.py:359-361 |
| Defines the function `_vocabulary` (lines 364-374). | `_vocabulary` | mcp/src/agents_remember/code_quality/projection_types.py:364-374 |
| Defines the function `_tuple_constant` (lines 377-379). | `_tuple_constant` | mcp/src/agents_remember/code_quality/projection_types.py:377-379 |

## Update History

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
