# mcp/src/agents_remember/worktrees/integration/lifecycle_operations.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/lifecycle_operations.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated            | 2026-08-22T10:39+02:00 |
| lastVerifiedCommitHash | `eb7ea60ab9919f009fef58f81afe5861aa1709da` |
| lastVerifiedCommitDate | 2026-08-22T11:44:33+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[governing overview](overview.md)

## Purpose

This module is the task-addressed control surface for starting, observing, recovering, and cancelling durable closeout and integration operations. Its two typed public starters own kind-specific admission and hand the shared controller an already resolved candidate plus explicit integration authority where applicable.

## Code Commentary

### Logic

`start_or_observe_operation` is the typed integrate-only caller. Under the lifecycle lease it validates configured authority, retains the exact irreversible integration record when one exists, or derives the integration authority and candidate from current contract state when no record is retained. `start_or_observe_closeout_operation` is the sole closeout candidate owner: it reloads under the lease, prevalidates raw admission, resolves the accepted input and lease-stable candidate, and checks lifecycle compatibility before publishing any record. The shared `_start_or_observe_operation` therefore accepts a required candidate and explicit optional integration authority; it does not cast raw input, infer kind-specific ownership, or recapture closeout provenance from ambient state.

The shared flow deliberately separates generation creation/conflict/terminal replacement from recovery, launch, and public projection. For closeout, accepted plan and candidate resolution precede compatibility, repository reconciliation precedes queued-record publication, and only then may recovery or a single launch occur. Duplicate accepted inputs converge on the immutable generation; conflicting live inputs refuse; a completed integrate attempt for the same task state cannot be replaced by different parameters. Reconciliation inspects queued/running worker liveness only while that PID may be meaningful. Terminal records do not get a special live-PID escape because every production writer clears `workerPid` when leaving queued/running.

`observe_operation` and `latest_operation_projection` return public task state. Stale or failed pre-boundary attempts may relaunch with the same input, while post-boundary integration recovery stays attached to the irreversible operation. A closeout intent reconciled as unchanged stays at attempt one, is not relaunched implicitly, and remains cancellable; L2 owns an explicit new mutation attempt. Detached launch uses the native subprocess boundary and a private process group.

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

- Each typed public caller owns candidate/authority derivation; the shared core requires those values.
- A closeout candidate tree is captured under the lifecycle lease before compatibility, journal publication, or launch and is reused by duplicates.
- Replacement of an agent or worker process does not change the task address.
- Closeout cancellation refuses only when mutation/finalization evidence retains the accepted
  generation; approval or phase alone is insufficient.
- Stale recovery is idempotent and cannot claim multiple concurrent workers.
- Terminal records cannot retain a meaningful worker PID; production writers clear it outside queued/running.

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
| Typed integrate and lease-bound closeout callers resolve their own authority/candidate before entering the required-value shared core. | `start_or_observe_operation`; `start_or_observe_closeout_operation`; `_start_or_observe_operation` | mcp/src/agents_remember/worktrees/integration/lifecycle_operations.py:109-220 |
| Generation creation/replacement is distinct from recovery, launch, and projection. | `_create_or_replace_generation`; `_recover_launch_and_project`; `_operation_execution` | mcp/src/agents_remember/worktrees/integration/lifecycle_operations.py:223-283 |
| Projection and cancellation expose task state without private operation identifiers. | `observe_operation`; `cancel_operation` | mcp/src/agents_remember/worktrees/integration/lifecycle_operations.py:301-306; mcp/src/agents_remember/worktrees/integration/lifecycle_operations.py:325-368 |
| Closeout reconciliation inspects worker liveness only for queued/running records and derives recovery projection from reconciled evidence. | `_reconcile_closeout_store` | mcp/src/agents_remember/worktrees/integration/lifecycle_operations.py:454-485 |
| Detached launch and queued-record creation preserve the supplied immutable candidate and native process boundary. | `launch_detached_worker`; `_queued_record` | mcp/src/agents_remember/worktrees/integration/lifecycle_operations.py:518-588 |
| An unchanged reconciled intent is not silently relaunched as a new mutation attempt. | `_should_recover` | mcp/src/agents_remember/worktrees/integration/lifecycle_operations.py:793-820 |

## Cross-Repo References

No sibling-repository protocol is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| The controller resolves all repository paths through the selected task contract. | `start_or_observe_operation`; `observe_operation` | mcp/src/agents_remember/worktrees/integration/lifecycle_operations.py:109-151; mcp/src/agents_remember/worktrees/integration/lifecycle_operations.py:301-306 |

## L23 Lifecycle Model Package Review

Lifecycle operation inputs, kinds, and records now come from `models.lifecycles.operation`. Process
launch, status, cancellation, recovery, and native-environment behavior are unchanged by the model
ownership move.

## L23 Final Candidate Disposition

Start-or-observe derives one durable closeout or integration operation from task plus kind and a
validated input fingerprint. Closeout retries validate raw observations against the accepted
immutable plan; recovery reconciles repository-bound mutation evidence and exact finalization
proof rather than replaying cells inferred from progress phases.

## 260815-DAG-L3 Cancellation And Queue Ownership

Pre-boundary cancellation releases the candidate's internal queue ownership through the same
task-addressed operation key. Worker termination is in `finally`: even if queue release fails, the
captured process group is still signalled after the store clears its PID, preventing a retry from
launching beside an orphaned old worker.

## 260815-DAG-L4 Integration-Authority Impact

L4 makes task-derived integration refs mechanically non-ordinary: repository defaults, sprint supers, and active atomic-series refs are censused across code and external memory. Mutation is admitted only through exact lifecycle authority, named-ref compare-and-swap, queue/repository serialization, or a terminal capability; stale topology, aliases, ambient checkouts, and torn recovery fail closed.

## 260821-CLIVE-L1 Closeout Admission Ordering

Generic lifecycle start rejects raw closeout input. The typed integrate caller owns retention, integration authority, and its candidate; lease-bound closeout admission is the sole closeout candidate owner. The closeout path holds the pure contract lease, reloads contract state, captures and normalizes the accepted plan and stable candidate, checks same/cross-kind compatibility, reconciles existing evidence, and only then publishes or launches the generation. The shared core requires the supplied candidate and explicit authority, while generation creation/replacement is separate from recovery/launch/projection. Duplicates validate against the immutable accepted plan. Restart reconciles mutation evidence and repairs derived recovery projection; cancellation is permitted only before retained evidence. Queue state is neither input authority nor lifecycle evidence.

## Update History

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1 candidate-11: rebound typed caller ownership, required-value shared-core flow, generation/recovery separation, reconciliation ordering, and terminal PID reasoning against accepted tree `4241908c`; verification metadata remains pinned until governed closeout stamps the landed code commit.

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
