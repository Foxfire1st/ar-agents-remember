# mcp/tests/test_organizational_completion_recovery_edges.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_organizational_completion_recovery_edges.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-23T16:08+02:00 |
| lastVerifiedCommitHash | `1d446724d099517f6f52d596b47827ae2391a2a4` |
| lastVerifiedCommitDate | 2026-08-24T00:21:10+02:00 |
| governingOverview | `../overview.md` |

## Governing Overview

[governing overview](../overview.md)

## Purpose

Forces the failure-time repair WAL and crash recovery for a failed final organizational quality gate.

## Code Commentary

The suite starts real queue/lifecycle state, persists the real repair WAL, injects the producer-to-finish crash, recovers through public `start_or_observe_operation`, pins one gate call and unchanged code/memory tips, then consumes the repair through the real cancel/reset route. It also forces malformed lifecycle states, immutability, foreign identity, binding, source, reset, owner, and recovery-evidence refusals.

## Invariants And Boundaries

- The production repair mutator accepts no caller-supplied lifecycle record.
- Refusal cases assert the canonical WAL, queue state, and contract bytes remain exact.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The focused suite owns the failure repair and crash-recovery surface. | `OrganizationalCompletionRecoveryEdgeTests` | mcp/tests/test_organizational_completion_recovery_edges.py:19-274 |

## Documentation References

No configured domain-documentation or cross-repository source applies to this file.

## 260821-CLIVE-L2 Current Regression Contract

The current forcing seams include `test_durable_repair_generation_is_immutable`, `test_repair_mutation_requires_the_canonical_cancelled_wal`, `test_gate_failure_wal_crash_recovers_without_rerunning_or_moving_refs`, `test_repair_contract_publication_refuses_a_third_byte_state`. The L2 additions force journal-owned claim transfer, exact protected-ref decisions, source-movement reconciliation, and organizational disposition/repair without queue-owned lifecycle evidence.

### Reconciled Source Evidence

| Finding | Citations | Source Path |
| --- | --- | --- |
| The current test source exercises `test_durable_repair_generation_is_immutable`, `test_repair_mutation_requires_the_canonical_cancelled_wal`, `test_gate_failure_wal_crash_recovers_without_rerunning_or_moving_refs`, `test_repair_contract_publication_refuses_a_third_byte_state`. | L76-L110; L112-L120; L122-L192; L194-L208 | `mcp/tests/test_organizational_completion_recovery_edges.py` |

## Update History

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this test card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-17T12:09+02:00 — 260815-DAG-L5: created onboarding for the organizational completion recovery-edge suite.
