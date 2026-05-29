# mcp/src/agents_remember/mcp/tools/providers.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember-md                               |
| path                   | `mcp/src/agents_remember/mcp/tools/providers.py` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-05-29T18:35+02:00|
| lastVerifiedCommitHash | `23f4d7681f7fcd729049c5f27878c84bbb8f8e58`                                        |
| lastVerifiedCommitDate | 2026-05-29T20:24:00+02:00|
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

### Invariants And Boundaries

- Transport-thin: provider lifecycle and query behavior lives in
  `controllers.provider_tools` and the provider packages.
- `provider_watchers_payload` and the `cgc_*`/`grepai_*` query builders default
  `dry_run=False` (act-by-default): a plain query returns results, and
  `dry_run=true` returns the planned provider command without executing it.

## Update History

- 2026-05-29T20:20+02:00: Recorded the act-by-default `dry_run` default on the provider/query payload builders.
- 2026-05-29T18:35+02:00: Created from the `mcp/tools.py` domain split (commit `01f503d`).
