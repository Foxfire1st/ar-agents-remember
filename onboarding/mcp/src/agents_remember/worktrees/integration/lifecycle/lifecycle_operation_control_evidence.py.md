# mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_control_evidence.py

## Governing Overview

[Governing route overview](overview.md)

## Purpose

Live Git evidence used to authorize lifecycle cancellation and recovery.

## Code Commentary

### Logic

Closeout cancellation reconciles only actual code and memory mutation evidence, then derives the matching recovery cells. There is no cancellation-specific ledger intent to preserve; exact protected-ref, worker-exit, and private-preparation proofs remain required.

The public surface is `prove_cancellable_git`, `unchanged_integration_refs`. Task-addressed retry, recover, cancel, resume, integrate, retire, and supersede decisions are derived from immutable journal state plus exact live Git/process evidence. Retry preserves accepted input; successor publication remains separately bound to exact cancellation and current candidate evidence. Output-free cancellation proves branch identity, HEAD/tree, and reflog identity unchanged while preserving a staged or repaired working-tree candidate as distinct successor input.

### Conventions

Pure classifiers return typed observations; mutation owners publish write-ahead intent and exact evidence before advancing. Public projections carry bounded expected/observed facts and executable task-addressed next actions without leaking private operation identity.

#### Invariants And Boundaries

- The canonical root journal, located through the address-only locator and immutable enclosure manifest, owns normal lifecycle state.
- Accepted input and proven commits are immutable; retry and recovery stay on the same generation until evidence admits a successor.
- A failed pre-commit gate may leave the old candidate staged, and a repair may change the live
  candidate. Neither is generation-owned Git output. Cancellation records both accepted and
  observed candidate/index/status identities while protecting refs and commits from silent change.
- An unattributed protected-ref change is a developer decision; it is never routed to a same-
  generation recovery action that the current evidence does not legally admit.
- Queue rows and mutable task documents are not lifecycle evidence or fallback location authorities.

### Todos

None recorded beyond the explicit terminal-archive boundary recorded by the governing overview.

### CCR private preparation boundary

Cancellation of retained private preparation first reopens the contract and verifies the preparation’s unchanged logical refs. Those per-intent facts are returned even when no Git mutation evidence exists, and are combined with mutation reconciliation when it does. Absence of published Git mutation is not enough to discard private preparation.

- The current `_cancellable_closeout_facts` boundary implements the preparation contract above. [1]

## Evidence

### Docs References

No external Domain Documentation source is configured for this slice. The current behavior is repository-owned and is supported by the source references below.

No configured external source applies.

### Repo-Internal References

The following current source boundaries establish the ledger-retirement behavior.

- `_reconciled_closeout_record` reconciles actual mutations and derives their two recovery commit cells. [2]
- `_cancellable_closeout_facts` combines protected-output and private-preparation facts for cancellation. [3]

The source file is the direct evidence for this file-specific ownership boundary.

- The module defines `prove_cancellable_git`; `unchanged_integration_refs` as its public seam. [4]

### Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

No additional cross-repository evidence applies.

## CCR-L42 current candidate

The legacy-output recovery refusal now states that proven migrated output cannot be cancelled or resumed; the exact recovery path remains required before any successor action.
