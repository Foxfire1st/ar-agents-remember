# mcp/src/agents_remember/models/tools/tool_schema_compaction.py

## Governing Overview

[Models route overview](../overview.md)

## Purpose

Pure, stdlib-only model-layer helper exporting `compact_tool_schema(schema)`, which returns a freshly deep-copied, lossless compacted JSON Schema for one advertised MCP tool. `mcp/server.py` invokes it once over every registered tool before role narrowing so advertised `inputSchema` payloads drop auto-generated metadata bloat without altering Python model docstrings, wire parameter contracts, or runtime Pydantic validation.

## Code Commentary

`_should_drop_keyword` enforces the exact three lossless metadata drops on schema nodes: (1) `"title"`, (2) `"default"` only when `value is None` (preserving every non-`null` default such as `False`, `True`, `0`, `""`, `[]`, or string/integer defaults), and (3) `"description"` only when `strip_description=True`.

`_compact_keyword_value` strictly separates name-keyed maps from schema nodes. It sets `strip_entry_description=is_root` exclusively on `"$defs"`, so model-level `"description"` prose is stripped only on immediate top-level `"$defs"` definitions while field-level property descriptions survive. For `_SCHEMA_MAP_KEYS` (`"properties"`, `"patternProperties"`, `"dependentSchemas"`), `_compact_schema_map` preserves every key name verbatim, so properties or definitions literally named `"title"`, `"default"`, or `"description"` are never dropped. It recurses through `_NESTED_SCHEMA_KEYS` (`"items"`, `"additionalProperties"`, `"not"`, `"if"`, `"then"`, `"else"`) and list-form `_SCHEMA_LIST_KEYS` (`"items"`, `"anyOf"`, `"oneOf"`, `"allOf"`, `"prefixItems"`), deep-copying non-mapping entries and non-schema mutable leaves (`required`, `enum`, non-`null` defaults) via `copy.deepcopy` so callers' input dicts are neither mutated nor aliased and malformed non-mapping entries pass through safely.

Compaction does not rewrite `anyOf` nullability, inline or rename `$defs`/`$ref`, or strip `additionalProperties`, `required`, `enum`, `const`, or `pattern`.

## Relationships

[`mcp/server.py`](../../mcp/server.py.md) calls `compact_tool_schema` through `_compact_server_tool_schemas` inside `create_server` immediately after `apply_read_only_marks` and before `_bound_role_tools` / `_scope_server_tools`, compacting unbound, role-bound, and explainer surfaces alike while leaving FastMCP's `fn_metadata.arg_model` untouched. The module sits at layer rank 2 beside [`role_tool_scope.py`](role_tool_scope.py.md) and [`tool_descriptions.py`](tool_descriptions.py.md), imports stdlib only (`copy`, `collections.abc`, `typing`), and is protected by [`test_tool_schema_compaction.py`](../../../../../tests/test_tool_schema_compaction.py.md) and [`test_role_tool_scope.py`](../../../../../tests/test_role_tool_scope.py.md).

## Evidence

- Public entry point starts root-level lossless schema compaction and returns an unaliased deep copy. [1]
- Drops only schema-level `title`, `default: null`, and flagged `description` metadata. [2]
- Separates root `$defs` and name-keyed schema maps from nested schema nodes and lists while deep-copying mutable leaves. [3]
- Recurses over schema nodes while applying the exact lossless keyword drops. [4]
