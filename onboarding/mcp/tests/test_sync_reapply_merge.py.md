# mcp/tests/test_sync_reapply_merge.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

Behavioral regression witnesses for the sync restore proof and cancellation sharing the exact native reapply construction, including union-catalog rows, effective worktree configuration, staged binary bytes and safe native-acquisition failure.

## Code Commentary

`ReapplyMergeTests` drives the real sync through `SyncFixture` in disposable repositories. Positive cases require the carried head, restored output and stash retirement. Negative cases remove a parked row or replace the actual reapply with the byte-distinct result of another algorithm; proof must fail; cancellation saves later bytes to scratch patches/path list before completing. Worktree-only driver/configuration cases distinguish the actual reapply context from the primary repository, while parked attribute edits must not replace the carried-head rule.

A binary file staged as added before parking carries carriage returns: the cancellation witness compares the restored tree and staged status, catching text-mode index reads. Injected native merge/configuration failures stop proof without a plain-file fallback; cancel succeeds under the fault, restores parked tree/head, empties stash and repeats terminally. These are assertion definitions, not a new invocation or acceptance receipt. The shared `snapshot_tree` records file bytes; the broader independent Reviewer evidence separately covers type/mode/index/record preservation.

`merge_values_in_use` reads tracked attribute files and `MERGE_CASES` declares known merge-value examples. The registration guard names any uncovered value and its source lines; each declared value is exercised by the real catalog-row sync case. Extending repository merge rules requires extending that behavioral table, not blindly accepting any attribute. Catalog/lane membership remains selection and dependency accounting, not test execution.

## Invariants And Boundaries

- One actual expected output, not acceptance of both diff algorithms.
- Driver/configuration/attribute acquisition failures cannot borrow success from a plain merge.
- Save-first cancellation retains owner bytes in scratch artifacts before terminal rollback.
- Rename relocation and checkout newline conversion remain outside this module; automatic save-before-cancel is asserted here.

## Evidence


- Union rows added at the same place finish sync with exact carried-first output. [1]

- A missing parked union row fails only its named path and retains stash authority. [2]
- Cancellation recognizes reapplied catalogs and restores the parked tree. [3]
- Cancellation recognizes a binary addition's exact staged bytes. [4]

- A byte-distinct other-algorithm result cannot satisfy restoration or authorize cancellation. [5]

- The effective worktree driver/configuration is used for proof and cancellation. [6]

- Native acquisition failure retains the stopped generation and refuses without fallback before recoverable cancellation. [7]

- Every repository merge value needs a declared real-sync case. [8]
