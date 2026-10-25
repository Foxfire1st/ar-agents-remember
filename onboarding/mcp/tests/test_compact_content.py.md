# test_compact_content.py

## Current operative account — MIK-R112

The current source facts below replace the former operative inventory. The separately labelled superseded claims describe only the pre-repair card. Original paragraphs, dated closures, evidence and citation identities remain intact in the explicitly historical section; they grant no current call, restored route or fresh execution acceptance.

- Current test calls server_info via _call_server_info.
- Minified text equality and structured-content assertions survive.

### Superseded inventory

- Pre-repair card claim: Card says the real MCP probe calls ping via _call_ping. This is superseded archival wording, not a current prescription.

### Source and authority bounds

- Source comparison: `mcp/tests/test_compact_content.py:50-79`.

Source inspection supplies no new test, native-host, whole-build, landing or memory acceptance. Retained internal services and historical fixtures do not re-advertise deleted MCP tools. Numbered references retain historical custody and may include disclosed inherited stale targets; currentness or proof truth is not inferred from them.

## Historical original card — preserved, not the current operative account

<details>
<summary>Retained original source accounts and producer history</summary>

## Governing Overview

[overview.md](../overview.md)

## Purpose

`test_compact_content.py` verifies the FastMCP compact-content shim: that it
installs once, leaves non-JSON blocks alone, and minifies the JSON text mirror of
a real tool call without disturbing structured content.

## Code Commentary

### Logic

`test_install_is_idempotent` calls `install_compact_content()` twice and asserts
the converter reference is unchanged after the second call.

`test_non_json_text_blocks_pass_through` feeds a plain string through the patched
`func_metadata._convert_to_content` and asserts the text is returned verbatim.

`test_tool_call_text_block_is_compact_and_matches_structured` builds a real
server with `create_server()` (which installs the shim), calls the `ping` tool
through an in-memory client session (`create_connected_server_and_client_session`
driven with `anyio.run`), and asserts the text block parses as JSON, contains no
newline, equals `result.structuredContent`, and reports `ok`.

### Conventions

The in-process session uses `server._mcp_server` (the low-level server behind
FastMCP) and the in-memory transport from `mcp.shared.memory`, so no stdio
subprocess is required. The `ping` tool is used because it needs no fixture state
beyond trusted settings.

### Invariants And Boundaries

The shim is text-mirror-only: the parsed text must equal `structuredContent`, and
the compaction must never raise on non-JSON content.

## Evidence

### Repo-Internal References

- The shim under test installs the FastMCP converter patch. [1]

- `create_server()` installs the shim before registering tools. [2]

- MCP settings fixtures come from `test_config.py`. [3]

</details>
