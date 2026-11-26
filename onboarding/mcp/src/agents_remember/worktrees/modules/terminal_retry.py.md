# mcp/src/agents_remember/worktrees/modules/terminal_retry.py

## Governing Overview

[modules overview](overview.md)

## Purpose

Finishes directory cleanup on retry for an exact, already-completed terminal generation (including any leftover `<worktree_group>/provider-runtime` directory as part of whole-folder removal) without crossing into a successor generation or recursively deleting surviving Git checkouts.

## Code Commentary

- `_require_generation` reloads the contract from disk and raises `AuthorityError` if the contract or `terminal_contract_authority_if_present(current)` differs from `expected: TerminalCleanupContractAuthority`.
- `_worktree_blockers` runs `_worktree_preflight(contract, force=False, mode=mode)` and additionally blocks any checkout marked `would_remove`, ensuring completed-generation retries handle directory residue only and never recursively delete a Git checkout.
- `retry_terminal_group` acquires `lifecycle_location_reservation` on live retries (`dry_run=False`), handles legacy series outside-scratch retries or delegates to `_retry_modern_group`, and converts `AuthorityError`, `ContractError`, `LifecycleOperationLocationError`, and `UnsafeLockFilesystemError` into a `{"terminal": "generation", "reason": ...}` blocker.
- `_retry_modern_group` derives `mode` (`cleanup`/`abandon`) from `expected.archive.cleanupArguments`, passes a `check_census` generation re-check callback into `archive_terminal_agents` before acquiring receipt locks or calling the host, and on live runs re-verifies the generation inside `reservation` before invoking `_apply_retry`.
- `_apply_retry` re-previews blockers, runs live `prepare_group_removal`, and invokes `remove_terminal_group` directly without any provider teardown step.

## Relationships

- Consumed by `worktrees/modules/cleanup.py` and `worktrees/modules/abandon.py` on accepted terminal retry paths.
- Serializes with `cli/role_launch_enclosure.py::publication_scope` through `worktrees/integration/lifecycle/lifecycle_location_reservation.py`.

## Evidence

- `_require_generation` reloads the contract and raises `AuthorityError` if the contract or its terminal archive authority has diverged from `expected`. [1]
- `_worktree_blockers` runs `_worktree_preflight` and blocks any surviving Git checkout marked `would_remove` so retries never recursively delete checkouts. [2]
- `retry_terminal_group` gates live retries with `lifecycle_location_reservation`, handles legacy series outside-scratch removal or modern retry, and maps generation/location/lock errors to a `terminal` blocker. [3]
- `_apply_retry` re-previews blockers, performs move-out via `prepare_group_removal`, and removes the group via `remove_terminal_group` without provider teardown. [4]
