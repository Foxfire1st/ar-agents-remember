# mcp/src/agents_remember/worktrees/modules/start.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/worktrees/modules/start.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-01T00:00+02:00                     |
| lastVerifiedCommitHash | `53b17f574a53ae400f8abb9fda264fa9fa3e8dff` |
| lastVerifiedCommitDate | 2026-06-02T16:24:22+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

Owns worktree start, attach, status result construction, and startup preparation
for external memory and providers.

## Code Commentary

Every entry point and helper takes the typed `WorktreeArgs` dataclass (imported
from `agents_remember.worktrees.modules.args`), replacing the former
`argparse.Namespace`; `import argparse` is gone. `start_result()` resolves
context, builds the default contract, prepares code and optional memory
worktrees, prepares provider runtime state when MCP-provided settings are
present, and writes the contract for real starts. `_build_start_contract`
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
than attaching to the dead binding.

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
| mtime-sync unit tests cover matching-file sync, target-only file preservation, `.git` skip, and dry-run no-op. | [test_worktree_mtime_sync.py](agents-remember-md/mcp/tests/test_worktree_mtime_sync.py) |

## Update History

- 2026-06-02T16:24+02:00: Normalized skill references in this module to full lowercase skill names; the missing-external-memory guidance names `c-00-initialize-memory-repo` (confirmed in source `_missing_memory_repo_state`). Reference-style normalization; behavior unchanged.
- 2026-06-01T00:00+02:00 — `start_result` now detects abandoned contracts and recreates instead of reattaching. `prepare_memory_for_start` calls `_sync_worktree_memory_mtimes` to mirror source-repo file mtimes onto the freshly checked-out memory worktree, enabling GrepAI clone reuse. Updated Code Commentary.
- 2026-05-31T12:50+02:00 — Re-typed every `args` param from `argparse.Namespace` to the new `WorktreeArgs` dataclass (dropping `import argparse`), added `task_name`/`worktree_name`/`provider_setup_config` non-`None` asserts, switched `provider_setup.load_settings`/`settings_path` to the path-only signature, and removed the dead `_cgc_enablement_state` helper; corrected Code Commentary and added the args.py reference (1.0.0 review remediation).
- 2026-05-29T18:35+02:00: `_load_memory_ledger` returns `MemoryLedger | dict[str, object]` so `prepare_memory_for_start` narrows the ledger before `find_mapping`/attribute access; behavior-preserving (commit `0549b28`).
- 2026-05-25T20:41+02:00: Created during worktree manager module extraction.
