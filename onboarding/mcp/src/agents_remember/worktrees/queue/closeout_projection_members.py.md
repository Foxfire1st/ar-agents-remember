# mcp/src/agents_remember/worktrees/queue/closeout_projection_members.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/queue/closeout_projection_members.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `99dc249bd507c20b09ece1169c2b1fa2af8e8c1b` |
| lastVerifiedCommitDate | 2026-09-02T05:53:10+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Closeout queue overview](overview.md)

## Purpose

Computes candidate-local readiness, dependency order, and stable source fingerprints for projection members.

## Code Commentary

### Logic

It combines task completion blockers, door admission reasons, candidate-local activation waits,
authored dependency ordering, and explicit source-plane digests into one bounded member record. A graph-less
sprint adds no synthetic contract-census ordering reason; source-pair activation already says
whether this exact master is selected, paused, or still reconciling.

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

## Docs References

The configured Domain Documentation registry is empty. No external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain source is required to establish this repository-owned implementation. | `ProjectionMemberContext` | mcp/src/agents_remember/worktrees/queue/closeout_projection_members.py:1-260 |

## Repo-Internal References

The source file is the direct evidence for this unit; its governing overview records adjacent owners.

| Finding | Anchor | Source |
| --- | --- | --- |
| Member construction consumes an exact precomputed topology fingerprint and the typed bound graph context. | `projection_member` | mcp/src/agents_remember/worktrees/queue/closeout_projection_members.py:35-72 |
| Candidate-local activation waits are combined with door admission before optional DAG waits. | `projection_member`; `_admission_waiting_reasons` | mcp/src/agents_remember/worktrees/queue/closeout_projection_members.py:48-72; mcp/src/agents_remember/worktrees/queue/closeout_projection_members.py:99-107 |
| Queue adapters delegate v2 projection/fingerprinting and preserve typed domain refusals. | `candidate_task_topology_fingerprint`; `semantic_topology_projection` | mcp/src/agents_remember/worktrees/queue/closeout_projection_members.py:184-226 |
| Door intent absence/staleness become explicit member blockers. | `ProjectionMemberContext.task_intent`; `_projection_blockers` | mcp/src/agents_remember/worktrees/queue/closeout_projection_members.py:45-45; mcp/src/agents_remember/worktrees/queue/closeout_projection_members.py:79-99 |

## Cross-Repo References

No cross-repository source is allowed by the resolved settings, and this unit owns no external
protocol claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repository reference applies. | `ProjectionMemberContext` | mcp/src/agents_remember/worktrees/queue/closeout_projection_members.py:1-260 |

## CCR-R02@v2 Door-Intent Member Readiness

Per `requirements/CCR-R02-v2-normative-task-intent-identity.md`, evidence must become stale when
meaning changes. `_projection_blockers` surfaces that rule as `door-task-intent-unavailable`
and `door-task-intent-stale`, so a door bound to missing or different intent blocks scheduling
readiness exactly, without the queue becoming an intent authority. Part of the landed L25 candidate
`99dc249b`.

## Update History

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for 99dc249bd507 (CCR-R02@v2/L25):
  the member readiness projection now binds the leaf's canonical task-intent identity and reports
  `door-task-intent-unavailable`/`door-task-intent-stale` member blockers. Verified at code
  commit 99dc249bd507c20b09ece1169c2b1fa2af8e8c1b.

- 2026-09-01T03:58+02:00 — Checklist follow-up: re-read the structurally changed member context,
  retained its exact claim/range, and anchored the row on the stable construction function while
  leaving commit verification to closeout.

- 2026-09-01T03:58+02:00 — 260831-CCR-L01 Attempt 8: replaced the queue-private whole-document
  topology digest with the task-domain `semantic-topology/v2` owner, bound graph index, and exact
  typed error translation. Verification remains closeout-owned.

- 2026-08-26T08:25+02:00 — Rebound the three full-module citations to the frozen 234-line source;
  no semantic claim changed.

- 2026-08-26T03:37+02:00 — Replaced sequential contract-census owner fields with explicit
  candidate-local activation waits and removed graph-less synthetic lane ordering. Verification
  remains post-Dagger/closeout-owned.

- 2026-08-25T15:44+02:00 — Created during PDLS whole-system reconciliation after source and
  requirement review. Verification remains closeout-owned.
