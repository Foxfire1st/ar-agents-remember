# mcp/src/agents_remember/application/tool_build_currentness.py

## Governing Overview

[overview](overview.md)

## Purpose

Carry one tool call's installed-build currentness reading from the MCP dispatch to the response shaping that runs in worker threads, so a stale installed server can annotate its ordinary answers.

## Code Commentary

The reading lives in a module `ContextVar` (default `None`). `tool_build_currentness(reading)` is a context manager that sets it for the duration of one call and always resets it on exit; `mcp/server.py` wraps each tool dispatch in it with the reading it took from `serving.build_currentness.build_currentness`. Because `asyncio.to_thread` copies the context, the response shaping that runs in a worker thread sees the same reading.

`current_tool_build_currentness()` returns the reading only when its `mode` is `installed` and its `state` is `stale`; a current, unknown or checkout reading, or no reading at all, returns `None`. `application/tool_response.py` calls it while enriching the validated envelope and sets `buildCurrentness` only from that filtered value. The status surface (`server_info`) inspects currentness itself and does not depend on this filter.

The module decides nothing about refusing a call: which writes a stale installed build may not run is decided in `mcp/build_staleness.py` before dispatch.

## Evidence

- Only an installed, stale reading is returned to annotate ordinary answers. [1]
- The reading is set for one call and always reset on exit. [2]
- The MCP dispatch takes the reading and runs the call inside the context manager. [3]
- Response enrichment attaches the filtered reading as `buildCurrentness`. [4]
