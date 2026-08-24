# mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_controls.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_controls.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:43+02:00 |
| lastVerifiedCommitHash | `f95487ec993b58d34911bba0206a7fa6ef9684eb` |
| lastVerifiedCommitDate | 2026-08-24T15:28:18+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[worktree integration overview](../overview.md)

## Purpose

Task-addressed lifecycle controls derived from durable and live evidence.

## Code Commentary

### Logic

The public surface is `LifecycleControlCommand`, `control_operation`. Task-addressed retry, recover, cancel, revise, integrate, retire, and supersede decisions are derived from immutable journal state plus exact live Git/process evidence. Retry preserves accepted input; revise composes proven-safe cancellation with a write-ahead successor; ambiguity routes to same-generation recovery.

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

| Finding | Citations | Source Path |
| --- | --- | --- |
| The module defines `LifecycleControlCommand`; `control_operation` as its public seam. | L125-L136; L149-L254 | `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_controls.py` |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

## 260821-CLIVE Task-Addressed Control Semantics

Cancel, recover, revise, retire, and supersede operate on canonical door+journal authority. Closeout
and direct cancel publish a waiting successor under the task-publication lock only after exact claim
and worker-exit proof. Supersede requires fresh grade/admission, authorized caller, and an immutable
declaration fingerprint; replay must match it. Revise validates fresh input and returns new closeout
apply arguments rather than writing a successor-intent WAL. Direct recovery runs only while its
caller owns integration/Git authority. Missing initial doors and competing declarations refuse.

## Update History

- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: reconciled all task-addressed controls with canonical door/journal ownership. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-24T00:27+02:00 — 260821-CLIVE-L2 committed-route reconciliation: moved this preserved sidecar to mirror `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_controls.py`, repointed current source evidence and governing context, and verified the source at code commit `1d446724d099517f6f52d596b47827ae2391a2a4`.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: created from the accepted full L2 candidate. Verification fields remain blank until the architect-owned closeout has a real code commit to stamp.
