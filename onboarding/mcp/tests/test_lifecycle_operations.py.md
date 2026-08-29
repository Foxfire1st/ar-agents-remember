# mcp/tests/test_lifecycle_operations.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_lifecycle_operations.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-29T16:27+02:00 |
| lastVerifiedCommitHash | `60e429d17e9fcbca3ab1c02563afcaa5761b8c5a` |
| lastVerifiedCommitDate | 2026-08-29T20:33:10+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

This is the forcing suite for durable asynchronous closeout/integration operations. It proves task-addressed identity, exact retry, immutable candidate capture, legal recovery, cancellation boundaries, detached execution, worker reporting, and public projection privacy.

## Code Commentary

### Logic

Tests create real task contracts and durable operation records, then exercise duplicate convergence, conflicting input refusal, changed candidate identity, stale recovery, exact approval reuse, cancellation, detached launch, progress, terminal outcomes, closeout/integration dispatch, and completion cleanup. Failed integration dispatch now preserves the truthful queue-release failure and reports `safeToReplace: false`; it does not collapse a failed release into a replaceable operation. Strict store-transition forcing—including public refusal to cancel an irreversible integrate operation—and parser/script bootstrap forcing live in `test_lifecycle_operation_store_invariants.py` and `test_lifecycle_operation_worker_entrypoint.py`, keeping this suite focused on public lifecycle behavior.

The detached-launch regression separately proves the native environment keeps its installed
`PYTHONPATH` byte-for-byte and does not inject the task worktree's `mcp/src`, while retaining the
private process group and task-addressed module invocation. It now also proves that the exact
`Popen` object transfers to the lifecycle-owned child registry before PID/fingerprint publication.
Together the regressions cover both sides of worker bootstrap: select installed code at launch,
retain and reap the real child, then bind its real services in `main`.

### Conventions

Filesystem and model transitions are real; subprocess and lifecycle mutation endpoints are doubled only at their external boundary.

### Invariants And Boundaries

- Agents use task and operation kind, never operation keys or worker PIDs.
- Input, candidate, state fingerprint, and approval claim cannot change across recovery.
- Cancellation cannot reclaim a consumed approval.
- A post-boundary failure remains recoverable as the same operation.
- An integration result is safe to replace only when its literal returned payload proves that boundary; queue-release failure remains visible.
- Detached launch retains the real process object for reaping; lifecycle journal identity remains
  PID/fingerprint-based and separate.

### Todos

None.

## Docs References

No external Domain Documentation source is configured for this project-owned operation protocol.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external source governs the internal durable lifecycle state machine. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Start, observe, retry, cancellation, launch, worker, and integration edges are forced on the public controller/runtime. | `test_start_returns_immediately_and_duplicate_observes_one_launch`; `test_run_worker_refuses_missing_or_non_startable_durable_state` | mcp/tests/test_lifecycle_operations.py:316-334; mcp/tests/test_lifecycle_operations.py:999-1026 |
| Failed integration dispatch preserves the exact queue-release failure and a truthful false replacement signal. | `test_execute_operation_dispatches_closeout_and_integration_payloads` | mcp/tests/test_lifecycle_operations.py:886-938 |
| Irreversible integrate cancellation is forced through the public controller in the focused store suite. | `test_integrate_boundary_cannot_be_cleared_or_cancelled` | mcp/tests/test_lifecycle_operation_store_invariants.py:291-317 |

## Cross-Repo References

No sibling-repository protocol is exercised.

| Finding | Anchor | Source |
| --- | --- | --- |
| Temporary worktree contracts isolate each operation proof. | `_contract`; `_input` | mcp/tests/test_lifecycle_operations.py:98-182; mcp/tests/test_lifecycle_operations.py:185-186 |

## L23 Lifecycle Model Package Review

The suite imports closeout/integration operation inputs from `models.lifecycles.operation`, the
dedicated model owner. Durable operation, installed-runtime selection, service binding, and
non-daemon authority coverage are unchanged.

## 260815-DAG-L4 Integration-Authority Forcing

This task extends this suite's production-bound fixtures or assertions for task-derived protected-ref ownership, durable closeout/integration authority, external-memory parity, and fail-closed recovery. The suite continues to exercise the real owner named in its existing purpose; the L4 delta adds exact negative or crash/retry evidence rather than a test-only bypass.

## 260815-DAG Master Full-Gate Repair

The 260815-DAG master full-gate repair moved the lifecycle-operation imports under
`worktrees/integration/` and `TaskRef` under `application/task_docs/`; the cross-kind and terminal
lease refusals now drive `lease.__enter__()` explicitly instead of opening the lease inside the
raises context, and the `killpg` patch target follows the moved module.

## 260821-CLIVE-L1 Lifecycle Journal Coverage

