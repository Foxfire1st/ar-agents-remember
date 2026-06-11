# test_compact_content.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_compact_content.py`        |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-29T08:53+02:00                     |
| lastVerifiedCommitHash | `a06bfa65dcee3c8b82652085c69f2a20f163e306` |
| lastVerifiedCommitDate | 2026-05-29T09:05:12+02:00                  |
| governingOverview      | `overview.md`                              |

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

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The shim under test installs the FastMCP converter patch. | [compact_content.py](agents-remember/mcp/src/agents_remember/mcp/compact_content.py) |
| `create_server()` installs the shim before registering tools. | [server.py](agents-remember/mcp/src/agents_remember/mcp/server.py) |
| MCP settings fixtures come from `test_config.py`. | [test_config.py](agents-remember/mcp/tests/test_config.py) |

## Update History

- 2026-05-29T08:53+02:00: Created onboarding for the compact-content shim tests.
