# mcp/src/agents_remember/worktrees/sync_transaction_parking.py

## Governing Overview

[Nearest governing route overview](overview.md)

## Purpose

Recover product-owned WIP parking when the process died before admission was journaled.

## Code Commentary

Orphan adoption checks the operation-specific stash message and actual recorded Git prestate before constructing a cancellation record. Unrelated stashes and mismatched authority are refused rather than guessed into this generation. The adopted record preserves the exact original stash holder; its sampled paths are guidance, not the restoration proof. This adapter owns pre-journal admission recovery, not a second landing or cleanup transaction.

## Evidence

- orphaned_cancel_record: qualified source contract. [1]
- _orphaned_park_stashes: qualified source contract. [2]
- _adopt_orphaned_park: qualified source contract. [3]
- _refuse_orphaned_park: qualified source contract. [4]
