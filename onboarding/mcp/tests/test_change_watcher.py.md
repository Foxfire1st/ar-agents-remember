# test_change_watcher.py

| Field                  | Value                                          |
| ---------------------- | ---------------------------------------------- |
| repository             | agents-remember                                |
| path                   | `mcp/tests/test_change_watcher.py`             |
| doc_type               | `file-level-onboarding`                        |
| lastUpdated | 2026-08-12T21:27+02:00 |
| lastVerifiedCommitHash |                                                `1580f92715ff93c988f9a15439ad9bec60ef4c5d`|
| lastVerifiedCommitDate |                                                2026-08-13T00:18:59+02:00|
| governingOverview      | `overview.md`                                  |

## Governing Overview

[mcp/tests overview](overview.md) — the route-local `mcp/tests/overview.md` governs this test
sidecar.

## Purpose

`test_change_watcher.py` (260712-PTS-L3) pins change-driven projection pacing across the watcher
module's three layers plus the projector integration: the derived watch-root list (R1) and the
input-event filter (self-trigger safety), the `ChangePacer` scheduling core, the projector run
loop with an injected watcher (quiet world = heartbeat-only, change = debounce-bounded latency,
burst = coalesced, failure = loud fixed-interval degrade, R7 fail-open), and one real-`watchfiles`
end-to-end pass (inotify → debounce → projection).

## Code Commentary

### Logic

`ProjectionInputRootsTests` prove an empty tree yields no roots, a fully-populated tree derives
exactly the documented projection-input surfaces and nothing else (including the two-level
`worktrees/*/*/provider-runtime` glob), and missing surfaces are skipped until they exist.
cit:([`InputEventFilterTests`], mcp/tests/test_change_watcher.py:98-139) prove genuine inputs pass while `*.tmp`, dotfiles, the
projection's own `latest-state/metrics.json` outputs, every control-plane lockfile, and the
remaining `workspace/` non-input churn (event river, cursor/lock, supervisor heartbeat) are dropped
— and that a *lifecycle's* `events.jsonl` is NOT confused with the workspace river (the parent-dir
check). Since 260731-EFA-L5 the lockfile case asserts on `operator-inbox.jsonl.lock` rather than
`operator-inbox.lock`, and a second lockfile case was added *outside* `workspace/`:
`lifecycles/L1/gates.jsonl.lock`.

`ChangePacerDeadlineTests` drive the pure `_next_deadline()` with synthetic monotonic instants —
deterministic, no sleeping: idle waits for the heartbeat; a lone change projects debounce (0.1s)
after it; a change inside the floor window is floored to one projection per interval; a sustained
burst is bounded by max-delay (= interval, R2); a degraded watcher ticks at the fixed interval;
and a heartbeat below the interval never undercuts it.

`AdaptiveProjectorTests` (async, real `Projector` over an empty tmp config) use `_FakeWatcher` (a
`ChangeWatch` fake that reports healthy then emits on demand) and `_CrashingWatcher`:
a quiet world projects only at heartbeat cadence (bounded beat count vs the ~32 the old interval
pacing would give); a single change projects within the debounce bound with
`last_wake_reason == "change"`; 25 rapid writes coalesce to 1-2 projections (unconditional
1-per-write would give 25); `watchfiles=None` (patched) and a crashed watcher task each degrade
LOUDLY (`assertLogs` ERROR: "watchfiles is not installed" / "change watcher task died") to
fixed-interval ticking despite a 30s heartbeat (`last_wake_reason == "interval"`, R7); a transient
root-derivation failure logs "projection input watcher FAILED", reports unhealthy first, and
recovers on the retry cycle instead of killing the task (review hardening F3, via a
`RecordingPacer` and a flaky `projection_input_roots` patch); `run()` owns the watcher task's
lifecycle (cancelled projector ⇒ stopped watcher); and WITHOUT a watcher the legacy
interval pacing is kept exactly (`_pacer is None`, `last_wake_reason is None`) — the sim/replay
and injected-`now()` path. `RealWatchfilesIntegrationTests` runs one end-to-end pass over the real
inotify backend (skipped when `watchfiles` is not installed): a real write under `tasks/` wakes
the projector with `last_wake_reason == "change"` within 5s.

### Conventions

Pacer tests set `_last_wake`/`_watcher_healthy`/`_first_pending` directly and assert
`(deadline, reason)` tuples — the scheduling core stays pure so no test sleeps to prove a
deadline. Projector tests use loose beat-count bounds to absorb slow-CI tick durations, drain
boot-time ticks (degraded start + floor) before measuring, and cancel the run task via
`addAsyncCleanup`. Every `Projector(...)` construction passes pacing as one
`ProjectionCadence(interval=..., heartbeat=...)` and the injected watcher as one
`ProjectionRefreshers(change_watcher=...)`, so a test tuning cadence names the cadence object
rather than loose keywords; the no-watcher legacy case passes cadence alone.
Instrumentation (`projection_count`, `last_wake_reason`) exists for exactly
these assertions plus ops.

