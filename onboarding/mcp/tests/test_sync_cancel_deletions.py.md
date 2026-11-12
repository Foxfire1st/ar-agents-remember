# mcp/tests/test_sync_cancel_deletions.py

## Governing Overview

[MCP tests](overview.md)

## Purpose

Protect save-first product cancellation when original parked work and later owner work contain staged or unstaged deletions. A deletion is native patch state, not a nonexistent untracked file to mirror.

## Code Commentary

Both cases use the existing disposable `SyncFixture`: park work into a reapply conflict, resolve it, delete another tracked file as later work, add genuine untracked binary bytes, move the source again, observe `continue` refusing the moved source, then cancel through the product. They compare the restored pre-sync HEAD, complete index entries, staged/unstaged binary diffs, worktree bytes/status and unrelated stash census. Only the sync-owned stash is consumed and the journal becomes cancelled.

The saved later deletion belongs only to its appropriate staged or unstaged patch; neither parked nor later deletion gets a nonexistent-file mirror. Saved-file digests appear in the answer. Replaying the saved patches and untracked mirror reconstructs the exact pre-cancel index tree and worktree; the already parked untracked candidate is supplied separately during replay. The staged case protects the observed index-only-classification regression; the unstaged case is a preservation control. These assertion definitions and catalog declarations are not execution receipts or a claim about every process-death window.

## Evidence

- Staged deletion cancellation returns the original parked partition and preserves later state through saved patches and binary mirrors. [1]
- Unstaged deletion cancellation preserves its original index/worktree partition through the same real operation and replay assertions. [2]
