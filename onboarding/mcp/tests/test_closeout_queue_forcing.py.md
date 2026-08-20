# mcp/tests/test_closeout_queue_forcing.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_closeout_queue_forcing.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated            | 2026-08-20T05:14+02:00 |
| lastVerifiedCommitHash | `f2e2f4b9c18d89cc0f5c901f43831e014701aae0` |
| lastVerifiedCommitDate | 2026-08-19T11:32:36+02:00|
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
| Canonical task-document identity is runtime-bounded without an unsupported `maxLength` schema. | `test_task_document_identity_is_runtime_bounded_without_unsupported_schema` | mcp/tests/test_closeout_queue_forcing.py:79-93 |
| Full route records and in-place evidence-byte drift are bound. | `test_full_route_record_and_in_place_evidence_bytes_are_bound` | mcp/tests/test_closeout_queue_forcing.py:95-116 |
| Graph recomputation and lane-owned task-tree freeze are forced under lock. | `test_claim_recomputes_graph_under_lock_and_lane_ownership_freezes_task_tree_writes` | mcp/tests/test_closeout_queue_forcing.py:115-176 |
| Graph admission and predecessor indexing are bounded. | `test_predecessor_index_is_linear_and_node_edge_admission_is_bounded` | mcp/tests/test_closeout_queue_forcing.py:177-243 |
| Projection names only operations legal for the current actor. | `test_projection_names_only_operations_the_candidate_can_take` | mcp/tests/test_closeout_queue_forcing.py:356-432 |
| WAL recovery is idempotent and raw operation keys never persist. | `test_wal_recovery_after_publish_is_idempotent_and_private_keys_never_persist` | mcp/tests/test_closeout_queue_forcing.py:507-533 |
| Sprint completion/reopen crash cuts recover through their WAL. | `test_sprint_status_wal_recovers_before_after_and_reopen_crash_cuts` | mcp/tests/test_closeout_queue_forcing.py:481-570 |

## Cross-Repo References

No meaningful cross-repository reference applies.

## Update History

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
