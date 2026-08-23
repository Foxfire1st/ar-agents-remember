# mcp/tests/test_closeout_queue.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_closeout_queue.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-23T16:08+02:00 |
| lastVerifiedCommitHash | `1d446724d099517f6f52d596b47827ae2391a2a4` |
| lastVerifiedCommitDate | 2026-08-24T00:21:10+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Exercises the closeout queue's model, authority, ordering, evidence, transition, durability,
capacity, projection-cost, and sprint-publication contracts against real task and Git fixtures.
The small model and split-evidence ownership checks live in `test_closeout_queue_models.py` so this
behavior suite remains below the repository hard size limit.

## Code Commentary

### Logic

`QueueFixture` constructs canonical sprint/master/leaf task documents, contracts, curator artifacts,
register rows, repositories, and ledger facts. Tests cover categorical grading and deterministic
ties, internal/disabled memory, request bounds, authority refusal, predecessor/blocker logistics,
candidate/evidence drift, lifecycle ownership, WAL retry receipts, state bounds, linear fleet work,
cross-sprint refusal, and completion/reopen locking.

### Conventions

The suite manipulates the public service and durable store with production-shaped artifacts; exact
failure states are asserted rather than inferred from source strings.

### Invariants And Boundaries

- Judgment and logistics tests remain separate.
- Negative cases mutate one candidate fact at a time.
- Scaling tests compare two fleet sizes and enforce explicit caps.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Core queue tests cover categorical ordering and graph/leaf ties. | `test_explicit_grades_order_ready_candidates_by_graph_then_leaf_tie` | mcp/tests/test_closeout_queue.py:618-639 |
| Internal and disabled memory modes use explicit not-applicable readiness. | `test_internal_and_disabled_memory_modes_use_explicit_not_applicable_readiness` | mcp/tests/test_closeout_queue.py:648-661 |
| Blocker and predecessor logistics remain separate from scheduling judgment. | `test_predecessors_and_atomic_blocker_control_logistics_not_judgment` | mcp/tests/test_closeout_queue.py:717-759 |
| Candidate/evidence drift fails closed. | `test_candidate_and_evidence_drift_fail_closed` | mcp/tests/test_closeout_queue.py:797-806 |
| WAL publication retry and request receipts are exercised behaviorally. | `test_mutations_require_stable_request_id_and_retry_after_wal_publish` | mcp/tests/test_closeout_queue.py:925-967 |
| Sprint completion publication is serialized with queue quiescence. | `test_sprint_completion_publication_is_serialized_with_queue_quiescence` | mcp/tests/test_closeout_queue.py:1113-1142 |
| Segment-graph queue scheduling and leaf-placement fact reporting split out under the file-size rail. | `SegmentGraphQueueTests` | mcp/tests/test_closeout_queue_segments.py:17-106 |

## Cross-Repo References

No meaningful cross-repository reference applies.

## 260815-DAG-L4 Integration-Authority Forcing

This task extends this suite's production-bound fixtures or assertions for task-derived protected-ref ownership, durable closeout/integration authority, external-memory parity, and fail-closed recovery. The suite continues to exercise the real owner named in its existing purpose; the L4 delta adds exact negative or crash/retry evidence rather than a test-only bypass.

## 260821-CLIVE-L2 Current Regression Contract

The current forcing seams include `test_explicit_grades_order_ready_candidates_by_graph_then_leaf_tie`, `test_ungraded_candidates_are_visible_but_cannot_be_selected`, `test_internal_and_disabled_memory_modes_use_explicit_not_applicable_readiness`, `test_request_shape_and_persisted_text_are_bounded`. This suite still exercises the transitional pre-L3 queue schema. L2's root journal owns the new recovery controls, but the tests do not prove a waiting-only queue; L3 owns that schema reduction.

### Reconciled Source Evidence

| Finding | Citations | Source Path |
| --- | --- | --- |
| The current test source exercises `test_explicit_grades_order_ready_candidates_by_graph_then_leaf_tie`, `test_ungraded_candidates_are_visible_but_cannot_be_selected`, `test_internal_and_disabled_memory_modes_use_explicit_not_applicable_readiness`, `test_request_shape_and_persisted_text_are_bounded`. | L618-L639; L641-L646; L648-L661; L663-L698 | `mcp/tests/test_closeout_queue.py` |

## Update History

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this test card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-19T22:32+02:00 — 260815-DAG-L13: the removed `require_queue_candidate_current` import and
  its direct drift-test call are gone; the atomic-release mock re-points to
  `closeout_queue_blocker.require_atomic_master_landed` after the blocker extraction. No scenario
  changed. Verification remains closeout-owned.

- 2026-08-19T08:55+02:00 — 260815-DAG-L11: the segment-graph queue scenarios moved to
  `test_closeout_queue_segments.py` under the file-size rail (fixtures imported from here);
  `QueueFixture` gains segment helpers. Verification remains closeout-owned.

- 2026-08-18T09:05+02:00 — Renamed the atomic 'barrier' concept to 'blocker' throughout (terminology unification; no behavioral change). Verification remains closeout-owned.

- 2026-08-16T04:06+02:00 — Dagger fixture repair: `QueueFixture` now publishes the real runtime configuration at the workspace-owned path consumed by lifecycle operation inputs.
- 2026-08-15T23:38+02:00 — Reconciled the suite's L4 fixture and forcing role for protected integration branches, durable operation authority, external-memory parity, and recovery. Verification metadata remains closeout-owned.

- 2026-08-15T14:05+02:00 — L3 final targeted-gate repair: shared queue fixtures now render the
  exact canonical Judgment and Priority Register headings, headers, separators, and rows consumed
  by production rather than relying on width-shaped Markdown fragments.
- 2026-08-15T12:53+02:00 — L3 targeted-gate repair: the atomic-series success fixture now proves
  explicit approved human review, preserving its intended all-prerequisites landing path.
- 2026-08-15T11:07+02:00 — L3 Dagger repair: made task rows canonical Markdown refs, stopped the
  negative grade fixture from healing its own corruption, restored exact tree-drift assertions,
  kept persistence-size forcing stable, and moved commit binding to the integration suite.
- 2026-08-15T10:24+02:00 — L3 file-size repair: moved the two small model/ownership checks into
  `test_closeout_queue_models.py`; the fixture and all queue behavior scenarios remain here.
- 2026-08-15T10:10+02:00 — L3 targeted-gate repair: imported the two split evidence modules
  directly and asserted their public owners are callable, allowing deterministic gate-scope
  derivation to select this existing behavior suite.
- 2026-08-15T09:53+02:00 — No content impact: L3's Pyright repair makes fixture model-validation
  boundaries and external-memory narrowing explicit; the queue scenarios, failure injection, and
  assertions are unchanged.
- 2026-08-15T09:10+02:00 — Created for L3's primary queue behavior and durability suite; verification remains closeout-owned.
