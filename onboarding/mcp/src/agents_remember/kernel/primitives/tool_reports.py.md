# mcp/src/agents_remember/kernel/primitives/tool_reports.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/kernel/primitives/tool_reports.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-10T05:30+02:00                     |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`|
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `overview.md`                              |

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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Compact builders that pair with the reports. | `compact_runtime_install_payload`; `compact_diagnostics_payload`; `compact_watchers_payload` | mcp/src/agents_remember/mcp/tools/core.py:105-128; mcp/src/agents_remember/mcp/tools/providers.py:55-70; mcp/src/agents_remember/mcp/tools/providers.py:90-100 |
| Budget/prune/redaction tests. | `ToolReportFileTests`; `CompactPayloadBudgetTests` | mcp/tests/test_tool_response_budgets.py:60-108; mcp/tests/test_tool_response_budgets.py:111-263 |

## Update History

- 2026-08-03T04:00:52+02:00 — 260731-EFA-L6 W3-B06 curator: curated 5 citation findings for compact response builders and their budget/redaction tests.

- 2026-06-10T05:30+02:00: Created for the S4 response token budgets (2.5.1).
