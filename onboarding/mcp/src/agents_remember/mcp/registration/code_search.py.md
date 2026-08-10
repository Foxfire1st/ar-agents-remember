# mcp/src/agents_remember/mcp/registration/code_search.py

| Field                  | Value                                                          |
| ---------------------- | -------------------------------------------------------------- |
| repository             | agents-remember                                                 |
| path                   | `mcp/src/agents_remember/mcp/registration/code_search.py`       |
| doc_type               | `file-level-onboarding`                                         |
| lastUpdated            | 2026-08-02T01:05+02:00                                          |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb`                      |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
| governingOverview      | `overview.md`                                                   |

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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The payload builders these forward to. | `grepai_search_payload`; `cgc_symbol_search_payload` | mcp/src/agents_remember/mcp/tools/providers.py:129-139; mcp/src/agents_remember/mcp/tools/providers.py:155-165 |
| `ProviderQueryScope`, `GrepaiRepoScope`, `GrepaiSearchQuery`, `GrepaiTraceQuery`. | "class ProviderQueryScope:"; "class GrepaiRepoScope:"; "class GrepaiSearchQuery:"; "class GrepaiTraceQuery:" | mcp/src/agents_remember/application/provider_tools.py:108-108; mcp/src/agents_remember/application/provider_tools.py:123-123; mcp/src/agents_remember/application/provider_tools.py:142-142; mcp/src/agents_remember/application/provider_tools.py:151-151 |
| Query/scope splitting proved through a live server. | `RegistrationWiringTests` | mcp/tests/test_mcp_registration_wiring.py:61-116 |

## Update History
- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: recorded the bare-`*` keyword-only signature remediation (PLR0917). Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-02T17:36:56+02:00 — 260731-EFA-L6 curator W1-B09: repaired 6 citation finding(s); scoped recheck clean.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-31T15:31+02:00 — 260731-EFA-L2 curator: created with the package. The eight search
  declarations moved out of `server.py`; each now packs `dry_run`/`timeout`/`worktree` into
  `ProviderQueryScope` and the GrepAI pair splits query from repo scope. Verification metadata pinned
  to the pre-change commit until closeout stamps the L2 code commit.
