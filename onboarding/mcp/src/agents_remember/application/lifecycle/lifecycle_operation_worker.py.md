# mcp/src/agents_remember/application/lifecycle/lifecycle_operation_worker.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/lifecycle/lifecycle_operation_worker.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-25T08:16+02:00 |
| lastVerifiedCommitHash | `cb6623775a04cbdeb0509dc26f08a8268189c3f6` |
| lastVerifiedCommitDate | `2026-08-25T08:12:56+02:00` |
| governingOverview | `../overview.md` |

## Governing Overview

[application overview](../overview.md)

## Purpose

This module is the detached process entry point for one durable closeout or integration operation. It turns a task-addressed durable record into the existing synchronous lifecycle implementation while publishing heartbeat, phase, command, boundary, result, and recovery evidence back to the operation store.

## Code Commentary

### Logic

`OperationRuntime` claims a queued record and follows bounded progress artifacts while work runs.
For closeout, terminal/recovery behavior depends on durable mutation evidence or exact contract
finalization proof, not on a phase or caller-supplied boundary boolean. `execute_operation`
reconstructs the captured gate policy, immutable candidate identity, and accepted effective input
before dispatching. `run_worker` loads the task contract and operation record by task plus operation
kind, never by an agent-retained runtime identifier.

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
- Closeout cancellation is effective only before mutation intent/proof or exact finalization retains
  the generation; integration retains its own operation-specific boundary.
- A retained closeout failure becomes `input-required` so recovery reconciles the same accepted
  mutation instead of replaying a new one.
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
| `OperationRuntime` publishes claimed, heartbeat, progress, and terminal durable state. | `OperationRuntime` | mcp/src/agents_remember/application/lifecycle/lifecycle_operation_worker.py:88-297 |
| Execution reconstructs captured policy and dispatches the exact closeout or integration input. | `execute_operation` | mcp/src/agents_remember/application/lifecycle/lifecycle_operation_worker.py:300-345 |

## Cross-Repo References

No meaningful cross-repository boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| The process operates only on the contract-resolved repository and memory worktrees. | `execute_operation` | mcp/src/agents_remember/application/lifecycle/lifecycle_operation_worker.py:300-345 |

## L23 Lifecycle Model Package Review

The worker now imports its operation inputs, projections, and policy snapshots from
`models.lifecycles.operation`. This is the sole package owner after the model move; record lookup,
service binding, execution, and recovery behavior are unchanged.

## L23 Final Candidate Disposition

The detached worker is the installed-runtime composition root for accepted closeout and integration
operations. It declares only `lifecycle-operation`, binds default services before dispatch, and
publishes durable progress/recovery evidence without acquiring MCP or dashboard daemon authority.

## 260815-DAG-L3 Reversible Queue Release

This former worker-owned queue-release responsibility is superseded. The worker now records the
truthful journal result only; closeout-door disposition and disposable queue projection are handled
by their dedicated owners. Failure retains the same task-addressed generation whenever journaled
mutation, integration, or worker-termination evidence requires recovery.

## 260815-DAG-L4 Authority Boundary

L4 routes this file's existing application, configuration, task, model, registration, or memory responsibility through the shared task-derived integration authority. The change preserves the file's owning altitude while ensuring protected code and external-memory refs cannot be mutated through an ordinary workbench or unjournaled helper.

## 260821-CLIVE-L1 Closeout Worker Contract

The worker rehydrates closeout execution exclusively from durable `effectiveInput`; raw request messages and blank sentinels never re-enter the apply path. It parses mutation evidence and the exact finalized-contract publication hash, derives the compatibility recovery tuple from commit-proven evidence, and retains or releases a closeout generation from those facts. Restart repairs a stale recovery projection from journal evidence. A phase name, approval boolean, or queue row is not lifecycle evidence.

## 260821-CLIVE-L2 Current Contract

The current source seams include `OperationCancelled`, `OperationRuntime`, `execute_operation`. Detached execution consumes durable journal input and reports through the operation store. Launch, exit, and termination evidence are explicit; worker authority is not cleared before exact process termination proof.

### Reconciled Source Evidence

| Finding | Anchor | Source |
| --- | --- | --- |
| The current module exposes `OperationCancelled`, `OperationRuntime`, `execute_operation` at this ownership boundary. | `OperationCancelled`; `OperationRuntime`; `execute_operation` | mcp/src/agents_remember/application/lifecycle/lifecycle_operation_worker.py:68-69; mcp/src/agents_remember/application/lifecycle/lifecycle_operation_worker.py:88-298; mcp/src/agents_remember/application/lifecycle/lifecycle_operation_worker.py:300-345 |

## 260824-PDLS Owner-Level Terminalization Contract

`terminal_operation_record` is now the pure canonical terminal transition used by both the detached
runtime and the quality owner preflight. If an accepted organizational-repair generation already
published its developer-decision payload, a later lower-level failure retains that durable result
instead of replacing it with a schema-incompatible symptom. The transition still derives recovery,
input-required, finish, guidance, and process-binding state from operation evidence; the preflight
only validates this owner and never duplicates the transition.

## Update History

- 2026-08-25T01:56+02:00 — 260824-PDLS extracted the pure terminal transition as the single owner,
  preserving canonical organizational-repair evidence and enabling one owner-level preflight.
- 2026-08-24T00:27+02:00 — 260821-CLIVE-L2 committed-route reconciliation: moved this preserved sidecar to mirror `mcp/src/agents_remember/application/lifecycle/lifecycle_operation_worker.py`, repointed current source evidence and governing context, and verified the source at code commit `1d446724d099517f6f52d596b47827ae2391a2a4`.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: curated against accepted candidate tree `4241908c`; verification metadata remains pinned until governed closeout stamps the landed code commit.

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
