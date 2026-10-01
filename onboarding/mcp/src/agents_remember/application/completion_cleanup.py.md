# mcp/src/agents_remember/application/completion_cleanup.py

## Governing Overview

[Application overview](overview.md)

## Purpose

`completion_cleanup.py` owns the resource-cleanup policy that runs only after a worktree
integration or lifecycle-finalization edge has already succeeded. It closes completed
worker/reviewer/curator seats when an exact durable report proves their turn finished, while
preserving the historical landed/archive mode as an explicit settings opt-out.

## Code Commentary

### Logic

`auto_complete_seats` resolves the enclosure contract to a canonical `TaskDocumentRef` through
`TaskDocumentTopology` and opens the durable terminal catalog. With
`autoCloseCompletedSeats=true`, `_retire_reported_leaf_seats` folds the operator inbox once, admits
only `turn-report` records with the exact `senderAgentId` and matching
`subjectTaskDocumentRef`, and retires matching live or landed task seats through `retire_entry`.
Missing proof is returned in
`autoCloseDeferredSeats`; per-seat exceptions are returned in `autoCloseFailedSeats`; successful
retirements are returned in `autoClosedSeats` and logged best-effort after catalog provenance is
durable. With auto-close disabled, the same finite role set uses `land_seats_for_task` and returns
`autoLandedSeats`. Candidate selection uses `binding_task_document_ref`, so a staged replacement is
closed with the same canonical leaf seat instead of escaping cleanup through its replacement field.

### Conventions

The completion edge supplies the human-readable reason and edge identifier. This module supplies
the finite eligible-role boundary and all cleanup side effects. Result keys use the public wire
names declared by the integration and finalization response models.

### Invariants And Boundaries

- Automatic close is report-gated by exact session and exact task-document identity; a missing or
  wrong-task report never kills a process.
- Only worker, reviewer, and curator are candidates. Manager and orchestrator are coordination
  owners and cannot enter the automatic cleanup set.
- Cleanup is subordinate to the already-successful completion edge. Contract, inbox, catalog,
  host, landing, or observer-log failures cannot rewrite integration/finalization success.
- Retirement uses the normal graceful-stop, tmux termination, and catalog-provenance path.
  Transcripts and durable reports are not deleted.
- The inbox is folded once per edge and the candidate list is read once, avoiding per-seat store
  rescans.
- Primary and staged-replacement rows are compared through their canonical binding document.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation entries are configured for this repository, and this module implements a
repository-local orchestration policy.

### Repo-Internal References

The worktree application entry points invoke this owner only after successful non-dry-run edges;
tests pin edge wiring separately from cleanup failure containment.

- The completion owner resolves task truth, folds report evidence, and applies the configured close/land policy. [1]
- Candidate selection includes every non-terminated role occupant bound to the canonical task document. [2]
- Cleanup is subordinate to successful completion; contract failures cannot rewrite the completed edge. [3]

### Cross-Repo References

No meaningful cross-repository boundary is owned by this module.
