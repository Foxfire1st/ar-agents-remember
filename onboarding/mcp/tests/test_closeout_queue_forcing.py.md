# mcp/tests/test_closeout_queue_forcing.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_closeout_queue_forcing.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-15T12:53+02:00 |
| lastVerifiedCommitHash | `17987fa66a642306eb8d20fa9a4bff2b881550d2` |
| lastVerifiedCommitDate | 2026-08-15T14:36:30+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Forces the high-risk exactness, locking, recovery, projection, and authority properties that a
happy-path queue suite could otherwise appear to satisfy without exercising production seams.

## Code Commentary

### Logic

Tests mutate full route records/evidence bytes, change graph revisions inside the lock window,
exercise task-tree freeze and atomic-barrier scope, measure the bounded graph helper, reject
malformed durable states, assert actor-exact legal operations, recover queue and sprint-status WAL
crash cuts, prove actor provenance plus the writer census are plane-owned, and force the canonical
task-document identity's runtime bounds without emitting unsupported projection-schema constraints.

### Conventions

Poisoned reads and injected publication failures are placed at the exact seam whose ordering is the
subject of the assertion.

### Invariants And Boundaries

- Evidence equality means byte and canonical-record equality, not summary equality.
- Graph/task publication races are forced under the same lock used in production.
- State and WAL serialization never reveal raw lifecycle operation keys.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Canonical task-document identity is runtime-bounded without an unsupported `maxLength` schema. | `test_task_document_identity_is_runtime_bounded_without_unsupported_schema` | mcp/tests/test_closeout_queue_forcing.py:61-78 |
| Full route records and in-place evidence-byte drift are bound. | `test_full_route_record_and_in_place_evidence_bytes_are_bound` | mcp/tests/test_closeout_queue_forcing.py:69-91 |
| Graph recomputation and lane-owned task-tree freeze are forced under lock. | `test_claim_recomputes_graph_under_lock_and_lane_ownership_freezes_task_tree_writes` | mcp/tests/test_closeout_queue_forcing.py:115-176 |
| Graph admission and predecessor indexing are bounded. | `test_predecessor_index_is_linear_and_node_edge_admission_is_bounded` | mcp/tests/test_closeout_queue_forcing.py:177-243 |
| Projection names only operations legal for the current actor. | `test_projection_names_only_operations_the_candidate_can_take` | mcp/tests/test_closeout_queue_forcing.py:356-432 |
| WAL recovery is idempotent and raw operation keys never persist. | `test_wal_recovery_after_publish_is_idempotent_and_private_keys_never_persist` | mcp/tests/test_closeout_queue_forcing.py:453-480 |
| Sprint completion/reopen crash cuts recover through their WAL. | `test_sprint_status_wal_recovers_before_after_and_reopen_crash_cuts` | mcp/tests/test_closeout_queue_forcing.py:481-570 |

## Cross-Repo References

No meaningful cross-repository reference applies.

## Update History

- 2026-08-15T12:53+02:00 — L3 targeted-gate repair: extended the ambient failure, unbound
  application-wrapper, exact actor projection, crash-cut, and writer-ownership forcing while the
  focused unit suites own individual branch matrices.
- 2026-08-15T09:53+02:00 — No content impact: L3's Pyright repair validates raw graph fixtures at
  their Pydantic boundary; the linear-scaling and admission-limit assertions are unchanged.
- 2026-08-15T09:36+02:00 — L3 fast-hook repair: added the boundary test for oversized canonical
  task refs and the deliberate absence of unrenderable `maxLength` schema keywords.
- 2026-08-15T09:10+02:00 — Created for L3's adversarial queue forcing suite; verification remains closeout-owned.
