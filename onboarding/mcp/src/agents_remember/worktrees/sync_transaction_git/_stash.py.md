# mcp/src/agents_remember/worktrees/sync_transaction_git/_stash.py

## Governing Overview

[Nearest governing route overview](overview.md)

## Purpose

Park and reapply exact substantive work while retaining the original recovery authority.

## Code Commentary

Typed side records preserve repository/branch identity. Only the memory root cache is disposable; a code-side memory.md remains substantive. Parking includes untracked work and a failed post-stash preflight restores the exact staged/unstaged partition before dropping its own stash. Reapply and cache-only recovery do not grant authority over other dirty paths. The original stash remains the restoration witness until terminal recovery; dropping it is distinct from merely settling a side. Stale-lock cleanup distinguishes a lock held by a live process from a stale file.

Cache-only stash-conflict recovery requires a clean substantive prestate and the existing restored-WIP proof; it is not an exception for substantive conflicts. Temporary cleanup and rollback retain recorded side/ref identity, and save-first recovery must preserve later owner work rather than classifying it as disposable cache.

## Evidence

- require_side_checkout: qualified source contract. [1]
- clear_stale_git_locks: qualified source contract. [2]
- park_worktree_wip: qualified source contract. [3]
- apply_parked_wip: qualified source contract. [4]
- drop_parked_wip: qualified source contract. [5]
- discard_memory_cache_changes: qualified source contract. [6]
