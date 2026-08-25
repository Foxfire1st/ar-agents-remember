# mcp/src/agents_remember/worktrees/integration/closeout/door.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/closeout/door.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-25T08:16+02:00 |
| lastVerifiedCommitHash | `cb6623775a04cbdeb0509dc26f08a8268189c3f6` |
| lastVerifiedCommitDate | `2026-08-25T08:12:56+02:00` |
| governingOverview | `../overview.md` |

## Governing Overview

[worktree integration overview](../overview.md)

## Purpose

Single contract publication owner for closeout-door generations.

## Code Commentary

### Logic

The public surface is `DoorContractReadFailure`, `DoorPublicationClassification`, `DoorPublicationError`, `door_generation_for_operation`, `successor_waiting_door`, `prepare_door_publication`. The contract owns a write-once closeout-door generation. Publication intent and exact observed contract bytes decide recovery; the queue may consume the published door but cannot synthesize, repair, or retain lifecycle evidence.

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
| The module defines `DoorContractReadFailure`; `DoorPublicationClassification`; `DoorPublicationError` as its public seam. | `DoorContractReadFailure`; `DoorPublicationClassification`; `DoorPublicationError` | mcp/src/agents_remember/worktrees/integration/closeout/door.py:30-74 |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

## 260821-CLIVE Sole Door Publication Authority

This module is the sole contract publication/CAS owner for door generations. Only an exact already
published waiting generation may become claimed, and the claimed operation identity is immutable.
A waiting successor hashes its predecessor edge plus the complete task, repository, and provenance
evidence. Legal door dispositions remain waiting/deferred/withdrawn/claimed; journal outcomes such
as cancel, retire, and supersede never masquerade as door states.

## Update History

- 2026-08-25T08:16+02:00 — 260824-PDLS wave 004: moved this preserved sidecar with its behavior-preserving package split, repointed source evidence, and verified the emergency-landed source path at code commit `cb6623775a04cbdeb0509dc26f08a8268189c3f6`; this is onboarding provenance, not Dagger certification.

- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: recorded sole door publication, exact claim, and successor identity rules. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: created from the accepted full L2 candidate. Verification fields remain blank until the architect-owned closeout has a real code commit to stamp.
