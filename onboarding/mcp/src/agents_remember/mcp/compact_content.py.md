# mcp/src/agents_remember/mcp/compact_content.py

| Field                  | Value                                                |
| ---------------------- | ---------------------------------------------------- |
| repository             | agents-remember                                   |
| path                   | `mcp/src/agents_remember/mcp/compact_content.py`     |
| doc_type               | `file-level-onboarding`                              |
| lastUpdated            | 2026-05-29T08:53+02:00                               |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb`           |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
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
whose text parses as JSON using `json.dumps(..., separators=("", ":"))`.
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

| Finding | Anchor | Source |
| --- | --- | --- |
| `create_server()` installs the shim as its first action. | `create_server` | mcp/src/agents_remember/mcp/server.py:32-44 |
| Behavior is verified through an in-process tool call. | `test_tool_call_text_block_is_compact_and_matches_structured` | mcp/tests/test_compact_content.py:50-72 |

## Update History

- 2026-08-03T02:32:19+02:00: Curator W3-B02 anchored 2 Repo-Internal citation rows with 2 exact identifiers and generated source ranges; verification metadata was preserved.
- 2026-05-29T08:53+02:00: Created onboarding for the FastMCP compact-content shim that minifies the JSON text mirror of tool results.
