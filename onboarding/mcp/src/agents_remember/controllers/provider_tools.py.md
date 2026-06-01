# mcp/src/agents_remember/controllers/provider_tools.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/controllers/provider_tools.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-02T02:00+02:00                     |
| lastVerifiedCommitHash | `01178eb7dfc7d8d2b5d38afc4d8a12358353cdc2` |
| lastVerifiedCommitDate | 2026-06-02T01:19:03+02:00|
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

`provider_watchers_tool` no longer accepts `action="refresh"` — it raises
`ValueError` with guidance directing callers to either `restart` (stop then
start, indexes preserved) or `invalidate-indexes` (destructive full rebuild,
formerly called `refresh`). The `_provider_invalidate_indexes` function
implements the destructive path under its new name.

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
- When a worktree target is resolved, its already-persisted settings file is
  used as-is and never deleted; only workspace-scope settings files are temp
  files that the controller writes and removes.
- GrepAI `--project` must be the runtime-normalized project id
  (`stable_provider_id`), and `repo_ids` are matched case-insensitively, so a
  configured id like `Cobalt` resolves to project `cobalt` instead of returning
  an empty result.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Provider summary and diagnostics projection live in the provider status module. | [status.py](agents-remember-md/mcp/src/agents_remember/providers/status.py) |
| Provider response models distinguish compact summaries from diagnostics/native payloads. | [providers.py](agents-remember-md/mcp/src/agents_remember/models/providers.py) |
| MCP payload builders validate this controller output through the model registry. | [tools/providers.py](agents-remember-md/mcp/src/agents_remember/mcp/tools/providers.py) |
| Unit tests guard action naming (refresh rejected, invalidate-indexes dispatches) and worktree routing resolution. | [test_provider_watcher_actions.py](agents-remember-md/mcp/tests/test_provider_watcher_actions.py); [test_provider_worktree_routing.py](agents-remember-md/mcp/tests/test_provider_worktree_routing.py) |

## Update History

- 2026-06-02T02:00+02:00 — `_grepai_project_selection` now emits `--project` as `stable_provider_id(repo_id)` (matching the watcher's project naming) and resolves `repo_ids` case-insensitively via the new `_canonical_repo_ids`; fixes uppercase repo ids (e.g. `Cobalt`) returning empty grepai_search/grepai_trace results. Updated Code Commentary and Invariants.
- 2026-06-01T00:00+02:00 — `action="refresh"` removed and replaced by `restart` (no index changes) and `invalidate-indexes` (destructive rebuild); `_provider_invalidate_indexes` implements the destructive path. All CGC/GrepAI query tools gained a `worktree` parameter routed through `_resolve_worktree_target` / `_worktree_provider_targets` / `_load_worktree_grepai_provider` / `_provider_operation_result`. Updated Purpose, Code Commentary, and Invariants.
- 2026-05-31T12:30+02:00 — Dropped the provider-runner integrity invariant: `_provider_operation_result` no longer calls `check_provider_runner_integrity` / returns a `runnerIntegrityFailed` block, and repo validation now goes through the shared `require_repo` guard (1.0.0 review remediation).
- 2026-05-30T21:33+02:00: Re-verified against `825a172` after the provider dockerization / never-cap-indexing run; the controller surface (status, diagnostics, watchers, GrepAI search/trace, typed CGC tools) and its act-by-default `dry_run` behavior still match. Repaired the builder reference — provider payload builders now live in `tools/providers.py` after the `01f503d` `mcp/tools.py` split.
- 2026-05-28T19:52+02:00: Created when provider MCP behavior moved out of the former `skill_tools.py` mega-facade.
