# mcp/src/agents_remember/worktrees/queue

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `mcp/src/agents_remember/worktrees/queue` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-08-25T17:21+02:00 |
| lastVerifiedCommitHash | `1abeed661cbbf813c7c8a1b651a14dbcf2ad2b4e` |
| lastVerifiedCommitDate | 2026-08-25T17:21:45+02:00|
| governingOverview | `../../../../overview.md` |

## Governing Overview

[mcp overview](../../../../overview.md)

## Purpose

Builds, invalidates, publishes, and serves the disposable sprint closeout scheduling projection.
Canonical task documents and closeout doors are its inputs; the root operation journal owns every
claimed lifecycle after admission.

## Hot Path Summary

Canonical changes invalidate affected sprint projections to invalid-empty. A complete rebuild is
computed off-side from current task topology, canonical waiting doors, and active series authority;
publication occurs only after an exact-current source recheck. `closeout_queue.py` exposes status,
rebuild, and the short first-ready claim-admission fence. Projection member and graph helpers own
only deterministic readiness and order.

## Conventions

- Projection errors and source problems are bounded and typed.
- The projection is evictable; canonical task, door, register, and journal sources are not copied
  into permanent queue authority.

## Invariants And Boundaries

- Only waiting door generations may be projection members.
- Task authoring never waits on or seeks permission from projection state.
- Claim, certification, commit, blocker, integration, and lifecycle evidence never live here.
- Graph-less atomic-sequential topology is valid; a graph, when present, contributes bounded order.

## 260821-CLIVE Final Disposable Projection Route

This route is a current scheduling projection, not a lifecycle subsystem. The canonical transaction
is intentionally simple:

```text
task or door mutation
  -> invalidate affected sprint projections to invalid-empty
  -> rebuild from current task topology + canonical waiting doors
  -> recheck the exact source fingerprint under the short task CAS
  -> publish valid-built, or remain invalid-empty
```

`closeout_projection.py` captures the bounded canonical census;
`closeout_projection_members.py` recomputes readiness and deterministic priority/graph order; and
`closeout_projection_publication.py` owns invalidation, preview, off-side rebuild, and exact-current
publication. `closeout_queue.py` exposes status/rebuild and the short first-ready claim admission
check. `closeout_queue_graph.py` owns only bounded DAG/order facts, while
`closeout_queue_evidence.py` retains canonical grade/admission source parsing.

Prior projection rows are never rebuild input. Only waiting door generations may be members.
Projection state cannot claim, certify, consume, block, release, abort, carry commits, or own
integration/lifecycle evidence. Task authoring is never subordinate to projection state. The five
deleted mutable-queue modules have no tombstones: still-current evidence moved to door source and
evidence owners; claim/cancel/supersede moved to the root operation journal; protected-ref exclusion
moved to atomic landing authority; and mutable blocker, `QueueBinding`, certification, consumption,
and action-driven initial-state contracts were retired rather than preserved as compatibility code.

## 260824-PDLS Final Projection Boundary

Queue construction, membership, evidence parsing, and publication now operate only on current task
truth and waiting door generations. Invalidation publishes invalid-empty state, rebuild derives a
fresh valid-built projection, and no queue row owns retry, claim, commit, certification, terminal,
or compatibility evidence.

## Update History

- 2026-08-25T17:21+02:00 — Reconciled queue parsing and publication with disposable projection
  ownership. Verification remains closeout-owned.

- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: replaced the transitional mutable queue route with invalidation/rebuild-only disposable projection ownership and removed obsolete queue cards. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-24T00:27+02:00 — 260821-CLIVE-L2 committed-route reconciliation: documented `closeout_queue_state.py` while preserving the explicit current-L2 versus waiting-only-L3 boundary, and verified the governed route at code commit `1d446724d099517f6f52d596b47827ae2391a2a4`.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: refreshed current route intent and source evidence for the accepted full L2 candidate; verification provenance and contract-scoped quality enforcement remain architect-closeout-owned.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: route claims reconciled to accepted candidate tree `4241908c`; verification metadata remains closeout-owned.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: created the `worktrees/queue` route —
  ten modules moved from `worktrees/` (flat) and `worktrees/modules/`. Verified at code commit
  e5cb139f.
