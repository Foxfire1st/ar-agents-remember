# mcp/src/agents_remember/mcp/tool_reports.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/mcp/tool_reports.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-10T05:30+02:00                     |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`|
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `../../../overview.md`                              |

## Purpose

`tool_reports.py` writes bulk tool diagnostics to temp report files so verbose
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

| Finding | Source Path |
| --- | --- |
| Compact builders that pair with the reports. | [core.py](agents-remember/mcp/src/agents_remember/mcp/tools/core.py); [providers.py](agents-remember/mcp/src/agents_remember/mcp/tools/providers.py) |
| Budget/prune/redaction tests. | [test_tool_response_budgets.py](agents-remember/mcp/tests/test_tool_response_budgets.py) |

## Update History

- 2026-06-10T05:30+02:00: Created for the S4 response token budgets (2.5.1).
