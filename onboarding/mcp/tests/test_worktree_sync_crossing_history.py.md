# mcp/tests/test_worktree_sync_crossing_history.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Covers history ownership and recovery when a master's structural memory merge pauses for content resolution.

## Code Commentary

The fixture checks a park with only a non-record conflict. A validator refusal after attempted close restores the open file on disk and in stage zero, so the crossing writer can confirm a dependent record before continuation closes the history in the merge commit. Interrupted-open cases distinguish missing or exact operation-owned state from an intervening edit. Other cases exercise empty-history landing and the boundaries for plain merges, clean structural merges and worktree restoration after commit.

## Relationships

Drives the managed merge path and its retained side record through `worktrees/sync_transaction.py` and `worktrees/sync_transaction_git/_merge.py`.

## Evidence

- A non-record park opens history and a refused continuation restores it before a dependent confirmation. [1]
- Resume finishes only the exact interrupted open and preserves an intervening owner edit. [2]
- Replay records the owner and the landing gate accepts committed closed empty history. [3]
- Plain parks and clean structural merges have no crossing-history owner. [4]
- A restore conflict after merge commit has no crossing-history owner. [5]
