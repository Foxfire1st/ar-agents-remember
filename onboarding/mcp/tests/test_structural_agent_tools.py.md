# mcp/tests/test_structural_agent_tools.py

| Field | Value |
|---|---|
| repository | agents-remember |
| path | `mcp/tests/test_structural_agent_tools.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-19T22:32+02:00 |
| lastVerifiedCommitHash |  `3eafc555c848ac45a07a07720641f1735f8df0eb`|
| lastVerifiedCommitDate |  2026-08-21T05:15:52+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Exercises the structural agent service boundary with real sprint/master/leaf task documents,
ambient hosted caller identity, qualified targets, replacement-aware routing, and exact-pinned
dispatch rollback.

## Code Commentary

### Logic

Fixtures materialize task containment and structural catalog seats. Tests cover both directions of
replacement-aware messaging, ambiguity refusal, successful dispatch brief delivery, and rollback
when the exact initial dispatch brief cannot be delivered. The 260821-ARSPAWN-L1 ambient
dispatch cohort (ambient spawn without hosted env, unknown-ref and altitude-mismatch refusals,
plane provenance kept structural, ambient rollback, sender-less brief post) moved VERBATIM into
`test_dispatch_agent_ambient.py` by the leaf's file-size fix (this suite had crossed the
1,200-line rail) — see that suite's card; this file retains the structural messaging, ambiguity,
dispatch-brief, and rollback coverage. Fix round 3 adds two plane-refusal tests pinning the
restructured (ambient-first) caller resolution's fail-closed property: a broken plane identity
refuses (`ambient-seat-stale`) WITHOUT downgrading to ambient, and dispatching a
`system-specialist` child from an architect seat refuses (`structural-child-refused`) — both assert
the spawn primitive is never called.

### Conventions

All task references point at isolated temporary task trees; no test writes candidate schema rows to
the deployed coordination root.

### Invariants And Boundaries

- Tests never identify targets by runtime id through the public operation.
- Both replacement directions remain reachable through the same structural address.
- Ambiguity is a typed failure, never first-match success.
- A child whose initial exact-pinned brief fails is retired before the error escapes.

### Todos

None.

## Docs References


## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixtures create real task containment and structural seats. | `_write_topology` | mcp/tests/test_structural_agent_tools.py:50-132 |
| The suite exercises the structural operation boundary. | `StructuralAgentToolTests` | mcp/tests/test_structural_agent_tools.py:134-241 |
| The restructured caller resolution refuses broken plane identity and unauthorized child roles without downgrading. | `test_plane_dispatch_refuses_broken_plane_identity_without_downgrading`; `test_plane_dispatch_refuses_an_unauthorized_child_role` | mcp/tests/test_structural_agent_tools.py:1040-1058; mcp/tests/test_structural_agent_tools.py:1059-1081 |

## Cross-Repo References


## L23 Final Candidate Disposition

Structural dispatch tests prove curator creation refuses stale lineage or a missing/stale route
review before process creation. Passing evidence is bound by the plane to the exact candidate and
canonical task/role seat, never to a model-supplied runtime id.

## 260815-DAG-L4 Integration-Authority Forcing

This task extends this suite's production-bound fixtures or assertions for task-derived protected-ref ownership, durable closeout/integration authority, external-memory parity, and fail-closed recovery. The suite continues to exercise the real owner named in its existing purpose; the L4 delta adds exact negative or crash/retry evidence rather than a test-only bypass.

## Update History

- 2026-08-21T04:00+02:00 — 260821-ARSPAWN-L1 fix round 4: the unauthorized-child refusal test now dispatches role `system-specialist` (was `worker`) — a portfolio-altitude child from an architect seat refuses `structural-child-refused`; no line-shift impact. Verification metadata pinned until closeout stamps the 260821-ARSPAWN-L1 commit.

- 2026-08-21T03:45+02:00 — 260821-ARSPAWN-L1 fix round 3: added the two plane-refusal tests (broken plane identity refuses `ambient-seat-stale` without downgrading; unauthorized child role refuses `structural-child-refused`), pinning the ambient-first `_resolve_dispatch_caller` restructure. Verification metadata pinned until closeout stamps the 260821-ARSPAWN-L1 commit.

- 2026-08-21T03:15+02:00 — 260821-ARSPAWN-L1 fix round 1: the ambient dispatch cohort moved verbatim out of this suite into the new `test_dispatch_agent_ambient.py` (file-size fix; this file dropped back under the 1,200-line rail); the suite's documented structural coverage is unchanged and its card now points to the new suite's card for the cohort. Verification metadata pinned until closeout stamps the 260821-ARSPAWN-L1 commit.

- 2026-08-21T02:50+02:00 — 260821-ARSPAWN-L1: added the ambient dispatch cohort (6 tests: spawn without hosted env, unknown-ref refusal, altitude-mismatch refusal, plane provenance kept structural, ambient rollback, sender-less brief post). Verification metadata pinned until closeout stamps the 260821-ARSPAWN-L1 commit.

- 2026-08-19T22:32+02:00 — No content impact: 260815-DAG-L13 added isinstance narrowing to the series-bootstrap assertions after `ensure_master_series_contract` gained the lane-blocked result union; documented dispatch/bootstrap behavior is unchanged. Verification remains closeout-owned.

- 2026-08-16T04:06+02:00 — Dagger fixture repair: the orphan organizational-master assertion now expects the exact missing commanding-sprint refusal emitted before atomic bootstrap authority.
- 2026-08-15T23:38+02:00 — Reconciled the suite's L4 fixture and forcing role for protected integration branches, durable operation authority, external-memory parity, and recovery. Verification metadata remains closeout-owned.
- 2026-08-14T06:40+02:00 — L23 final candidate review: structural dispatch forcing cases cover
  canonical task/role authority, current lineage, candidate-bound route review, and refusal before
  curator host creation. Verification remains closeout-owned.

- 2026-08-11T06:47+02:00 — 260731-EFA-L19: created for structural agent-operation regression coverage.
