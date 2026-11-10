# mcp/src/agents_remember/mcp/build_staleness.py

## Governing Overview

[overview](../../../overview.md)

## Purpose

Names the publication tool calls that an MCP server running a stale installed build must refuse, and builds that refusal answer.

## Code Commentary

`server.py`'s `call_tool` asks this module only when the process's build reading is an installed build in state `stale`, after validating the call's arguments against the registered tool's argument model. `is_stale_build_write(name, arguments)` matches publication, not every side effect:

- any call with `dry_run` exactly `True` is not a write;
- the fixed `_WRITERS` set — closeout apply, integration, checkpoint and recorded landing, direct landing, sync, lifecycle finalize, citation note revision, route-index refresh, memory init, baseline adopt, carryover apply and task reopen — is a write;
- `knowledge_write` is a write only with `commit` exactly `True`;
- `citation_fix` is a write unless its `mode` is `poll` (absent mode counts as `sync`);
- `curator_coherence` is a write only when its `request` mapping's `action` is `publish`;
- `task_doc` is a write for every valid operation except `linkage_report`; the operation list is imported from the task-document tools only at that point, never during discovery.

Every other name — reads, previews, checkout work, host operations, messages and tool names this set does not list — returns `False`, so a newly added publication tool is not refused until it is named here.

`stale_build_refusal(name, reading)` answers through `complete_tool_response` with `ok: false`, code `server-build-stale`, an error naming the loaded and installed digests and the remedy (restart or reconnect this MCP server, or restart the dashboard if it serves the call), and the reading as `buildCurrentness`. The answer boundary validates that payload against the shared `StaleBuildRefusalResponse` model instead of the tool's own response model, and keeps the whole stripped result as the answer.

## Evidence

- The fixed publication-writer set. [1]
- An explicit dry run is never a stale-build write. [2]
- `knowledge_write` counts only with `commit` set to `True`. [3]
- `citation_fix` counts unless it polls. [4]
- `curator_coherence` counts only for the publish action. [5]
- `task_doc` counts for every valid operation except the linkage report, imported lazily. [6]
- The refusal answer carries code `server-build-stale`, both digests, the remedy and the reading. [7]
- Dispatch consults this module only for a stale installed build, after argument validation. [8]
- A `server-build-stale` payload validates against the shared refusal model. [9]
- The answer boundary keeps the stripped whole result for a stale-build refusal. [10]
