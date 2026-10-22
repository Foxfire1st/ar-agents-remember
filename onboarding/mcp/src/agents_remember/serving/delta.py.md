# mcp/src/agents_remember/serving/delta.py

## Governing Overview

[overview.md](overview.md)

## Purpose

`delta.py` is the **pure** per-entity projection diff — the transport-side computation that
turns two consecutive `WorkspaceProjection` snapshots into the minimal set of named SSE
change events the `state` channel emits. Kept out of the reducer (which produces full
projections), so the observer stays a pure fold. Since 260703-L15 it is also the **change
gate**: comparison runs over *stable forms* (volatile now-relative age fields stripped), so a
tick where only ages advanced emits nothing — the fix for the ~780 KB/tick full-payload
re-emission that OOM'd long-lived dashboard tabs.

## Code Commentary

`VOLATILE_AGE_FIELDS` — the six now-relative age keys recomputed from the tick clock every
projection (`staleSeconds`, `snapshotStaleSeconds`, `ageSeconds`, `waitSeconds`,
`heartbeatAgeSeconds`, `elapsedSeconds`). Mirrored byte-for-byte client-side (`dashboard/src/data/servedAges.ts`);
both sides carry lockstep tests.

`_strip_volatile` / `_stable_dump` — a node's stable form: the wire dump (by-alias, none-free)
with volatile keys recursively removed. `StableProjectionState` holds one projection's stable
forms (tasks by qualified key, enclosures/providers by their own identities, plus taskCounts/metrics/analytics/activeWorktreeGroups);
`stable_projection_state(projection)` computes them once (~4–5 ms on the ~800 KB live payload).

`DeltaEvent(event, data)` is a frozen transport value: task upserts use `task`, removals `task.removed` with `{key: ...}`, and aggregate count changes use `taskCounts`. Enclosure/provider and activeWorktreeGroups/metrics/analytics events retain their own contracts. There are no lifecycle collection deltas.

`diff_projection(previous, current, *, previous_state=None, current_state=None)` returns `[]` on
the first tick (`previous is None` — the first projection is delivered as the snapshot, not
deltas). Otherwise it diffs the task/enclosure/provider collections via `_collection_deltas` on their stable
forms, and emits a whole-value event for `activeWorktreeGroups` and a whole-block event for
`taskCounts`/`metrics`/`analytics` when the *stable* forms differ. The optional `*_state` arguments accept
precomputed stable forms — the projector caches the previous tick's so each tick pays for ONE
stable dump — while the pure two-argument call form still works (tests, ad-hoc use). An emitted
node is always the CURRENT model in full, so fresh ages ride along with every real change.

`_collection_deltas(name, current_nodes, previous_stable, current_stable, *, key)` emits an
upsert `DeltaEvent` for every added or stable-changed item (in projection order), and a sorted
set of `*.removed` markers for ids gone from `current`. Sorting removals keeps the output
deterministic (replay/sim fixtures compare byte-for-byte).


**L184 — NEW-LIMIT-FROM-REPORT-ONLY.** Deltas are the only update a client sees after the first read, so the fact's removal is realized here. The obligation this leaf records for this place is stated in the invariant named here; the card's earlier account of this file stands, and this paragraph adds what the change made true.

## Invariants And Boundaries

- **Pure** — no I/O, no FastAPI import; takes already-built projections.
- **Deterministic ordering** — upserts in projection order, removals sorted by `str(id)`.
- **Volatile-age-insensitive** — a node whose only change is a `VOLATILE_AGE_FIELDS` value never
  emits (measured live: this took the idle stream from ~780 KB/tick to 0 B/tick); the client
  advances displayed ages locally from its arrival anchors, so staleness surfaces stay truthful.
- **Field-set lockstep** with `dashboard/src/data/servedAges.ts` — keep the two sets identical.

## Evidence

### Repo-Internal References

- WorkspaceProjection version 2 carries native tasks and taskCounts, unbound enclosures, providers, active worktree groups, optional closeout queues, metrics and analytics; each TaskEntry has a qualified key/reference and may own worktrees. Stable diff state keys tasks by entry.key, enclosures by enclosure and providers by id; counts, active groups, metrics and analytics use whole-value comparisons. There is no lifecycles collection in this schema. [1]
- The projector calls the stable-state and diff functions, publishes the projection, and broadcasts resulting items. [2]
- The client mirror of the volatile set + local age advancement. [3]
