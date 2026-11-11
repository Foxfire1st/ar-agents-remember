# mcp/src/agents_remember/worktrees/sync_transaction_sources.py

## Governing Overview

[worktrees overview](overview.md)

## Purpose

Resolve the branches a sync's source strategy names to their current tips at admission, read and remove the refs a default-source sync pinned, rebuild the source choice for a journal-less recovery, and refuse a continue onto a source line that moved.

## Code Commentary

`resolve_sync_sources(contract, sync_source)` returns a `SourceSelection`: the strategy and each side's branch and current tip, the memory side only for external memory with a memory repository. An unrecorded repository default raises `BranchAuthorityUnavailable`; the transaction answers it as `sync-source-unavailable` before anything moves. `source_pair` is the own-line form (code tip, memory tip, external flag).

`default_source_refs` lists one side's pinned default-source refs by the branch their names carry; an unreadable listing raises `SyncGitProofError`. `recovered_default_branch` returns the pinned branch for a side rebuilt from refs, or `None` for the own line, and admits only one such ref at the pinned source commit; otherwise it refuses naming the refs found, the expected one, `git update-ref -d` and cancel. `recovered_source_strategy` treats a pinned code default as a repository-default generation, so that cancel also deletes the pin. `delete_default_source_refs` deletes every default-source ref of one side by expected value.

`moved_source_sides` reads each moving side's recorded source branch on continue and returns a refusal naming cancel when that tip is no longer the commit the sync carries or cannot be read; an `already-current` or skipped side is not read.

## Relationships

`sync_transaction.py` calls `resolve_sync_sources` at admission and `moved_source_sides` on continue. `sync_transaction_authority.py` uses `default_source_refs` to see pinned authority and `recovered_default_branch` to rebuild a side from refs. `sync_transaction_recovery.py` rebuilds the source choice with `recovered_source_strategy` and deletes pins on the partial-authority path with `delete_default_source_refs`. `activation/atomic_series_activation_transaction.py` reads `source_pair` for the gate that publishes `active`. The ref prefix comes from `sync_transaction_state.sync_side_default_source_prefix`; deletion goes through `sync_transaction_git.delete_pinned_ref`.

## Evidence

- Admission resolves the strategy's branches to tips, the memory side only for external memory. [1]
- The own-line pair the activation gate reads. [2]
- A rebuilt side's pinned default is admitted only when unique and at the pinned source commit. [3]
- A pinned code default marks the rebuilt record as a repository-default generation. [4]
- A continue onto a moved or unreadable source tip returns a refusal naming cancel. [5]
- An unresolvable default answers `sync-source-unavailable` before anything moves. [6]
