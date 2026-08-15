# mcp/src/agents_remember/application/provider_tools.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/application/provider_tools.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-02T01:05+02:00                     |
| lastVerifiedCommitHash | `17987fa66a642306eb8d20fa9a4bff2b881550d2` |
| lastVerifiedCommitDate | 2026-08-15T14:36:30+02:00|
| governingOverview      | `overview.md`                              |

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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Provider summary and diagnostics projection live in the provider status module. | `provider_status_packet`; `provider_diagnostics_packet` | mcp/src/agents_remember/providers/status.py:53-87; mcp/src/agents_remember/providers/status.py:105-127 |
| Provider response models distinguish compact summaries from diagnostics/native payloads. | `ProviderSummary`; `ProviderStatusResponse`; `ProviderDiagnosticsResponse`; `ProviderNativeToolResponse` | mcp/src/agents_remember/models/providers.py:75-93; mcp/src/agents_remember/models/providers.py:96-119; mcp/src/agents_remember/models/providers.py:138-158; mcp/src/agents_remember/models/providers.py:182-188 |
| Provider status and diagnostics payload builders produce the application-facing model inputs. | `provider_status_payload`; `provider_diagnostics_payload` | mcp/src/agents_remember/mcp/tools/providers.py:33-37; mcp/src/agents_remember/mcp/tools/providers.py:40-52 |
| The base tool payload delegates the builder output to completion without normalizing it itself. | `_tool_payload` | mcp/src/agents_remember/mcp/tools/base.py:73-75 |
| Complete tool responses validate the normalized payload. | `complete_tool_response` | mcp/src/agents_remember/application/tool_response.py:47-61 |
| Finalization converts the completed response into the model-facing result. | `finalize_tool_response` | mcp/src/agents_remember/models/tool_response.py:15-26 |
| The registry selects the response model for each provider tool. | `TOOL_RESPONSE_MODELS` | mcp/src/agents_remember/models/tool_registry.py:116-179 |
| Unit tests guard action naming (refresh rejected), the disk-disabled invalidate-indexes refusal, the always-legal stop, and worktree routing resolution. | `WatcherActionNamingTests`; `WorktreeTargetResolutionTests` | mcp/tests/test_provider_watcher_actions.py:43-77; mcp/tests/test_provider_worktree_routing.py:66-125 |
| The launch-authority configuration exposes reload and requirement gates. | `ProviderAuthority`; `reload_provider_authority`; `require_provider_launch_authority` | mcp/src/agents_remember/kernel/primitives/runtime_config.py:151-171; mcp/src/agents_remember/kernel/primitives/runtime_config.py:174-199; mcp/src/agents_remember/kernel/primitives/runtime_config.py:202-221 |
| The watcher application entry point calls the launch gate. | `provider_watchers_tool` | mcp/src/agents_remember/application/provider_tools.py:48-87 |
| The query application entry point delegates to `_provider_operation_result`, whose required-provider path invokes the launch authority before the provider operation. | `grepai_search_tool`; `_provider_operation_result` | mcp/src/agents_remember/application/provider_tools.py:273-303; mcp/src/agents_remember/application/provider_tools.py:736-783 |
| Containment tests pin the launch gate's refusal and armed-path semantics. | `ReloadProviderAuthorityTests`; `QueryFunnelGateTests` | mcp/tests/test_provider_containment.py:78-121; mcp/tests/test_provider_containment.py:180-196 |

## Update History

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-04T15:32:44+02:00 — 260731-EFA-L6 S18-B08 curator: rebound direct payload delegation and the query helper's required-provider launch path to their operative extents, preserving owner splits.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — 260731-EFA-L6 curator: source moved. `mcp/src/agents_remember/controllers/` was renamed to `application/`, so this sidecar moved with its source; path metadata and every in-body path follow, and the prose adopts "the application layer" / "an application entry point" for what it used to call a controller. Behavior is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-31T15:31+02:00 — 260731-EFA-L2: introduced `ProviderQueryScope` (+ `WORKSPACE_QUERY_SCOPE`),
  `GrepaiRepoScope` (+ `ALL_INDEXED_REPOS`), `GrepaiSearchQuery`, `GrepaiTraceQuery` and the internal
  `ProviderOperation` / `_grepai_target` / `_grepai_operation` / `_canonical_repo_ids` seams; every
  query tool's keyword list moved onto them. The launch-authority gate, worktree scoping, refusal
  behaviour and native argument vectors are unchanged. Verification metadata pinned until closeout
  stamps the L2 code commit.
- 2026-07-07T17:40+02:00 — 260707-HFX-L1 review fix: `_provider_operation_result` gained
  `launch_capable_provider` — the SPECIFIC provider must be armed in the live map (GrepAI
  funnels pass `grepai-memory`, CGC funnels pass `codegraphcontext-code`; missing ⇒
  `ConfigError` before the runner is invoked), so an armed grepai no longer authorizes a cgc
  one-shot. Verification metadata pinned until closeout stamps the HFX-L1 commit.
- 2026-07-07T16:30+02:00 — 260707-HFX-L1 (provider containment R1): `provider_watchers_tool`
  gates `start`/`restart`/`invalidate-indexes` through `require_provider_launch_authority`
  (disk-disabled ⇒ `ConfigError`; armed ⇒ the action runs on the live map) while
  `stop`/`status`/`shutdown-all` stay legal; `_provider_operation_result` gained
  `launch_capable` and `grepai_search`/`grepai_trace`/`cgc_visualize`/`_cgc_run_tool` pass
  `True`, so one-shot runner containers are gated too; a worktree `settings_path_override` is
  honored only under an armed live authority. Updated Code Commentary and Invariants.
  Verification metadata pinned until closeout stamps the HFX-L1 commit.
- 2026-07-02T15:40+02:00 — `cgc_dependencies_tool` now emits CodeGraphContext's
  current `analyze deps <module>` command instead of the stale
  `analyze dependencies <module>` spelling. Updated Code Commentary and
  Invariants.
- 2026-06-02T02:00+02:00 — `_grepai_project_selection` now emits `--project` as `stable_provider_id(repo_id)` (matching the watcher's project naming) and resolves `repo_ids` case-insensitively via the new `_canonical_repo_ids`; fixes uppercase repo ids (e.g. `Cobalt`) returning empty grepai_search/grepai_trace results. Updated Code Commentary and Invariants.
- 2026-06-01T00:00+02:00 — `action="refresh"` removed and replaced by `restart` (no index changes) and `invalidate-indexes` (destructive rebuild); `_provider_invalidate_indexes` implements the destructive path. All CGC/GrepAI query tools gained a `worktree` parameter routed through `_resolve_worktree_target` / `_worktree_provider_targets` / `_load_worktree_grepai_provider` / `_provider_operation_result`. Updated Purpose, Code Commentary, and Invariants.
- 2026-05-31T12:30+02:00 — Dropped the provider-runner integrity invariant: `_provider_operation_result` no longer calls `check_provider_runner_integrity` / returns a `runnerIntegrityFailed` block, and repo validation now goes through the shared `require_repo` guard (1.0.0 review remediation).
- 2026-05-30T21:33+02:00: Re-verified against `825a172` after the provider dockerization / never-cap-indexing run; the controller surface (status, diagnostics, watchers, GrepAI search/trace, typed CGC tools) and its act-by-default `dry_run` behavior still match. Repaired the builder reference — provider payload builders now live in `tools/providers.py` after the `01f503d` `mcp/tools.py` split.
- 2026-05-28T19:52+02:00: Created when provider MCP behavior moved out of the former `skill_tools.py` mega-facade.
