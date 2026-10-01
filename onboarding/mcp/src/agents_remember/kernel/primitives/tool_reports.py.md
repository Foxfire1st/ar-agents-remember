# mcp/src/agents_remember/kernel/primitives/tool_reports.py

## Governing Overview

[kernel primitives overview](overview.md)

## Purpose

`kernel/primitives/tool_reports.py` (moved from `mcp/tool_reports.py` by 260731-EFA-L9) writes bulk tool diagnostics to temp report files so verbose
passthrough payloads (raw provider status trees, watcher rebind runs, command
transcripts — historically up to >50k chars per response) stay out of MCP tool
responses. The compact response keeps the outcome plus a `reportPath`.

## Code Commentary

### Logic

`write_tool_report(coordination_root, tool, payload, label)` writes redacted
JSON to `temp/tool-reports/<tool>/<UTC-timestamp>-<label>.json` (collision
counter on same-second writes) and immediately prunes the folder.
`prune_tool_reports` keeps the newest `KEEP_LAST` (5) files and drops anything
older than `MAX_AGE_DAYS` (7). `redact_secrets` walks the whole structure and
masks `PASSWORD=...` values in any string.

### Invariants And Boundaries

- Retention is write-time and deterministic — no daemons, timers, or hidden
  background behavior; disk stays bounded regardless of call frequency.
- Reports are files on disk: secrets are redacted unconditionally (the
  response-path `summarize_command_logs` only redacts failing nodes).
- Consumers: `runtime_install`, `provider_diagnostics`, `provider_watchers`
  payload builders in the MCP tool layer; internal callers keep full data.

## Evidence

### Repo-Internal References

- Compact builders that pair with the reports. [1]
