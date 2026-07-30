# test_change_watcher.py

| Field                  | Value                                          |
| ---------------------- | ---------------------------------------------- |
| repository             | agents-remember                                |
| path                   | `mcp/tests/test_change_watcher.py`             |
| doc_type               | `file-level-onboarding`                        |
| lastUpdated | 2026-07-30T12:51+02:00 |
| lastVerifiedCommitHash |                                                `3a8ff703d796dc585b86a458daaf9eb2af6b2b31`|
| lastVerifiedCommitDate |                                                2026-07-30T13:59:13+02:00|
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
`InputEventFilterTests` prove genuine inputs pass while `*.tmp`, dotfiles, the projection's own
`latest-state/metrics.json` outputs, and the `workspace/` non-input churn (event river,
cursor/lock, `operator-inbox.lock`, supervisor heartbeat) are dropped — and that a *lifecycle's*
`events.jsonl` is NOT confused with the workspace river (the parent-dir check).

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
`addAsyncCleanup`. Instrumentation (`projection_count`, `last_wake_reason`) exists for exactly
these assertions plus ops.

## Docs References

No external documentation governs these repo-local pacing regressions; `system/sources.md` has no
Domain Documentation entries.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant documentation found after checking live sources; no Domain Documentation entries are configured. | N/A | N/A |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Root derivation, event filter, pure pacer deadline, adaptive projector, and real-backend suites. | L46-L130; L133-L181; L212-L387; L390-L432 | [mcp/tests/test_change_watcher.py](agents-remember/mcp/tests/test_change_watcher.py) |
| The module under test: derived roots, event filter, `ChangePacer`, `ProjectionInputWatcher`, and the R-numbered contracts the suites pin. | L1-L384 | [mcp/src/agents_remember/serving/change_watcher.py](agents-remember/mcp/src/agents_remember/serving/change_watcher.py) |
| The projector integration under test: pacer wiring, watch-task lifecycle, `_on_watch_task_done` fail-open, and the `projection_count`/`last_wake_reason` instrumentation. | L105-L124; L149-L205 | [mcp/src/agents_remember/serving/projector.py](agents-remember/mcp/src/agents_remember/serving/projector.py) |

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
