# mcp/src/agents_remember/mcp/server.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/mcp/server.py`    |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-04T22:15+02:00                     |
| lastVerifiedCommitHash | `0eba27a75a37ebc4ce1baeb9da9d7b7a879a8974` |
| lastVerifiedCommitDate | 2026-06-04T22:38:48+02:00|
| governingOverview      | `../../../overview.md`                     |

## Purpose

`server.py` wires the stdio FastMCP server and registers the model-visible
Agents Remember tools.

## Code Commentary

### Logic

`create_server()` first calls `install_compact_content()` (idempotent) so the
JSON text mirror of every tool result is emitted without FastMCP's hardcoded
indentation, then builds the FastMCP instance and registers typed tool functions
that delegate to payload builders. The current public surface includes context,
drift, route index, memory init, skill install, provider status, provider
diagnostics, provider watcher, GrepAI, CodeGraphContext, worktree, memory
baseline/carryover, and benchmark tools.

The registered `memory_quality_check` tool accepts a repo id plus optional
check names/detail limits and forwards them to the payload/controller layer. It
is the full closeout quality gate; task-start guidance continues to use
`drift_check` for the maintenance worklist.

The public CGC provider surface is typed at registration time. The server
registers `cgc_symbol_search`, `cgc_callers`, `cgc_callees`,
`cgc_dependencies`, `cgc_complexity`, and `cgc_visualize` instead of a generic
`cgc_query` endpoint. All CGC and GrepAI query tools now accept an optional
`worktree` parameter forwarded to the payload layer, which routes to a
worktree's isolated provider stack.

The public GrepAI provider surface is typed at registration time as well.
`grepai_search` registers `repo_ids`, `all_repos`, `limit`, and
`output_format` around the required query, while `grepai_trace` registers
`trace_action`, `symbol`, optional repo scoping, optional graph depth, and
output format. The server only forwards these fields to the payload layer.

The `provider_watchers` docstring now describes `restart` (stop then start,
indexes preserved — use to wake a stale watcher) and `invalidate-indexes`
(DELETE and rebuild every index from scratch: full re-embed + full graph
re-index, slow and CPU-heavy) as distinct actions. The former `refresh` action
is no longer listed; it is rejected at the controller with guidance.

`worktree_cleanup` now accepts `teardown_providers` (default `true`), which
reclaims the worktree's isolated provider stack (containers, networks,
provider-runtime tree) before removing worktrees and branches.

`worktree_abandon` is newly registered. It discards a worktree-backed task
without integration: reclaims its isolated provider stack, removes worktrees,
deletes task branches, and removes the group dir. Without `force` it refuses
dirty worktrees and unmerged branches (reporting them); `force=true` discards
with `git worktree remove --force` / `git branch -D`.

`runtime_install` registers the reconcile flags `dry_run` (act-by-default
`False`), `include_benchmarks`, `install_provider_deps` (default `True`), and
`no_cache` (default `False`). Its operator text now distinguishes preserved user
data (`memory-repos/`, `providers/data/`) from managed scaffold, and explains
that `install_provider_deps=true` may refresh `providers/runners/` after
stopping watchers so containers rebind cleanly, then starts/rechecks watchers
without rebuilding indexes. `no_cache=true` forces a from-scratch provider image
rebuild that bypasses the skip-if-tag-exists shortcut. Registered tool functions
carry human-facing descriptions (docstrings) surfaced to the harness's tool
list.

`codex_benchmark_run` exposes an optional `codex_sandbox` argument whose
registered default is `CODEX_BENCHMARK_SANDBOX` (imported from
`agents_remember.benchmarks.runner`), which now resolves to Codex's own
`default` sandbox rather than `danger-full-access`. Callers must opt into
`danger-full-access` explicitly (trusted local runs only). The server only
forwards the value; the runner validates it against its allowlist and maps
`default` to an omitted `--sandbox` CLI argument. A real benchmark run is also
refused unless the MCP settings enable benchmarks (`benchmarksEnabled`), and
benchmark tools stay `dry_run=True` so a run is never implicit.

`provider_diagnostics` is registered as the explicit detail tool for raw
provider state, keeping `context_packet` and `provider_status` focused on
compact readiness summaries.

Registered tools follow an **act-by-default** `dry_run` contract: effectful
tools and the read-only `cgc_*`/`grepai_*` query tools register `dry_run=False`,
so a plain call does the work (queries return results; `dry_run=true` returns
the planned provider command without executing it). The two `*_closeout_apply`
tools keep `dry_run=False` paired with explicit `*_preview` tools, and the two
`codex_benchmark_*` tools are the only `dry_run=True` defaults — a real
benchmark run clones repos and executes Codex agents, so it stays preview-first.

### Invariants And Boundaries

