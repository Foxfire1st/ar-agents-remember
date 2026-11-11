# mcp/tests/test_sync_source_strategy.py

## Governing Overview

[overview](overview.md)

## Purpose

The unit tests prove that each sync source strategy answers every question the sync transaction asks of it, and that the recovery refusals name what they found and the way out. They use plain records and contracts; the repository default branch is read through a stub.

## Code Commentary

`source_strategy` maps an omitted or empty `sync_source` to `CONTRACT_LINE` and `repository-default` to `REPOSITORY_DEFAULT`, and refuses any other value with a message naming `repository-default`.

The contract line reads the contract's source branches, moves the base pair to the pulled tips (keeping the base of a skipped side), adds no sync-log keys, pins no ref, reports no moved default and records empty source fields. Its finalization moves the pair and appends the entry, and the undo removes both; an undo whose sync log does not hold this generation's entry is refused as not owned by it.

The repository default reads the stubbed default branches, keeps the base pair, logs `syncSource` with each side's source branch and commit, pins the side's ref under its default-source prefix and records the contract's own source branches. A contract whose source branch changed after the sync was admitted is refused with a message naming both branches and ending in the `worktree_sync` cancel route. `moved_default` names a side whose repository default changed. Finalization appends only the sync-log entry, and the undo removes only that entry.

`recovered_default_branch` returns the one pinned default-source ref at the pinned commit, or nothing when there is none. Two refs at that commit are refused with every ref found, the expected single ref and a message ending in the cancel route.

## Relationships

The strategies are `ContractLineSource` and `RepositoryDefaultSource` in `mcp/src/agents_remember/worktrees/sync_source_strategy.py`; `recovered_default_branch` is in `mcp/src/agents_remember/worktrees/sync_transaction_sources.py`. `test_sync_repository_default.py` covers the default-source sync route itself.

## Evidence

- The strategy is chosen once from the request or journal value, and any other value is refused. [1]
- The contract line moves the pair to the pulled sources and its undo is refused without its own log entry. [2]
- The repository default keeps the pair, pins its ref, logs its sources and refuses a retargeted journal branch. [3]
- Inconsistent recovery refs are refused with what was found, the expected ref and the cancel route. [4]
