# mcp/src/agents_remember/worktrees/sync_transaction_git/_read.py

## Governing Overview

[Nearest governing route overview](overview.md)

## Purpose

Read exact refs, stash inventory and content identity for managed sync.

## Code Commentary

Ref inspection distinguishes an invalid name, an absent ref and a Git inspection error. Pinned refs use expected-value creation/deletion. The complete tracked and third-parent untracked stash inventory is proof input; sample_paths is display-only. Content reads preserve binary and symlink bytes. Root memory.md is excluded only on the memory side. Rename mapping follows carried regular-file renames without turning a diagnostic sample into a complete inventory. Completed output must be the admitted fast-forward or exact two-parent merge in pre-sync/source order.

A dirty path is untracked only after successful Git reads find it in neither the index nor current HEAD. Index absence alone also describes a staged deletion: its state belongs in the native staged patch, not a mirror of nonexistent bytes. A staged addition remains index-owned; an unstaged deletion remains tracked. Failed holder inspection never establishes untracked status. The shared predicate also keeps tracked deletion fingerprints in retained-state capture; classification alone does not establish transaction ownership.

## Evidence

- Untracked classification requires successful absence from index and HEAD; staged deletions remain patch-owned. [7]

- read_ref: qualified source contract. [1]
- create_pinned_ref: qualified source contract. [2]
- delete_pinned_ref: qualified source contract. [3]
- stashed_parked_paths: qualified source contract. [4]
- renamed_parked_paths: qualified source contract. [5]
- side_merge_completed: qualified source contract. [6]
