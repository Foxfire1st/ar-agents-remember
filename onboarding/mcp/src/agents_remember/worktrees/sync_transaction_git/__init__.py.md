# mcp/src/agents_remember/worktrees/sync_transaction_git/__init__.py

## Governing Overview

[Nearest governing route overview](overview.md)

## Purpose

Compatibility import surface for the split managed-sync Git helpers.

## Code Commentary

The facade re-exports the prior public names; it is not a second implementation. Readers, native reapply proof, parking, save-first cancellation and memory merging have qualified owners in the adjacent modules. Internal evidence belongs to those owners, not to an import-only symbol in this facade.

## Evidence

- Compatibility exports have qualified implementation owners. [1]
