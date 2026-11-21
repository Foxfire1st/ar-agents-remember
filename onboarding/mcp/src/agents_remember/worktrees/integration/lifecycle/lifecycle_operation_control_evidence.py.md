# mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_control_evidence.py

## Governing Overview

[Governing route overview](overview.md)

## Purpose

Live Git evidence used to authorize lifecycle cancellation and recovery.

## Code Commentary

### Logic

The live direct-landing cancellation path reconciles code and memory mutation evidence and derives matching recovery cells. Ambiguous or proven output requires recovery. `workerExitProven=True` is a retained cancellation-evidence field. `prove_cancellable_git` populates it without observing a process.

`prove_cancellable_git` checks protected branch identity, HEAD/tree and reflog identity against the accepted prestate. It can preserve a staged or repaired candidate as distinct observed input. On apply, changed reconciliation uses the store's conditional update. The module retains `unchanged_integration_refs` to compare refs for the stored integration evidence shape. The registered journal control refuses ordinary closeout and integration records before entering cancellation.

### Conventions

Pure classifiers return typed observations; mutation owners publish write-ahead intent and exact evidence before advancing. Public projections carry bounded expected/observed facts and executable task-addressed next actions without leaking private operation identity.

#### Invariants And Boundaries

- The canonical root journal, located through the locator and immutable enclosure manifest, retains direct generations and historical ordinary records.
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

The shared evidence helper checks unchanged logical refs when a supplied record retains private preparation. Those per-intent facts are returned even without mutation evidence and are combined with Git facts when present. This is a retained validation boundary for record contents. Ordinary closeout enters its synchronous tool.

- `_cancellable_closeout_facts` checks unchanged logical refs when the supplied record carries retained private preparation. [1]

## Evidence

### Docs References

No external Domain Documentation source is configured for this slice. The current behavior is repository-owned and is supported by the source references below.

No configured external source applies.

### Repo-Internal References

The following current source boundaries establish the ledger-retirement behavior.

- `_reconciled_closeout_record` reconciles actual mutations and derives their two recovery commit cells. [2]
- `_cancellable_closeout_facts` combines protected-output and private-preparation facts for cancellation. [3]

The source file is the direct evidence for this file-specific ownership boundary.


- `prove_cancellable_git` derives exact no-output evidence. `unchanged_integration_refs` remains the ref-comparison helper for stored integration evidence. [4]


### Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

No additional cross-repository evidence applies.

## Historical CCR-L42 legacy-output refusal

The retained evidence helper's legacy-output refusal states that proven migrated output cannot be cancelled or resumed; the exact recovery path remains required before any successor action.
