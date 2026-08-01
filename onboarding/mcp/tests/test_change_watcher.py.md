# test_change_watcher.py

| Field                  | Value                                          |
| ---------------------- | ---------------------------------------------- |
| repository             | agents-remember                                |
| path                   | `mcp/tests/test_change_watcher.py`             |
| doc_type               | `file-level-onboarding`                        |
| lastUpdated | 2026-08-01T16:25+02:00 |
| lastVerifiedCommitHash |                                                `a714114ef94eedb8042fb4caa38d9469f4767dd6`|
| lastVerifiedCommitDate |                                                2026-08-01T18:06:36+02:00|
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
`InputEventFilterTests` (L98-L139) prove genuine inputs pass while `*.tmp`, dotfiles, the
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

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant documentation found after checking live sources; no Domain Documentation entries are configured. | N/A | N/A |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Root derivation, event filter, domain mapping, pure pacer deadline, adaptive projector, and real-backend suites. | L48-L95; L98-L139; L142-L170; L173-L221; L252-L441; L444-L485 | [mcp/tests/test_change_watcher.py](agents-remember/mcp/tests/test_change_watcher.py) |
| The module under test: the derived roots, the event filter and the lockfile suffix it now derives from `lock_path_for` instead of naming, the pure `ChangePacer`, and the live `ProjectionInputWatcher`. | `_DURABLE_LOG_LOCK_SUFFIX` L142-L156; `projection_input_roots` L159-L184; `is_projection_input_event` L187-L205; `ChangePacer` L283-L376; `ProjectionInputWatcher` L379-L487 | [mcp/src/agents_remember/serving/change_watcher.py](agents-remember/mcp/src/agents_remember/serving/change_watcher.py) |
| The projector integration under test: pacer wiring, watch-task lifecycle, `_on_watch_task_done` fail-open, and the `projection_count`/`last_wake_reason` instrumentation. | `ProjectionRefreshers` L107-L118; `NO_PROJECTION_REFRESHERS` L123; `Projector.__init__` L129-L173; `run` L193-L236; `_on_watch_task_done` L238-L249 | [mcp/src/agents_remember/serving/projector.py](agents-remember/mcp/src/agents_remember/serving/projector.py) |
| The naming function the exclusion is derived from, and the six logs whose lockfiles it therefore covers wherever they live. | `lock_path_for`; `exclusive_access` | [mcp/src/agents_remember/controlplane/durable_store.py](agents-remember/mcp/src/agents_remember/controlplane/durable_store.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Same-repository tests only. | N/A | N/A |

## 260727-CHATS-IM-L2 Current Delta

Coverage now proves tasks/lifecycles/workspace path mapping, multi-domain coalescing, full-refresh
fallback for an unknown accepted path, and the exact task-domain wake through both the adaptive
worker and real watchfiles integration.

## Update History

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
