# mcp/src/agents_remember/mcp/tools/providers.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember-md                               |
| path                   | `mcp/src/agents_remember/mcp/tools/providers.py` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-01T00:00+02:00|
| lastVerifiedCommitHash | `4117c3d98eadb4265af6e55f3dd8f2552e8589a0`                                        |
| lastVerifiedCommitDate | 2026-06-01T20:31:44+02:00|
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

`provider_watchers_payload` now wraps its controller result with
`summarize_command_logs` (imported from
`providers.lifecycle.log_capture`) before returning, trimming large stdout/stderr
from watcher lifecycle responses.

All CGC and GrepAI query builder functions now accept and forward an optional
`worktree` parameter to the controller layer.

### Invariants And Boundaries

- Transport-thin: provider lifecycle and query behavior lives in
  `controllers.provider_tools` and the provider packages.
- `provider_watchers_payload` and the `cgc_*`/`grepai_*` query builders default
  `dry_run=False` (act-by-default): a plain query returns results, and
  `dry_run=true` returns the planned provider command without executing it.

## Update History

- 2026-06-01T00:00+02:00 — `provider_watchers_payload` now applies `summarize_command_logs`; all CGC/GrepAI builders gained a `worktree` parameter forwarded to the controller.
- 2026-05-29T20:20+02:00: Recorded the act-by-default `dry_run` default on the provider/query payload builders.
- 2026-05-29T18:35+02:00: Created from the `mcp/tools.py` domain split (commit `01f503d`).
