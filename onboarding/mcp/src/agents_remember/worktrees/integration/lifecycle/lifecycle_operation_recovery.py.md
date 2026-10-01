# mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_recovery.py

## Governing Overview

[worktree integration overview](../overview.md)

## Purpose

Same-generation journal recovery and direct-landing execution ownership.

## Code Commentary

### Logic

Direct recovery enters through `recover_direct_landing_under_authority`; same-generation requeue is supplied by `generation.resume.requeued_same_generation`. Task-addressed retry, recover, cancel, revise, integrate, retire, and supersede decisions are derived from immutable journal state plus exact live Git/process evidence. Retry preserves accepted input; revise composes proven-safe cancellation with a write-ahead successor; ambiguity routes to same-generation recovery.

`recover_direct_landing_under_authority` delegates the pre-attempt recoverability guard, typed
post-failure translation, and strict-current-record selection to named helpers. Only the
integration boundary's typed `DirectLandingError` enters public recovery translation. An
unexpected `RuntimeError` is an invariant defect and propagates instead of being mislabeled as a
recoverable operation outcome. This centralizes the public error vocabulary without hiding defects.

### Conventions

Pure classifiers return typed observations; mutation owners publish write-ahead intent and exact evidence before advancing. Public projections carry bounded expected/observed facts and executable task-addressed next actions without leaking private operation identity.

### Invariants And Boundaries

- The canonical root journal, located through the address-only locator and immutable enclosure manifest, owns normal lifecycle state.
- Accepted input and proven commits are immutable; retry and recovery stay on the same generation until evidence admits a successor.
- Queue rows and mutable task documents are not lifecycle evidence or fallback location authorities.
- Every typed direct-attempt failure is reclassified once against the latest journal record before
  a public refusal is returned; callers do not reproduce the lower-level failure family. Untyped
  invariant failures remain loud.

### Todos

None recorded beyond the explicit terminal-archive boundary recorded by the governing overview.

## Evidence

### Docs References

No configured Domain Documentation source applies to this repository-internal lifecycle seam.

### Repo-Internal References

The source file is the direct evidence for this file-specific ownership boundary.

- The module defines `recover_direct_landing`; `direct_recovery_refusal`; `reconcile_control_mutations` as its public seam. [1]
- One translator reclassifies typed direct failures against current evidence while invariant runtime errors remain loud. [2]

### Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

## 260821-CLIVE Caller-Owned Recovery Authority

`recover_direct_landing_under_authority` no longer acquires the integration lock internally; its
caller must already own that authority. Recovery stays in the same generation, uses strict current
reads, and routes ambiguous classifier states to developer decision. The retired successor-WAL
bypass and synthetic recovery paths are absent.
