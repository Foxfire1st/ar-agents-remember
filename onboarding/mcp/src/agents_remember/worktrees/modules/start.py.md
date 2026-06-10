# mcp/src/agents_remember/worktrees/modules/start.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/worktrees/modules/start.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-10T07:30+02:00     |
| lastVerifiedCommitHash | `ebe9ef2aa882b5ed6df6dcb2491452efc0cf5c30` |
| lastVerifiedCommitDate | 2026-06-10T07:59:14+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

Owns worktree start, attach, status result construction, and startup preparation
for external memory and providers.

## Code Commentary

Every entry point and helper takes the typed `WorktreeArgs` dataclass (imported
from `agents_remember.worktrees.modules.args`), replacing the former
`argparse.Namespace`; `import argparse` is gone. `start_result()` resolves
context, builds the default contract, prepares code and optional memory
worktrees, runs the synchronous provider preflight, writes the contract for
real starts, and then LAUNCHES provider setup in the background (GitHub #53).
The ordering is deliberate: the contract is the durable anchor
`worktree_status` polls while the setup thread runs, so it must exist before
the launch. `plan_providers_for_start` is the sync preflight (skip /
enablement / settings checks — config-level failures still block the start
fast); `run_or_launch_provider_setup` keeps dry runs fully synchronous
(`planned`, unchanged shape) and otherwise delegates to
`provider_async.launch_provider_setup`, returning `starting` with the progress
file. The settings path transfers to the launcher's cleanup only when
`provider_setup_config.unlink_settings_after_setup` is set (the controller's
temp-file ownership handshake). `prepare_providers_for_start` remains as the
facade/CLI wrapper composing both halves in one call. `_build_start_contract`
asserts `args.task_name`/`args.worktree_name` are non-`None`, and
`_provider_start_paths` asserts `args.provider_setup_config` is non-`None`,
before use. Provider setup remains typed through `ProviderSetupRequest`; there is
no coordinator script or host-binary fallback path here. `provider_setup.load_settings`
and `provider_setup.settings_path` are now called with the settings path alone
(the `target_coordination_root` argument was dropped), and the dead
`_cgc_enablement_state` helper was removed in favour of the unified
`_provider_enablement_state`.

When an existing contract is found on disk, `start_result` now checks its
`cleanup` field: if `cleanup == "abandoned"` the contract is a tombstone whose
worktrees and branches were already discarded, so start recreates fresh rather
than attaching to the dead binding. With `args.retry_provider_setup` set, an
existing live contract routes to `_retry_provider_setup_result` instead of
attaching: refused (exit 2, poll hint) while
`provider_async.provider_setup_running` reports a fresh heartbeat, otherwise
the preflight + launch re-run against the existing contract and the result is
`provider-setup-retried` — the recovery path for failed or stale background
setups.

`prepare_memory_for_start` now also calls `_sync_worktree_memory_mtimes` after
preparing the memory worktree. `git checkout` stamps every file with the current
time; GrepAI's watcher skips unchanged files by `ModTime`, so brand-new mtimes
make every file look modified and force a full re-embed — defeating the DB clone.
`_sync_worktree_memory_mtimes` walks the freshly checked-out memory worktree,
finds each file's counterpart in the source memory repo, and calls `os.utime` to
copy the source mtime onto the worktree file. Files absent in the source are left
untouched and counted as `filesMissingInSource`. The `.git` subtree is skipped.
The result is returned as `mtimeSync` in the `prepare_memory_for_start` payload.

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Defines the `WorktreeArgs` dataclass that types every start/attach/status input. | [args.py](agents-remember-md/mcp/src/agents_remember/worktrees/modules/args.py) |
| Provider setup requests are implemented by the providers package. | [provider_setup.py](agents-remember-md/mcp/src/agents_remember/providers/provider_setup.py) |
| Worktree tests cover memory compatibility, disabled-memory choices, and dirty external-memory blocking. | [test_worktree_support.py](agents-remember-md/mcp/tests/test_worktree_support.py) |
| Launcher, ordering, retry, and guard coverage for the async path. | [test_provider_async.py](agents-remember-md/mcp/tests/test_provider_async.py) |
| Background launcher and status projection. | [provider_async.py](provider_async.py.md) |
| mtime-sync unit tests cover matching-file sync, target-only file preservation, `.git` skip, and dry-run no-op. | [test_worktree_mtime_sync.py](agents-remember-md/mcp/tests/test_worktree_mtime_sync.py) |

## Update History

- 2026-06-10T07:30+02:00 — GitHub #53: provider setup moved to a background launch. `prepare_providers_for_start` split into `plan_providers_for_start` (sync preflight) + `run_or_launch_provider_setup` (dry-run sync / real launch via `provider_async`); the contract write moved BEFORE the launch; `_run_provider_setup` became the request builder `_provider_setup_request`; `_started_result` summary names the background poll loop; added the `retry_provider_setup` path on existing contracts.
- 2026-06-10T00:40+02:00 — Added the Windows long-path preflight: on hosts with `LongPathsEnabled=0`, `start_result` blocks (exit 2) before creating worktrees when the projected worktree path plus the longest tracked path in the code or external-memory repo exceeds `WINDOWS_MAX_PATH_BUDGET` (250). The block payload reports the computed lengths and both remedies (enable long paths / shorter worktree name). `long_path_block_payload` is the pure, platform-independent decision; `_windows_long_paths_enabled` reads the registry and returns True off-Windows. Existing-contract attach still short-circuits before the preflight.
- 2026-06-02T16:24+02:00: Normalized skill references in this module to full lowercase skill names; the missing-external-memory guidance names `c-00-initialize-memory-repo` (confirmed in source `_missing_memory_repo_state`). Reference-style normalization; behavior unchanged.
- 2026-06-01T00:00+02:00 — `start_result` now detects abandoned contracts and recreates instead of reattaching. `prepare_memory_for_start` calls `_sync_worktree_memory_mtimes` to mirror source-repo file mtimes onto the freshly checked-out memory worktree, enabling GrepAI clone reuse. Updated Code Commentary.
- 2026-05-31T12:50+02:00 — Re-typed every `args` param from `argparse.Namespace` to the new `WorktreeArgs` dataclass (dropping `import argparse`), added `task_name`/`worktree_name`/`provider_setup_config` non-`None` asserts, switched `provider_setup.load_settings`/`settings_path` to the path-only signature, and removed the dead `_cgc_enablement_state` helper; corrected Code Commentary and added the args.py reference (1.0.0 review remediation).
- 2026-05-29T18:35+02:00: `_load_memory_ledger` returns `MemoryLedger | dict[str, object]` so `prepare_memory_for_start` narrows the ledger before `find_mapping`/attribute access; behavior-preserving (commit `0549b28`).
- 2026-05-25T20:41+02:00: Created during worktree manager module extraction.
