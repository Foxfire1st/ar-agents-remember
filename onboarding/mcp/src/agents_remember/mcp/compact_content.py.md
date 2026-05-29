# mcp/src/agents_remember/mcp/compact_content.py

| Field                  | Value                                                |
| ---------------------- | ---------------------------------------------------- |
| repository             | agents-remember-md                                   |
| path                   | `mcp/src/agents_remember/mcp/compact_content.py`     |
| doc_type               | `file-level-onboarding`                              |
| lastUpdated            | 2026-05-29T08:53+02:00                               |
| lastVerifiedCommitHash | `a06bfa65dcee3c8b82652085c69f2a20f163e306`           |
| lastVerifiedCommitDate | 2026-05-29T09:05:12+02:00                            |
| governingOverview      | `../../../overview.md`                               |

## Purpose

`compact_content.py` removes FastMCP's hardcoded pretty-printing from the
unstructured JSON text block that mirrors every tool result, so tool responses
do not waste tokens on indentation whitespace.

## Code Commentary

### Logic

FastMCP serializes the text mirror of a tool result with
`pydantic_core.to_json(result, fallback=str, indent=2)` inside
`mcp.server.fastmcp.utilities.func_metadata._convert_to_content`. There is no
public configuration hook for that indent in the supported `mcp` range.

`install_compact_content()` monkeypatches `_convert_to_content` with a wrapper
that calls the original converter, then re-serializes any `TextContent` block
whose text parses as JSON using `json.dumps(..., separators=(",", ":"))`.
`_compact_text_block()` performs the per-block re-serialization and returns the
block unchanged when the text is not JSON (wrapped in `contextlib.suppress`),
so plain-string and already-minified blocks pass through untouched. The patch is
idempotent: a module-level `_installed` flag short-circuits repeated calls, so it
is safe to invoke from every `create_server()`.

The shim only rewrites the unstructured text content. The `structuredContent`
half of the result is produced elsewhere in FastMCP and is never touched, so the
compacted text remains a faithful mirror of the structured payload.

### Invariants And Boundaries

- This patches a FastMCP internal (`func_metadata._convert_to_content`). It must
  be re-validated on any `mcp` upgrade; `pyproject.toml` keeps the `mcp<2` upper
  bound for this reason.
- Only re-serialize JSON text blocks; never raise on non-JSON content.
- Do not touch `structuredContent`; the shim is text-mirror-only.
- Keep installation idempotent and side-effect-free beyond the one-time patch.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| `create_server()` installs the shim as its first action. | [server.py](agents-remember-md/mcp/src/agents_remember/mcp/server.py) |
| Behavior is verified through an in-process tool call. | [test_compact_content.py](agents-remember-md/mcp/tests/test_compact_content.py) |

## Update History

- 2026-05-29T08:53+02:00: Created onboarding for the FastMCP compact-content shim that minifies the JSON text mirror of tool results.
