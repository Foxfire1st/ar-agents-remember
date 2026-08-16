# mcp/src/agents_remember/controlplane/closeout_queue_store.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/controlplane/closeout_queue_store.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-15T09:10+02:00 |
| lastVerifiedCommitHash | `8bf6edad7e7e65e27cf735be0822f604531d0c8a` |
| lastVerifiedCommitDate | 2026-08-16T10:54:02+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[control-plane overview](overview.md)

## Purpose

Owns bounded, lock-protected persistence for one sprint's canonical closeout-candidate artifact and
its adjacent one-record recovery scratch file.

## Code Commentary

### Logic

The store derives contained task-local artifact paths, serializes public and lifecycle-worker
writers under the durable-store lock, records bounded idempotency receipts, publishes mutations
through a WAL, and recovers before every read or write. The same lock serializes task-fact changes
with lane ownership and atomically coordinates sprint completion/reopen with queue closure.

### Conventions

The canonical JSON state is the survival record; `.closeout-candidates.pending` is recoverable
publication scratch. MCP owns public writes and compaction, while the lifecycle-operation worker is
an explicit writer for internal claim/certify/consume transitions.

### Invariants And Boundaries

- Request ids are stable idempotency keys and cannot be reused with different payloads.
- At most the most recent 128 receipts survive.
- Task facts freeze while a selected or in-flight candidate owns the lane; an atomic barrier also
  excludes topology-changing writes outside its block.
- Completion/reopen publication is recovered against the canonical task status.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Store ownership explicitly includes MCP and lifecycle-operation writers. | "QUEUE_OWNERSHIP = StoreOwnership(" | mcp/src/agents_remember/controlplane/closeout_queue_store.py:27-40 |
| Mutation receipts and WAL publication make request retry idempotent. | `transact` | mcp/src/agents_remember/controlplane/closeout_queue_store.py:97-149 |
| Sprint completion/reopen publication shares the queue lock and enforces quiescence. | `publish_sprint_update` | mcp/src/agents_remember/controlplane/closeout_queue_store.py:151-220 |
| Task-fact publication shares the queue lock with lane and barrier ownership. | `publish_task_facts_update` | mcp/src/agents_remember/controlplane/closeout_queue_store.py:222-265 |
| Recovery either publishes the exact next revision, recognizes it as already published, or refuses divergence. | `_recover` | mcp/src/agents_remember/controlplane/closeout_queue_store.py:267-296 |

## Cross-Repo References

No meaningful cross-repository reference applies.

## 260815-DAG-L4 Authority Boundary

L4 routes this file's existing application, configuration, task, model, registration, or memory responsibility through the shared task-derived integration authority. The change preserves the file's owning altitude while ensuring protected code and external-memory refs cannot be mutated through an ordinary workbench or unjournaled helper.

## Update History

- 2026-08-15T23:38+02:00 — Reconciled this file's L4 role in task-derived integration authority and protected code/memory boundaries. Verification metadata remains closeout-owned.

- 2026-08-15T09:53+02:00 — No content impact: L3's Pyright repair made the sprint-publication
  callback/result generic explicit; runtime publication, locking, WAL, and recovery behavior are
  unchanged, and verification remains closeout-owned.
- 2026-08-15T09:10+02:00 — Created for L3's bounded canonical queue store, task-fact lock, and sprint-status recovery contract; verification remains closeout-owned.
