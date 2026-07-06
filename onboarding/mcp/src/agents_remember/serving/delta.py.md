# mcp/src/agents_remember/serving/delta.py

| Field                  | Value                                       |
| ---------------------- | ------------------------------------------- |
| repository             | agents-remember                             |
| path                   | `mcp/src/agents_remember/serving/delta.py`  |
| doc_type               | `file-level-onboarding`                     |
| lastUpdated            | 2026-07-07T05:06+02:00                      |
| lastVerifiedCommitHash | `6ea2a422210b4b9797d2c7c8df5f9994813f9331`  |
| lastVerifiedCommitDate | 2026-07-06T21:07:46+02:00|
| governingOverview      | `overview.md`                               |

## Purpose

`delta.py` is the **pure** per-entity projection diff — the transport-side computation that
turns two consecutive `WorkspaceProjection` snapshots into the minimal set of named SSE
change events the `state` channel emits. Kept out of the reducer (which produces full
projections), so the observer stays a pure fold. Since 260703-L15 it is also the **change
gate**: comparison runs over *stable forms* (volatile now-relative age fields stripped), so a
tick where only ages advanced emits nothing — the fix for the ~780 KB/tick full-payload
re-emission that OOM'd long-lived dashboard tabs.

## Code Commentary

`VOLATILE_AGE_FIELDS` — the five now-relative age keys recomputed from the tick clock every
projection (`staleSeconds`, `snapshotStaleSeconds`, `ageSeconds`, `waitSeconds`,
`heartbeatAgeSeconds`). Mirrored byte-for-byte client-side (`dashboard/src/data/servedAges.ts`);
both sides carry lockstep tests.

`_strip_volatile` / `_stable_dump` — a node's stable form: the wire dump (by-alias, none-free)
with volatile keys recursively removed. `StableProjectionState` holds one projection's stable
forms (id-keyed per collection + metrics/analytics/activeWorktreeGroups);
`stable_projection_state(projection)` computes them once (~4–5 ms on the ~800 KB live payload).

`DeltaEvent(event, data)` is a frozen dataclass: `event` is the SSE event name
(`lifecycle`, `lifecycle.removed`, `enclosure`, `provider`, `activeWorktreeGroups`, `metrics`,
`analytics`), `data` is an upserted projection node (`BaseModel`) or a `dict` payload (a `{key: id}`
removal marker, or the `activeWorktreeGroups` whole-value wrapper).

`diff_projection(previous, current, *, previous_state=None, current_state=None)` returns `[]` on
the first tick (`previous is None` — the first projection is delivered as the snapshot, not
deltas). Otherwise it diffs the three flat collections via `_collection_deltas` on their stable
forms, and emits a whole-value event for `activeWorktreeGroups` and a whole-block event for
`metrics`/`analytics` when the *stable* forms differ. The optional `*_state` arguments accept
precomputed stable forms — the projector caches the previous tick's so each tick pays for ONE
stable dump — while the pure two-argument call form still works (tests, ad-hoc use). An emitted
node is always the CURRENT model in full, so fresh ages ride along with every real change.

`_collection_deltas(name, current_nodes, previous_stable, current_stable, *, key)` emits an
upsert `DeltaEvent` for every added or stable-changed item (in projection order), and a sorted
set of `*.removed` markers for ids gone from `current`. Sorting removals keeps the output
deterministic (replay/sim fixtures compare byte-for-byte).

## Invariants And Boundaries

- **Pure** — no I/O, no FastAPI import; takes already-built projections.
- **Deterministic ordering** — upserts in projection order, removals sorted by `str(id)`.
- **Volatile-age-insensitive** — a node whose only change is a `VOLATILE_AGE_FIELDS` value never
  emits (measured live: this took the idle stream from ~780 KB/tick to 0 B/tick); the client
  advances displayed ages locally from its arrival anchors, so staleness surfaces stay truthful.
- **Field-set lockstep** with `dashboard/src/data/servedAges.ts` — keep the two sets identical.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The projection schema diffed here (flat, id-keyed collections). | [observer/projection.py](agents-remember/mcp/src/agents_remember/observer/projection.py) |
| The projector that calls this, caches stable forms, and broadcasts. | [projector.py](agents-remember/mcp/src/agents_remember/serving/projector.py) |
| The client mirror of the volatile set + local age advancement. | [servedAges.ts](agents-remember/dashboard/src/data/servedAges.ts) |

## Update History

- 2026-07-07T05:06+02:00 — 260703-L15 S1 (the change gate): comparison moved to stable forms —
  `VOLATILE_AGE_FIELDS`, `_strip_volatile`/`_stable_dump`, `StableProjectionState` +
  `stable_projection_state`, and `diff_projection` gained optional precomputed-state arguments.
  Volatile-only ticks emit nothing (live measurement: 779,889 B/tick → 0).
  Verification metadata pinned until closeout stamps the L15 commit.
- 2026-06-28T07:30+02:00 — Task 33: `diff_projection` now emits an `activeWorktreeGroups` whole-value delta
  (wrapped `{"activeWorktreeGroups": [...]}`, since it is a bare list rather than a keyed node) when the
  set changes, alongside the `metrics`/`analytics` whole-block events. Verification metadata pinned until
  closeout stamps the code commit.
- 2026-06-14T11:30+02:00 — Created for slice 04 commit 4a: the pure `diff_projection` +
  `DeltaEvent` per-entity diff (developer call: per-entity deltas in v1, not deferred).
  Verification metadata pinned until closeout stamps the 4a code commit.
