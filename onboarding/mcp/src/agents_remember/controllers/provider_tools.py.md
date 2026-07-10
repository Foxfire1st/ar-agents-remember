# mcp/src/agents_remember/controllers/provider_tools.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/controllers/provider_tools.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-07T17:40+02:00                     |
| lastVerifiedCommitHash | `0d5ce6784930aa4e9006ab4bbf2b788a3296abce` |
| lastVerifiedCommitDate | 2026-07-10T22:30:19+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`provider_tools.py` is the controller surface for provider status,
diagnostics, watcher lifecycle, GrepAI search/trace, and CodeGraphContext MCP
tools.

## Code Commentary

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

All CGC and GrepAI query tools accept an optional `worktree` parameter. When a
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
- `provider_watchers_tool` and the `cgc_*`/`grepai_*` query controllers default
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
  files that the controller writes and removes.
- GrepAI `--project` must be the runtime-normalized project id
  (`stable_provider_id`), and `repo_ids` are matched case-insensitively, so a
  configured id like `Cobalt` resolves to project `cobalt` instead of returning
  an empty result.
- `cgc_dependencies` must keep using the native `analyze deps <module>` command
  shape; provider readiness does not prove this typed wrapper is correct.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Provider summary and diagnostics projection live in the provider status module. | [status.py](agents-remember/mcp/src/agents_remember/providers/status.py) |
| Provider response models distinguish compact summaries from diagnostics/native payloads. | [providers.py](agents-remember/mcp/src/agents_remember/models/providers.py) |
| MCP payload builders validate this controller output through the model registry. | [tools/providers.py](agents-remember/mcp/src/agents_remember/mcp/tools/providers.py) |
| Unit tests guard action naming (refresh rejected), the disk-disabled invalidate-indexes refusal, the always-legal stop, and worktree routing resolution. | [test_provider_watcher_actions.py](agents-remember/mcp/tests/test_provider_watcher_actions.py); [test_provider_worktree_routing.py](agents-remember/mcp/tests/test_provider_worktree_routing.py) |
| The launch-authority reload/gate the watcher and query controllers call (containment R1). | [config.py](agents-remember/mcp/src/agents_remember/mcp/config.py) |
| Containment tests pin the launch gate's refusal and armed-path semantics. | [test_provider_containment.py](agents-remember/mcp/tests/test_provider_containment.py) |

## Update History

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
