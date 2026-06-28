# mcp/src/agents_remember/serving/projector.py

| Field                  | Value                                          |
| ---------------------- | ---------------------------------------------- |
| repository             | agents-remember                                |
| path                   | `mcp/src/agents_remember/serving/projector.py` |
| doc_type               | `file-level-onboarding`                        |
| lastUpdated            | 2026-06-28T03:02+02:00                         |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`     |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `overview.md`                                  |

## Purpose

`projector.py` is the single shared projection loop fanned out to every SSE client: it ticks
`project_and_write`, diffs each new projection against the last, and broadcasts per-entity
deltas. N clients cost one re-projection per tick — what makes the single multiplexed
EventSource scale. Two seams (`now`, `before_tick`) keep it generic across live and sim (4b).

## Code Commentary

`Projector(config, *, interval=1.0, now=None, before_tick=None, provider_refresher=None)` holds the latest
`WorkspaceProjection`, a monotonic sequence counter, and a set of per-connection `asyncio.Queue`
subscribers. `now` is the clock the tick projects at (defaults to `_utcnow`, wall-clock UTC
re-read every tick); `before_tick` is an optional hook run with that same moment just before each
projection (sim feeds the next due fixture events through it). `provider_refresher` follows the
`ProviderStateRefresh` protocol and is passed into `project_and_write` after `before_tick`, so live
dashboards can refresh provider current-state while sim/replay tests can keep projection inputs fixed.
Both default to live behaviour.

- `prime()` computes the first projection (so the first client gets an immediate snapshot); it is
  resilient — a failure is logged and left for the tick loop to retry (the app serves `503` from
  `/api/state` until a tick succeeds).
- `run()` is the tick loop: `await sleep(interval)`, then `_tick_sync(self._now())` in a worker
  thread, `diff_projection` the result against the previous, bump the sequence per delta and
  `_broadcast`. A broad `except` around the tick keeps one bad read from killing the loop.
- `_tick_sync(moment)` (off the loop thread) runs `before_tick(moment)` if set, then returns
  `project_and_write(config, now=moment, provider_refresher=...)` — so the feeder write,
  optional provider refresh, and re-projection share one moment.
- `current()` returns `(seq, latest)` for a new connection's snapshot.
- `subscribe()` is an async generator: it registers a fresh queue, yields `(seq, delta)` items,
  and discards the queue in `finally` when the consumer stops.

## Invariants And Boundaries

- **One re-projection per tick**, regardless of client count (fan-out, not per-connection
  projection).
- **Reads only through `McpRuntimeConfig`** (NS #5) — `project_and_write` owns path resolution;
  no host paths here.
- `_tick_sync` runs in a thread so its blocking file I/O (feeder append + projection write) never
  stalls the event loop.
- **Sim is a seam, not a fork:** `now`/`before_tick` default to live; the same loop drives sim
  with a replay clock + fixture feeder, so the SSE output is byte-identical.
- The diff lives in `delta.py` (pure); this module only orchestrates and broadcasts.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The tick entry it drives (read → fold → atomic write), accepting the `now` seam. | [observer/projection_store.py](agents-remember/mcp/src/agents_remember/observer/projection_store.py) |
| The pure per-entity diff it broadcasts. | [delta.py](agents-remember/mcp/src/agents_remember/serving/delta.py) |
| The app that starts/stops the loop and subscribes connections. | [app.py](agents-remember/mcp/src/agents_remember/serving/app.py) |
| The sim clock + feeder that drive the `now`/`before_tick` seams. | [sim.py](agents-remember/mcp/src/agents_remember/serving/sim.py) |

## Update History

- 2026-06-27T23:08+02:00 — Task 31 provider-state honesty: `Projector` now accepts an optional provider refresher and passes it to `project_and_write` on each tick, keeping sim fixed-input and live dashboard refresh behavior separate. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-14T11:30+02:00 — Updated for slice 04 commit 4b: added the `now` and `before_tick`
  seams and the `_tick_sync(moment)` helper (one moment per tick, shared by the feeder hook and
  `project_and_write`) so sim replays through the same loop. Verification metadata pinned until
  closeout stamps the 4b code commit.
- 2026-06-14T11:30+02:00 — Created for slice 04 commit 4a: the shared `Projector`
  (prime/run/current/subscribe) tick-and-fan-out loop. Verification metadata pinned until
  closeout stamps the 4a code commit.
