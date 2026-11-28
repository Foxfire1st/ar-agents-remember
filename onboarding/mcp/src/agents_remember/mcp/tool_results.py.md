# mcp/src/agents_remember/mcp/tool_results.py

## Governing Overview

[overview](../../../overview.md)

## Purpose

Constructs direct MCP 2.x `CallToolResult` values inside the MCP adapter boundary using only public `mcp.server.mcpserver` / `mcp.types` and `pydantic` APIs, without monkeypatching SDK internals, inspecting private `fn_metadata`, or holding process-global state. Serializes JSON text blocks with compact single-line UTF-8 separators (`ensure_ascii=False`, `separators=(",", ":")`), preserves schema-validated `structured_content` for explicitly typed tools while omitting it when `structured_output=False`, and emits compact single-line UTF-8 JSON with `structured_content=None` for early-return transport guard refusals.

## Code Commentary

### Logic

- `compact_json_text(value)` dumps `value` through `pydantic_core.to_json(..., fallback=str)` and re-emits compact UTF-8 JSON (`ensure_ascii=False`, `separators=(",", ":")`).
- `compact_content_blocks(result)` converts Python return values into compact MCP content blocks: `None` becomes `[]`, existing content block types pass through unchanged, public `mcp.server.mcpserver` `Image`/`Audio` helpers convert via their content methods, lists/tuples flatten recursively, strings stay verbatim in `TextContent`, and all other values serialize via `compact_json_text`.
- `structured_output_spec(fn, structured_output=None)` derives a frozen `StructuredOutputSpec(output_model, wrap_output)` purely from `fn`'s Python return annotation (`inspect.signature(..., eval_str=True)` and `pydantic.TypeAdapter(...).json_schema()`): returning `None` when `structured_output=False`, when the return type is missing, content-only, bare `dict`, or non-schema-serializable; unwrapping `Annotated`/`InputRequiredResult`/`CallToolResult` unions; and setting `wrap_output=True` for primitives and non-`dict[str, ...]` generics.
- `build_call_tool_result(spec, result)` passes `InputRequiredResult` and `CallToolResult` through unchanged; otherwise builds `CallToolResult(content=compact_content_blocks(result))`, adding `TypeAdapter`/`BaseModel`-validated `structured_content` (wrapped under `{"result": dumped}` when `spec.wrap_output` is set) only when `spec` is present. Tools registered without a `StructuredOutputSpec` (including the 44 generic `dict[str, Any]`/`dict[str, object]` public tools and bare-dict explainer tools) emit compact text blocks and `structured_content=None`.
- `build_early_refusal_result(payload)` constructs `CallToolResult(content=[TextContent(type="text", text=compact_json_text(payload))], structured_content=None)` for early-return transport guard refusals (explainer forged-seat and stale-build guards), emitting compact single-line UTF-8 JSON text with no duplicate `structured_content`.

### Invariants And Boundaries

- Keeps all MCP SDK result types inside `mcp/` (importing only public `Audio`, `Image`, and `mcp.types`) so `application/tool_response.py` remains transport-independent and no internal SDK tools/utilities module is imported.
- Holds no process-global mutable state and installs no SDK monkeypatch (replacing the retired `compact_content.py` patch on `func_metadata._convert_to_content`).
- Generic `dict[str, Any]`/`dict[str, object]` public tools omit `<name>DictOutput` `outputSchema` and duplicate `structured_content` (via `AgentsRememberMCP.add_tool`), while explicitly typed `BaseModel` tools keep `outputSchema` and validated `structured_content`, bare-dict explainer tools emit compact text without `structured_content`, and early-return guard refusals emit compact single-line UTF-8 JSON text with `structured_content=None`.

## Evidence

- `structured_output_spec` and `build_call_tool_result` derive structured-output plans from return annotations and build compact `CallToolResult` values with validated `structured_content` only when a spec is present. [1]
- `compact_content_blocks` and `compact_json_text` serialize Python tool results into compact UTF-8 JSON `TextContent` and media blocks. [2]

- `build_early_refusal_result` emits compact single-line UTF-8 JSON text via `compact_json_text` with `structured_content=None` for early-return transport guard refusals. [3]
- `AgentsRememberMCP.add_tool` disables `structured_output` for generic `dict[str, Any]`/`dict[str, object]` return annotations, computes `structured_output_spec`, and routes normal calls and early refusals through `wrap_registered_tool` and `build_early_refusal_result`. [4]
- Wire-parity tests verify compact single-line JSON text, omitted generic `outputSchema` and `structured_content`, bare-dict explainer outputs, and compact early refusals over `Client(server, mode="legacy")`. [5]
