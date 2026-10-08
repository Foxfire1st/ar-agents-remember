# mcp/src/agents_remember/cli/role_launch_archive_recovery.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

Reconciles archive debt left by a closing that could not write it. The existing terminal observation
loop drives a bounded cursor over the coordination tree's launch receipts; exact terminal contract
and leaf-document truth decide which receipts are still owed, so a restart settles them without a
person calling anything.

## Code Commentary

### Logic

`LeafArchiveRecovery.tick` runs at most once per `RECOVERY_INTERVAL_SECONDS` (5 s). It lazily builds
`_scan(self.config.coordination_root / "tasks")`, a generator that walks at most 16 levels deep and
yields one entry per inspected node. Each tick inspects at most `SCAN_ENTRIES_PER_PASS` (128) entries;
`RECOVERY_BUDGET_SECONDS` (2 s) is the host-attempt deadline inside that pass, not a preemptive bound
on filesystem traversal, parsing or locking, which continue outside the timed call. For every `.json`
receipt under a `paseo-native-executions` directory or its `history/` child it records an
`ArchiveAttempt`.

`LeafArchiveRecovery._terminal_contract` accepts a receipt only when its workspace contract is a
leaf contract with `cleanup` `completed` or `abandoned`, its repository and coordination root match
the configuration, and the canonical leaf document still names the same leaf. Unreadable records
prove no identity and are revisited on a later bounded scan; `close` drops the cursor.

### Invariants And Boundaries

- The cursor is disposable and holds only directory iterators; no worklist or queue is persisted.
- No symlink is followed and no report artifact or message binding is read as a receipt.
- Each pass is bounded by its entry cap and cursor depth, and the time budget bounds host attempts, not filesystem work; the retained cursor resumes where the last pass stopped, so progression through the tree is finite across completed filesystem operations. No unconditional observer-tail or whole-operation timing guarantee is derived from these bounds.

## Evidence

- The bounded cursor inspects a limited number of entries per pass. [1]
- The scan walks bounded depth and yields per inspected entry. [2]
- Only exact terminal leaf contract and document truth is admitted. [3]
- The pass cadence and budgets are constants. [4]
