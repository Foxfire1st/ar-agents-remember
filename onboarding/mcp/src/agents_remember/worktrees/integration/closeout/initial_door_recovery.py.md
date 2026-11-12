# mcp/src/agents_remember/worktrees/integration/closeout/initial_door_recovery.py

## Governing Overview

[worktree integration overview](../overview.md)

## Purpose

Pure classifier for the sole recoverable initial closeout-door intent gap.

## Code Commentary

### Logic

The public surface is `InitialCloseoutDoorRecoveryClassification`, `classify_initial_closeout_door_recovery`. The journal owns a write-once closeout-door generation. Publication intent and the journal's own state transition decide recovery; the queue may consume the published door but cannot synthesize, repair, or retain lifecycle evidence.

Since the closeout-door cut (commit `fad9808e`) the live door is read through
`live_closeout_door(contract)` rather than a `contract.closeout_door` field, which no longer exists.
The projected `contractDoor` observation therefore reports `None` when no live door is published,
instead of reading contract bytes.

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

- The module defines `InitialCloseoutDoorRecoveryClassification`; `classify_initial_closeout_door_recovery` as its public seam. [1]

### Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

## 260821-CLIVE No Synthetic Initial Door

Recovery no longer fabricates a missing generation-1 claimed door. A canonical closeout record that
lacks its create-time door intent/proof is a developer-decision state and automatic recovery is
forbidden. Durable authority must have been journaled before the crash; later filesystem shape or
queue membership cannot backfill it.
