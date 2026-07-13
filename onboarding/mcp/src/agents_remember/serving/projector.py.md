# mcp/src/agents_remember/serving/projector.py

| Field                  | Value                                          |
| ---------------------- | ---------------------------------------------- |
| repository             | agents-remember                                |
| path                   | `mcp/src/agents_remember/serving/projector.py` |
| doc_type               | `file-level-onboarding`                        |
| lastUpdated            | 2026-07-12T20:24+02:00                         |
| lastVerifiedCommitHash | `b120efbfda76931cfa8eb9f24c9a808a62c10d1e`     |
| lastVerifiedCommitDate | 2026-07-13T12:33:57+02:00|
| governingOverview      | `overview.md`                                  |

## Purpose

`projector.py` is the single shared projection loop fanned out to every SSE client: it ticks
`project_and_write`, diffs each new projection against the last on their *stable forms*
(260703-L15), and broadcasts per-entity deltas. N clients cost one re-projection per tick — what
makes the single multiplexed EventSource scale. Two seams (`now`, `before_tick`) keep it generic
across live and sim (4b). Because the diff ignores volatile ages, the sequence counter only
advances on real content changes — making `revision` a truthful `/api/state` ETag fingerprint.
Since **260712-PTS-L3** the pacemaker is adaptive: with an injected `change_watcher` the loop wakes
on debounced input changes or an idle heartbeat instead of an unconditional `sleep(interval)` — a
quiet daemon idles near zero CPU (py-spy 2026-07-12 had `_tick_sync` at 11.1s of a 15s sample under
the old 1s always-tick) while the tick body stays byte-identical.

## Code Commentary

`Projector(config, *, interval=1.0, heartbeat=None, now=None, before_tick=None,
provider_refresher=None, landing_refresher=None, change_watcher=None)` holds the
published `(seq, WorkspaceProjection)` tuple, the previous tick's `StableProjectionState`, a boot
nonce, and a set of per-connection `asyncio.Queue` subscribers. `now` is the clock the tick
projects at (defaults to `_utcnow`, wall-clock UTC re-read every tick); `before_tick` is an
optional hook run with that same moment just before each projection (sim feeds the next due
fixture events through it). `provider_refresher` follows the `ProviderStateRefresh` protocol and
is passed into `project_and_write` after `before_tick`. All default to live behaviour.

- `prime()` computes the first projection (so the first client gets an immediate snapshot) and
  seeds the stable-form cache; it is resilient — a failure is logged and left for the tick loop
  to retry (the app serves `503` from `/api/state` until a tick succeeds).
- `run()` is the tick loop: wait for the next wake — `await self._pacer.wait()` when a
  `change_watcher` was injected (260712-PTS-L3: the `ChangePacer` built in `__init__` with
  `heartbeat` when not `None`, else `DEFAULT_HEARTBEAT_SECONDS`; the wait's return value lands in
  `last_wake_reason`),
  otherwise the exact legacy `await sleep(interval)` — then `_tick_sync(self._now())` in a worker
  thread, compute the new tick's `stable_projection_state` ONCE, `diff_projection` against the
  previous with both cached stable forms, bump the sequence per delta and `_broadcast`, then
  publish `(seq, current)` as ONE tuple. A broad `except` around the tick keeps one bad read
  from killing the loop; `projection_count` increments per successful projection (R7 tests + ops
  instrumentation, alongside `last_wake_reason`: `"change"`/`"heartbeat"`/`"interval"`).
- **Watch-task lifecycle (260712-PTS-L3)** mirrors the landing-refresher task: `run()` starts
  `self._change_watcher.run(self._pacer)` as a task, and shutdown cancels-and-awaits both through
  the shared `_shutdown_task` helper (a stored exception from an already-dead task is logged, never
  allowed to replace the Projector cancellation and skip the lifespan's terminal-host cleanup). The
  watch task gets an `add_done_callback(self._on_watch_task_done)`: a watcher task that dies (or
  returns) must not leave the pacer believing changes are still detected — that would silently
  stretch every wake to the heartbeat — so the callback logs a loud ERROR and flips
  `set_watcher_healthy(False)`, degrading to fixed-interval ticking (R7 fail-open).
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
  with a replay clock + fixture feeder, so the SSE output is byte-identical. Sim (and every
  injected-`now()` test) gets NO pacer — `change_watcher=None` keeps the exact legacy
  `sleep(interval)` pacemaker, because the sim feeder writes only *inside* a tick and a
  change-gated loop would never wake.
- **Adaptive waking changes when a tick runs, never what it does (260712-PTS-L3).** Freshness
  bounds: a change becomes an SSE delta within debounce + projection time (floored to one
  projection per `interval` when busy); with no changes, `/api/state` staleness and time-derived
  field resolution are bounded by the heartbeat (default 15s). A failed/absent watcher degrades
  LOUDLY to the legacy fixed-interval ticking — fail-open, never fail-silent, never a crash.
- The diff lives in `delta.py` (pure); this module only orchestrates, caches, and broadcasts.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The tick entry it drives (read → fold → atomic write), accepting the `now` seam. | [observer/projection_store.py](agents-remember/mcp/src/agents_remember/observer/projection_store.py) |
| The pure stable-form diff it broadcasts + the volatile field set. | [delta.py](agents-remember/mcp/src/agents_remember/serving/delta.py) |
| The change-driven pacing pieces (260712-PTS-L3): the `ChangePacer` this loop awaits, the `ChangeWatch` protocol seam, and the live `ProjectionInputWatcher`. | [change_watcher.py](agents-remember/mcp/src/agents_remember/serving/change_watcher.py) |
| The adaptive-projector regressions (L212-L387): heartbeat-only quiet world, debounce-bounded change latency, burst coalescing, loud degrade on missing wheel/crashed watcher, watch-task lifecycle ownership, and legacy pacing without a watcher. | [test_change_watcher.py](agents-remember/mcp/tests/test_change_watcher.py) |
| The app that starts/stops the loop, subscribes connections, and serves `revision` as the ETag. | [app.py](agents-remember/mcp/src/agents_remember/serving/app.py) |
| The sim clock + feeder that drive the `now`/`before_tick` seams. | [sim.py](agents-remember/mcp/src/agents_remember/serving/sim.py) |

## Update History
- 2026-07-12T20:24+02:00 — 260712-PTS-L3: the unconditional `sleep(interval)` pacemaker became
  change-or-heartbeat waking when a `change_watcher` is injected (`ChangePacer` built with
  `heartbeat` when not `None`, else `DEFAULT_HEARTBEAT_SECONDS`; no watcher ⇒ exact legacy pacing,
  which sim and injected-`now()` tests keep). Tick body, prime, diff/broadcast, and ETag revision untouched.
  Watch-task lifecycle mirrors the landing-refresher task (shared `_shutdown_task` helper);
  `_on_watch_task_done` degrades a dead watcher loudly to fixed-interval ticking (R7 fail-open).
  Added `projection_count`/`last_wake_reason` instrumentation. Verification metadata pinned until
  closeout stamps the PTS-L3 commit.
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