- Server functions should perform registration and argument forwarding only.
- Tool behavior and safety checks belong in payload builders/controllers.
- `install_compact_content()` must run before tools are exercised; keep the call
  at the top of `create_server()`. It only affects text-mirror serialization, not
  `structuredContent` or tool behavior.
- Do not add a raw shell or arbitrary command tool to this server.
- Do not collapse GrepAI back into free-form query/native argument forwarding;
  the registration should mirror the supported MCP contract.
- Do not turn benchmark sandbox selection into a generic Codex argument surface.
- Keep detailed provider troubleshooting behind `provider_diagnostics`; do not
  hide raw provider internals in `context_packet`.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Payload builders are defined in the `mcp/tools/` package (split by domain behind a facade `__init__.py`). | [tools/](agents-remember-md/mcp/src/agents_remember/mcp/tools) |
| Provider diagnostics payloads are modeled separately from compact provider summaries. | [providers.py](agents-remember-md/mcp/src/agents_remember/models/providers.py) |
| The config loader rejects coordinator `system/settings.json` as MCP authority. | [config.py](agents-remember-md/mcp/src/agents_remember/mcp/config.py) |
| The compact-content shim installed at server creation minifies tool-result text. | [compact_content.py](agents-remember-md/mcp/src/agents_remember/mcp/compact_content.py) |
| The `runtime_install` tool docstring names preserved user data, managed provider scaffold replacement, watcher rebind behavior, and non-index-rebuilding post-install watcher checks. | [server.py](agents-remember-md/mcp/src/agents_remember/mcp/server.py) |

## Update History

- 2026-06-04T22:15+02:00: Updated `runtime_install` operator text to clarify provider runner refresh during `install_provider_deps=true`, watcher rebind/recheck behavior, and index preservation.
- 2026-06-02T04:40+02:00: `skills_install` tool dropped the `layout` parameter after the installer became a single flat copy (U-01-core-skills dissolved). `l-01-session-job-lifecycle` skill series, Sub-task B/S7, mcp 1.1.0.
- 2026-06-02T04:25+02:00: `worktree_start` docstring dropped the retired `heavy-task` workflow_kind (now `light-task`/`chat-task`) after the heavy workflow was retired. `l-01-session-job-lifecycle` skill series, Sub-task B/S6, mcp 1.1.0.
- 2026-06-01T00:00+02:00 — `provider_watchers` docstring updated to name `restart` (index-preserving) and `invalidate-indexes` (destructive rebuild) as distinct actions, replacing `refresh`. All CGC/GrepAI query tools gained `worktree` parameter. `worktree_cleanup` gained `teardown_providers`. `worktree_abandon` newly registered with `force`. Updated Code Commentary Logic section.
- 2026-05-31T12:30+02:00 — Resolved the hardening follow-up: `codex_sandbox`'s registered default is now `CODEX_BENCHMARK_SANDBOX` (Codex's own `default` sandbox, not `danger-full-access`), callers must opt into full access explicitly, and a real run is refused unless MCP settings set `benchmarksEnabled` (1.0.0 review remediation).
- 2026-05-30T21:33+02:00: Documented the 0.9.x registration changes — `runtime_install`'s `no_cache` flag (from-scratch image rebuild) alongside `install_provider_deps`, the human-facing tool descriptions now surfaced to the harness, and the literal `codex_sandbox="danger-full-access"` registered default (noted as a hardening follow-up). Verified against `8927f03`.
- 2026-05-29T20:20+02:00: Recorded the act-by-default `dry_run` contract (effectful + `cgc_*`/`grepai_*` query tools register `dry_run=False`; only `codex_benchmark_*` keeps `dry_run=True`) and refreshed the stale payload-builder reference to the `mcp/tools/` package.
- 2026-05-29T08:53+02:00: Updated after `create_server()` began installing the FastMCP compact-content shim to minify tool-result text mirrors.
- 2026-05-28T19:52+02:00: Updated after registering the dedicated `provider_diagnostics` MCP tool.
- 2026-05-26T23:11+02:00: Refreshed verification metadata after source commit `5ab704a` landed typed GrepAI search and trace registration.
- 2026-05-26T22:54+02:00: Updated after GrepAI search and trace registration gained typed scope, output, and trace-action arguments.
- 2026-05-24T10:06+02:00: Refreshed verification metadata after source commit `f48a346` exposed benchmark sandbox options through the MCP server.
- 2026-05-24T08:56+02:00: Updated after `codex_benchmark_run` registered the optional `codex_sandbox` forwarding argument.
- 2026-05-24T02:47+02:00: Updated after registering `memory_quality_check` as the closeout quality gate.
- 2026-05-23T20:42+02:00: Updated CGC registration from generic `cgc_query` to typed CGC tools.
- 2026-05-23T13:09+02:00: Updated for the complete Phase 04 public MCP tool surface.
