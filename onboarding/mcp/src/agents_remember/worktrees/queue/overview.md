# mcp/src/agents_remember/worktrees/queue

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `mcp/src/agents_remember/worktrees/queue` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-09-01T03:58+02:00 |
| lastVerifiedCommitHash | `47c8d102c2430d5337dbe207d4601efb4844fec0` |
| lastVerifiedCommitDate | 2026-09-01T08:53:56+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[worktrees overview](../overview.md)

## Purpose

Builds, invalidates, publishes, and serves the disposable sprint closeout scheduling projection.
Canonical task documents and closeout doors are its inputs; the root operation journal owns every
claimed lifecycle after admission.

## Hot Path Summary

Canonical changes invalidate affected sprint projections to invalid-empty. A complete rebuild is
computed off-side from current task topology, canonical waiting doors, and source-pair activation;
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
- Activation is read-only input: the selected master can be active or reconciling, and every other
  live series projects as paused. The queue cannot select, release, or repair that authority.

## IAS Closeout-Recovery Ledger Boundary

`closeout_recovery.py` remains in this transitional package location but owns journal recovery,
not queue authority. It reuses an exact current code/memory edge idempotently and prepends a new
ledger row when unchanged code acquires a later memory state. Older same-code rows remain audit
history; malformed bytes, wrong heads, and unreachable content still fail closed.

## IAS Source-Pair Activation Projection

Multiple live atomic-series contracts for one protected source pair are normal. The queue observes
the single disposable activation snapshot and derives only a waiting reason: unselected,
reconciling, or paused by another selected master. A malformed snapshot becomes a typed projection
source problem with an explicit selecting repair; rebuild does not infer a winner from prior queue
rows, task ordering, a contract census, or ambient Git.

This does not subordinate task authoring to selection. Task mutation publishes canonical truth,
invalidates the affected projection to empty, and causes a rebuild from that new truth. Selection
and sync lifecycle remain separate worktree authorities, so invalidation cannot destroy retained
conflicts, commit evidence, or an in-flight operation.

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
check. `closeout_queue_graph.py` owns the queue adapter around the task domain's one bounded,
deep-immutable semantic graph index, while
`closeout_queue_evidence.py` retains canonical grade/admission source parsing.

`closeout_projection_source_facts.py` makes currentness inputs explicit: one source plane contains
task address plus only fields classified as completion readiness, and a second contains the
`semantic-topology/v2` fingerprint. `closeout_projection_snapshot.py` freezes one exact readable,
classified census before publication. Whole task documents, private v1 topology tables, and old
projection rows are not source inputs.

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

## MCAR-L02 Structured Curator Evidence

The queue evidence adapter no longer parses a stable Markdown filename. It delegates curator
evidence to the closeout integration route's sole structured currentness validator, then converts
that exact evidence list into door/projection facts. Generated reports are evidence bytes only;
historical files cannot compete with the stable manifest.

## 260831-CCR-L01 Semantic Source Planes

Member readiness now receives one already-computed task-domain topology fingerprint. Queue adapters
translate typed topology refusals without changing status/detail and never maintain a parallel
identity algorithm. Graph-backed rebuild resolves and compares the authored graph once, substitutes
the sole immutable bound graph into the sprint context, and reuses its indexes for every candidate.
Graphless atomic-sequential mode remains explicit and valid.

## Update History

- 2026-09-01T03:58+02:00 — 260831-CCR-L01 Attempt 8: separated completion-readiness and
  `semantic-topology/v2` source planes, added immutable source snapshots, and bound all graph-backed
  member reads to one task-domain index. Verification remains closeout-owned.

- 2026-08-29T08:52+02:00 — Replaced curator Markdown parsing with the shared structured authority
  validator. Verification remains closeout-owned.

- 2026-08-26T14:32+02:00 — Documented the closeout-recovery ledger distinction without expanding
  queue authority: exact current reuse is idempotent and later same-code memory state appends
  history.

- 2026-08-26T02:55+02:00 — Direct IAS architecture refresh: linked the new worktrees parent
  overview and recorded activation as read-only scheduling input. Multiple live series are normal;
  task authoring stays upstream, and the queue gains no selection or lifecycle authority.

- 2026-08-25T17:21+02:00 — Reconciled queue parsing and publication with disposable projection
  ownership. Verification remains closeout-owned.

- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: replaced the transitional mutable queue route with invalidation/rebuild-only disposable projection ownership and removed obsolete queue cards. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-24T00:27+02:00 — 260821-CLIVE-L2 committed-route reconciliation: documented `closeout_queue_state.py` while preserving the explicit current-L2 versus waiting-only-L3 boundary, and verified the governed route at code commit `1d446724d099517f6f52d596b47827ae2391a2a4`.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: refreshed current route intent and source evidence for the accepted full L2 candidate; verification provenance and contract-scoped quality enforcement remain architect-closeout-owned.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: route claims reconciled to accepted candidate tree `4241908c`; verification metadata remains closeout-owned.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: created the `worktrees/queue` route —
  ten modules moved from `worktrees/` (flat) and `worktrees/modules/`. Verified at code commit
  e5cb139f.
