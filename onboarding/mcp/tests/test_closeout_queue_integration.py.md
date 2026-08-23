# mcp/tests/test_closeout_queue_integration.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_closeout_queue_integration.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T00:18+02:00 |
| lastVerifiedCommitHash | `1d446724d099517f6f52d596b47827ae2391a2a4` |
| lastVerifiedCommitDate | 2026-08-24T00:21:10+02:00 |
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
Task-addressed cancellation snapshots canonical task JSON, its rendered Markdown, and protected
code/memory refs separately from the mutable enclosure contract and root journal. It forbids every
queue inspect/write/recreate route, proves the projection stays absent or byte-identical, then
requires the exact same door generation to move from claimed to cancelled while the journal records
terminal cancellation evidence.
The former conflict-reset generation scenario is now isolated in
`test_closeout_queue_generation_transition.py`; irreversible worker-release retention is isolated
in `test_lifecycle_worker_release_guards.py`.

### Conventions

Only unrelated expensive gates are mocked in the production closeout success fixture. Queue,
contract, Git, and lifecycle state transitions remain real. Cancellation forcing patches queue
store methods to fail loudly if any post-claim projection access occurs; task-document bytes and
protected refs are compared independently from the expected door/journal mutation.

### Invariants And Boundaries

- The final queue recheck is immediately before the irreversible source move.
- Closeout certification is based on the actual committed tree and contract.
- Reversible terminal retry preserves one task-addressed operation and cannot leave an old worker
  running after queue-release failure.
- Cancellation preserves canonical task JSON/Markdown and protected source refs, but must not
  freeze the enclosure contract or journal that own the same-generation claimed-to-cancelled
  transition.
- After journal claim transfer, cancellation may not inspect, mutate, or recreate queue projection.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies.

## Repo-Internal References

The test source is direct evidence for the production queue/door/journal boundary forced here.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Production integration claims, revalidates, and consumes the exact candidate. | L254-L274 | `mcp/tests/test_closeout_queue_integration.py` |
| Journal claim transfer consumes the queue once, deletes the projection, and forbids later reads. | L300-L345 | `mcp/tests/test_closeout_queue_integration.py` |
| Task-addressed cancellation preserves canonical task JSON/Markdown and protected refs, forbids queue access/recreation, publishes the exact same-generation cancelled door, and records durable cancellation evidence. | L139-L207; L570-L627 | `mcp/tests/test_closeout_queue_integration.py` |
| Real closeout success commits the exact tree and certifies the queue candidate. | L674-L722 | `mcp/tests/test_closeout_queue_integration.py` |
| Post-contract/pre-certification recovery is same-generation and idempotent. | L724-L796 | `mcp/tests/test_closeout_queue_integration.py` |

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

## 260821-CLIVE-L1 Fixture Migration

Queue integration fixtures now use canonical contract publication and accepted closeout admission/effective input. Assertions continue to cover candidate selection, lifecycle correlation, certification, and integration; they do not treat queue rows as closeout lifecycle or Git evidence.

## 260821-CLIVE-L2 Current Regression Contract

The current forcing seams include
`test_production_integrate_claims_revalidates_and_consumes_exact_candidate`,
`test_closeout_certification_and_integration_claim_bind_exact_commits`,
`test_journal_claim_transfer_consumes_queue_once_then_never_reads_it`,
`test_retired_door_fences_preserved_stale_candidate_at_every_boundary`, and
`test_task_addressed_cancellation_does_not_require_or_recreate_queue_projection`. L2 proves that
the integration operation consumes the queue once at claim transfer and then uses journal
evidence, and that cancellation after claim changes only its owning door/journal lifecycle plane
while task truth, protected refs, and the absent projection remain unchanged. Legacy-named
closeout certification coverage remains transitional; this suite does not prove the final
waiting-only queue schema, whose removal belongs to L3.

### Reconciled Source Evidence

| Finding | Citations | Source Path |
| --- | --- | --- |
| The current source forces exact integration claim/commit binding, one-time queue-to-journal transfer, stale-door fencing, and queue-independent cancellation. | L254-L345; L346-L419; L570-L627 | `mcp/tests/test_closeout_queue_integration.py` |

## Update History

- 2026-08-24T00:18+02:00 — No content impact: the architect extracted the unchanged cancellation
  door/journal assertions into `_assert_cancelled_door` and `_assert_cancelled_operation` to satisfy
  deterministic Ruff statement limits, then applied formatter-only line collapses. Current source
  citations now include the helpers and shifted test ranges; no assertion or behavior changed.
- 2026-08-24T00:10+02:00 — 260821-CLIVE-L2: reconciled cancellation forcing by authority plane:
  canonical task JSON/rendered Markdown and protected refs remain unchanged, queue access and
  recreation are forbidden, and the same door generation plus root journal perform the exact
  claimed-to-cancelled transition. The architect supplied the accepted exact Dagger result;
  verification metadata remains closeout-owned.
- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this test card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: curated relationship changes against accepted candidate tree `4241908c`; verification metadata remains pinned until governed closeout.

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
