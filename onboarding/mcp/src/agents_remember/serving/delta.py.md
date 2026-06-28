# mcp/src/agents_remember/serving/delta.py

| Field                  | Value                                       |
| ---------------------- | ------------------------------------------- |
| repository             | agents-remember                             |
| path                   | `mcp/src/agents_remember/serving/delta.py`  |
| doc_type               | `file-level-onboarding`                     |
| lastUpdated            | 2026-06-14T11:30+02:00                      |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`  |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `overview.md`                               |

## Purpose

`delta.py` is the **pure** per-entity projection diff — the transport-side computation that
turns two consecutive `WorkspaceProjection` snapshots into the minimal set of named SSE
change events the `state` channel emits. Kept out of the reducer (which produces full
projections), so the observer stays a pure fold.

## Code Commentary

`DeltaEvent(event, data)` is a frozen dataclass: `event` is the SSE event name
(`lifecycle`, `lifecycle.removed`, `enclosure`, `provider`, `activeWorktreeGroups`, `metrics`,
`analytics`), `data` is an upserted projection node (`BaseModel`) or a `dict` payload (a `{key: id}`
removal marker, or the `activeWorktreeGroups` whole-value wrapper).

`diff_projection(previous, current)` returns `[]` on the first tick (`previous is None` — the
first projection is delivered as the snapshot, not deltas). Otherwise it diffs the three flat
collections via `_collection_deltas` (lifecycles by `id`, enclosures by `enclosure`,
providers by `id`), and emits a whole-value event for `activeWorktreeGroups` (Task 33 — a bare list,
not a keyed node, so it rides as `{"activeWorktreeGroups": [...]}` and the client unwraps it) and a
whole-block event for `metrics`/`analytics`, each when it differs.

`_collection_deltas(name, previous, current, *, key)` builds by-key dicts, emits an upsert
`DeltaEvent` for every added or changed item (in projection order), and a sorted set of
`*.removed` markers for ids gone from `current`. Sorting removals keeps the output
deterministic (replay/sim fixtures compare byte-for-byte).

## Invariants And Boundaries

- **Pure** — no I/O, no FastAPI import; takes already-built projections.
- **Deterministic ordering** — upserts in projection order, removals sorted by `str(id)`.
- Equality is Pydantic field-wise (`extra="forbid"` models), so an unchanged item never
  emits a delta.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The projection schema diffed here (flat, id-keyed collections). | [observer/projection.py](agents-remember/mcp/src/agents_remember/observer/projection.py) |
| The projector that calls this and broadcasts the result. | [projector.py](agents-remember/mcp/src/agents_remember/serving/projector.py) |

## Update History

- 2026-06-28T07:30+02:00 — Task 33: `diff_projection` now emits an `activeWorktreeGroups` whole-value delta
  (wrapped `{"activeWorktreeGroups": [...]}`, since it is a bare list rather than a keyed node) when the
  set changes, alongside the `metrics`/`analytics` whole-block events. Verification metadata pinned until
  closeout stamps the code commit.
- 2026-06-14T11:30+02:00 — Created for slice 04 commit 4a: the pure `diff_projection` +
  `DeltaEvent` per-entity diff (developer call: per-entity deltas in v1, not deferred).
  Verification metadata pinned until closeout stamps the 4a code commit.
