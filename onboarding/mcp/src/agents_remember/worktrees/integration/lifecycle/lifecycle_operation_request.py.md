# mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_request.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_request.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:43+02:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d` |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview | `../overview.md` |

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

## Docs References

No configured Domain Documentation source applies to this repository-internal lifecycle seam.

## Repo-Internal References

The source file is the direct evidence for this file-specific ownership boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module defines `LifecycleControlRequestError`; `validate_lifecycle_control_request` as its public seam. | `LifecycleControlRequestError`; `validate_lifecycle_control_request` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_request.py:21-35; mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_request.py:38-72 |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

## 260821-CLIVE Exact Public Control Shapes

Authority-free request fields are validated before durable reads. Supersede requires grade and
admission together, while every other action forbids them. Commit messages remain revise-only.
This exact action matrix prevents partial control requests from reaching journal or task mutation.

## Update History

- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: aligned public control request validation with supersede and revise authority. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-24T00:27+02:00 — 260821-CLIVE-L2 committed-route reconciliation: moved this preserved sidecar to mirror `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_request.py`, repointed current source evidence and governing context, and verified the source at code commit `1d446724d099517f6f52d596b47827ae2391a2a4`.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: created from the accepted full L2 candidate. Verification fields remain blank until the architect-owned closeout has a real code commit to stamp.
