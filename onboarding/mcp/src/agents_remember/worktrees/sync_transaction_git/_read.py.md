# mcp/src/agents_remember/worktrees/sync_transaction_git/_read.py

## Governing Overview

[Nearest governing route overview](overview.md)

## Purpose

Read exact refs, stash inventory and content identity for managed sync.

## Code Commentary

Ref inspection distinguishes an invalid name, an absent ref and a Git inspection error. Pinned refs use expected-value creation/deletion. The complete tracked and third-parent untracked stash inventory is proof input; sample_paths is display-only. Content reads preserve binary and symlink bytes. Root memory.md is excluded only on the memory side. Rename mapping follows carried regular-file renames without turning a diagnostic sample into a complete inventory. Completed output must be the admitted fast-forward or exact two-parent merge in pre-sync/source order.

## Evidence

- read_ref: qualified source contract. [1]
- create_pinned_ref: qualified source contract. [2]
- delete_pinned_ref: qualified source contract. [3]
- stashed_parked_paths: qualified source contract. [4]
- renamed_parked_paths: qualified source contract. [5]
- side_merge_completed: qualified source contract. [6]
