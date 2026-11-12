# mcp/src/agents_remember/controlplane/held_store_discovery.py

## Governing Overview

[overview](overview.md)

## Purpose

Resumable, entry-budgeted discovery of native receipts and held stores, so a held-message reader never walks
a population without a bound and never presents a partial walk as a whole one.

## Code Commentary

`EXECUTIONS_DIRECTORY` is defined here once and imported by the CLI receipt owner; receipt discovery uses the same directory name without importing CLI.

Each scan is one open `DirectoryWalk` over an `os.scandir` handle, advanced by an explicit budget and able to
resume from its cursor rather than restart. Receipt roots are found by naming the holder, not by a fixed depth:
`receipt_holder` answers `<root>/<EXECUTIONS_DIRECTORY>`, `receipt_holder_chain` the directories above it, and
`task_receipt_steps` yields one step per task folder with its holder first, skipping `history` and `message-bindings`.

The budgets are the contract: `ENUMERATION_BUDGET = 256` entries per pass, `MAX_HELD_FOLDER_WALKS = 64` open or
cached folders — evicting one closes its scan — and `MAX_HELD_FOLDER_STORES = 64` stores per held folder. Beyond
`RECEIPT_WALK_DEPTH = 16` open levels the branch is shed and the observation is reported incomplete, not
truncated-and-complete.

`HeldFolderDiscovery` retains at most the configured number of newest JSON stores per folder in a heap. For a successful scan, `FolderListing.done` means its directory iterator was exhausted; `whole` additionally requires that the number of encountered JSON stores did not exceed the returned-store limit. Entry-budget exhaustion leaves the scan open and resumable. A missing folder is complete and empty; an unreadable folder ends with `done=True` and `whole=False`. Receipt-walk depth shedding is a separate completeness result, not folder-listing exhaustion.

## Evidence boundary

Current source interpretation at the reviewed freeze; bounded enumeration, shedding and resumption are pinned by
`mcp/tests/test_attention_discovery.py` and `test_held_store_authority.py`. No live-page witness and no CPU or
resource measurement: MIK-R200 evidence item 6 is unrun and carried to L36, item 7 unrun.
