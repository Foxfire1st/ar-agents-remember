# mcp/src/agents_remember/worktrees/queue/closeout_projection_members.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/queue/closeout_projection_members.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-26T08:25+02:00 |
| lastVerifiedCommitHash |  `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d`|
| lastVerifiedCommitDate |  2026-08-26T08:10:26+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Closeout queue overview](overview.md)

## Purpose

Computes candidate-local readiness, dependency order, and stable source fingerprints for projection members.

## Code Commentary

### Logic

It combines task completion blockers, door admission reasons, candidate-local activation waits,
authored dependency ordering, and topology/file digests into one bounded member record. A graph-less
sprint adds no synthetic contract-census ordering reason; source-pair activation already says
whether this exact master is selected, paused, or still reconciling.

### Conventions

Typed records and refusal payloads remain owned at the narrowest stable boundary. Callers consume
the public function or model instead of re-deriving its lower-level state machine.

### Invariants And Boundaries

- Readiness follows current task truth and door identity; every waiting reason is bounded and attributable; planning edits require recomputation, not task locking.
- `activation_waiting` is an explicit input supplied by selector observation. This module never
  selects a master or reconstructs an owner from live contract presence.
- Without an authored graph, dependency waiting is empty; the removed global
  `atomic-series-lane-owned-by` fallback must not return.
- Missing, unreadable, ambiguous, or conflicting authority fails loudly; this file does not add a
  fallback or compatibility shadow.

### Todos

None recorded.

## Docs References

The configured Domain Documentation registry is empty. No external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain source is required to establish this repository-owned implementation. | `ProjectionMemberContext` | mcp/src/agents_remember/worktrees/queue/closeout_projection_members.py:1-234 |

## Repo-Internal References

The source file is the direct evidence for this unit; its governing overview records adjacent owners.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's concrete API, control flow, and validation boundary are implemented here. | `ProjectionMemberContext` | mcp/src/agents_remember/worktrees/queue/closeout_projection_members.py:1-234 |
| Candidate-local activation waits are combined with door admission before optional DAG waits. | `projection_member`; `_admission_waiting_reasons` | mcp/src/agents_remember/worktrees/queue/closeout_projection_members.py:37-60; mcp/src/agents_remember/worktrees/queue/closeout_projection_members.py:93-100 |

## Cross-Repo References

No cross-repository source is allowed by the resolved settings, and this unit owns no external
protocol claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repository reference applies. | `ProjectionMemberContext` | mcp/src/agents_remember/worktrees/queue/closeout_projection_members.py:1-234 |

## Update History

- 2026-08-26T08:25+02:00 — Rebound the three full-module citations to the frozen 234-line source;
  no semantic claim changed.

- 2026-08-26T03:37+02:00 — Replaced sequential contract-census owner fields with explicit
  candidate-local activation waits and removed graph-less synthetic lane ordering. Verification
  remains post-Dagger/closeout-owned.

- 2026-08-25T15:44+02:00 — Created during PDLS whole-system reconciliation after source and
  requirement review. Verification remains closeout-owned.