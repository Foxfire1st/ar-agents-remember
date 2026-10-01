# mcp/src/agents_remember/mcp/tools/providers.py

## Governing Overview

[overview.md](overview.md)

## Purpose

Provider status/diagnostics and CGC/GrepAI query payload builders.

## Code Commentary

### Logic

Holds `provider_status_payload`, `provider_diagnostics_payload`,
`provider_watchers_payload`, `grepai_search_payload`, `grepai_trace_payload`,
and the CGC query builders (`cgc_symbol_search`, `cgc_callers`, `cgc_callees`,
`cgc_dependencies`, `cgc_complexity`, `cgc_visualize`). Each forwards typed
arguments to the matching `application.provider_tools` function and returns
through `base._tool_payload`.

`provider_diagnostics_payload` and `provider_watchers_payload` are
response-budgeted (S4, 2.5.1): each writes its full application entry point payload to a
temp report via `write_tool_report` (`mcp/tool_reports.py`, keep-5/7-day
retention, secrets redacted) and returns a compact builder result with
`reportPath` inline. `compact_diagnostics_payload` drops `rawStatus`, the
`currentState` body (a verbatim copy of the on-disk current.json that
`currentStateFile` already points at), and `items[].rawStatus`.
`compact_watchers_payload` keeps per-step/per-provider outcome dicts
(`provider`, `action`, `ok`, ...) and drops the raw provider payloads; the
watchers report is written **before** `summarize_command_logs` mutates the
payload, so the report keeps full logs while the inline response stays lean.

All CGC and GrepAI query builders route their execution knobs through one
`ProviderQueryScope(worktree, dry_run, timeout)` (260731-EFA-L2; `WORKSPACE_QUERY_SCOPE` is the
shared default). `worktree` still targets a worktree's isolated stack by name. The GrepAI pair
additionally take `GrepaiSearchQuery` / `GrepaiTraceQuery` (the query, limit/depth, output format)
and `repos: GrepaiRepoScope(repo_ids, all_repos)` (`ALL_INDEXED_REPOS` by default), while the CGC
builders keep `repo_id` plus their one domain argument positional. Query result payloads are not
compacted — the search/analysis results are the point of the call.

The published MCP signatures stay flat; `mcp/registration/code_search.py` builds these objects.

### Invariants And Boundaries

- Transport-thin: provider lifecycle and query behavior lives in
  `application.provider_tools` and the provider packages.
- Compaction lives in this MCP tool layer only: internal consumers
  (current-state writer, application entry points) keep the full data; only the wire
  payload slims down.
- `provider_watchers_payload` and the `cgc_*`/`grepai_*` query builders default
  `dry_run=False` (act-by-default): a plain query returns results, and
  `dry_run=true` returns the planned provider command without executing it.