The async projector fixture registers its temporary-directory cleanup through
`addCleanup` during `setUp`, while each started projector registers its later
`addAsyncCleanup` cancellation/await. Unittest's LIFO cleanup stack therefore
drains the projector before removing the filesystem it may still touch. This
is test-fixture ownership only; the production projector's shield-and-drain
cancellation semantics are unchanged.

**The lockfile exclusion is asserted as a derived rule, not as a name list, and the second case is
what makes that visible.** The filter no longer carries a literal basename; it matches the suffix
`_DURABLE_LOG_LOCK_SUFFIX`, which the module computes from
`durable_store.lock_path_for(Path("log.jsonl"))` and applies in **every** watched directory. That
derivation is what the new `lifecycles/L1/gates.jsonl.lock` case pins: five of the six durable logs
live only under `workspace/`, but `gates.jsonl` also exists once per lifecycle, so its lockfile
appears in every lifecycle directory — a place a `workspace/`-scoped name list structurally could
not reach. The first case, `operator-inbox.jsonl.lock`, records why derivation was adopted at all:
the list held `operator-inbox.lock` while `lock_path_for` had moved to the whole-log-name form, so
the exclusion had silently stopped matching anything and the busiest write in the tree was waking
the projector.

## Docs References

No external documentation governs these repo-local pacing regressions; `system/sources.md` has no
Domain Documentation entries.

| Finding | Anchor | Source |
| --- | --- | --- |


## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Root derivation and event filtering are covered by focused tests. | `ProjectionInputRootsTests`; `InputEventFilterTests` | mcp/tests/test_change_watcher.py:48-95; mcp/tests/test_change_watcher.py:98-139 |
| Domain mapping and the pure pacer deadline are covered separately. | `ProjectionDomainMappingTests`; `ChangePacerDeadlineTests` | mcp/tests/test_change_watcher.py:142-170; mcp/tests/test_change_watcher.py:173-221 |
| Adaptive projection and real watchfiles integration are covered separately. | `AdaptiveProjectorTests`; `RealWatchfilesIntegrationTests` | mcp/tests/test_change_watcher.py:252-441; mcp/tests/test_change_watcher.py:444-485 |
| The module derives roots and filters lockfiles/events through named helpers and exposes the pacer and watcher. | `_DURABLE_LOG_LOCK_SUFFIX`; `projection_input_roots`; `is_projection_input_event`; `ChangePacer`; `ProjectionInputWatcher` | mcp/src/agents_remember/serving/change_watcher.py:156-156; mcp/src/agents_remember/serving/change_watcher.py:159-184; mcp/src/agents_remember/serving/change_watcher.py:187-205; mcp/src/agents_remember/serving/change_watcher.py:283-376; mcp/src/agents_remember/serving/change_watcher.py:379-487 |
| The current projector run loop owns pacer wiring, watch-task lifecycle, fail-open completion, and wake instrumentation while finalization drains the watcher and landing refresher. | `ProjectionRefreshers`; `NO_PROJECTION_REFRESHERS`; "async def run(self) -> None:"; `_on_watch_task_done` | mcp/src/agents_remember/serving/projector.py:112-123; mcp/src/agents_remember/serving/projector.py:128-128; mcp/src/agents_remember/serving/projector.py:197-240; mcp/src/agents_remember/serving/projector.py:263-275 |
| The lock exclusion is derived from the durable-store naming function and held by the access context. | `lock_path_for`; `exclusive_access` | mcp/src/agents_remember/controlplane/durable_store.py:291-298; mcp/src/agents_remember/controlplane/durable_store.py:348-394 |

## Cross-Repo References

No meaningful cross-repo references found.

## L23 Projector Cancellation Compatibility

The adaptive watcher cases still exercise `Projector.run`; that loop now drains
any in-flight shielded thread tick before cancellation returns. Watcher
lifecycle, pacing, and fail-open recovery claims remain unchanged, while the
serving suite owns the dedicated blocked-tick cancellation regression.

| Finding | Anchor | Source |
| --- | --- | --- |


## 260727-CHATS-IM-L2 Current Delta

Coverage now proves tasks/lifecycles/workspace path mapping, multi-domain coalescing, full-refresh
fallback for an unknown accepted path, and the exact task-domain wake through both the adaptive
worker and real watchfiles integration.

