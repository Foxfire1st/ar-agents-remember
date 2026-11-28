# test_compact_content.py

## Current operative account

`test_compact_content.py` (`CompactToolResultWireTests`) verifies the MCP 2.x direct `CallToolResult` wire contract in `mcp/tool_results.py` and `AgentsRememberMCP` over `Client(server, mode="legacy")`:

- `test_dict_content_blocks_are_compact_utf8_json` verifies `compact_content_blocks` serializes dict results into compact UTF-8 JSON `TextContent` blocks without indentation.
- `test_wire_tool_list_answers_and_extension_match_start_tree_contract` verifies `initialize` capabilities (`extensions` and `experimental={}`), all 44 generic `dict[str, Any]`/`dict[str, object]` public tools omit `outputSchema` and emit compact single-line JSON text with `structured_content=None`, exact validation and unknown-tool `ToolError` wire texts, `skills/list`, `skills/get`, and `skill://index.json`.
- `test_explainer_tools_and_early_refusals_preserve_start_tree_wire_shape` verifies bare-dict explainer tools omit `outputSchema` and emit compact JSON without `structured_content`, and forged-seat and stale-build early refusals also emit compact single-line UTF-8 JSON text with `structured_content=None`.
- `test_every_roles_wire_tool_list_keeps_exact_bytes_and_unmutated_stored_tools` verifies base `MCPServer.list_tools` schemas stay uncompacted, `server_info` merges site-declared `ToolAnnotations` hints (`readOnlyHint: True`, `destructiveHint: False`, `idempotentHint: True`, `openWorldHint: False`), `read_ar_files` omits `refresh`, and every canonical role and `system-specialist` alias matches the unbound wire slice byte-for-byte.
- `test_no_private_mcp_sdk_access_remains_in_repository` scans `mcp/src`, `mcp/test_support`, `scripts`, and `mcp/tests` via AST to fail on any private MCP SDK attribute access or internal SDK module import.

## Evidence

- `create_server()` constructs `AgentsRememberMCP` with `build_skills_extension()`, `preserve_handshake_extensions`, and `enforce_read_only_marks=True`, and dispatches tool results through registration-time `wrap_registered_tool` (`build_call_tool_result` and `build_early_refusal_result`). [2]

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

- Direct CallToolResult construction and compact single-line UTF-8 JSON serialization live in mcp/tool_results.py (build_call_tool_result, compact_content_blocks, build_early_refusal_result). [1]

- Role wire-byte parity, merged server_info ToolAnnotations, unmutated stored tool schemas, and repository-wide private MCP SDK access AST guard live in CompactToolResultWireTests. [4]
