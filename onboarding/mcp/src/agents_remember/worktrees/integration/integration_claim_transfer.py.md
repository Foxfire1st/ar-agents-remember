# mcp/src/agents_remember/worktrees/integration/integration_claim_transfer.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/integration_claim_transfer.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:43+02:00 |
| lastVerifiedCommitHash | `f95487ec993b58d34911bba0206a7fa6ef9684eb` |
| lastVerifiedCommitDate | 2026-08-24T15:28:18+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[worktree integration overview](overview.md)

## Purpose

Lease-serialized transfer from scheduling projection to integration journal.

## Code Commentary

### Logic

The public surface is `transfer_and_publish_integration_claim`. Claim transfer is serialized under
the lifecycle lease and proves the exact claimed source journal before publication. Later recovery
uses the retained door/source-journal evidence and never depends on a projection row.

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
| The module defines `transfer_and_publish_integration_claim` as its public seam. | L20-L55 | `mcp/src/agents_remember/worktrees/integration/integration_claim_transfer.py` |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

## 260821-CLIVE Terminology-Only Delta

CLIVE changes only the local description/progress wording from consuming a certified queue row to
proving the claimed source journal. The transfer flow owned by this file is otherwise unchanged;
door/source-journal policy lives at the integration publication fence and organizational-completion
owners.

## Update History

- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: verified the local change as terminology-only while correcting the authority noun. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: created from the accepted full L2 candidate. Verification fields remain blank until the architect-owned closeout has a real code commit to stamp.
