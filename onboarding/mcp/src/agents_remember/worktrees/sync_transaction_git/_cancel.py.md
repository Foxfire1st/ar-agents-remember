# mcp/src/agents_remember/worktrees/sync_transaction_git/_cancel.py

## Governing Overview

[Nearest governing route overview](overview.md)

## Purpose

Assess exact cancellation ownership and save unattributable state before rollback.

## Code Commentary

Live stash/index content and retained full-index/worktree fingerprints are different ownership witnesses. Unknown attribution is not proof of later work and is never adopted as transaction output. Index blobs are binary, so newline conversion cannot invent ownership. Native merge faults retain their actual reason and confer no destructive authority. Save-first recovery writes staged.patch relative to HEAD, unstaged.patch relative to the index, a path list and exact untracked byte mirrors; symlink mirrors hold link-target bytes. Readback verifies saved digests before retry discards that state. Only explicitly proven owned untracked paths may be removed without first preserving them. Saving, verification and discard remain separate steps so a failed discard retains usable saved state.

## Evidence

- assess_stash_tree: qualified source contract. [1]
- assess_retained_tree: qualified source contract. [2]
- _index_later_paths: qualified source contract. [3]
- save_unproven_state: qualified source contract. [4]
- read_saved_unproven_state: qualified source contract. [5]
- discard_saved_unproven: qualified source contract. [6]
