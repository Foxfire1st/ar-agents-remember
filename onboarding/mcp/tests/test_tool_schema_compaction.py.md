# mcp/tests/test_tool_schema_compaction.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

Protects lossless JSON-Schema compaction in `models/tools/tool_schema_compaction.py` and its server-wide wiring in `mcp/server.py::create_server` across both unbound and explainer-mounted surfaces.

## Code Commentary

The autouse `_no_inherited_binding` fixture strips inherited `AR_*` environment variables so in-process server construction is deterministic.

`test_compact_tool_schema_is_lossless_and_immutable` runs `compact_tool_schema` on `_sample_compaction_schema()` and asserts input non-mutation, zero residual violations through `_schema_compaction_violations`, idempotence (`compact_tool_schema(compacted) == compacted`), survival of literal `title`, `description`, and `default` property names and `$defs["title"]`, preservation of non-`null` defaults (`True`, `0`, `""`, `[]`, `50`, `"task-intent/v1"`), `patternProperties`, `dependentSchemas`, Draft-7 list-form `items` (including malformed non-mapping entries), combinators, nested property descriptions (while top-level `$defs.title.description` is stripped), and deep-copy non-aliasing after mutating returned `required`, `enum`, and default list leaves.

`test_create_server_compacts_every_advertised_schema_with_contract_parity` parametrizes `with_explainer` (`False`, `True`), compares `create_server(config).list_tools()` against an uncompacted baseline (monkeypatching `server_module._compact_server_tool_schemas` to a no-op), and asserts identical tool order, identical read-only `annotations`, zero compaction violations on every tool's `inputSchema`, and exact equality with `_contract_signature(raw.inputSchema)`.

## Relationships

Declared in the `unit-regression` lane of [`test-evidence-lanes.toml`](test-evidence-lanes.toml.md), and named in [`evidence-lifecycle.toml`](evidence-lifecycle.toml.md) as an exact consumer of `_user_settings_guard.py` and the Node-profile `package-lock.json`. Complements [`test_role_tool_scope.py`](test_role_tool_scope.py.md) (which enforces per-role compact byte ceilings, the 500-character raw description ceiling, and real-stdio Manager 32-tool validation) and [`test_tool_descriptions.py`](test_tool_descriptions.py.md) (which enforces normalized 600-character bounds, doc pointers, and 120-character argument descriptions).

## Evidence

- Unit test proves the three lossless metadata drops, literal property and `$defs` name survival, idempotence, malformed-entry safety, and deep-copy immutability. [1]
- Server parity test proves exact tool order, read-only annotation parity, zero residual compaction violations, and wire-contract parity on both unbound and explainer-mounted servers. [2]
