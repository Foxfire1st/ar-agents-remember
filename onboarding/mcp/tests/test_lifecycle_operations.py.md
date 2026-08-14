# mcp/tests/test_lifecycle_operations.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_lifecycle_operations.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-12T15:19+02:00 |
| lastVerifiedCommitHash |  `aeca9a2839c965218a61a3040e15cb84367ebeca`|
| lastVerifiedCommitDate |  2026-08-14T13:35:55+02:00|
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
| Start, observe, retry, recovery, transition, cancellation, launch, worker, and integration edges are all forced. | `test_start_returns_immediately_and_duplicate_observes_one_launch`; `test_worker_parser_main_and_script_entry_use_task_addressing` | mcp/tests/test_lifecycle_operations.py:111-126; mcp/tests/test_lifecycle_operations.py:867-924 |

## Cross-Repo References

No sibling-repository protocol is exercised.

| Finding | Anchor | Source |
| --- | --- | --- |
| Temporary worktree contracts isolate each operation proof. | `_contract`; `_input` | mcp/tests/test_lifecycle_operations.py:52-106 |

## L23 Lifecycle Model Package Review

The suite imports closeout/integration operation inputs from `models.lifecycles.operation`, the
dedicated model owner. Durable operation, installed-runtime selection, service binding, and
non-daemon authority coverage are unchanged.

## Update History
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
