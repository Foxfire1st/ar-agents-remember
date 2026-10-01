# mcp/src/agents_remember/application/provider_tools.py

## Governing Overview

[overview.md](overview.md)

## Purpose

`provider_tools.py` is the application entry point surface for provider status,
diagnostics, watcher lifecycle, GrepAI search/trace, and CodeGraphContext MCP
tools.

## Code Commentary

### Query Parameter Objects (260731-EFA-L2)

The query tools' shared execution knobs are one frozen `ProviderQueryScope(worktree, dry_run,
timeout)` — `WORKSPACE_QUERY_SCOPE` is the shared default (workspace stack, real run, provider
default timeout). GrepAI additionally splits its inputs into the query itself
(`GrepaiSearchQuery(query, limit, output_format)` / `GrepaiTraceQuery(trace_action, symbol, depth,
output_format)`) and the repo scope (`GrepaiRepoScope(repo_ids, all_repos)`, default
`ALL_INDEXED_REPOS`). The CGC tools keep `repo_id` plus their one domain argument positional and
take `scope=` for the rest.

Two internal seams were named at the same time: `ProviderOperation` (the operation name plus its
native argument vector, built by `_grepai_operation`) and `_grepai_target` / `_canonical_repo_ids`,
which carry the worktree-target and repo-id normalization that used to be inline. `GrepaiProjectSelection`
and `WorktreeProviderTarget` are unchanged.

Status and diagnostics delegate to `providers.status`. Watcher actions route
through provider lifecycle services and write current provider state when a
real status/refresh result is produced. GrepAI helpers validate configured repo
scope, workspace/project selection, output format, trace action, and numeric
limits before calling `lifecycle_service.run_grepai_lifecycle()`. CGC helpers
construct fixed native argument vectors for typed code-relationship operations
before calling `lifecycle_service.run_cgc_lifecycle()`.
The `cgc_dependencies` wrapper maps to CodeGraphContext's current native
dependency analyzer subcommand, `analyze deps <module>`.

`provider_watchers_tool` no longer accepts `action="refresh"` — it raises
`ValueError` with guidance directing callers to either `restart` (stop then
start, indexes preserved) or `invalidate-indexes` (destructive full rebuild,
formerly called `refresh`). The `_provider_invalidate_indexes` function
implements the destructive path under its new name.

Launch-capable operations are gated on the live on-disk authority (containment
R1, 260707-HFX-L1). `provider_watchers_tool` calls
`require_provider_launch_authority` for `start`, `restart`, and
`invalidate-indexes` (rebuilding launches indexers): a disk-disabled or
unreadable authority file refuses with `ConfigError`, an armed one swaps the
LIVE providers map into the config the action runs on. `stop`, `status`, and
`shutdown-all` are never gated — stopping is always legal. The GrepAI/CGC
query tools (`grepai_search`, `grepai_trace`, `cgc_visualize`, and every typed
wrapper through `_cgc_run_tool`) pass `launch_capable=True` into
`_provider_operation_result`, because a query spins a one-shot runner
container and a worktree's persisted settings file is stamped `enabled: true`
forever — neither is launch authority. Each funnel also names its
`launch_capable_provider` — the GrepAI funnels pass `grepai-memory`, the CGC
funnels (`cgc_visualize` and `_cgc_run_tool`) pass `codegraphcontext-code` —
and the gate refuses with `ConfigError` when that SPECIFIC provider is missing
from the live map (review follow-up): an armed grepai authority no longer
authorizes a cgc one-shot runner. The gate always runs for
launch-capable operations; when a worktree `settings_path_override` resolved,
the worktree's own stack settings still drive the run (the live map replaces
the config only on the temp-settings path), but only under an armed authority.

All CGC and GrepAI query tools accept an optional `worktree` inside their
`ProviderQueryScope`. When a
`worktree` name is given (or a single stack is discoverable for the repo),
`_resolve_worktree_target` locates the worktree's persisted lifecycle-settings
file and `_provider_operation_result` uses it directly without writing or
deleting a temp settings file (`owns_settings=False`). The resolved result
carries `worktreeScoped=True`. `_worktree_provider_targets` discovers stacks
by scanning `worktrees/<repo>/<group>/provider-runtime/provider-state.json`
files.

For GrepAI tools, the worktree's `grepai-memory` provider settings (loaded by
`_load_worktree_grepai_provider`) are passed to `_grepai_project_selection` as
`provider_settings`, overriding the workspace-scope settings from config.

`_grepai_project_selection` resolves user-supplied `repo_ids` to their configured
spelling case-insensitively (`_canonical_repo_ids`) and emits each `--project` as
the runtime-normalized id `stable_provider_id(repo_id)`, matching how the watcher
names projects. A configured repo id like `Cobalt` is therefore queried as project
`cobalt`; without this the raw id was passed verbatim and matched no project.

## Invariants And Boundaries

- Provider callers may name configured repo IDs and typed options, not
  arbitrary provider roots or generic native command strings.
- `provider_diagnostics` is the detail tool for raw provider state; normal
  context-facing provider status stays compact.
- `provider_watchers_tool` and the `cgc_*`/`grepai_*` query application entry points default
  `dry_run=False` (act-by-default): a plain query returns results and
  `dry_run=true` returns the planned provider command without executing it.
  `provider_watchers` still forces a live path for `action="status"`.
- `action="refresh"` is permanently rejected with guidance; the destructive
  rebuild path is now `action="invalidate-indexes"` and the non-destructive
  restart path is `action="restart"`.
- `start`/`restart`/`invalidate-indexes` and every launch-capable query tool
  re-read the on-disk authority fail-closed (containment R1); `stop`,
  `status`, and `shutdown-all` must stay ungated so teardown and observation
  are always legal.
- A launch-capable query is gated on its SPECIFIC provider
  (`launch_capable_provider`), not on any-provider-armed: an authority that
  enables only `grepai-memory` must not authorize a `codegraphcontext-code`
  one-shot runner.
- A worktree `settings_path_override` is honored only under an armed live
  authority; it never bypasses the launch gate, because the persisted worktree
  settings file always says `enabled: true`.
- When a worktree target is resolved, its already-persisted settings file is
  used as-is and never deleted; only workspace-scope settings files are temp
  files that the application entry point writes and removes.
- GrepAI `--project` must be the runtime-normalized project id
  (`stable_provider_id`), and `repo_ids` are matched case-insensitively, so a
  configured id like `Cobalt` resolves to project `cobalt` instead of returning
  an empty result.
- `cgc_dependencies` must keep using the native `analyze deps <module>` command
  shape; provider readiness does not prove this typed wrapper is correct.

## Evidence

### Repo-Internal References

- Provider summary and diagnostics projection live in the provider status module. [1]
- Provider response models distinguish compact summaries from diagnostics/native payloads. [2]
- Provider status and diagnostics payload builders produce the application-facing model inputs. [3]
- The base tool payload delegates the builder output to completion without normalizing it itself. [4]
- Complete tool responses validate the normalized payload. [5]
- Finalization converts the completed response into the model-facing result. [6]
- The registry selects the response model for each provider tool. [7]
- Watcher actions reject ambiguous refresh, retain stop/status, and require live launch authority for start/restart/invalidation. [8]
- The launch-authority configuration exposes reload and requirement gates. [9]
- The watcher application entry point calls the launch gate. [10]
- The query application entry point delegates to `_provider_operation_result`, whose required-provider path invokes the launch authority before the provider operation. [11]

## 260918-TSIP-L6 One Declared Refusal Per Provider Tool

Eight provider tools answered an ordinary absent capability with a bare exception, so the caller
lost `ok`, `status` and the way out — `grepai_search`, `grepai_trace` and the six `cgc_*` tools
(`T34`). Each now declares its refusal exactly once, in `_PROVIDER_REFUSAL_SITES` (`:109-195`)
keyed by operation, and the declaration has two halves because the family has two shapes:
`provider_refusal_payload` (`:196-220`) builds the envelope a tool can **return**, and
`provider_refusal_result` (`:221-239`) turns the error an owner **raises** into the same envelope,
returning `None` for an error that is not this condition so an unrelated failure still surfaces.

The two guards are what make it one place rather than eight: `resolve_grepai_query` (`:240-274`)
and `resolve_cgc_capability` (`:275-294`) are called first by their families, so "the provider is
not configured or not armed on this host" is answered identically for every member and names
`provider_watchers` as the way out. This is the constructive shape `provider_status_tool` (`:35-42`)
and `provider_diagnostics_tool` (`:43-50`) already used — their `state: "noProviders"` answer is
what the nine were brought up to, not a tolerated exception. Two argument-validation raises
(`:493`, `:538`) deliberately still raise: a malformed argument is not a condition the product
declares, and the entry point's own input model refuses it.
