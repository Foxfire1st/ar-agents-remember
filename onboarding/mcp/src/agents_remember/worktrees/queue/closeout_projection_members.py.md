# mcp/src/agents_remember/worktrees/queue/closeout_projection_members.py

## Governing Overview

[Closeout queue overview](overview.md)

## Purpose

Computes candidate-local readiness, dependency order, and stable source fingerprints for projection members.

## Code Commentary

### Logic

It combines task completion blockers, door admission reasons, candidate-local activation waits,
authored dependency ordering, and explicit source-plane digests into one bounded member record. A graph-less
sprint adds no synthetic contract-census ordering reason; the addressed contract's own activation
record already says whether it is vacant, still reconciling, or active — and because activation is
keyed per series contract, no foreign master's state contributes a waiting reason here.

Candidate topology identity is owned by `tasks.semantic_topology`: this module adapts the shared
`QueueGraphContext` to `semantic-topology/v2`, translates typed domain refusals without losing status
or detail, and consumes the fingerprint already computed for the member. It no longer hashes the
whole candidate document or maintains a queue-private v1 identity.

Since 260831-CCR (commit `99dc249b`) the member context carries the candidate's canonical
task-intent identity (`ProjectionMemberContext.task_intent`, line 45) and `_projection_blockers`
(line 79-99) adds two door-currentness reasons beside topology staleness:
`door-task-intent-unavailable` when the door's `taskIntent` is not a `TaskIntentIdentity`
(line 88) and `door-task-intent-stale` when the door binds a different intent than the member's
current canonical one (line 89) — mirroring the shared currentness rule: intent absence or a
meaning change stales scheduling readiness without making the queue the intent authority.

### Conventions

Typed records and refusal payloads remain owned at the narrowest stable boundary. Callers consume
the public function or model instead of re-deriving its lower-level state machine.

### Invariants And Boundaries

- Readiness follows current task truth and door identity; every waiting reason is bounded and attributable; planning edits require recomputation, not task locking.
- `activation_waiting` is an explicit input supplied by selector observation. This module never
  selects a master or reconstructs an owner from live contract presence.
- Without an authored graph, dependency waiting is empty; the removed global
  `atomic-series-lane-owned-by` fallback must not return.
- Topology identity is exactly `semantic-topology/v2`; no whole-document or v1 fallback is accepted.
- A member whose door intent is missing or stale reports the exact `door-task-intent-*` reason;
  the queue never mints a digest or infers intent from prose.
- Missing, unreadable, ambiguous, or conflicting authority fails loudly; this file does not add a
  fallback or compatibility shadow.

### Todos

None recorded.

## Evidence

### Docs References

The configured Domain Documentation registry is empty. No external documentation claim is made.

- No external domain source is required to establish this repository-owned implementation. [1]

### Repo-Internal References

The source file is the direct evidence for this unit; its governing overview records adjacent owners.

- Member construction consumes an exact precomputed topology fingerprint and the typed bound graph context. [2]
- Candidate-local activation waits are combined with door admission before optional DAG waits. [3]
- Queue adapters delegate v2 projection/fingerprinting and preserve typed domain refusals. [4]
- Door intent absence/staleness become explicit member blockers. [5]

### Cross-Repo References

No cross-repository source is allowed by the resolved settings, and this unit owns no external
protocol claim.

- No meaningful cross-repository reference applies. [6]

## CCR-R02@v2 Door-Intent Member Readiness

Per `requirements/CCR-R02-v2-normative-task-intent-identity.md`, evidence must become stale when
meaning changes. `_projection_blockers` surfaces that rule as `door-task-intent-unavailable`
and `door-task-intent-stale`, so a door bound to missing or different intent blocks scheduling
readiness exactly, without the queue becoming an intent authority. Part of the landed L25 candidate
`99dc249b`.
