# mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_request.py

## Governing Overview

[worktree integration overview](../overview.md)

## Purpose

Typed validation for the public lifecycle-control request envelope.

## Code Commentary

### Logic

The public surface is `LifecycleControlRequestError`, `validate_lifecycle_control_request`. Task-addressed retry, recover, cancel, revise, integrate, retire, and supersede decisions are derived from immutable journal state plus exact live Git/process evidence. Retry preserves accepted input; revise composes proven-safe cancellation with a write-ahead successor; ambiguity routes to same-generation recovery.

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

- The module defines `LifecycleControlRequestError`; `validate_lifecycle_control_request` as its public seam. [1]

### Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

## 260821-CLIVE Exact Public Control Shapes

Authority-free request fields are validated before durable reads. Supersede requires grade and
admission together, while every other action forbids them. Commit messages remain revise-only.
This exact action matrix prevents partial control requests from reaching journal or task mutation.

## CCR-L42 current candidate

Commit-message fields are accepted only for the `resume` successor request, replacing `revise`; every other lifecycle-control action refuses present commit-message fields.
