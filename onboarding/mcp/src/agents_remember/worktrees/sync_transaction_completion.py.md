# mcp/src/agents_remember/worktrees/sync_transaction_completion.py

## Governing Overview

[worktrees overview](overview.md)

## Purpose

Build the answer of a completed sync pass, live at finalization or replayed from the journal, so both name the same state, crossings and memory repair debt.

## Code Commentary

`completed_sync_result` reloads the contract and refuses with `SyncGitProofError` unless its base pair equals the strategy's target bases. The state is `sync-pass-completed-memory-skipped` when memory was skipped, `sync-pass-completed-source-moved-again` when a recorded source branch no longer points at the commit the sync pulled, and `synced` otherwise, with the strategy's `synced_summary` for a clean pass. The payload carries both side payloads, the bases, the strategy's result keys (`syncSource` for a repository-default sync), the fetch evidence and the crossing summaries; an unfinished state adds `sync_source_lineage` guidance whose dry-run arguments select the same source again.

`_source_moved_again` reads the source branches the sync recorded, never a re-resolved name. `successful_crossings` returns the `crossing_summary` of each side's journaled crossing report in side order; one report is answered as `crossing`, several as a list. `_name_memory_repair_debt` adds `memoryRepairDebt` (side, rule IDs, the statement and the result head) when the memory side journaled repair debt.

## Relationships

`sync_transaction_recovery.finalize_sync` answers through `completed_sync_result`, and `sync_transaction_results` imports it through the recovery module; `sync_transaction_results.terminal_resolution_replay` replays a completed generation through it. The source strategy (`sync_source_strategy`) supplies the target bases, summary, result keys and request arguments; `sync_transaction_authority` supplies the contract reload and side payloads; `knowledge_crossing.crossing_summary` shapes each crossing summary.

## Evidence

- The answer refuses a contract pair that is not the finalized one and names state, sources and debt. [1]
- "Moved again" reads the recorded source branches. [2]
- Crossing summaries come from the journaled reports. [3]
- Journaled memory repair debt is named with its rules and statement. [4]
- Finalization answers through the completed result. [5]
