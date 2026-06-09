# mcp/src/agents_remember/mcp/tools/providers.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember-md                               |
| path                   | `mcp/src/agents_remember/mcp/tools/providers.py` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-10T05:30+02:00     |
| lastVerifiedCommitHash | `592274a52cec61d97521771c630272c72240ed01`                                        |
| lastVerifiedCommitDate | 2026-06-10T01:38:42+02:00|
| governingOverview      | `overview.md`                                    |

## Purpose

Provider status/diagnostics and CGC/GrepAI query payload builders.

## Code Commentary

### Logic

Holds `provider_status_payload`, `provider_diagnostics_payload`,
`provider_watchers_payload`, `grepai_search_payload`, `grepai_trace_payload`,
and the CGC query builders (`cgc_symbol_search`, `cgc_callers`, `cgc_callees`,
`cgc_dependencies`, `cgc_complexity`, `cgc_visualize`). Each forwards typed
arguments to the matching `controllers.provider_tools` function and returns
through `base._tool_payload`.

`provider_diagnostics_payload` and `provider_watchers_payload` are
response-budgeted (S4, 2.5.1): each writes its full controller payload to a
temp report via `write_tool_report` (`mcp/tool_reports.py`, keep-5/7-day
retention, secrets redacted) and returns a compact builder result with
`reportPath` inline. `compact_diagnostics_payload` drops `rawStatus`, the
`currentState` body (a verbatim copy of the on-disk current.json that
`currentStateFile` already points at), and `items[].rawStatus`.
`compact_watchers_payload` keeps per-step/per-provider outcome dicts
(`provider`, `action`, `ok`, ...) and drops the raw provider payloads; the
watchers report is written **before** `summarize_command_logs` mutates the
payload, so the report keeps full logs while the inline response stays lean.

All CGC and GrepAI query builder functions accept and forward an optional
`worktree` parameter to the controller layer; their result payloads are not
compacted because the search/analysis results are the point of the call.

### Invariants And Boundaries

- Transport-thin: provider lifecycle and query behavior lives in
  `controllers.provider_tools` and the provider packages.
- Compaction lives in this MCP tool layer only: internal consumers
  (current-state writer, controllers) keep the full data; only the wire
  payload slims down.
- `provider_watchers_payload` and the `cgc_*`/`grepai_*` query builders default
  `dry_run=False` (act-by-default): a plain query returns results, and
  `dry_run=true` returns the planned provider command without executing it.

## Update History

- 2026-06-10T05:30+02:00 — `provider_diagnostics_payload` and `provider_watchers_payload` file their full payloads via `write_tool_report` and return compact builders (`compact_diagnostics_payload` drops rawStatus/currentState bodies; `compact_watchers_payload` keeps per-provider outcomes only) with `reportPath` inline. Compaction lives in this MCP tool layer only — internal consumers keep full data.
- 2026-06-01T00:00+02:00 — `provider_watchers_payload` now applies `summarize_command_logs`; all CGC/GrepAI builders gained a `worktree` parameter forwarded to the controller.
- 2026-05-29T20:20+02:00: Recorded the act-by-default `dry_run` default on the provider/query payload builders.
- 2026-05-29T18:35+02:00: Created from the `mcp/tools.py` domain split (commit `01f503d`).
