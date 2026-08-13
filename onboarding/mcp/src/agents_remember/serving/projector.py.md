# mcp/src/agents_remember/serving/projector.py

| Field                  | Value                                          |
| ---------------------- | ---------------------------------------------- |
| repository             | agents-remember                                |
| path                   | `mcp/src/agents_remember/serving/projector.py` |
| doc_type               | `file-level-onboarding`                        |
| lastUpdated | 2026-07-30T12:51+02:00 |
| lastVerifiedCommitHash | `1580f92715ff93c988f9a15439ad9bec60ef4c5d`     |
| lastVerifiedCommitDate | 2026-08-13T00:18:59+02:00|
| governingOverview      | `overview.md`                                  |

## Governing Overview

[serving route overview](overview.md)

## Purpose

`projector.py` is the single shared projection loop fanned out to every SSE client: it ticks
`project_and_write`, derives snapshot or per-entity events from each successful projection, commits
the `(sequence, projection)` authority, and only then notifies every registered SSE subscriber. N
clients still cost one re-projection per tick. The subscriber boundary is now atomic as well:
registration and current-snapshot capture happen with no await between them, so a transition is
either present in the captured snapshot or queued for that subscriber, never lost between two
owners. If `prime()` failed, the first successful tick publishes one full recovery snapshot before
ordinary stable-form deltas resume; an identical later projection emits nothing.

Two seams (`now`, `before_tick`) keep the loop generic across live and sim. Because the stable-form
diff ignores volatile ages, the sequence advances only on real content changes and remains a
truthful `/api/state` ETag component. Since **260712-PTS-L3** an injected `change_watcher` wakes the
loop on debounced input changes or an idle heartbeat; without one, fixed-interval pacing remains.

## Code Commentary

### Logic

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
  thread and hand the successful projection to `_publish_projection()`. A broad `except` around the
  tick keeps one bad read from killing the loop; `projection_count` increments per successful
  projection (R7 tests + ops instrumentation, alongside `last_wake_reason`:
  `"change"`/`"heartbeat"`/`"interval"`).
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
- `_publish_projection(current)` is the only successful-tick publication boundary. It computes the
  stable state and event batch first, emits a full `snapshot` only when prior authority is absent,
  increments sequence numbers, commits `_latest_stable` and `_published`, then broadcasts the
  prepared items. Because the method contains no await, a subscription cannot interleave between
  commit and notification.
- `current()` returns the atomically published `(seq, latest)` for `/api/state` and revision reads.
- `revision(seq)` returns `"{boot_id}-{seq}"` — the opaque content fingerprint `/api/state`
  serves as its weak ETag. The boot nonce (`uuid4().hex[:12]`) exists because seq restarts at 0
  on every process start: without it a client holding `"…-0"` from the previous process would
  304 against different content.
- `subscribe()` is the complete SSE subscription authority: it registers a fresh queue and captures
  `_published` in the same event-loop activation, yields the captured projection as a `snapshot`
  when present, then drains queued events. Its `finally` discards exactly that queue when the
  consumer closes or is cancelled.

### 260712-TRH-L7 projector/observer boundary

`Projector.run` starts the bounded refresher once, passes its current snapshot into each local projection tick, and cancels it during shutdown. A stored refresher exception is logged rather than replacing the projector cancellation path.

### Invariants And Boundaries

