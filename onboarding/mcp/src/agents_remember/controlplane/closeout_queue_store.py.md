# mcp/src/agents_remember/controlplane/closeout_queue_store.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/controlplane/closeout_queue_store.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-25T15:44+02:00 |
| lastVerifiedCommitHash | `1abeed661cbbf813c7c8a1b651a14dbcf2ad2b4e` |
| lastVerifiedCommitDate | 2026-08-25T17:21:45+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[control-plane overview](overview.md)

## Purpose

Owns bounded persistence and exact-current publication for one sprint's disposable closeout
projection.

## Code Commentary

### Logic

The store derives the contained projection path. Reads degrade malformed, unreadable, or
source-mismatched bytes to invalid-empty. Invalidation publishes durable empty state immediately.
Rebuild writes a complete candidate off-side and takes the short task-publication mutex only to
recheck the exact current source before publishing valid-built.

### Conventions

Canonical task, door, and operation-journal records are the survival evidence. Projection JSON is
disposable and may be invalidated/rebuilt; off-side scratch never becomes a compatibility reader or
secondary authority.

### Invariants And Boundaries

- Task mutation is never blocked by projection state.
- Publication produces only invalid-empty or valid-built state.
- A source change between build and publish leaves the projection invalid-empty.
- No stale member, task freeze, blocker, receipt, claim, commit, or lifecycle fallback survives.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Effective reads fail closed to invalid-empty on bad or stale projection bytes. | `read_effective` | `mcp/src/agents_remember/controlplane/closeout_queue_store.py` |
| Rebuild publishes only after an exact-current source recheck. | `rebuild` | `mcp/src/agents_remember/controlplane/closeout_queue_store.py` |

## Cross-Repo References

No meaningful cross-repository reference applies.

## 260815-DAG-L4 Authority Boundary

L4 routes this file's existing application, configuration, task, model, registration, or memory responsibility through the shared task-derived integration authority. The change preserves the file's owning altitude while ensuring protected code and external-memory refs cannot be mutated through an ordinary workbench or unjournaled helper.

## 260821-CLIVE Final Projection Store

The store is now deliberately disposable. `read_raw` degrades malformed projection bytes to
invalid-empty, and `read_effective` also treats unreadable or source-mismatched state as
invalid-empty. Invalidation durably publishes an empty projection. Rebuild creates the complete
candidate off-side, then takes the short task-publication mutex only to recheck the exact current
source and publish valid-built; otherwise it remains invalid-empty. There is no candidate lifecycle,
receipt, blocker, task-freeze, or stale-row fallback in this store.


## PDLS Reconciliation

Projection persistence now enforces disposable `valid-built` / `invalid-empty` state without retaining stale candidate rows or lifecycle evidence.

This change preserves the file's existing authority boundary. No threshold exception, silent
fallback, or compatibility reader was added.
## Update History

- 2026-08-25T15:44+02:00 — PDLS whole-system reconciliation updated the implementation summary
  above after source and requirement review. Verification remains closeout-owned.


- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: rewrote the authority boundary from mutable queue state to invalid-empty/valid-built disposable projection storage. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-18T09:05+02:00 — Renamed the atomic 'barrier' concept to 'blocker' throughout (terminology unification; no behavioral change). Verification remains closeout-owned.

- 2026-08-15T23:38+02:00 — Reconciled this file's L4 role in task-derived integration authority and protected code/memory boundaries. Verification metadata remains closeout-owned.

- 2026-08-15T09:53+02:00 — No content impact: L3's Pyright repair made the sprint-publication
  callback/result generic explicit; runtime publication, locking, WAL, and recovery behavior are
  unchanged, and verification remains closeout-owned.
- 2026-08-15T09:10+02:00 — Created for L3's bounded canonical queue store, task-fact lock, and sprint-status recovery contract; verification remains closeout-owned.
