# mcp/src/agents_remember/worktrees/integration/lifecycle/worker/launch.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/lifecycle/worker/launch.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-25T08:16+02:00 |
| lastVerifiedCommitHash | `cb6623775a04cbdeb0509dc26f08a8268189c3f6` |
| lastVerifiedCommitDate | `2026-08-25T08:12:56+02:00` |
| governingOverview | `../../overview.md` |

## Governing Overview

[worktree integration overview](../../overview.md)

## Purpose

Stable failure publication for detached lifecycle-worker launch.

## Code Commentary

### Logic

The public surface is `launch_or_fail`. Worker authority remains durable until exact process identity and termination are proven. Signal, permission, launch, or observation failure records a termination-required/public recovery result and blocks replacement instead of optimistically clearing the PID or lease.

### Conventions

Pure classifiers return typed observations; mutation owners publish write-ahead intent and exact evidence before advancing. Public projections carry bounded expected/observed facts and executable task-addressed next actions without leaking private operation identity.

### Invariants And Boundaries

- The canonical root journal, located through the address-only locator and immutable enclosure manifest, owns normal lifecycle state.
- Accepted input and proven commits are immutable; retry and recovery stay on the same generation until evidence admits a successor.
- Queue rows and mutable task documents are not lifecycle evidence or fallback location authorities.

### Todos

None recorded beyond the explicit terminal-archive boundary recorded by the governing overview.

### CCR private preparation boundary

A failed worker launch preserves a closeout generation with retained private preparation as `input-required` and uses the exact recovery phase. Its next action is recovery, not replacement/retry of a fresh generation; the private-preparation phase does not imply consumed approval.

| Finding | Anchor | Source |
| --- | --- | --- |
| The current `launch_or_fail` boundary implements the preparation contract above. | "def launch_or_fail" | mcp/src/agents_remember/worktrees/integration/lifecycle/worker/launch.py:26-83 |

## Docs References

No configured Domain Documentation source applies to this repository-internal lifecycle seam.

## Repo-Internal References

The source file is the direct evidence for this file-specific ownership boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module defines `launch_or_fail` as its public seam. | `launch_or_fail` | mcp/src/agents_remember/worktrees/integration/lifecycle/worker/launch.py:26-82 |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

## Update History

- 2026-09-07 — Reconciled the preparation contract introduced by 245057 against surviving d361 source; retained prior history and verification pins.


- 2026-08-25T08:16+02:00 — 260824-PDLS wave 004: moved this preserved sidecar with its behavior-preserving package split, repointed source evidence, and verified the emergency-landed source path at code commit `cb6623775a04cbdeb0509dc26f08a8268189c3f6`; this is onboarding provenance, not Dagger certification.

- 2026-08-24T00:27+02:00 — 260821-CLIVE-L2 committed-route reconciliation: moved this preserved sidecar to mirror `mcp/src/agents_remember/worktrees/integration/lifecycle/worker/launch.py`, repointed current source evidence and governing context, and verified the source at code commit `1d446724d099517f6f52d596b47827ae2391a2a4`.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: created from the accepted full L2 candidate. Verification fields remain blank until the architect-owned closeout has a real code commit to stamp.
