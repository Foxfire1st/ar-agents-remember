# mcp/tests/test_sync_repository_default.py

## Governing Overview

[MCP test overview](overview.md)

## Purpose

Prove the repository-default sync: with the leaf's own line on `sprint` and the default on `main`, `sync_source="repository-default"` pulls `main`, journals the choice and its pins, appends one sync-log entry and keeps the base pair; resume and cancel read the journal and pins only, and continue reads the default live.

## Code Commentary

`RepositoryDefaultSyncTests` runs the real sync over `SyncFixture` repositories. Any other `sync_source` value answers `sync-input-invalid` naming `sync_source`. A preview answers `would-sync` with `syncSource` and both sides' `main` branch and commit, and the public landing answer keeps them; the sync answers `synced`, both worktrees contain the default tips, the base pair is unchanged, the one log entry carries `syncSource`, the source branches and commits and `codeHeadTo`, `main` and `sprint` are not written, and no pin remains. A later `main` commit makes `completed_sync_result` answer `sync-pass-completed-source-moved-again` with `sync_source` in its next arguments, while a `sprint` commit does not.

A stopped default sync journals `syncSource`, the own-line `codeSourceFrom`/`memorySourceFrom` and the pinned `main` source. The journal refuses beside an ordinary record and beside a retargeted contract, and a hand-edited source branch has no pin. After the remote default moves, a dry run answers `sync-active`, continue answers `sync-source-moved`, and an unreadable default makes `moved_default` return a refusal; cancel still restores the pre-sync head and leaves the log, base and pins as before. An ordinary stopped sync continued with the default source answers `sync-input-mismatch`. With the journal deleted, ref recovery rebuilds the default generation for cancel.

The module-level case runs `_legacy_series_memory_refusal` on a series with unconverted memory whose own line moved: the own-line sync refuses as `sync-unconverted-memory-locked`, and the default sync, whose default branch already sits at the work tip, is admitted.

Two module-level cases follow the retry hint a refusal gives before any journal exists: after the contract changed during the source refresh, `_sync_live` answers `sync-contract-changed-retry`, and a series admission refusal answers its retry arguments; both name `sync_source` as the caller chose it, the repository default or none for the own line, so following the hint repeats the same sync.

## Relationships

It exercises `worktrees/sync_source_strategy.py`, `worktrees/sync_transaction_sources.py`, `worktrees/sync_transaction_authority.py` (`require_record_contract`, `require_pinned_authority`), `worktrees/sync_transaction_completion.py`, the cancel and ref-recovery path of `worktrees/sync_transaction_recovery.py`, and the series early check in `worktrees/activation/atomic_series_activation_transaction.py`. Fixtures come from `test_worktree_sync.py`, `test_sync_reapply_merge.py` and `test_closeout_queue.py` (`QueueFixture`).

## Evidence

- Only the repository default is a selectable sync source. [1]
- A default sync pulls `main`, keeps the pair, logs the sources and leaves both lines unwritten. [2]
- Resume and cancel read the journal and pins; continue reads the default. [3]
- An ordinary stopped sync cannot be continued as a default sync. [4]
- Ref recovery rebuilds the recorded default branch for cancel. [5]
- The series early check judges the default branch on a default sync. [6]
- A retry hint given before a journal exists, after a changed contract or a series admission refusal, repeats the caller's sync source. [7]
