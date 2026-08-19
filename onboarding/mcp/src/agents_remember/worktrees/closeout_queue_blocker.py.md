# mcp/src/agents_remember/worktrees/closeout_queue_blocker.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/closeout_queue_blocker.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-19T22:32+02:00 |
| lastVerifiedCommitHash | `b523f53b193e9783e7c7e6410c772e7d64d8df17` |
| lastVerifiedCommitDate | 2026-08-19T21:54:50+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[MCP overview](../../../overview.md)

## Purpose

Owns the atomic-blocker transitions — acquire, release, abort — extracted from
`closeout_queue.py` under the file-size rail (260815-DAG-L13-R3), plus the shared
lane-refusal fact helpers: structured refusal payloads, the sync-first boundary recovery naming,
and the stale-by-evidence sibling report.

## Code Commentary

### Logic

An in-flight atomic block owns the sprint landing lane for its entire lifetime: acquisition
requires the atomic nature, current series source bases, complete predecessors, a drained lane,
and a non-blank rationale. The lane is drained when no candidate sits in a lane-occupying state
(`LANE_OCCUPYING_STATES`: selected, closeout-in-flight, integration-in-flight) — a certified
candidate has left the closeout lane and no longer hard-blocks acquisition. Refusals carry
structured facts (`atomicBlockerOwner`, `ownerCandidate`, `inFlightOrganizationalLeafs`) so the
start-anyway decision stays strategist/orchestrator judgment over reported facts. A repeated
acquisition by the same master at the same graph revision is idempotent; a stale-revision blocker
must be released first. Release requires the exact owner, no remaining owned candidates, the
canonical master completion edge, and the landed-series proof; abort requires a canonical
strategist/orchestrator judgment. `_boundary_recovery` names `recovery: worktree_sync` when a
boundary refusal is a stale base (L13-R2), and `_stale_sibling_facts` reports every remaining
candidate whose recorded base pair no longer matches the new source tips after a landing — a
sibling whose contract cannot be read is reported as a `contract-unreadable` fact row, never
silently skipped.

### Conventions

Blocker refusals raise `CloseoutQueueError` with stable status strings; machine-readable facts
ride inside the detail as a sorted JSON object. Private helpers are imported by
`closeout_queue.py` (transitions) and `closeout_queue_lifecycle.py` (recovery/facts helpers).

### Invariants And Boundaries

- The scheduler never admits a second atomic block concurrently.
- Blocker acquisition reports in-flight organizational leafs as facts; it never decides from
  them.
- A normal release requires the completed atomic master to prove one exact landed series; abort
  requires canonical judgment authority.
- Lane ownership follows lane-occupying candidate states only; declaration and certification do
  not own the lane.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies; blocker doctrine is repository-internal.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Acquisition enforces nature, bases, predecessors, a drained lane, and rationale, with structured refusal facts. | `_acquire_blocker` | mcp/src/agents_remember/worktrees/closeout_queue_blocker.py:81-144 |
| Release binds the exact owner, an empty block, master completion, and the landed-series proof. | `_release_blocker` | mcp/src/agents_remember/worktrees/closeout_queue_blocker.py:147-180 |
| Abort requires a canonical strategist/orchestrator judgment row. | `_abort_blocker` | mcp/src/agents_remember/worktrees/closeout_queue_blocker.py:183-205 |
| Refusal payloads carry the blocker owner, lane candidate, and in-flight organizational facts. | `_refusal_facts` | mcp/src/agents_remember/worktrees/closeout_queue_blocker.py:55-64 |
| Stale-base boundary refusals name the sync-first recovery. | `_boundary_recovery` | mcp/src/agents_remember/worktrees/closeout_queue_blocker.py:208-218 |
| Post-landing stale-by-evidence siblings are reported, with unreadable contracts as fact rows. | `_stale_sibling_facts` | mcp/src/agents_remember/worktrees/closeout_queue_blocker.py:221-264 |

## Cross-Repo References

No meaningful cross-repository reference applies.

## Update History

- 2026-08-19T22:32+02:00 — 260815-DAG-L13: created for the atomic-blocker transition extraction
  from `closeout_queue.py` — blocker semantics unchanged except the lane-drain narrowing to
  lane-occupying states and the structured refusal facts; also owns the sync-first boundary
  recovery naming and the stale-by-evidence sibling report. Verification remains closeout-owned.
