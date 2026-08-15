# mcp/tests/test_closeout_queue_integration.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_closeout_queue_integration.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-15T14:24+02:00 |
| lastVerifiedCommitHash | `17987fa66a642306eb8d20fa9a4bff2b881550d2` |
| lastVerifiedCommitDate | 2026-08-15T14:36:30+02:00|
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
| Production integration claims, revalidates, and consumes the exact candidate. | `test_production_integrate_claims_revalidates_and_consumes_exact_candidate` | mcp/tests/test_closeout_queue_integration.py:92-109 |
| Evidence drift at the pre-merge boundary refuses with the exact mechanistic status and reason. | `test_boundary_rechecks_evidence_after_claim_before_source_merge` | mcp/tests/test_closeout_queue_integration.py:131-166 |
| Cancellation release failure still terminates the captured worker and requeues the same operation. | `test_cancel_release_failure_still_terminates_worker_and_requeues_same_operation` | mcp/tests/test_closeout_queue_integration.py:294-333 |
| Real closeout success commits the exact tree and certifies the queue candidate. | `test_production_closeout_commits_exact_tree_and_certifies_queue_candidate` | mcp/tests/test_closeout_queue_integration.py:444-488 |
| Post-contract/pre-certification crash retry preserves worker-owned irreversible progress, projects apply-only recovery, and is idempotent. | `test_post_contract_write_pre_certification_crash_recovers_idempotently` | mcp/tests/test_closeout_queue_integration.py:441-511 |

## Cross-Repo References

No meaningful cross-repository reference applies.

## Update History

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
