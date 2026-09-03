# mcp/src/agents_remember/worktrees/integration/lifecycle/worker/child_processes.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/lifecycle/worker/child_processes.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-29T16:10+02:00 |
| lastVerifiedCommitHash |  `60e429d17e9fcbca3ab1c02563afcaa5761b8c5a`|
| lastVerifiedCommitDate |  2026-08-29T20:33:10+02:00|
| governingOverview | `../../overview.md` |

## Governing Overview

[worktree integration overview](../../overview.md)

## Purpose

Owns the `Popen` objects for detached lifecycle workers until one dedicated waiter has reaped each
child. This is process-ownership infrastructure, separate from the pidfd signaling boundary.

## Code Commentary

### Logic

`DetachedWorkerChildren.retain` records the exact process object under its numeric PID, treats a
second retain of that same object as idempotent, and refuses a different object using the same PID.
It then starts one daemon waiter. `_wait_and_release` calls `Popen.wait()` and removes the registry
entry only if the completed object is still the exact owner. `retain_detached_worker_child` exposes
the single process-transfer seam used after lifecycle-worker launch.

### Conventions

The launching process retains the real `Popen`; the detached child is not reduced to a PID before
ownership transfers. Registry mutation is protected by one lock, while blocking `wait()` happens
outside that lock.

### Invariants And Boundaries

- Every successfully launched detached worker has an owning `Popen` until it is reaped.
- PID reuse cannot cause one waiter to remove a successor's registry entry.
- This module does not signal processes, inspect pidfds, or provide a `killpg` fallback.
- Reaping is not proof of lifecycle cancellation; termination evidence remains owned by
  `termination.py` and the lifecycle journal.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies to this repository-owned process boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external source is required for the in-process ownership contract. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Retention is idempotent for the same object, refuses PID aliasing, and starts one waiter. | "def retain(self, process: subprocess.Popen[Any]) -> None:" | mcp/src/agents_remember/worktrees/integration/lifecycle/worker/child_processes.py:10-30 |
| The waiter reaps through `Popen.wait()` and releases only the exact retained owner. | "def _wait_and_release(self, process: subprocess.Popen[Any]) -> None:" | mcp/src/agents_remember/worktrees/integration/lifecycle/worker/child_processes.py:32-38 |
| Lifecycle launch transfers the real child object to this owner. | "def retain_detached_worker_child(process: subprocess.Popen[Any]) -> None:"; "retain_detached_worker_child(process)" | mcp/src/agents_remember/worktrees/integration/lifecycle/worker/child_processes.py:41-47; mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operations.py:969-969 |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| The owner operates only on children launched by this MCP process. | — | — |

## Update History

- 2026-08-29T16:10+02:00 — Created for the Python 3.13 runtime migration's separate child-ownership
  and reaping correction. Verification remains closeout-owned.
