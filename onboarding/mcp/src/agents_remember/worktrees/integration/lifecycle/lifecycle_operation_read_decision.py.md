# mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_read_decision.py

## Governing Overview

[worktree integration overview](../overview.md)

## Purpose

Bounded public decision for one strict current/successor journal read failure.

## Code Commentary

### Logic

The public surface is `LifecycleJournalReadDecision`, `lifecycle_journal_read_decision`. This file bounds public refusal evidence and next actions. Missing, unreadable, mismatched, or ambiguous artifacts remain typed decisions with expected/observed facts; they are never downgraded to absence and private operation keys never cross the public boundary.

### Conventions

Pure classifiers return typed observations; mutation owners publish write-ahead intent and exact evidence before advancing. Public projections carry bounded expected/observed facts and executable task-addressed next actions without leaking private operation identity.

### Invariants And Boundaries

- The canonical root journal, located through the address-only locator and immutable enclosure manifest, owns normal lifecycle state.
- Accepted input and proven commits are immutable; retry and recovery stay on the same generation until evidence admits a successor.
- Queue rows and mutable task documents are not lifecycle evidence or fallback location authorities.

### Todos

None recorded beyond the explicit terminal-archive boundary recorded by the governing overview.

## Evidence

### Docs References

No configured Domain Documentation source applies to this repository-internal lifecycle seam.

### Repo-Internal References

The source file is the direct evidence for this file-specific ownership boundary.

- The module defines `LifecycleJournalReadDecision`; `lifecycle_journal_read_decision` as its public seam. [1]

### Cross-Repo References

No meaningful cross-repository boundary is owned by this file.
