# mcp/tests/test_closeout_queue_integration.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_closeout_queue_integration.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-21T00:45+02:00 |
| lastVerifiedCommitHash | `e5cb139f66abbd6502d4dcc4be883eb5f49770fe` |
| lastVerifiedCommitDate | 2026-08-21T00:28:23+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Exercises the queue through the production worktree closeout, integration, cancellation, failure,
and crash-recovery boundaries.

## Code Commentary

### Logic

The suite proves integration claims/revalidates/consumes the exact certified candidate immediately
around the source merge; closeout/integration refuse missing bound topology; cancellation and
reversible worker failure release internal ownership; release failure stays observable while the
worker is still terminated; and real closeout success commits the exact tree, writes the contract,
certifies the queue, and recovers idempotently after a post-contract/pre-certification crash.

### Conventions

Only unrelated expensive gates are mocked in the production closeout success fixture. Queue,
contract, Git, and lifecycle state transitions remain real.

### Invariants And Boundaries

- The final queue recheck is immediately before the irreversible source move.
- Closeout certification is based on the actual committed tree and contract.
- Reversible terminal retry preserves one task-addressed operation and cannot leave an old worker
  running after queue-release failure.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Production integration claims, revalidates, and consumes the exact candidate. | `test_production_integrate_claims_revalidates_and_consumes_exact_candidate` | mcp/tests/test_closeout_queue_integration.py:115-132 |
| Evidence drift at the pre-merge boundary refuses with the exact mechanistic status and reason. | `test_boundary_rechecks_evidence_after_claim_before_source_merge` | mcp/tests/test_closeout_queue_integration.py:294-328 |
| Cancellation release failure still terminates the captured worker and requeues the same operation. | `test_cancel_release_failure_still_terminates_worker_and_requeues_same_operation` | mcp/tests/test_closeout_queue_integration.py:475-514 |
| Real closeout success commits the exact tree and certifies the queue candidate. | `test_production_closeout_commits_exact_tree_and_certifies_queue_candidate` | mcp/tests/test_closeout_queue_integration.py:622-666 |
| Post-contract/pre-certification crash retry preserves worker-owned irreversible progress, projects apply-only recovery, and is idempotent. | `test_post_contract_write_pre_certification_crash_recovers_idempotently` | mcp/tests/test_closeout_queue_integration.py:668-736 |

## Cross-Repo References

No meaningful cross-repository reference applies.

## 260815-DAG-L4 Integration-Authority Forcing

This task extends this suite's production-bound fixtures or assertions for task-derived protected-ref ownership, durable closeout/integration authority, external-memory parity, and fail-closed recovery. The suite continues to exercise the real owner named in its existing purpose; the L4 delta adds exact negative or crash/retry evidence rather than a test-only bypass.

## 260815-DAG Master Full-Gate Repair

The 260815-DAG master full-gate repair moved this suite's imports to the restructured packages:
queue owners (`closeout_queue`, `closeout_queue_lifecycle`, `QueueActor`) now import from
`worktrees/queue/`, lifecycle-operation store/dispatch and integration owners from
`worktrees/integration/`, and the queue request model from `models/queue/`; the `__main__` runner
was removed. No assertions changed.

## Update History

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: queue, lifecycle-operation,
  integration-authority, and model imports follow the package moves (`worktrees/queue/`,
  `worktrees/integration/`, `models/queue/`); the `__main__` runner was removed. Verified at code
  commit e5cb139f.
- 2026-08-17T12:30+02:00 — No content impact: L5 coverage-pragma/import alignment only; the documented integration behavior is unchanged.

- 2026-08-16T09:45+02:00 — The graph-disappearance regression now bypasses only earlier source-state and lineage projections so the real queue claim/revalidation owner must reject the missing graph before merge.
- 2026-08-16T08:12+02:00 — Dagger fixture repair: the missing-sprint-graph integration route now isolates both preview target resolution and durable-operation target authority so it reaches the queue refusal it owns.
- 2026-08-16T05:18+02:00 — Dagger fixture repair: synthetic completed closeouts use the typed `contract-finalization` phase before `completed`, matching the durable lifecycle vocabulary without bypassing queue ownership.
- 2026-08-16T04:06+02:00 — Dagger fixture repair: queue-bound closeout and integration tests use real lifecycle operation keys and runtime config paths; graph-disappearance tests isolate the queue ownership seam after exact source-lineage validation.
- 2026-08-15T23:38+02:00 — Reconciled the suite's L4 fixture and forcing role for protected integration branches, durable operation authority, external-memory parity, and recovery. Verification metadata remains closeout-owned.

- 2026-08-15T14:24+02:00 — L3 final diff-coverage repair: the normal nonzero operation-result
  case now expects the worker process to finish normally while the durable operation records
  failure, and a separate real `run_worker` exception case proves an unreleased reversible queue
  claim is combined into the durable terminal reason and returns process failure.
- 2026-08-15T14:05+02:00 — L3 final targeted-gate repair: the reversible worker-release failure
  now supplies the real fixture configuration and mocks only the lower release call, so the real
  worker helper records queueReleaseFailure and the test reaches its intended seam.
- 2026-08-15T13:27+02:00 — No content impact: added an explicit non-`None` narrowing for the
  failed operation's result immediately before the existing queue-release-failure assertion;
  runtime behavior and asserted value are unchanged.
- 2026-08-15T13:18+02:00 — No content impact: repository Ruff formatting changed only layout;
  production closeout/integration and recovery assertions are identical.
- 2026-08-15T12:53+02:00 — L3 targeted-gate repair: the failed-worker recovery scenario now
  claims the real selected candidate, records the nonzero closeout result plus queue-release
  failure, and proves same-operation retry from the projected blocked state.
- 2026-08-15T11:07+02:00 — L3 Dagger repair: production-seam fixtures now use real lifecycle
  operation ownership; evidence drift asserts its exact status/reason, and the post-contract crash
  drives worker progress before proving in-flight apply-only recovery and idempotent certification.
- 2026-08-15T09:10+02:00 — Created for L3's production closeout/integration and lifecycle-recovery suite; verification remains closeout-owned.
