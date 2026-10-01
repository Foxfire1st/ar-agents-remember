# mcp/src/agents_remember/mcp/registration/code_search.py

## Governing Overview

[registration route overview](overview.md)

## 260731-EFA-L8 Change

The tool-registration functions gained bare-`*` keyword-only signatures (the 19
PLR0917 fixes across `mcp/registration/*.py`); the rule stays enabled and call sites
already pass keywords. Registered tools are unchanged.

## Purpose

`register_code_search_tools(server, config)` declares the provider-backed search surface: the two
GrepAI semantic tools (`grepai_search`, `grepai_trace`) and the six CodeGraphContext graph tools
(`cgc_symbol_search`, `cgc_callers`, `cgc_callees`, `cgc_dependencies`, `cgc_complexity`,
`cgc_visualize`).

## Code Commentary

### Logic

Every declaration ends with the same three execution arguments — `dry_run`, `timeout`, `worktree` —
and packs them into one `ProviderQueryScope`. `worktree` targets a worktree's isolated provider
stack by name; omitting it defaults to a single active worktree for the repo, otherwise the
workspace stack. `dry_run=true` returns the planned provider command without running it, which is
why these read-only tools still carry a dry-run flag.

The two GrepAI tools additionally split their inputs in two: the query itself
(`GrepaiSearchQuery(query, limit, output_format)` / `GrepaiTraceQuery(trace_action, symbol, depth,
output_format)`) and the repo scope (`GrepaiRepoScope(repo_ids, all_repos)`, `all_repos=True` by
default). `trace_action` is `callers` | `callees` | `graph`, and `depth` applies only to `graph`.
`output_format` is `json` or `toon`.

The CGC tools pass their domain arguments positionally (`repo_id` plus name/function/module) and
keep only the scope packed. `cgc_callers` takes an optional `file` to disambiguate same-named
functions; `cgc_complexity`'s `function` is optional and omitting it reports the whole repo;
`cgc_visualize` serves a browser view on `port` (default 8000).

The typed surface is deliberate: this route registers eight named tools instead of one generic
`cgc_query`/free-form GrepAI endpoint, so the published schema mirrors the supported provider
contract rather than forwarding native arguments.

### Invariants And Boundaries

- Do not collapse these back into a generic query endpoint or free-form native-argument forwarding.
- All eight are read-only apart from `cgc_visualize` serving a port; each needs its provider enabled,
  running and indexed, and says so in its docstring.
- Query construction, provider dispatch, and the dry-run command rendering live in
  `application/provider_tools.py`.

## Evidence

### Repo-Internal References

- The payload builders these forward to. [1]
- `ProviderQueryScope`, `GrepaiRepoScope`, `GrepaiSearchQuery`, `GrepaiTraceQuery`. [2]
