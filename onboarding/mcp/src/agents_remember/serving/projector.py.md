# mcp/src/agents_remember/serving/projector.py

| Field                  | Value                                          |
| ---------------------- | ---------------------------------------------- |
| repository             | agents-remember                                |
| path                   | `mcp/src/agents_remember/serving/projector.py` |
| doc_type               | `file-level-onboarding`                        |
| lastUpdated            | 2026-07-07T05:08+02:00                         |
| lastVerifiedCommitHash | `300664e63f2dbb5f0701d37bbc17ff5358960c77`     |
| lastVerifiedCommitDate | 2026-07-12T18:11:57+02:00|
| governingOverview      | `overview.md`                                  |

## Purpose

`projector.py` is the single shared projection loop fanned out to every SSE client: it ticks
`project_and_write`, diffs each new projection against the last on their *stable forms*
(260703-L15), and broadcasts per-entity deltas. N clients cost one re-projection per tick — what
makes the single multiplexed EventSource scale. Two seams (`now`, `before_tick`) keep it generic
across live and sim (4b). Because the diff ignores volatile ages, the sequence counter only
advances on real content changes — making `revision` a truthful `/api/state` ETag fingerprint.

## Code Commentary

`Projector(config, *, interval=1.0, now=None, before_tick=None, provider_refresher=None)` holds the
published `(seq, WorkspaceProjection)` tuple, the previous tick's `StableProjectionState`, a boot
nonce, and a set of per-connection `asyncio.Queue` subscribers. `now` is the clock the tick
projects at (defaults to `_utcnow`, wall-clock UTC re-read every tick); `before_tick` is an
optional hook run with that same moment just before each projection (sim feeds the next due
fixture events through it). `provider_refresher` follows the `ProviderStateRefresh` protocol and
is passed into `project_and_write` after `before_tick`. All default to live behaviour.

- `prime()` computes the first projection (so the first client gets an immediate snapshot) and
  seeds the stable-form cache; it is resilient — a failure is logged and left for the tick loop
  to retry (the app serves `503` from `/api/state` until a tick succeeds).
- `run()` is the tick loop: `await sleep(interval)`, then `_tick_sync(self._now())` in a worker
  thread, compute the new tick's `stable_projection_state` ONCE, `diff_projection` against the
  previous with both cached stable forms, bump the sequence per delta and `_broadcast`, then
  publish `(seq, current)` as ONE tuple. A broad `except` around the tick keeps one bad read
  from killing the loop.
- **Atomic publish** — `/api/state` runs in a FastAPI threadpool, so `(seq, projection)` live in
  a single `_published` tuple; two separate attributes could tear (a bumped seq read against the
  previous snapshot would hand a poller a stale body under a fresh ETag).
- `_tick_sync(moment)` (off the loop thread) runs `before_tick(moment)` if set, then returns
  `project_and_write(config, now=moment, provider_refresher=...)`.
- `current()` returns the published `(seq, latest)` for a new connection's snapshot.
- `revision(seq)` returns `"{boot_id}-{seq}"` — the opaque content fingerprint `/api/state`
  serves as its weak ETag. The boot nonce (`uuid4().hex[:12]`) exists because seq restarts at 0
  on every process start: without it a client holding `"…-0"` from the previous process would
  304 against different content.
- `subscribe()` is an async generator: it registers a fresh queue, yields `(seq, delta)` items,
  and discards the queue in `finally` when the consumer stops.

### 260712-TRH-L7 projector/observer boundary

`Projector.run` starts the bounded refresher once, passes its current snapshot into each local projection tick, and cancels it during shutdown. A stored refresher exception is logged rather than replacing the projector cancellation path.

## Invariants And Boundaries

- **One re-projection per tick**, regardless of client count (fan-out, not per-connection
  projection); since L15 also **one stable dump per tick** (the previous tick's is cached).
- **seq advances only on content change** — the stable-form diff makes the sequence a content
  revision; volatile-age-only ticks broadcast nothing and mint no new revision.
- **Reads only through `McpRuntimeConfig`** (NS #5) — `project_and_write` owns path resolution;
  no host paths here.
- `_tick_sync` runs in a thread so its blocking file I/O never stalls the event loop.
- **Sim is a seam, not a fork:** `now`/`before_tick` default to live; the same loop drives sim
  with a replay clock + fixture feeder, so the SSE output is byte-identical.
- The diff lives in `delta.py` (pure); this module only orchestrates, caches, and broadcasts.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The tick entry it drives (read → fold → atomic write), accepting the `now` seam. | [observer/projection_store.py](agents-remember/mcp/src/agents_remember/observer/projection_store.py) |
| The pure stable-form diff it broadcasts + the volatile field set. | [delta.py](agents-remember/mcp/src/agents_remember/serving/delta.py) |
| The app that starts/stops the loop, subscribes connections, and serves `revision` as the ETag. | [app.py](agents-remember/mcp/src/agents_remember/serving/app.py) |
| The sim clock + feeder that drive the `now`/`before_tick` seams. | [sim.py](agents-remember/mcp/src/agents_remember/serving/sim.py) |

## Update History
- 2026-07-12T17:30+02:00 — 260712-TRH-L7: Projector owns refresher startup/cancellation, consumes network-free snapshots, and logs a dead refresher during cancellation so lifecycle shutdown continues safely.

- 2026-07-07T05:08+02:00 — 260703-L15 S1: stable-form diffing with a per-tick cache
  (`_latest_stable`), atomic `(seq, projection)` publish (`_published` tuple; threadpool tear
  guard), and the `revision(seq)` content fingerprint (boot nonce + seq) behind the `/api/state`
  ETag. Verification metadata pinned until closeout stamps the L15 commit.
- 2026-06-27T23:08+02:00 — Task 31 provider-state honesty: `Projector` now accepts an optional provider refresher and passes it to `project_and_write` on each tick, keeping sim fixed-input and live dashboard refresh behavior separate. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-14T11:30+02:00 — Updated for slice 04 commit 4b: added the `now` and `before_tick`
  seams and the `_tick_sync(moment)` helper (one moment per tick, shared by the feeder hook and
  `project_and_write`) so sim replays through the same loop. Verification metadata pinned until
  closeout stamps the 4b code commit.
- 2026-06-14T11:30+02:00 — Created for slice 04 commit 4a: the shared `Projector`
  (prime/run/current/subscribe) tick-and-fan-out loop. Verification metadata pinned until
  closeout stamps the 4a code commit.
