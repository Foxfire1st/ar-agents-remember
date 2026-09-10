# mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_control_errors.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_control_errors.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T00:27+02:00 |
| lastVerifiedCommitHash | `6f3e3fde75a1ca0202c9b07557cf86a7893e8532` |
| lastVerifiedCommitDate | 2026-09-10T07:24:09+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[worktree integration overview](../overview.md)

## Purpose

Typed lifecycle-control refusals with executable public next actions.

## Code Commentary

### Logic

The public surface is `LifecycleControlError`. This file bounds public refusal evidence and next actions. Missing, unreadable, mismatched, or ambiguous artifacts remain typed decisions with expected/observed facts; they are never downgraded to absence and private operation keys never cross the public boundary.

### Conventions

Pure classifiers return typed observations; mutation owners publish write-ahead intent and exact evidence before advancing. Public projections carry bounded expected/observed facts and executable task-addressed next actions without leaking private operation identity.

### Invariants And Boundaries

- The canonical root journal, located through the address-only locator and immutable enclosure manifest, owns normal lifecycle state.
- Accepted input and proven commits are immutable; retry and recovery stay on the same generation until evidence admits a successor.
- Queue rows and mutable task documents are not lifecycle evidence or fallback location authorities.

### Todos

None recorded beyond the explicit terminal-archive boundary recorded by the governing overview.

## Docs References

No configured Domain Documentation source applies to this repository-internal lifecycle seam.

## Repo-Internal References

The source file is the direct evidence for this file-specific ownership boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module defines `LifecycleControlError` as its public seam. | `LifecycleControlError` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_control_errors.py:14-99 |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

## CCR-L42 current candidate

Lifecycle control errors now use `resume` for fresh closeout-successor inputs, including the code-commit message arguments, replacing the retired `revise` action name.

## Update History
- 2026-09-10T00:20:36+02:00 — CCR-L42 current candidate reconciliation: Lifecycle control errors now use `resume` for fresh closeout-successor inputs, including the code-commit message arguments, replacing the retired `revise` action name.

- 2026-08-24T00:27+02:00 — 260821-CLIVE-L2 committed-route reconciliation: moved this preserved sidecar to mirror `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_control_errors.py`, repointed current source evidence and governing context, and verified the source at code commit `1d446724d099517f6f52d596b47827ae2391a2a4`.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: created from the accepted full L2 candidate. Verification fields remain blank until the architect-owned closeout has a real code commit to stamp.
