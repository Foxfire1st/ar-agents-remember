# test_compact_content.py

## Current operative account

`test_compact_content.py` (`CompactToolResultWireTests`) verifies the MCP 2.x direct `CallToolResult` wire contract in `mcp/tool_results.py` and `AgentsRememberMCP` over `Client(server, mode="legacy")`:

- `test_dict_content_blocks_are_compact_utf8_json` verifies `compact_content_blocks` serializes dict results into compact UTF-8 JSON `TextContent` blocks without indentation.
- `test_wire_tool_list_answers_and_extension_match_start_tree_contract` verifies `initialize` capabilities (`extensions` and `experimental={}`), all 44 public tools' `<name>DictOutput` schemas, compact JSON text mirroring `structured_content`, exact validation and unknown-tool `ToolError` wire texts, `skills/list`, `skills/get`, and `skill://index.json`.
- `test_explainer_tools_and_early_refusals_preserve_start_tree_wire_shape` verifies bare-dict explainer tools omit `outputSchema` and emit compact JSON without `structured_content`, while forged-seat and stale-build early refusals emit indented JSON text with `structured_content`.

## Evidence

- Direct `CallToolResult` construction and compact JSON serialization live in `mcp/tool_results.py` (`build_call_tool_result`, `compact_content_blocks`, `build_early_refusal_result`), replacing the retired `compact_content.py` monkeypatch. [1]
- `create_server()` constructs `AgentsRememberMCP` with `build_skills_extension()` and `preserve_handshake_extensions`, and dispatches tool results through `build_call_tool_result` and `build_early_refusal_result`. [2]

- MCP settings fixtures come from `test_config.py`. [3]

## Historical original card — preserved, not the current operative account

<details>
<summary>Retained original source accounts and producer history</summary>

## Governing Overview

[overview.md](../overview.md)

## Purpose

`test_compact_content.py` originally verified the 1.x FastMCP compact-content shim (`compact_content.py`, retired under `261125-DEP-L3`): that it installed once, left non-JSON blocks alone, and minified the JSON text mirror of a real tool call without disturbing structured content.

## Code Commentary

### Logic

Historical 1.x cases (`test_install_is_idempotent`, `test_non_json_text_blocks_pass_through`, `test_tool_call_text_block_is_compact_and_matches_structured`) tested `install_compact_content()` and `func_metadata._convert_to_content` over `create_connected_server_and_client_session`. Those cases were replaced by `CompactToolResultWireTests` against `mcp/tool_results.py` and `Client(server, mode="legacy")`.

</details>
