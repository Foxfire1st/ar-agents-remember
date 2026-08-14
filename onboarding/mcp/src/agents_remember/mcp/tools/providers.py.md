# mcp/src/agents_remember/mcp/tools/providers.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                               |
| path                   | `mcp/src/agents_remember/mcp/tools/providers.py` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-02T01:05+02:00     |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`                                        |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `overview.md`                                    |

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

## Update History

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-31T15:31+02:00 — 260731-EFA-L2: the eight query builders took `scope: ProviderQueryScope`
  in place of the separate `worktree`/`dry_run`/`timeout` keywords, and the GrepAI pair took
  `GrepaiSearchQuery`/`GrepaiTraceQuery` plus `repos: GrepaiRepoScope`. The three provider-control
  builders and all compaction are unchanged. Verification metadata pinned until closeout stamps the
  L2 code commit.
- 2026-06-10T05:30+02:00 — `provider_diagnostics_payload` and `provider_watchers_payload` file their full payloads via `write_tool_report` and return compact builders (`compact_diagnostics_payload` drops rawStatus/currentState bodies; `compact_watchers_payload` keeps per-provider outcomes only) with `reportPath` inline. Compaction lives in this MCP tool layer only — internal consumers keep full data.
- 2026-06-01T00:00+02:00 — `provider_watchers_payload` now applies `summarize_command_logs`; all CGC/GrepAI builders gained a `worktree` parameter forwarded to the controller.
- 2026-05-29T20:20+02:00: Recorded the act-by-default `dry_run` default on the provider/query payload builders.
- 2026-05-29T18:35+02:00: Created from the `mcp/tools.py` domain split (commit `01f503d`).
