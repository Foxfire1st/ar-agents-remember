# mcp/src/agents_remember/worktrees/integration/atomic_series_terminal.py

## Governing Overview

[Worktree-integration overview](overview.md)

## Purpose

Issues the ephemeral capability required to clean up or abandon an atomic series enclosure.

## Code Commentary

The permit binds the exact canonical series address, operation, contract, active context, and
current thread. Children must already be retired unless a retry is backed by exact archived
terminal authority. The permit is deliberately unforgeable and valid only inside the bounded
terminal transaction that created it.

## Invariants And Boundaries

- A permit cannot be serialized, reused, or treated as queue-held terminal authority.
- Retry authority comes from exact archived terminal proof, not missing worktree state.
- Cleanup and abandon must prove the same series and transaction context.

## Evidence

### Repo-Internal References

- Terminal series authority is an ephemeral context-bound capability. [1]
