# mcp/src/agents_remember/worktrees/integration/initial_closeout_door_recovery.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/initial_closeout_door_recovery.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:43+02:00 |
| lastVerifiedCommitHash | `f95487ec993b58d34911bba0206a7fa6ef9684eb` |
| lastVerifiedCommitDate | 2026-08-24T15:28:18+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[worktree integration overview](overview.md)

## Purpose

Pure classifier for the sole recoverable initial closeout-door intent gap.

## Code Commentary

### Logic

The public surface is `InitialCloseoutDoorRecoveryClassification`, `classify_initial_closeout_door_recovery`. The contract owns a write-once closeout-door generation. Publication intent and exact observed contract bytes decide recovery; the queue may consume the published door but cannot synthesize, repair, or retain lifecycle evidence.

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
| The module defines `InitialCloseoutDoorRecoveryClassification`; `classify_initial_closeout_door_recovery` as its public seam. | L32-L52; L55-L85 | `mcp/src/agents_remember/worktrees/integration/initial_closeout_door_recovery.py` |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

## 260821-CLIVE No Synthetic Initial Door

Recovery no longer fabricates a missing generation-1 claimed door. A canonical closeout record that
lacks its create-time door intent/proof is a developer-decision state and automatic recovery is
forbidden. Durable authority must have been journaled before the crash; later filesystem shape or
queue membership cannot backfill it.

## Update History

- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: removed synthetic initial-door recovery from the documented contract. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: created from the accepted full L2 candidate. Verification fields remain blank until the architect-owned closeout has a real code commit to stamp.
