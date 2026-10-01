# mcp/src/agents_remember/worktrees/activation/atomic_series_activation_terminal.py

## Governing Overview

[activation overview](overview.md)

## Purpose

This file bridges a successful terminal series operation to the per-contract activation selector after
lifecycle locks are gone. It makes cleanup release visible without turning cleanup or the queue into
selector owners.

## Code Commentary

### Logic

`with_terminal_atomic_series_release` is inert for leaves, previews, and failed terminal operations.
For a successful series result it calls the exact terminal release owner, adds activation source
facts, and classifies the outcome as vacant, already vacant, different selection preserved, or
unreadable preserved. An actual release exception converts the otherwise successful result into a
retryable failure before the caller deletes the canonical contract pointer.

### Conventions

The bridge wraps and enriches `WorktreeCommandResult`; it does not write task documents or queue
projections. It addresses one contract-keyed record, so classification distinguishes a record naming
another contract from a missing one.

### Invariants And Boundaries

- Release runs after lifecycle/store locks, before destructive contract deletion.
- The release addresses only this exact contract's own record; a foreign contract's state is never
  read as a shared per-pair slot and is never cleared by this terminal operation.
- Corrupt selector evidence stays preserved for the next exact selecting repair.
- Terminal scheduling state is not inferred from cleanup success alone.

### Todos

Final call sites and citations are reconciled to the frozen source; do not stamp an uncommitted file.

## Evidence

### Docs References

No Domain Documentation source is configured for this memory root.

### Repo-Internal References

- Exact terminal release preserves absent, unreadable, or foreign selection and vacates only a record that selects this exact contract. [1]
- Focused tests prove a release addresses only the released contract and that a foreign contract's record can never be adopted. [2]

### Cross-Repo References

No cross-repository source is configured for this memory root.
