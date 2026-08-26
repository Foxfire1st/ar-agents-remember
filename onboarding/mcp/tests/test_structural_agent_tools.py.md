# mcp/tests/test_structural_agent_tools.py

| Field | Value |
|---|---|
| repository | agents-remember |
| path | `mcp/tests/test_structural_agent_tools.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-26T06:45+02:00 |
| lastVerifiedCommitHash | `c51373425be3e3f488590ad2f444810df89b4ffb` |
| lastVerifiedCommitDate | 2026-08-26T19:22:10+02:00|
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

The atomic-series bootstrap repository fixture seeds external `memory.md` with the current
`ar/super` code-tip mapping. Its partial-bootstrap restart case advances both protected source
tips, then seeds the newly advanced code tip into the memory ledger before retrying. The case
therefore exercises fresh paired-source recovery rather than constructing a mid-cycle pair that
correct admission must refuse.

### Conventions

All task references point at isolated temporary task trees; no test writes candidate schema rows to
the deployed coordination root.

### Invariants And Boundaries

- Tests never identify targets by runtime id through the public operation.
- Both replacement directions remain reachable through the same structural address.
- Ambiguity is a typed failure, never first-match success.
- A child whose initial exact-pinned brief fails is retired before the error escapes.
- Atomic manager and worker seats are spawned only after the owning master is observed active; a
  released parent is reselected before worker spawn.
- Missing sprint integrationBranch, invalid manager altitude, and missing repository surface as
  `series-admission-refused` and never reach process spawn.
- A successful paired-source bootstrap fixture must map the exact admitted code tip at the
  admitted external-memory tip; advancing two repositories independently is not sufficient.

### Todos

None.

## Docs References


## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixtures create real task containment and structural seats. | `_write_topology` | mcp/tests/test_structural_agent_tools.py:86-137 |
| The suite exercises the structural operation boundary. | `StructuralAgentToolTests` | mcp/tests/test_structural_agent_tools.py:164-1090 |
| The restructured caller resolution refuses broken plane identity and unauthorized child roles without downgrading. | `test_plane_dispatch_refuses_broken_plane_identity_without_downgrading`; `test_plane_dispatch_refuses_an_unauthorized_child_role` | mcp/tests/test_structural_agent_tools.py:1140-1157; mcp/tests/test_structural_agent_tools.py:1159-1180 |

## Cross-Repo References


## L23 Final Candidate Disposition

Structural dispatch tests prove curator creation refuses stale lineage or a missing/stale route
review before process creation. Passing evidence is bound by the plane to the exact candidate and
canonical task/role seat, never to a model-supplied runtime id.

## 260815-DAG-L4 Integration-Authority Forcing

This task extends this suite's production-bound fixtures or assertions for task-derived protected-ref ownership, durable closeout/integration authority, external-memory parity, and fail-closed recovery. The suite continues to exercise the real owner named in its existing purpose; the L4 delta adds exact negative or crash/retry evidence rather than a test-only bypass.

## 260821-CLIVE-L2 Current Regression Contract

The current forcing seams include `test_child_to_replacement_parent_is_resolved_by_task_containment`, `test_parent_to_replacement_child_is_resolved_by_document_and_role`, `test_duplicate_current_occupants_fail_closed`, `test_curator_dispatch_refuses_before_spawn_without_leaf_review_contract`. The L2 additions prove structural/task publication serialization without a global queue/lifecycle authoring lock and keep public control/gate identity task-addressed.

### Reconciled Source Evidence

| Finding | Anchor | Source |
| --- | --- | --- |
| The current test source exercises `test_child_to_replacement_parent_is_resolved_by_task_containment`, `test_parent_to_replacement_child_is_resolved_by_document_and_role`, `test_duplicate_current_occupants_fail_closed`, `test_curator_dispatch_refuses_before_spawn_without_leaf_review_contract`. | `test_child_to_replacement_parent_is_resolved_by_task_containment`; `test_parent_to_replacement_child_is_resolved_by_document_and_role`; `test_duplicate_current_occupants_fail_closed`; `test_curator_dispatch_refuses_before_spawn_without_leaf_review_contract` | mcp/tests/test_structural_agent_tools.py:186-211; mcp/tests/test_structural_agent_tools.py:213-237; mcp/tests/test_structural_agent_tools.py:239-245; mcp/tests/test_structural_agent_tools.py:247-265 |

## 260821-ARSPAWN-L2 Transaction Boundary Coverage

Replacement-aware message tests prove that durable envelopes contain only the canonical document
and role, then reach the replacement through delivery-time resolution. Failed-briefing tests
prove that rollback requires faithful plane provenance and positive no-brief evidence for the
matching private generation; unknown evidence refuses without cleanup. The rollback directly
uses transaction authority and does not invoke public retire policy.

## Update History

- 2026-08-26T12:30+02:00 — Reconciled ARSPAWN-L2 address-only replacement messaging and private,
  evidence-gated rollback forcing onto the IAS test card. No certifying test execution is
  claimed.

- 2026-08-26T06:45+02:00 — Corrected the partial-bootstrap forcing world to seed the fresh code
  tip into the canonical memory ledger before retrying paired-source admission. This records source
  shape only and makes no Dagger/test-execution claim.

- 2026-08-26T03:37+02:00 — Extended structural forcing from manager bootstrap to manager and
  worker source-pair admission. Tests observe active selection inside the spawn seam and retain
  fail-before-spawn refusal checks. Verification remains post-Dagger/closeout-owned.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this test card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

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
