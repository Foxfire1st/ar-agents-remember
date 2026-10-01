# mcp/src/agents_remember/controlplane/closeout_queue_store.py

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

## Evidence

### Docs References

No configured Domain Documentation source applies.

### Repo-Internal References

- Effective reads fail closed to invalid-empty on bad or stale projection bytes. [1]
- Rebuild publishes only after an exact-current source recheck. [2]

### Cross-Repo References

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
