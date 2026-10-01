# mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_enclosure_terminal.py

## Governing Overview

[Governing route overview](overview.md)

## Purpose

Validates external terminal archive/receipt proof and the exact predecessor authority required to
publish a successor enclosure.

## Code Commentary

### Logic

A restartable predecessor must have no code or memory closeout/integration outputs. The terminal proof no longer tests retired ledger output cells; exact archive, receipt, locator, and predecessor evidence still governs successor publication.

Archive paths are fixed by the publication request and must be outside the old enclosure root.
Digest, receipt, and the pre-deletion locator must match. A surviving terminal contract may advance
only from archive-ready to the exact cleanup-completed state; restart requires a restartable
tombstone and exact terminal predecessor identity.

### Conventions

Accepted input, exact Git facts, and typed owner results stay distinct from disposable projections.

### Invariants And Boundaries

- A missing or deleted enclosure is never sufficient successor evidence.
- Archive, receipt, locator, and predecessor proofs must agree byte-for-byte.
- Successor publication is part of the terminal enclosure transaction, not a standalone WAL.

### Todos

None recorded for the ledger-retirement boundary.

## Evidence

### Docs References

No external Domain Documentation source is configured for this slice. The current behavior is repository-owned and is supported by the source references below.

No configured external source applies.

### Cross-Repo References

No separately configured cross-repository implementation governs this file; any external-memory repository is addressed by the task contract.

No additional cross-repository evidence applies.

### Repo-Internal References

The following current source boundaries establish the ledger-retirement behavior.

- `restartable_predecessor_contract` requires a terminal restartable contract without recorded code/memory outputs. [1]
- `require_successor_generation` validates exact terminal predecessor and successor identities. [2]