This suite now constructs closeout admission from normalized effective input and exercises strict schema 3.0, immutable duplicate plans, stable candidate identity, explicit cross-kind compatibility under the lease, evidence-derived cancellation/retention, worker rehydration, and recovery projection. Raw closeout input through the generic starter and legacy/extra store shapes fail closed; queue projection is not used as journal evidence.

## 260821-CLIVE-L2 Current Regression Contract

The current forcing seams include `test_integration_authority_refuses_incomplete_closeout_edges`, `test_start_returns_immediately_and_duplicate_observes_one_launch`, `test_conflicting_commit_message_refuses_while_task_operation_exists`, `test_contract_lifecycle_lease_excludes_cross_kind_and_terminal_mutation`. The L2 additions force locator-rooted journal access, legal task-addressed controls, write-ahead successors, exact worker termination, total expected-failure projection, and same-generation convergence.

### Reconciled Source Evidence

| Finding | Anchor | Source |
| --- | --- | --- |
| The current test source exercises `test_integration_authority_refuses_incomplete_closeout_edges`, `test_start_returns_immediately_and_duplicate_observes_one_launch`, `test_conflicting_commit_message_refuses_while_task_operation_exists`, `test_contract_lifecycle_lease_excludes_cross_kind_and_terminal_mutation`. | `test_integration_authority_refuses_incomplete_closeout_edges`; `test_start_returns_immediately_and_duplicate_observes_one_launch`; `test_conflicting_commit_message_refuses_while_task_operation_exists`; `test_contract_lifecycle_lease_excludes_cross_kind_and_terminal_mutation` | mcp/tests/test_lifecycle_operations.py:292-313; mcp/tests/test_lifecycle_operations.py:316-334; mcp/tests/test_lifecycle_operations.py:337-347; mcp/tests/test_lifecycle_operations.py:350-361 |


## PDLS Reconciliation

Lifecycle operation tests now cover explicit retry/replacement after failed or terminal generations and convergent initial-door publication.

The test continues to exercise production-owned behavior. No diagnostic result is treated as
certifying evidence and no fallback or threshold exception was introduced.
## Update History

- 2026-08-29T16:27+02:00 — Extended detached-launch forcing to require ownership transfer of the
  exact `Popen` object to the lifecycle reaper.

- 2026-08-25T15:44+02:00 — PDLS whole-system reconciliation updated the implementation summary
  above after source and requirement review. Verification remains closeout-owned.


- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this test card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1 candidate-11: rebound truthful `queueReleaseFailure`/`safeToReplace` dispatch forcing and the public irreversible-integrate cancellation relationship against accepted tree `4241908c`; verification metadata remains pinned until governed closeout.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: lifecycle-operation imports moved under
  `worktrees/integration/` and `TaskRef` under `application/task_docs/`; the lease-refusal test now
  drives `lease.__enter__()` explicitly and the `killpg` mock follows the moved module. Verified at code
  commit e5cb139f.
- 2026-08-16T07:05+02:00 — L4 Dagger repair: the closeout dispatch fixture now performs the real queued-to-running-to-completed journal transitions before starting integration, preserving cross-operation lease semantics.
- 2026-08-16T05:18+02:00 — Dagger fixture repair: integration worker dispatch carries the real absolute runtime settings path created by the shared contract fixture.
- 2026-08-16T04:06+02:00 — Dagger fixture repair: operation inputs reference a real workspace settings file and cancellation preview patches the canonical configured-contract resolver.
- 2026-08-15T23:38+02:00 — Reconciled the suite's L4 fixture and forcing role for protected integration branches, durable operation authority, external-memory parity, and recovery. Verification metadata remains closeout-owned.
- 2026-08-14T06:38+02:00 — L23 final candidate review: lifecycle-operation tests cover idempotent
  start/observe, conflicting fingerprints, detached recovery, monotonic terminal evidence, and the
  pre/post-claim boundary. Verification remains closeout-owned.

- 2026-08-13T09:05+02:00 — L23 curator: reviewed the operation-model import move and confirmed the
  tested lifecycle contract is unchanged; final provenance remains closeout-owned.

- 2026-08-12T16:54+02:00 — 260731-EFA-L23 installed-runtime repair: extended detached-launch proof
  to preserve the installed runtime `PYTHONPATH` and exclude unpublished task-checkout source, paired
  with the packaged-entry service-binding proof. Focused verification remains code-owned; memory
  provenance remains closeout-owned.

- 2026-08-12T16:52+02:00 — 260731-EFA-L23 packaged-worker repair: extended the existing parser/main
  regression to prove default worktree services are built and bound before worker dispatch. The
  focused test passes with configuration-owned xdist auto; verification provenance remains
  closeout-owned.

- 2026-08-12T15:19+02:00 — Created with L23's complete durable lifecycle operation forcing suite; verification provenance remains closeout-owned.
