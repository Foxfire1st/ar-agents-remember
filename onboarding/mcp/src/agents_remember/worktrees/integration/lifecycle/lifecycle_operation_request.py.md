# mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_request.py

## Governing Overview

[worktree integration overview](../overview.md)

## Purpose

Typed validation for the public lifecycle-control request envelope.

## Code Commentary

### Logic

`validate_lifecycle_control_request` checks the supplied generation, developer intent and action-specific fields before authority reads. The registered control vocabulary is `retry`, `recover`, `resume`, `cancel`, `retire` and `supersede`. Request validation checks shape. The lifecycle control handler separately decides which actions an admitted direct generation can use.

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

- `LifecycleControlRequestError` and `validate_lifecycle_control_request` own authority-free request validation. [1]

### Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

## Public Control Shapes

The request requires a positive expected generation and a nonblank intent note. Only `resume` may carry commit-message fields. `supersede` requires both grade and admission, and every other action forbids them. An accepted envelope still needs the handler's generation and evidence checks.

The 260821-CLIVE request used the earlier action name `revise` for commit-message fields. CCR-L42 replaced that request action name with `resume`.
