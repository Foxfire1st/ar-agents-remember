# mcp/src/agents_remember/serving/delta.py

| Field                  | Value                                       |
| ---------------------- | ------------------------------------------- |
| repository             | agents-remember                             |
| path                   | `mcp/src/agents_remember/serving/delta.py`  |
| doc_type               | `file-level-onboarding`                     |
| lastUpdated            | 2026-07-07T05:06+02:00                      |
| lastVerifiedCommitHash | `28a66feae742bf02fe4b647388b220f921cc7007`  |
| lastVerifiedCommitDate | 2026-08-15T03:44:49+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| The projection schema diffed here (flat, id-keyed collections). | "class WorkspaceProjection(BaseModel):"; "lifecycles: list[LifecycleProjection]"; "enclosures: list[EnclosureNode]"; "providers: list[ProviderNode]"; "metrics: Metrics"; "analytics: Analytics" | mcp/src/agents_remember/observer/projection.py:1026-1026; mcp/src/agents_remember/observer/projection.py:1033-1035; mcp/src/agents_remember/observer/projection.py:1044-1045 |
| The projector calls the stable-state and diff functions, publishes the projection, and broadcasts resulting items. | "class Projector:"; "def stable_projection_state("; "def diff_projection("; "def _publish_projection("; "def _broadcast(" | mcp/src/agents_remember/serving/delta.py:83-83; mcp/src/agents_remember/serving/delta.py:109-109; mcp/src/agents_remember/serving/projector.py:131-131; mcp/src/agents_remember/serving/projector.py:292-292; mcp/src/agents_remember/serving/projector.py:334-334 |
| The client mirror of the volatile set + local age advancement. | `VOLATILE_AGE_FIELDS`; `stampServed`; `servedAgeSeconds` | dashboard/src/data/servedAges.ts:16-22; dashboard/src/data/servedAges.ts:59-61; dashboard/src/data/servedAges.ts:68-78 |

## Update History
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-03T03:56+02:00 — 260731-EFA-L6 W3-B10 curator: anchored 3 table citations and normalized 3 source paths; no unresolved Tier-3 claims.

- 2026-07-31T16:35+02:00 — No content impact: the only change to
  `mcp/src/agents_remember/serving/delta.py` since the L2 base commit is the whole-tree `ruff
  format` pass in `00e8379`, which re-wrapped 3 line(s) with no token change whatsoever. Checked
  by parsing both revisions and comparing the abstract syntax trees (identical) and the comment
  tokens (identical), so no symbol, signature, default, decorator, control-flow branch, docstring,
  or assertion this card describes has moved, and every claim this card makes about its own source
  still holds.

- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator ATTESTATION: this file was touched by the whole-tree `ruff format` commit (`00e8379`) and by nothing else — `git diff 00e8379 -- <this file>` is empty, so no identifier, signature, branch or behaviour in it changed in this leaf and no claim in this sidecar can have been invalidated by it. Attested, deliberately not rewritten.
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
