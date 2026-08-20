# mcp/src/agents_remember/application/lifecycle_operation_worker.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/lifecycle_operation_worker.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-21T00:45+02:00 |
| lastVerifiedCommitHash | `e5cb139f66abbd6502d4dcc4be883eb5f49770fe` |
| lastVerifiedCommitDate | 2026-08-21T00:28:23+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[application overview](overview.md)

## Purpose

This module is the detached process entry point for one durable closeout or integration operation. It turns a task-addressed durable record into the existing synchronous lifecycle implementation while publishing heartbeat, phase, command, boundary, result, and recovery evidence back to the operation store.

## Code Commentary

### Logic

`OperationRuntime` claims a queued record, follows the quality progress artifacts while work runs, and makes terminal state depend on whether the operation crossed its irreversible boundary. `execute_operation` reconstructs the captured gate policy and immutable candidate identity before dispatching to closeout or integration. `run_worker` loads the task contract and operation record by task plus operation kind, never by an agent-retained runtime identifier.

`main` is the packaged detached worker's composition root. Before dispatching the task-addressed
record it builds and binds the default `WorktreeServices`, ensuring closeout/integration reach the
real provider, memory-quality, citation, and worktree adapters instead of failing at the first
service-port access. Library callers remain free to bind test services explicitly; this binding is
owned by the CLI process boundary.

The worker parses quality/queue/repair evidence from the progress payload and, on failure, finalizes the organizational gate-failed repair handoff instead of a bare error.

### Conventions

The worker is launched as a private process group and communicates through atomic durable files. Progress text is bounded diagnostic evidence; the operation record remains authority.

### Invariants And Boundaries

- A consumed approval remains bound to the same operation fingerprint and candidate tree.
- Cancellation is effective only before the irreversible boundary.
- A post-boundary failure becomes `input-required` so recovery reconciles the same mutation instead of replaying a new one.
- The worker never invents a task, role, runtime, or inbox identity.

### Todos

None.

## Docs References

No external Domain Documentation source is configured for this repository; this worker's contract is project-owned.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external document governs this internal lifecycle worker. | — | — |

## Repo-Internal References

The source records the lifecycle transition and recovery boundary directly.

| Finding | Anchor | Source |
| --- | --- | --- |
| `OperationRuntime` publishes claimed, heartbeat, progress, and terminal durable state. | `OperationRuntime` | mcp/src/agents_remember/application/lifecycle_operation_worker.py:64-213 |
| Execution reconstructs captured policy and dispatches the exact closeout or integration input. | `execute_operation` | mcp/src/agents_remember/application/lifecycle_operation_worker.py:252-301 |

## Cross-Repo References

No meaningful cross-repository boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| The process operates only on the contract-resolved repository and memory worktrees. | `execute_operation` | mcp/src/agents_remember/application/lifecycle_operation_worker.py:252-301 |

## L23 Lifecycle Model Package Review

The worker now imports its operation inputs, projections, and policy snapshots from
`models.lifecycles.operation`. This is the sole package owner after the model move; record lookup,
service binding, execution, and recovery behavior are unchanged.

## L23 Final Candidate Disposition

The detached worker is the installed-runtime composition root for accepted closeout and integration
operations. It declares only `lifecycle-operation`, binds default services before dispatch, and
publishes durable progress/recovery evidence without acquiring MCP or dashboard daemon authority.

## 260815-DAG-L3 Reversible Queue Release

Failed closeout/integration workers now release queue ownership only while the operation is still
pre-boundary. A release failure is preserved in the terminal operation payload/error instead of
being hidden, so retry keeps the original task-addressed operation and cannot silently schedule a
different candidate.

## 260815-DAG-L4 Authority Boundary

L4 routes this file's existing application, configuration, task, model, registration, or memory responsibility through the shared task-derived integration authority. The change preserves the file's owning altitude while ensuring protected code and external-memory refs cannot be mutated through an ordinary workbench or unjournaled helper.

## Update History

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-17T12:30+02:00 — 260815-DAG-L5: the worker now parses and persists `quality_certification`, `queue_completion`, and `organizational_repair` evidence and finalizes the organizational gate-failed repair handoff. Verification remains closeout-owned.

- 2026-08-15T23:38+02:00 — Reconciled this file's L4 role in task-derived integration authority and protected code/memory boundaries. Verification metadata remains closeout-owned.

- 2026-08-15T09:10+02:00 — L3 content update: documented pre-boundary queue release and visible
  release failure on worker failure; verification remains closeout-owned.
- 2026-08-14T06:30+02:00 — L23 final candidate review: the detached worker binds default services
  under its narrow lifecycle-operation declaration and reports monotonic recovery evidence without
  borrowing daemon authority. Verification remains closeout-owned.

- 2026-08-13T09:05+02:00 — L23 curator: reviewed the lifecycle-model package move and recorded its
  exact import boundary; no worker behavior changed and final provenance remains closeout-owned.

- 2026-08-12T16:52+02:00 — 260731-EFA-L23 packaged-worker repair: recorded that the detached CLI
  composition root builds and binds default worktree services before running the task-addressed
  operation. This prevents installed workers from failing pre-boundary with unbound service ports;
  verification provenance remains closeout-owned.

- 2026-08-12T15:19+02:00 — Created for L23 durable task-addressed lifecycle operations; verification provenance remains closeout-owned.
