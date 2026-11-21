# mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_control_errors.py

## Governing Overview

[Governing route overview](overview.md)

## Purpose

Typed lifecycle-control refusals with executable public next actions.

## Code Commentary

### Logic

`response_fields` projects bounded expected and observed facts and any explicit replacement tool. Absent or matching historical closeout and integration generations are refused by the control owner with the matching synchronous tool. A record for a different generation returns `lifecycle-generation-changed`. The generic formatter retains code and memory message placeholders for a resume-shaped response.

The public surface is `LifecycleControlError`. This file bounds public refusal evidence and next actions. Missing, unreadable, mismatched, or ambiguous artifacts remain typed decisions with expected/observed facts; they are never downgraded to absence and private operation keys never cross the public boundary.

### Conventions

Pure classifiers return typed observations; mutation owners publish write-ahead intent and exact evidence before advancing. Public projections carry bounded expected/observed facts and executable task-addressed next actions without leaking private operation identity.

#### Invariants And Boundaries

- The canonical root journal, located through the address-only locator and immutable enclosure manifest, owns normal lifecycle state.
- Accepted input and proven commits are immutable; retry and recovery stay on the same generation until evidence admits a successor.
- Queue rows and mutable task documents are not lifecycle evidence or fallback location authorities.

### Todos

None recorded beyond the explicit terminal-archive boundary recorded by the governing overview.

## Evidence

### Docs References

No external Domain Documentation source is configured for this slice. The current behavior is repository-owned and is supported by the source references below.

No configured external source applies.

### Repo-Internal References

The following current source boundaries establish the ledger-retirement behavior.

- `LifecycleControlError` bounds refusal details and projects the action or explicit replacement tool supplied by the caller. [1]

The source file is the direct evidence for this file-specific ownership boundary.

- The module defines `LifecycleControlError` as its public seam. [2]

### Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

No additional cross-repository evidence applies.

## Historical CCR-L42 successor syntax

Before ordinary closeout journal execution was retired, lifecycle control errors used `resume` for fresh closeout-successor inputs, including the code-commit message arguments, replacing the retired `revise` action name.
