# mcp/src/agents_remember/worktrees/modules/cleanup.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/worktrees/modules/cleanup.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-10T07:30+02:00     |
| lastVerifiedCommitHash | `ab7e21b4ab4b8526adcdad8ea2243657b8aea7a0` |
| lastVerifiedCommitDate | 2026-06-10T08:21:41+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

Owns post-integration cleanup of registered worktrees, merged task branches,
and empty worktree folders.

## Code Commentary

`cleanup_result` takes the typed `WorktreeArgs` dataclass (imported from
`agents_remember.worktrees.modules.args`), replacing the former
`argparse.Namespace`; it reads `args.approved`, `args.dry_run`,
`args.teardown_providers`, and `args.contract_path`, asserting the latter is
non-`None` before loading the contract. Cleanup requires completed integration
and explicit approval for real mutation.

When `args.teardown_providers` is true (the default), `cleanup_result` calls
`teardown_worktree_providers` first to reclaim the worktree's isolated provider
stack (Docker containers, networks, and the `provider-runtime/` tree) before
removing worktrees and directories. The teardown result is included in the
response under `providers`. When `teardown_providers` is false, a
`{"state": "skipped"}` placeholder is returned.

`remove_registered_worktree` now accepts an optional `force` keyword (default
`False`); when true it passes `--force` to `git worktree remove`. This is used
by `abandon.py` for force discard.

`delete_branch_force` is newly added and uses `git branch -D` to delete an
unmerged branch; it is used by `abandon.py`'s force path.

Cleanup still removes registered code and memory worktrees, deletes branches
only when Git proves they are merged, removes empty directories, records cleanup
completion in the contract, and reports branches Git refused to delete.

`cleanup_result` blocks (exit 2) while
`provider_async.provider_setup_running(contract)` reports a live background
setup — teardown must not race the setup thread; a dead thread surfaces as a
stale heartbeat and does not block (GitHub #53).

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Defines the `WorktreeArgs` dataclass that types the `cleanup_result` input. | [args.py](agents-remember/mcp/src/agents_remember/worktrees/modules/args.py) |
| Integration creates the scratch memory integration branch name that cleanup may remove. | [integrate.py](agents-remember/mcp/src/agents_remember/worktrees/modules/integrate.py) |
| Provider teardown is delegated to this module. | [provider_teardown.py](agents-remember/mcp/src/agents_remember/worktrees/modules/provider_teardown.py) |
| `delete_branch_force` and `remove_registered_worktree(force=...)` are reused by abandon. | [abandon.py](agents-remember/mcp/src/agents_remember/worktrees/modules/abandon.py) |
| Worktree tests cover cleanup preconditions and completed cleanup state. | [test_worktree_support.py](agents-remember/mcp/tests/test_worktree_support.py) |

## Update History

- 2026-06-10T07:30+02:00 — `cleanup_result` blocks (exit 2) while `provider_async.provider_setup_running(contract)` reports a live background setup — teardown must not race the setup thread; a dead thread surfaces as a stale heartbeat and does not block (GitHub #53).
- 2026-06-01T00:00+02:00 — `cleanup_result` now conditionally calls `teardown_worktree_providers` via the new `args.teardown_providers` flag (default true); `remove_registered_worktree` gained an optional `force` keyword; `delete_branch_force` added. Updated Code Commentary and added provider teardown + abandon cross-references.
- 2026-05-31T12:50+02:00 — `cleanup_result` arg re-typed from `argparse.Namespace` to the new `WorktreeArgs` dataclass (imported from `modules.args`) with an `args.contract_path is not None` assert; corrected Code Commentary to name the typed param and added the args.py reference (1.0.0 review remediation).
- 2026-05-25T20:41+02:00: Created during worktree manager module extraction.
