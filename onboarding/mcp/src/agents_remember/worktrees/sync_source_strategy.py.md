# mcp/src/agents_remember/worktrees/sync_source_strategy.py

## Governing Overview

[worktrees overview](overview.md)

## Purpose

Decide, once per sync, which line the sync pulls: the contract's own source line (`sync_source` omitted, `""` in the journal) or each repository's default branch (`sync_source="repository-default"`). One strategy object per choice answers every question the transaction asks of that choice, so no caller compares the mode itself.

## Code Commentary

`source_strategy` maps a request value (`None` when omitted) or a journal value (`""`) to `CONTRACT_LINE` or `REPOSITORY_DEFAULT` and raises `ValueError` for any other value; `SELECTABLE_SYNC_SOURCES` holds the one value a caller may name.

`SyncSourceStrategy` is the seam: the branch per side, whether the recorded base pair already carries the sources, the bases a finalized sync records, the extra sync-log keys, the extra pinned ref, the live moved-default check, the source branch the journal must carry, the journal fields recorded at admission, whether the contract already holds this generation's finalization, and how a cancel removes it.

`ContractLineSource` is the own-line route: a finalized sync moves the base pair to the source commits (the memory base stays when memory was skipped), adds no log keys and no pin, and its undo proves the moved pair and the trailing entry's `FINALIZED_KEYS` before restoring the old pair and dropping that entry.

`RepositoryDefaultSource` reads the code repository's `origin/HEAD` default and the memory repository's `origin/HEAD` or `memory_init` record (`repository_default_branch_of`; an unrecorded default raises `BranchAuthorityUnavailable`). It keeps the base pair, so only the work branches decide whether a sync is already current; it pins each side's resolved branch in a ref under `sync_side_default_source_prefix`; its log keys add `syncSource` and each side's source branch and commit. `moved_default` is the only live default read after admission and is asked only on continue: a default that changed or cannot be read returns a refusal sentence naming cancel. `journal_source_branch` keeps the recorded default as the source but refuses, naming cancel, when the contract's own source branch differs from the one recorded at admission (`codeSourceFrom`/`memorySourceFrom`). Its finalization is recognised by the contract's last sync-log entry (`owns_log_entry`), and its cancel removes only that entry.

`sync_log_entry` builds the entry a finalized generation appends, without its time: from and to bases, the side plans, the produced heads `codeHeadTo`/`memoryHeadTo`, and the strategy's own keys.

## Relationships

`sync_transaction.py` validates `sync_source` against `SELECTABLE_SYNC_SOURCES`, records the choice at admission and asks `moved_default` on continue. `sync_transaction_sources.py` resolves the chosen branches to tips and rebuilds the strategy from pins. `sync_transaction_authority.py` pins, checks and deletes the default-source ref and validates the journal against the contract through `journal_source_branch`. `sync_transaction_recovery.py` finalizes and cancels through `finalized`, `finalization_absent`, `without_finalization` and `sync_log_entry`. `sync_transaction_completion.py` reads `target_bases`, `synced_summary`, `result_keys` and `request_args`. `sync_source_refresh.py` and `activation/atomic_series_activation_transaction.py` read `source_branch`. The default-branch readers belong to `integration/integration_branch_repository.py`.

## Evidence

- A request or journal value selects one strategy; any other value raises. [1]
- The seam names every question the transaction asks of the source choice. [2]
- The own line moves the base pair to the sources and undoes only a proven finalization. [3]
- The default strategy keeps the pair, pins its branch and adds source keys to the log. [4]
- On continue a changed or unreadable default returns a refusal naming cancel. [5]
- A retargeted contract refuses beside the recorded default. [6]
- The finalized entry carries bases, plans, produced heads and the strategy's keys. [7]
