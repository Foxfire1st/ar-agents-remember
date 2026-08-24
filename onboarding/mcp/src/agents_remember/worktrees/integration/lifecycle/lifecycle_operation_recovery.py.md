# mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_recovery.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_recovery.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:43+02:00 |
| lastVerifiedCommitHash | `f95487ec993b58d34911bba0206a7fa6ef9684eb` |
| lastVerifiedCommitDate | 2026-08-24T15:28:18+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[worktree integration overview](../overview.md)

## Purpose

Same-generation journal recovery and direct-landing execution ownership.

## Code Commentary

### Logic

The public surface is `recover_direct_landing`, `direct_recovery_refusal`, `reconcile_control_mutations`, `requeued_same_generation`. Task-addressed retry, recover, cancel, revise, integrate, retire, and supersede decisions are derived from immutable journal state plus exact live Git/process evidence. Retry preserves accepted input; revise composes proven-safe cancellation with a write-ahead successor; ambiguity routes to same-generation recovery.

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
| The module defines `recover_direct_landing`; `direct_recovery_refusal`; `reconcile_control_mutations` as its public seam. | L36-L102; L105-L115; L118-L163 | `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_recovery.py` |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

## 260821-CLIVE Caller-Owned Recovery Authority

`recover_direct_landing_under_authority` no longer acquires the integration lock internally; its
caller must already own that authority. Recovery stays in the same generation, uses strict current
reads, and routes ambiguous classifier states to developer decision. The retired successor-WAL
bypass and synthetic recovery paths are absent.

## Update History

- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: recorded caller-owned integration authority and same-generation strict recovery. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-24T00:27+02:00 — 260821-CLIVE-L2 committed-route reconciliation: moved this preserved sidecar to mirror `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_recovery.py`, repointed current source evidence and governing context, and verified the source at code commit `1d446724d099517f6f52d596b47827ae2391a2a4`.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: created from the accepted full L2 candidate. Verification fields remain blank until the architect-owned closeout has a real code commit to stamp.
