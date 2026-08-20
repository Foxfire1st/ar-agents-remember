# mcp/src/agents_remember/worktrees/integration/lifecycle_operations.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/lifecycle_operations.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated            | 2026-08-21T00:45+02:00 |
| lastVerifiedCommitHash | `e5cb139f66abbd6502d4dcc4be883eb5f49770fe` |
| lastVerifiedCommitDate | 2026-08-21T00:28:23+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp overview](../../../overview.md)

## Purpose

This module is the task-addressed control surface for starting, observing, recovering, and cancelling durable closeout and integration operations. It privately derives operation identity from the task contract, accepted input, contract state, and immutable candidate tree.

## Code Commentary

### Logic

`start_or_observe_operation` returns immediately after creating or observing one durable attempt. Duplicate accepted inputs converge on the same record; conflicting inputs refuse. `observe_operation` and `latest_operation_projection` return public task state. Stale or failed pre-boundary attempts may relaunch with the same input, while post-boundary recovery stays attached to the consumed approval. Detached launch uses the native subprocess boundary and a private process group.

`launch_detached_worker` deliberately preserves the installed MCP runtime's normalized
`PYTHONPATH`; it does not prepend the task checkout's unpublished `mcp/src`. The worker still runs
with the task worktree as its current directory and task contract as its address, but its executable
code comes from the installed runtime. This prevents the detached subprocess from re-entering
checkout-development mode and colliding with the official-root isolation guard.

`operation_state_fingerprint` moved to `lifecycle_operation_identity.py`; the failed organizational-completion cancellation path now resolves the gate-bound repair evidence and routes through `prepare_organizational_completion_repair`.

### Conventions

Public callers supply task plus operation kind, never worker PID, operation key, or record path. Fingerprints are canonical JSON hashes; projections deliberately omit private identity.

The operation-state fingerprint includes both code and external-memory base commits. A successful
sync that absorbs a conflict source delta therefore creates a new closeout generation even when the
old closeout/candidate cells were reset to the same vocabulary values; the prior completed attempt
cannot be mistaken for the required targeted re-closeout.

### Invariants And Boundaries

- A candidate tree is captured before launch and reused by retries.
- Replacement of an agent or worker process does not change the task address.
- Cancellation refuses after approval or irreversible mutation is claimed.
- Stale recovery is idempotent and cannot claim multiple concurrent workers.

### Todos

None.

## Docs References

No external Domain Documentation source is configured for the internal lifecycle plane.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external document governs this task-addressed operation controller. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Start/observe converges duplicates and binds recovery to canonical task state. | `start_or_observe_operation` | mcp/src/agents_remember/worktrees/integration/lifecycle_operations.py:94-104 |
| Projection and cancellation expose task state without private operation identifiers. | `observe_operation`; `cancel_operation` | mcp/src/agents_remember/worktrees/integration/lifecycle_operations.py:188-193; mcp/src/agents_remember/worktrees/integration/lifecycle_operations.py:212-217 |
| Detached launch and queued-record creation preserve the immutable candidate and native process boundary. | `launch_detached_worker`; `_queued_record` | mcp/src/agents_remember/worktrees/integration/lifecycle_operations.py:343-379; mcp/src/agents_remember/worktrees/integration/lifecycle_operations.py:382-408 |

## Cross-Repo References

No sibling-repository protocol is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| The controller resolves all repository paths through the selected task contract. | `start_or_observe_operation`; `observe_operation` | mcp/src/agents_remember/worktrees/integration/lifecycle_operations.py:94-104; mcp/src/agents_remember/worktrees/integration/lifecycle_operations.py:188-193 |

## L23 Lifecycle Model Package Review

Lifecycle operation inputs, kinds, and records now come from `models.lifecycles.operation`. Process
launch, status, cancellation, recovery, and native-environment behavior are unchanged by the model
ownership move.

## L23 Final Candidate Disposition

Start-or-observe derives one durable closeout or integration operation from task plus kind and a
validated input fingerprint. Retries observe the same work, conflicting inputs refuse, and recovery
continues from monotonic phase evidence rather than replaying completed irreversible cells.

## 260815-DAG-L3 Cancellation And Queue Ownership

Pre-boundary cancellation releases the candidate's internal queue ownership through the same
task-addressed operation key. Worker termination is in `finally`: even if queue release fails, the
captured process group is still signalled after the store clears its PID, preventing a retry from
launching beside an orphaned old worker.

## 260815-DAG-L4 Integration-Authority Impact

L4 makes task-derived integration refs mechanically non-ordinary: repository defaults, sprint supers, and active atomic-series refs are censused across code and external memory. Mutation is admitted only through exact lifecycle authority, named-ref compare-and-swap, queue/repository serialization, or a terminal capability; stale topology, aliases, ambient checkouts, and torn recovery fail closed.

## Update History

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: source moved to `mcp/src/agents_remember/worktrees/integration/lifecycle_operations.py` (new package route); the citation fixer repointed in-body references; import paths updated inside the module. Verified at code commit e5cb139f.


- 2026-08-20T05:12+02:00 — L13 landed-wave refresh: the series closeout-report routing
  commit (0a746c9f) touched this source; card re-verified against the current file, verification
  stamp advanced to 0a746c9f. Body unchanged — the documented contract still holds.


- 2026-08-19T04:05+02:00 — No content impact: 260815-DAG-L10 re-pointed the internal
  `_require_configured_task_identity` series worktree-group equality check at
  `worktree_group_for(...)`; this card never documented that internal predicate, and the
  task-addressed start/observe/cancel behavior it describes is unchanged. Verification metadata
  stamped at the landed code commit `e41ea31d`.

- 2026-08-17T12:30+02:00 — 260815-DAG-L5: extracted `operation_state_fingerprint` to `lifecycle_operation_identity.py` and wired the failed final-leaf cancel/reset repair through `prepare_organizational_completion_repair`. Verification remains closeout-owned.

- 2026-08-16T08:12+02:00 — Dagger repair: bound operation generations to code/memory base commits so conflict-resolution sync makes the next targeted closeout observably fresh.

- 2026-08-15T23:38+02:00 — Reconciled this worktree owner's role in task-derived protected-ref authority, exact named-ref movement, and crash-safe recovery. Verification metadata remains closeout-owned.

- 2026-08-15T09:10+02:00 — L3 content update: documented reversible queue release and guaranteed
  worker termination on cancellation; verification remains closeout-owned.
- 2026-08-14T06:36+02:00 — L23 final candidate review: task-addressed start/observe dispatch keeps
  one durable operation per kind/fingerprint and recovers terminal evidence without replaying
  completed irreversible phases. Verification remains closeout-owned.

- 2026-08-13T09:05+02:00 — L23 curator: reviewed the operation-model package move and confirmed no
  lifecycle execution behavior changed; final provenance remains closeout-owned.

- 2026-08-12T16:54+02:00 — 260731-EFA-L23 installed-runtime repair: recorded that detached launch
  preserves the installed MCP `PYTHONPATH` and excludes the task checkout source root while keeping
  task-addressed cwd/contract context. Verification provenance remains closeout-owned.

- 2026-08-12T15:19+02:00 — Created for L23 task-addressed asynchronous lifecycle control; verification provenance remains closeout-owned.