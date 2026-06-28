# mcp/src/agents_remember/controllers/worktree_tools.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/controllers/worktree_tools.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-23T22:50+02:00     |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1` |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`worktree_tools.py` is the controller surface for worktree start, attach,
status, closeout preview/apply, integration, cleanup, and lifecycle finalization
tools. The direct
closeout preview/apply controllers (and the `_direct_closeout` helper) were
removed with the direct-closeout tool surface (issue #62): closeout is
worktree-only.

## Code Commentary

The module resolves allowed repositories and coordination-contained paths from
`McpRuntimeConfig`, builds typed `git_worktree_manager.WorktreeArgs`, and
delegates lifecycle work to `worktrees.git_worktree_manager`. Repo resolution
and path confinement use the shared `_guards` helpers (`require_repo`,
`require_within_coordination`) so the security boundary lives in one place.
Worktree start can include provider setup by writing MCP-derived lifecycle
settings and handing a package-local provider setup config to the worktree
manager. `worktree_start_tool` forwards `stale_base_choice` (GitHub #54) into
`WorktreeArgs` for the stale-base preflight recovery; the controller adds no
behavior of its own. `worktree_sync_tool` (GitHub #54 sub-task D) is the
contract-path-based controller for the mid-task base sync: it confines
`contract_path` via `require_within_coordination` and forwards
`memory_sync_choice`/`dry_run` to `git_worktree_manager.sync_result`.
`lifecycle_finalize_task_tool` confines the contract and optional task-document
paths under the coordination root, builds `git_worktree_manager.FinalizeArgs`,
and delegates final readiness, cleanup, and task-document reconciliation to the
worktree finalizer.

Slice 2c wires the observable lifecycle here while the git module stays
observer-free: `worktree_start_tool` resolves a `lifecycle_id` (the active
lifecycle's id, or a fresh `new_ulid()` when none is active), threads it into
`WorktreeArgs`, and after `start_result` calls `_attribute_start` — promoting the
active lifecycle into the contract (`ambient().promote`) on a `started` result, or
adopting the minted id when none was active. `worktree_attach_tool` gains
`on_unsaved` and calls `_attribute_attach`, which drives `ambient().attach` (the
§1.3 resume table: adopt when none is active, no-op on the same id, auto-pause a
persistent current, route an unsaved fleeting through the save gate —
`SaveGateRequired` when `on_unsaved` is absent). Both helpers no-op when no
ambient is installed (CLI/tests).

## Invariants And Boundaries

- Repo IDs must resolve through MCP settings; disallowed IDs and paths escaping
  `coordination_root` raise `AuthorityError` (via the `_guards` helpers).
- Contract paths and memory/source paths must stay under the configured
  coordination root unless a specific tool owns a setup target.
- Worktree operations call package services directly; CLI entrypoints remain
  print adapters.
- `worktree_start_tool`/`worktree_integrate_tool`/`worktree_cleanup_tool`/`lifecycle_finalize_task_tool` default
  `dry_run=False` (act-by-default); the `*_closeout_apply` controllers keep
  `dry_run=False` paired with their `*_preview` tools. `dry_run=true` previews.

## Repo-Internal References
`worktree_start_tool` marks the temp lifecycle settings file with
`unlink_settings_after_setup=True` and skips its own `finally` unlink when
`_settings_owned_by_background(result)` sees a providers state of `starting` —
the background setup thread reads the file and owns the unlink (GitHub #53).
The new `retry_provider_setup` flag is forwarded to the worktree layer, and the
provider timeout is `config.timeout_caps["providerSetupSeconds"]` (default
`DEFAULT_PROVIDER_SETUP_SECONDS`, 1800) instead of the docker-control 120 —
the documented setup cap now actually governs the worktree flow.


| Finding | Source Path |
| --- | --- |
| Worktree service behavior is owned by the worktree manager and modules. | [git_worktree_manager.py](agents-remember/mcp/src/agents_remember/worktrees/git_worktree_manager.py) |
| Worktree response models define the public tool envelopes and context summary. | [worktree.py](agents-remember/mcp/src/agents_remember/models/worktree.py) |
| Shared repo/path authority guards (`require_repo`, `require_within_coordination`). | [_guards.py](agents-remember/mcp/src/agents_remember/controllers/_guards.py) |
| Lifecycle finalization behavior is delegated to the worktree finalizer module. | [finalize.py](agents-remember/mcp/src/agents_remember/worktrees/modules/finalize.py) |

## Series-Contract Notes

Worktree start/attach/status controllers accept `parent_task` and `leaf_id` and report lifecycle attribution against `enclosure_path`, with `contract_path` retained only as the existing wire-compatible field.

## Update History

- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: worktree start/attach/status controllers now accept `leaf_id` and `parent_task`, and lifecycle attribution prefers `enclosure_path` while keeping `contract_path` as a compatibility payload field. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-23T22:50+02:00 — Added `lifecycle_finalize_task_tool`: coordination-confined contract/task-doc paths are converted into `FinalizeArgs` and delegated to `git_worktree_manager.finalize_result`. The controller remains a path-authority and typed-argument facade; finalization behavior lives in `worktrees/modules/finalize.py`. Verification metadata pinned until closeout stamps the source commit.
- 2026-06-13T18:45+02:00 — Slice 2c: wired the observable lifecycle. `worktree_start_tool` resolves + threads a `lifecycle_id` (active id or fresh mint) and `_attribute_start` promotes/adopts it after start; `worktree_attach_tool` gains `on_unsaved` and `_attribute_attach` drives the `ambient().attach` §1.3 resume table (adopt / no-op / pause+adopt / save gate). The git module stays observer-free; both helpers no-op without an ambient. Verification metadata pinned until closeout stamps the 2c code commit.
- 2026-06-11T06:47+02:00 — Removed `direct_closeout_preview_tool` / `direct_closeout_apply_tool` and the `_direct_closeout` helper (issue #62 worktree-only closeout); the controller surface is now start, attach, status, sync, closeout preview/apply, integrate, cleanup, abandon.
- 2026-06-10T09:56+02:00 — Added `worktree_sync_tool` (contract-path confinement + `memory_sync_choice`/`dry_run` forwarding to `sync_result`) for the GitHub #54 mid-task base sync.
- 2026-06-10T09:30+02:00 — `worktree_start_tool` forwards the new `stale_base_choice` recovery selector into `WorktreeArgs` (GitHub #54 stale-base preflight); plumbing only.
- 2026-06-10T07:30+02:00 — worktree_start async support (GitHub #53): the provider setup config now carries `unlink_settings_after_setup=True` and the controller skips its `finally` unlink when the result's providers state is `starting` (`_settings_owned_by_background`) — the background thread reads the temp settings file and owns the unlink. New `retry_provider_setup` flag forwarded to the worktree layer. The provider timeout switched from the hardcoded `DEFAULT_DOCKER_CONTROL_SECONDS` (120) to `config.timeout_caps['providerSetupSeconds']` (default `DEFAULT_PROVIDER_SETUP_SECONDS`, 1800) — the documented setup cap now actually governs the worktree flow (GitHub #58 evidence showed the 120s bound on seed exports).
- 2026-06-01T20:45+02:00 — Added `worktree_abandon_tool` to the controller surface and threaded the `teardown_providers` flag through `worktree_cleanup_tool` (behavior detail lives in `provider_tools.py.md`, `abandon.py.md`, `cleanup.py.md`).
- 2026-05-31T12:30+02:00 — Repo/path guards moved to shared `_guards` (require_repo/require_within_coordination) raising AuthorityError, and namespaces are now typed `git_worktree_manager.WorktreeArgs` instead of `argparse.Namespace` (1.0.0 review remediation).
- 2026-05-30T21:33+02:00: Re-verified against `825a172` after the 0.9.x provider/worktree run; the controller surface (start, attach, status, closeout preview/apply, direct closeout preview/apply, integrate, cleanup), its coordination-containment rules, and the act-by-default `dry_run` behavior still match the source. References (`git_worktree_manager.py`, `models/worktree.py`) verified present.
- 2026-05-28T19:52+02:00: Created when worktree MCP controllers moved into their own domain module.