## Update History
- 2026-08-12T21:27+02:00 — L23 curator follow-up: re-read the closeout-only cleanup race and documented the `AdaptiveProjectorTests` LIFO fixture boundary: later async projector cancellation/await runs before the earlier registered temporary-directory cleanup. Production projector behavior is unchanged; the owner reports the crashed-watcher case green in 20 consecutive sanitized runs. Verification remains closeout-owned.
- 2026-08-12T20:24+02:00 — L23 curator: re-read the adaptive projector tests against shield-and-drain cancellation; existing watcher claims remain accurate and the focused cancellation arm lives in `test_serving.py`. Verification remains closeout-owned.
- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-04T11:32:09+02:00 — 260731-EFA-L6 S18-B02 curator: split watcher, projector, test, and lock claims by source owner and generated final citation ranges with the scoped fixer.
- 2026-08-02T16:44:03+02:00 — W1-B07 curator: repaired 1 repository-reference citation (1/1 anchored and sourced; scoped citation check clean).

- 2026-08-01T16:25+02:00 — 260731-EFA-L5 curator: `InputEventFilterTests`' lockfile assertion moved
  from `operator-inbox.lock` to `operator-inbox.jsonl.lock` and gained a second case *outside*
  `workspace/` — `lifecycles/L1/gates.jsonl.lock`. Recorded the reason rather than the edit: the
  exclusion is no longer a basename list but a suffix the module derives from
  `durable_store.lock_path_for` (`_DURABLE_LOG_LOCK_SUFFIX`, `change_watcher.py` L142-L156) and
  applies in every watched directory, and that derivation is exactly what the lifecycle case pins —
  `gates.jsonl` exists once per lifecycle as well as under `workspace/`, so its lockfile appears in
  every lifecycle directory, which a `workspace/`-scoped name list could not express. The first case
  records why the derivation was adopted: the list still held `operator-inbox.lock` after
  `lock_path_for` had moved to the whole-log-name form, so the exclusion had silently stopped
  matching and the tree's highest-frequency write was waking the projector. **Citations re-derived
  and repaired.** The four added lines shifted every suite after the filter tests by +4, so the
  own-file row was re-read end by end and re-anchored (L48-L97; L98-L137; L138-L168; L169-L219;
  L248-L438; L440-L485 → L48-L95; L98-L139; L142-L170; L173-L221; L252-L441; L444-L485). Two rows
  were wrong independently of this leaf and are now fixed: the module row cited `L1-L384` for a file
  that was 465 lines at the base commit and is 487 now — replaced with named symbols and verified
  ranges; and the projector row cited `L105-L124; L149-L205` while naming `_on_watch_task_done`,
  which is at L238-L249 and was never inside it — the same start-right / stop-short shape the L4
  citation audit found, replaced with `ProjectionRefreshers` L107-L118, `NO_PROJECTION_REFRESHERS`
  L123, `Projector.__init__` L129-L173, `run` L193-L236 and `_on_watch_task_done` L238-L249. The
  `durable_store.py` row is
  cited **by symbol with no line range**: that module grew ~100 lines mid-leaf and every earlier
  range into it was invalidated. No pacer, projector or real-watchfiles assertion changed.
  Verification metadata untouched.

- 2026-07-31T16:50+02:00 — 260731-EFA-L2 curator: every `Projector(...)` construction in the
  adaptive and real-watchfiles suites now threads `ProjectionCadence(interval=...,
  heartbeat=...)` and `ProjectionRefreshers(change_watcher=...)` instead of three loose
  keywords, so the Conventions paragraph names both parameter objects. The rewrapped
  constructions moved the adaptive-projector and real-backend suites down the file, and the
  own-file reference row was re-verified line by line and re-anchored (L46-L130; L133-L181;
  L212-L387; L390-L432 became L48-L97; L98-L137; L138-L168; L169-L219; L248-L438; L440-L485,
  with the previously unlisted domain-mapping suite now named). No assertion, log string, or
  test name changed.

- 2026-07-30T12:51+02:00 — 260727-CHATS-IM-L2 curator: added path-to-domain,
  coalescing, fail-open unknown-path, adaptive-worker, and real-watchfiles assertions for domain
  invalidation. Verification metadata remains pinned until closeout.

- 2026-07-12T20:24+02:00 — 260712-PTS-L3: created alongside `serving/change_watcher.py` — root
  derivation exactness, self-trigger/event filtering (incl. the lifecycle-vs-workspace
  `events.jsonl` distinction and the review-hardening `operator-inbox.lock` drop), the pure
  `_next_deadline` scheduling table (heartbeat/debounce/floor/max-delay/degraded/never-undercut),
  adaptive-projector integration (heartbeat-only quiet world, debounce-bounded change, burst
  coalescing, loud missing-wheel/crashed-watcher/derivation-failure degrades with retry,
  watch-task lifecycle ownership, legacy pacing without a watcher), and one real-inotify
  end-to-end pass. Verification metadata remains empty until closeout stamps the PTS-L3 code
  commit.