- **One re-projection per tick**, regardless of client count (fan-out, not per-connection
  projection); since L15 also **one stable dump per tick** (the previous tick's is cached).
- **No snapshot/subscription handoff gap.** Queue registration precedes `_published` capture with no
  await, so each state transition is observed exactly through the captured snapshot or that queue.
- **First recovery is full authority, not an empty diff.** A successful tick after failed `prime()`
  emits one full snapshot; publishing the identical recovered state emits nothing, and later real
  changes return to named deltas.
- **Publish before notify.** `_latest_stable` and `_published` commit before any subscriber queue is
  notified, keeping `/api/state`, later subscribers, and existing subscribers on one authority.
- **Subscriber cleanup is explicit.** The generator's `finally` removes the exact queue on ordinary
  close or cancellation; the app owns outer closure with `contextlib.aclosing()`.
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

### Conventions

Projection/event computation stays synchronous after the off-loop read so subscription activation
and publication each have one non-interleavable event-loop boundary. Per-subscriber queues are
unbounded under the existing local fan-out contract; `_broadcast()` therefore remains a
non-awaiting notification step rather than a second publication owner.

### Todos

No task-independent follow-up was identified during MX-FIX-1 review.

## Docs References

The resolved Domain Documentation registry has no entries. This module's atomicity and recovery
contracts are repository-owned and are proven by source plus deterministic tests.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available for this repository-local projector update. | — | — |

## Repo-Internal References

The projector sits between the observer read/fold and the app's wire decoration. The source and
regression suite below prove the ordering rather than relying on timing observations.

| Finding | Anchor | Source |
| --- | --- | --- |
| The projector publishes one successful tick by computing events, committing stable/current authority, then notifying subscribers. | "def _publish_projection(" | mcp/src/agents_remember/serving/projector.py:292-292 |
| Subscription activation registers its queue before current-snapshot capture and removes it in `finally`. | "self._subscribers.add(queue)"; "self._subscribers.discard(queue)" | mcp/src/agents_remember/serving/projector.py:346-346; mcp/src/agents_remember/serving/projector.py:354-354 |
| The app consumes one projector subscription, decorates every snapshot with build/heartbeat identity, and explicitly closes the iterator. |"async with contextlib.aclosing(projector.subscribe())"; "payload.update(served_state_tail("|mcp/src/agents_remember/serving/_app_common.py:135-135; mcp/src/agents_remember/serving/_app_common.py:145-145|
| Deterministic tests force the former handoff interleaving, failed-prime recovery, identical-state suppression, later delta, and cancellation cleanup. | `test_snapshot_then_delta`; `test_snapshot_subscription_cannot_lose_an_interleaved_projection`; `test_failed_prime_recovery_emits_one_snapshot_then_normal_deltas`; `test_cancelled_waiting_stream_releases_its_subscription` | mcp/tests/test_serving.py:436-448; mcp/tests/test_serving.py:450-470; mcp/tests/test_serving.py:472-500; mcp/tests/test_serving.py:502-512 |
| The pure stable-form diff supplies ordinary post-recovery entity events and excludes volatile ages. | "VOLATILE_AGE_FIELDS = frozenset("; "def diff_projection(" | mcp/src/agents_remember/serving/delta.py:36-36; mcp/src/agents_remember/serving/delta.py:109-109 |
| The observer tick entry performs the read/fold/atomic-file projection that this module publishes. | "def write_projection("; "def project_and_write(" | mcp/src/agents_remember/serving/projections/projection_store.py:158-158; mcp/src/agents_remember/serving/projections/projection_store.py:214-214 |
| Change-driven pacing remains owned by `ChangePacer`/`ChangeWatch`; it changes wake timing, not publication semantics. | "class ChangePacer:"; "class ChangeWatch(Protocol):" | mcp/src/agents_remember/serving/change_watcher.py:275-275; mcp/src/agents_remember/serving/change_watcher.py:285-285 |

## Cross-Repo References

No neighboring repository or external service governs this in-process publication boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| The reviewed projector, app, and tests are wholly repository-local. | — | — |

## 260727-CHATS-IM-L2 Current Delta

The watched production worker owns one `ProjectionInputState`. Startup uses a full refresh;
change wakes pass the coalesced domain set; heartbeats advance only heartbeat-owned state.
Watcherless execution and failed watcher fallback retain full-refresh behavior.

## 260731-EFA-L2 Current Delta

`Projector(config, *, cadence, replay, refreshers)` — five loose keywords became three named
concepts, all with module-level defaults:

- **`ProjectionCadence`** (`DEFAULT_PROJECTION_CADENCE`, from the new stdlib-only
  [cadence.py](cadence.py.md)) — `interval` (the floor between ticks) and `heartbeat` (the ceiling
  on staleness in a quiet world). One pacing decision.
- **`ProjectionReplay`** (`now`, `before_tick`; `LIVE_PROJECTION_CLOCK` = both `None` = live
  serving) — the sim/replay seam. **They are one substitution**: sim wires a replay clock together
  with the feeder that writes the world that clock is about, and a replay clock without its feeder
  ticks over a world that never moves.
- **`ProjectionRefreshers`** (`provider`, `landing`, `change_watcher`; `NO_PROJECTION_REFRESHERS`)
  — the side-inputs a LIVE tick drives, plus the watcher that lets it wake early. All three are
  enabled together for live serving and disabled together for sim replay (the feeder only writes
  *inside* a tick, so a change-gated loop would never wake). One choice — "is this projector
  attached to a moving world?" — not three independent hooks.

Adaptive waking is unchanged: with a change watcher the run loop paces via the `ChangePacer`
(change-driven + heartbeat, floored to one tick per `interval`); without one — sim replay and the
injected-`now()` tests — it keeps the exact `sleep(interval)` pacemaker.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## L23 Cancellation Drain

Projection ticks now run as shielded thread tasks. On serving shutdown,
cancellation is returned to the caller only after the real filesystem tick is
drained, preventing a late atomic projection write from racing temporary
worktree cleanup while preserving cancellation as the public outcome.

## Update History
- 2026-08-12T20:10+02:00 — L23 curator: documented shield-and-drain semantics for threaded projection ticks; verification remains closeout-owned.
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-02T22:10:00+02:00 — 260731-EFA-L6 W2-B05 curator: anchored 7 citation rows and normalized 3 prose citation groups; scoped citation check now passes.

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 3 cross-file line citations. The
  `test_serving.py` row is anchored to the four `StreamEventsTests` cases that prove it
  cit:([`test_snapshot_then_delta`; `test_snapshot_subscription_cannot_lose_an_interleaved_projection`; `test_failed_prime_recovery_emits_one_snapshot_then_normal_deltas`; `test_cancelled_waiting_stream_releases_its_subscription`], mcp/tests/test_serving.py:436-448; mcp/tests/test_serving.py:450-470; mcp/tests/test_serving.py:472-500; mcp/tests/test_serving.py:502-512), including identical-state suppression and later deltas. The pure-diff row is anchored to
  cit:(["VOLATILE_AGE_FIELDS = frozenset("; "def _strip_volatile("; "def stable_projection_state("; "def diff_projection("; "def _collection_deltas("], mcp/src/agents_remember/serving/delta.py:36-36; mcp/src/agents_remember/serving/delta.py:48-48; mcp/src/agents_remember/serving/delta.py:83-83; mcp/src/agents_remember/serving/delta.py:109-109; mcp/src/agents_remember/serving/delta.py:155-155), while the observer row is anchored to
  cit:(["def write_projection("; "def project_and_write("], mcp/src/agents_remember/serving/projections/projection_store.py:158-158; mcp/src/agents_remember/serving/projections/projection_store.py:214-214). Read all ranges back.
- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 3 cross-file line citations. The
  `test_serving.py` row is anchored to the four `StreamEventsTests` cases that prove it
  cit:([`test_snapshot_then_delta`; `test_snapshot_subscription_cannot_lose_an_interleaved_projection`; `test_failed_prime_recovery_emits_one_snapshot_then_normal_deltas`; `test_cancelled_waiting_stream_releases_its_subscription`], mcp/tests/test_serving.py:387-399; mcp/tests/test_serving.py:401-421; mcp/tests/test_serving.py:423-451; mcp/tests/test_serving.py:472-512), including identical-state suppression and later deltas. The pure-diff row is anchored to
  cit:(["VOLATILE_AGE_FIELDS = frozenset("; "def _strip_volatile("; "def stable_projection_state("; "def diff_projection("; "def _collection_deltas("], mcp/src/agents_remember/serving/delta.py:36-36; mcp/src/agents_remember/serving/delta.py:48-48; mcp/src/agents_remember/serving/delta.py:83-83; mcp/src/agents_remember/serving/delta.py:109-109; mcp/src/agents_remember/serving/delta.py:155-155), while the observer row is anchored to
  cit:(["def write_projection("; "def project_and_write("], mcp/src/agents_remember/serving/projections/projection_store.py:158-158; mcp/src/agents_remember/serving/projections/projection_store.py:214-214). Read all ranges back.
- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator: recorded the `ProjectionCadence` / `ProjectionReplay` / `ProjectionRefreshers` constructor concepts and their module defaults; pacing behaviour unchanged.
- 2026-07-30T12:51+02:00 — 260727-CHATS-IM-L2 curator: the live projection worker now
  owns one `ProjectionInputState`, converts watcher wakes into full/change/heartbeat refreshes, and
  passes the exact invalidated domains to the projection write edge. Watcherless replay/tests keep
  full-refresh behavior; watcher failure still fails open. Verification metadata remains pinned
  until closeout.
- 2026-07-18T14:16+02:00 — 260715-FEUI-MX-FIX-1: documented the single-owner atomic
  subscribe-and-snapshot boundary, compute-then-publish-then-notify ordering, one full first-recovery
  snapshot, identical-recovery suppression, ordinary later deltas, and explicit cancellation
  cleanup. Verification metadata remains pinned until closeout stamps the candidate commit.
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
