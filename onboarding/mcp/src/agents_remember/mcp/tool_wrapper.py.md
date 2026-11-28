# mcp/src/agents_remember/mcp/tool_wrapper.py

## Governing Overview

[overview](../../../overview.md)

## Purpose

Wraps each tool callable registered through `AgentsRememberMCP.add_tool` in an async handler that enforces stale-build publication refusal, synchronous write-lock ordering and `thread_workers` offloading, and direct compact `CallToolResult` construction without reading private MCP SDK metadata.

## Code Commentary

`AgentsRememberMCP.add_tool` binds one frozen `RegisteredToolPolicy` (tool name, effective `ToolAnnotations`, return-annotation `StructuredOutputSpec | None`, write-lock supplier, and write-lock cancellation logger) and calls `wrap_registered_tool(fn, policy)` before registering the wrapper with `MCPServer.add_tool`.

- `is_async_callable(fn)` detects coroutine functions and callable objects whose `__call__` is a coroutine function.
- `admitted_arguments(kwargs)` normalizes SDK-validated keyword arguments for staleness and write-lock classification: it skips injected `Context` parameters and converts `pydantic.BaseModel` values via `model_dump()` so nested request models (`memory_quality_check`, `curator_coherence`) remain inspectable as dicts.
- `nonwriting_call(tool_name, annotations, arguments)` lets advertised read-only tools (`read_only_hint is True`) and explicitly non-writing modes (`context_packet` with `include_freshness` false, `memory_quality_check` in `start`/`poll`, `citation_fix` in `start`/`poll` or `dry_run=True`) bypass the per-server synchronous write lock.
- `wrap_registered_tool(fn, policy)` preserves `fn`'s signature and metadata via `@functools.wraps(fn)` so `MCPServer` keeps the original input/output schemas. On invocation, after the SDK validates arguments:
  1. If `current_tool_build_currentness()` carries an installed stale reading and `is_stale_build_write(policy.tool_name, admitted)` is true, it builds `stale_build_refusal` in a detached request thread (`run_in_detached_request_thread`) and returns `build_early_refusal_result(refused)` without running `fn`.
  2. Async callables run directly on the event loop; synchronous callables run through `_run_sync_call`, which offloads via `run_in_request_thread` and serializes potentially mutating sync calls under the server's write lock until their worker exits (logging `write-lock` cancellation via `on_write_lock_cancelled` if cancelled before lock acquisition).
  3. Normal results convert through `build_call_tool_result(policy.output_spec, raw)` into a compact `CallToolResult` (or pass `InputRequiredResult` / `CallToolResult` through unchanged).

## Relationships

Called exclusively from `mcp/server.py` (`AgentsRememberMCP.add_tool`), delegating stale-build checks to `mcp/build_staleness.py`, thread execution to `mcp/thread_workers.py`, and wire conversion to `mcp/tool_results.py`. Keeps synchronous offload, write-lock policy, and stale-build enforcement off `MCPServer` private attributes (`_tool_manager`, `fn_metadata`, `Tool.model_copy`).

## Evidence

- `RegisteredToolPolicy` binds per-tool annotations, structured output plan, write-lock acquisition, and write-lock cancellation logging. [1]
- `admitted_arguments` skips injected `Context` values and dumps validated `BaseModel` arguments to dicts for staleness and write-lock checks. [2]
- `nonwriting_call` bypasses the synchronous write lock only for centrally read-only tools and explicitly non-writing modes. [3]
- `wrap_registered_tool` checks stale-build publication refusal before execution, dispatches async or offloaded sync handlers, and returns compact `CallToolResult` values. [4]
- `_run_sync_call` offloads synchronous handlers via `run_in_request_thread` and holds the server write lock around potentially mutating calls while logging pre-acquisition cancellations. [5]

- `AgentsRememberMCP.add_tool` merges `read_only_annotations`, disables `structured_output` for generic `dict[str, Any]`/`dict[str, object]` tools before computing `structured_output_spec`, wraps each tool with `wrap_registered_tool`, and registers it via public `MCPServer.add_tool`. [6]
