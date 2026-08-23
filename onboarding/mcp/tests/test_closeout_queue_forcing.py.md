# mcp/tests/test_closeout_queue_forcing.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_closeout_queue_forcing.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-23T16:08+02:00 |
| lastVerifiedCommitHash | `1d446724d099517f6f52d596b47827ae2391a2a4` |
| lastVerifiedCommitDate | 2026-08-24T00:21:10+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Forces the high-risk exactness, locking, recovery, projection, and authority properties that a
happy-path queue suite could otherwise appear to satisfy without exercising production seams.

## Code Commentary

### Logic

Tests mutate full route records/evidence bytes, change graph revisions inside the lock window,
exercise task-tree freeze and atomic-blocker scope, measure the bounded graph helper, reject
malformed durable states, assert actor-exact legal operations, recover queue and sprint-status WAL
crash cuts, prove actor provenance plus the writer census are plane-owned, and force the canonical
task-document identity's runtime bounds without emitting unsupported projection-schema constraints.

### Conventions

Poisoned reads and injected publication failures are placed at the exact seam whose ordering is the
subject of the assertion.

### Invariants And Boundaries

- Evidence equality means byte and canonical-record equality, not summary equality.
- Graph/task publication races are forced under the same lock used in production.
- Own-blocker reopen forcing first advances the organizational super, then rebuilds the atomic
  code and memory source/work pair from that exact tip; own-master success is therefore distinct
  from stale-lineage refusal, while another master remains frozen.
- State and WAL serialization never reveal raw lifecycle operation keys.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Canonical task-document identity is runtime-bounded without an unsupported `maxLength` schema. | `test_task_document_identity_is_runtime_bounded_without_unsupported_schema` | mcp/tests/test_closeout_queue_forcing.py:94-108 |
| Full route records and in-place evidence-byte drift are bound. | `test_full_route_record_and_in_place_evidence_bytes_are_bound` | mcp/tests/test_closeout_queue_forcing.py:110-131 |
| Graph recomputation and lane-owned task-tree freeze are forced under lock. | `test_claim_recomputes_graph_under_lock_and_lane_ownership_freezes_task_tree_writes` | mcp/tests/test_closeout_queue_forcing.py:157-217 |
| Graph admission and predecessor indexing are bounded. | `test_predecessor_index_is_linear_and_node_edge_admission_is_bounded` | mcp/tests/test_closeout_queue_forcing.py:219-290 |
| Projection names only operations legal for the current actor. | `test_projection_names_only_operations_the_candidate_can_take` | mcp/tests/test_closeout_queue_forcing.py:433-531 |
| WAL recovery is idempotent and raw operation keys never persist. | `test_wal_recovery_after_publish_is_idempotent_and_private_keys_never_persist` | mcp/tests/test_closeout_queue_forcing.py:553-579 |
| Sprint completion/reopen crash cuts recover through their WAL. | `test_sprint_status_wal_recovers_before_after_and_reopen_crash_cuts` | mcp/tests/test_closeout_queue_forcing.py:581-674 |

## Cross-Repo References

No meaningful cross-repository reference applies.

## 260815-DAG Master Full-Gate Repair

The 260815-DAG master full-gate repair moved this suite's imports under the restructured packages
(`application/task_docs/`, `models/queue/`, `worktrees/queue/`, `worktrees/integration/`) and
removed the `__main__` runner. The queue WAL crash-cut recovery proof now wraps `fixture.status()`
in a `CloseoutQueueStore._publish` patch with `fail_after_task_publication`, so the recovery
republish resolves through the closure to `original_publish` rather than calling the patched method.

## 260821-CLIVE-L1 Fixture Migration

Queue-forcing cases now publish contracts and closeouts through the canonical typed input/admission support. The tested task-tree and blocker behavior is otherwise unchanged. This migration preserves the boundary that scheduler projection consumes completed lifecycle facts but never validates or retains commit-message intent.

## 260821-CLIVE-L2 Current Regression Contract

The current forcing seams include `test_task_document_identity_is_runtime_bounded_without_unsupported_schema`, `test_full_route_record_and_in_place_evidence_bytes_are_bound`, `test_graph_revision_and_transitive_source_lineage_recompute_before_closeout`, `test_claim_recomputes_graph_under_lock_and_lane_ownership_freezes_task_tree_writes`. The historical test names expose the pre-L3 freeze/queue contract still present in this candidate. L2 moves operation recovery to the journal; L3 must replace the queue/task freeze semantics and their tests.

### Reconciled Source Evidence

| Finding | Citations | Source Path |
| --- | --- | --- |
| The current test source exercises `test_task_document_identity_is_runtime_bounded_without_unsupported_schema`, `test_full_route_record_and_in_place_evidence_bytes_are_bound`, `test_graph_revision_and_transitive_source_lineage_recompute_before_closeout`, `test_claim_recomputes_graph_under_lock_and_lane_ownership_freezes_task_tree_writes`. | L94-L108; L110-L131; L133-L155; L157-L217 | `mcp/tests/test_closeout_queue_forcing.py` |

## Update History

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this test card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: curated relationship changes against accepted candidate tree `4241908c`; verification metadata remains pinned until governed closeout.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: imports follow the package moves
  (`application/task_docs/`, `models/queue/`, `worktrees/queue/`, `worktrees/integration/`); the WAL
  crash-cut proof patches `CloseoutQueueStore._publish` so recovery republishes through the closure
  to `original_publish`; the `__main__` runner was removed. Verified at code commit e5cb139f.


- 2026-08-20T09:35+02:00 — 260815-DAG-L16: seat-path regressions preserved (renamed forcing
  suite); the ambient declared-caller path is covered by the new
  `test_seat_independent_execution.py`. Verified at code commit a9d50e08.


- 2026-08-20T05:14+02:00 — L11 landed-wave refresh: the leaf-segment graph-model commit (f2e2f4b9)
  touched this source; card re-verified against the current file, verification stamp advanced to
  f2e2f4b9, shifted test-name citation ranges re-pinned. Body unchanged.


- 2026-08-18T09:05+02:00 — Renamed the atomic 'barrier' concept to 'blocker' throughout (terminology unification; no behavioral change). Verification remains closeout-owned.

- 2026-08-16T05:18+02:00 — Dagger fixture repair: the legal-operation projection completes its certified closeout lifecycle before opening integration, preserving the per-contract lease while reaching the intended queue projection state.
- 2026-08-16T04:06+02:00 — Dagger fixture repair: closeout and integration lifecycle inputs use the QueueFixture workspace configuration rather than a nonexistent coordination-local settings file.
- 2026-08-16T02:51+02:00 — L4 blocker/lineage repair: rebuilt the owning atomic pair after the
  super advance so the test isolates own-master reopen authority from stale source lineage while
  retaining the other-master refusal.

- 2026-08-15T12:53+02:00 — L3 targeted-gate repair: extended the ambient failure, unbound
  application-wrapper, exact actor projection, crash-cut, and writer-ownership forcing while the
  focused unit suites own individual branch matrices.
- 2026-08-15T09:53+02:00 — No content impact: L3's Pyright repair validates raw graph fixtures at
  their Pydantic boundary; the linear-scaling and admission-limit assertions are unchanged.
- 2026-08-15T09:36+02:00 — L3 fast-hook repair: added the boundary test for oversized canonical
  task refs and the deliberate absence of unrenderable `maxLength` schema keywords.
- 2026-08-15T09:10+02:00 — Created for L3's adversarial queue forcing suite; verification remains closeout-owned.
