# mcp/tests/test_mcp_build_staleness.py

## Governing Overview

[overview](overview.md)

## Purpose

Proves that an installed MCP server whose loaded build is stale refuses the declared publication operations before their handler runs, while reads, messages, planning calls, dry runs and unknown tool names keep answering with the stale reading attached.

## Code Commentary

The module patches `agents_remember.mcp.server.build_currentness` with a fixed `installed`/`stale` reading carrying two distinct digests, then calls tools registered on a real `AgentsRememberMCP` instance, once over the in-memory MCP client transport and otherwise through `call_tool`. A stale publication answers `ok: false` with code `server-build-stale`, both digests, the restart-or-reconnect remedy and the `buildCurrentness` payload, and the handler is never entered; the same call with `dry_run: true` enters the handler and carries the stale annotation. The publication set is checked from both sides through `is_stale_build_write`: `knowledge_write` counts only with `commit: true`, `curator_coherence` only for `action: publish`, `citation_fix` not in `poll` mode, and every `task_doc` operation except `linkage_report` and except a dry run. A non-publication call answers under a stale, absent or `unknown` reading, and only the stale reading adds the annotation.

Two answer-shaping cases sit beside the gate: the stale annotation survives the overflow short form within a 400-token bound, and a `runtime_install` dry-run preview with 50 host actions keeps all of them in the call's named log rather than a `reportPath`. The last case shows `run_runtime_install` planning the dashboard with `plan_running_dashboard` on a dry run (never `ensure_running_dashboard`) and, on a real run, reporting a failed dashboard restart as `ok: false` with its detail and pid. Builds, installs and the dashboard are fakes; no live server restarts.

## Evidence

- A stale refusal is structured content over the real MCP transport and the handler is not entered [1]
- Every declared publication refuses before its handler with both digests and the remedy; its dry run answers [2]
- Reads, messages, planning calls and unknown tools are not publication; unknown or absent readings add no annotation [3]
- Every task-document operation except `linkage_report` and dry runs is publication [4]
- A runtime-install preview keeps every host action in its named log [5]
- The stale annotation survives answer overflow [6]
- Runtime install previews the dashboard without restarting it and reports a failed restart [7]
- The publication predicate under test [8]
