# mcp/src/agents_remember/worktrees/lifecycle_operations.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/lifecycle_operations.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-12T15:19+02:00 |
| lastVerifiedCommitHash |  `a09b906bbf2855c3479b4d3199607ff8689b7d93`|
| lastVerifiedCommitDate |  2026-08-13T13:51:44+02:00|
| governingOverview | `../../../overview.md` |

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

### Conventions

Public callers supply task plus operation kind, never worker PID, operation key, or record path. Fingerprints are canonical JSON hashes; projections deliberately omit private identity.

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
| Start/observe converges duplicates and binds recovery to canonical task state. | `start_or_observe_operation` | mcp/src/agents_remember/worktrees/lifecycle_operations.py:48-132 |
| Projection and cancellation expose task state without private operation identifiers. | `observe_operation`; `cancel_operation` | mcp/src/agents_remember/worktrees/lifecycle_operations.py:134-212 |
| Detached launch and queued-record creation preserve the immutable candidate and native process boundary. | `launch_detached_worker`; `_queued_record` | mcp/src/agents_remember/worktrees/lifecycle_operations.py:214-297 |

## Cross-Repo References

No sibling-repository protocol is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| The controller resolves all repository paths through the selected task contract. | `start_or_observe_operation`; `observe_operation` | mcp/src/agents_remember/worktrees/lifecycle_operations.py:83-212 |

## L23 Lifecycle Model Package Review

Lifecycle operation inputs, kinds, and records now come from `models.lifecycles.operation`. Process
launch, status, cancellation, recovery, and native-environment behavior are unchanged by the model
ownership move.

## Update History

- 2026-08-13T09:05+02:00 — L23 curator: reviewed the operation-model package move and confirmed no
  lifecycle execution behavior changed; final provenance remains closeout-owned.

- 2026-08-12T16:54+02:00 — 260731-EFA-L23 installed-runtime repair: recorded that detached launch
  preserves the installed MCP `PYTHONPATH` and excludes the task checkout source root while keeping
  task-addressed cwd/contract context. Verification provenance remains closeout-owned.

- 2026-08-12T15:19+02:00 — Created for L23 task-addressed asynchronous lifecycle control; verification provenance remains closeout-owned.
