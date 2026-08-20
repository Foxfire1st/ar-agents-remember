# mcp/tests/test_lifecycle_operations.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_lifecycle_operations.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-21T00:45+02:00 |
| lastVerifiedCommitHash |  `e5cb139f66abbd6502d4dcc4be883eb5f49770fe`|
| lastVerifiedCommitDate |  2026-08-21T00:28:23+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

This is the forcing suite for durable asynchronous closeout/integration operations. It proves task-addressed identity, exact retry, immutable candidate capture, legal recovery, cancellation boundaries, detached execution, worker reporting, and public projection privacy.

## Code Commentary

### Logic

Tests create real task contracts and durable operation records, then exercise duplicate convergence, conflicting input refusal, changed candidate identity, stale recovery, exact approval reuse, store corruption and transition guards, cancellation, detached launch, progress, terminal outcomes, closeout/integration dispatch, completion cleanup, and script entry.

The packaged-entry regression now also doubles the service builder and binder, proving `main`
creates the default `WorktreeServices`, binds that exact instance, and only then calls `run_worker`
with the parsed contract path and operation kind. This covers the installed-process composition
boundary rather than merely proving argument parsing and `__main__` exit propagation.

The detached-launch regression separately proves the native environment keeps its installed
`PYTHONPATH` byte-for-byte and does not inject the task worktree's `mcp/src`, while retaining the
private process group and task-addressed module invocation. Together the two regressions cover both
sides of worker bootstrap: select installed code at launch, then bind its real services in `main`.

### Conventions

Filesystem and model transitions are real; subprocess and lifecycle mutation endpoints are doubled only at their external boundary.

### Invariants And Boundaries

- Agents use task and operation kind, never operation keys or worker PIDs.
- Input, candidate, state fingerprint, and approval claim cannot change across recovery.
- Cancellation cannot reclaim a consumed approval.
- A post-boundary failure remains recoverable as the same operation.

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
| Start, observe, retry, recovery, transition, cancellation, launch, worker, and integration edges are all forced. | `test_start_returns_immediately_and_duplicate_observes_one_launch`; `test_worker_parser_main_and_script_entry_use_task_addressing` | mcp/tests/test_lifecycle_operations.py:232-247; mcp/tests/test_lifecycle_operations.py:1014-1071 |

## Cross-Repo References

No sibling-repository protocol is exercised.

| Finding | Anchor | Source |
| --- | --- | --- |
| Temporary worktree contracts isolate each operation proof. | `_contract`; `_input` | mcp/tests/test_lifecycle_operations.py:61-141; mcp/tests/test_lifecycle_operations.py:144-150 |

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

## Update History

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
