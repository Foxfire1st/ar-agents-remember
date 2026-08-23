# mcp/src/agents_remember/worktrees/queue

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `mcp/src/agents_remember/worktrees/queue` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-08-24T00:27+02:00 |
| lastVerifiedCommitHash | `1d446724d099517f6f52d596b47827ae2391a2a4` |
| lastVerifiedCommitDate | 2026-08-24T00:21:10+02:00 |
| governingOverview | `../../../../overview.md` |

## Governing Overview

[mcp overview](../../../../overview.md)

## Purpose

The closeout-queue mechanism package (260815-DAG master full-gate repair): `closeout_queue.py` and
its helpers moved here from `worktrees/` (flat) / `worktrees/modules/`. In the L2 candidate this
route is transitional: scheduling and remaining closeout claim/certification code still live here,
while canonical operation recovery and durable lifecycle evidence have moved to the root journal.
`closeout_queue_state.py` now isolates the pure current action vocabulary, initial-state constructor,
and actor-bound request fingerprint from persistence and transition code.

## Hot Path Summary

This route still owns the pre-L3 queue projection, including selected/in-flight/certified states,
closeout claim/certification, exact commit comparisons, and narrow scheduling serialization. L2
removes queue authority from the new retry/recover/cancel/revise and worker/direct-landing paths,
but it does not yet make this package waiting-only.

Closeout operations claim/publish queue candidates through the queue store; the lifecycle module
certifies and claims candidates for closeout; `closeout_staged_quality` gates staged code. The
application `closeout_queue.py` and the `worktrees/modules/*` operations consume this package.

## Conventions

- Queue errors carry `task-closeout-queue-*` / `task-sprint-linkage-*` typed statuses.
- The queue remains a bounded, evictable mechanism; the closeout register/sections stay canonical.

## Invariants And Boundaries

- Only the queue mechanism lives here; application entry points (`application/closeout_queue.py`)
  and models (`models/queue/`) are separate.
- The staged-quality gate refuses without a Dagger-certified candidate; no host fallback.

## 260821-CLIVE-L1 Preview And Recovery Boundary

This route's closeout preview renders the already-normalized effective plan and includes messages only for enabled legs. Its recovery helper brackets code and ledger Git mutations with journal intent/proof and treats verified-existing commits as projection facts, not fabricated mutations. These helpers do not make the scheduling queue an owner of input, commit evidence, operation generations, or lifecycle state; the queue redesign remains L3.

## 260821-CLIVE-L2 Current Architecture

Queue state may still select and certify a candidate whose exact door and commits agree. Operation recovery, cancellation, worker termination, direct landing, and legacy repair now live in the root journal/integration route, and journal claim transfer removes the new integration operation's dependence on later queue reads. The remaining lifecycle-shaped queue schema is transitional current source, not the target architecture; L3 removes it and owns task-change invalidation plus waiting-only rebuild.

The extracted pure state helper still names selection, grading/admission, and blocker actions because those are present L2 facts. Its existence must not be read as approval of those actions for the L3 queue; task authoring remains upstream of the planned invalidation/rebuild projection.

### Reconciled Source Evidence

| Finding | Citations | Source Path |
| --- | --- | --- |
| Door-gated candidate evidence. | L35-L43; L46-L137 | `mcp/src/agents_remember/worktrees/queue/closeout_queue_door.py` |
| Scheduling-only lifecycle correlation. | L389-L422; L425-L507 | `mcp/src/agents_remember/worktrees/queue/closeout_queue_lifecycle.py` |
| Pure current action validation, revision-zero construction, and actor-bound request fingerprinting. | L18-L40; L43-L66 | `mcp/src/agents_remember/worktrees/queue/closeout_queue_state.py` |

## Update History

- 2026-08-24T00:27+02:00 — 260821-CLIVE-L2 committed-route reconciliation: documented `closeout_queue_state.py` while preserving the explicit current-L2 versus waiting-only-L3 boundary, and verified the governed route at code commit `1d446724d099517f6f52d596b47827ae2391a2a4`.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: refreshed current route intent and source evidence for the accepted full L2 candidate; verification provenance and contract-scoped quality enforcement remain architect-closeout-owned.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: route claims reconciled to accepted candidate tree `4241908c`; verification metadata remains closeout-owned.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: created the `worktrees/queue` route —
  ten modules moved from `worktrees/` (flat) and `worktrees/modules/`. Verified at code commit
  e5cb139f.
