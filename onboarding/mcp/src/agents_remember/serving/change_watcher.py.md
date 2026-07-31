# mcp/src/agents_remember/serving/change_watcher.py

| Field                  | Value                                                |
| ---------------------- | ---------------------------------------------------- |
| repository             | agents-remember                                      |
| path                   | `mcp/src/agents_remember/serving/change_watcher.py`  |
| doc_type               | `file-level-onboarding`                              |
| lastUpdated | 2026-07-30T12:51+02:00 |
| lastVerifiedCommitHash |                                                      `3a8ff703d796dc585b86a458daaf9eb2af6b2b31`|
| lastVerifiedCommitDate |                                                      2026-07-30T13:59:13+02:00|
| governingOverview      | `overview.md`                                        |

## Governing Overview

[serving overview](overview.md)

## Purpose

`change_watcher.py` (260712-PTS-L3, master 260712-PTS) makes the projector's waking
**change-driven** instead of unconditional. Before this leaf the projector re-projected the whole
world every `--interval` seconds (production 1.0s) even when nothing changed — a 2026-07-12 py-spy
sample showed `_tick_sync` at 11.1s of a 15s window (~160% steady CPU on a quiet-but-large tree).
This module contains the three pieces that fix the *when* without touching the *what*: the derived
watch-root list over the projection's actual input surfaces, the input-event filter (self-trigger
safety), and the `ChangePacer` wake scheduler (debounce + max-delay + interval floor + idle
heartbeat) fed by the `ProjectionInputWatcher` `watchfiles`/inotify task. The projector's tick body
is byte-identical either way — only the pacemaker changed.

## Code Commentary

### Logic

`projection_input_roots(config)` derives the watch roots reader-by-reader from what
`observer.projection_store.project_and_write` reads (the authoritative derivation table with the
readers each root feeds is the module docstring, R1): `<coord>/tasks`, the observer
`lifecycles`/`workspace`/drift-snapshot dirs, `logs/providers/{status,setup}`,
`temp/{worktree-start,tool-reports}`. Only existing dirs are returned (`watchfiles`
refuses missing paths); dirs that appear later ride the periodic watch-set refresh. **Nothing
under `worktrees/` is ever a watch root** — the checkouts are ~50k dirs and each task's
`provider-runtime` holds live container data (Postgres/grepai) that is unreadable to the daemon
user and churns on every container write; watching it recursively crashed the whole watch on
permission-denied and would have re-projected on WAL writes. Worktree `provider-state.json`
changes are infrequent and heartbeat-covered, and central provider status is watched via
`logs/providers`. `awatch` also passes `ignore_permission_denied=True` as defence-in-depth. A
regression test asserts no watch root falls under `worktrees/`. Deliberately
NOT watched, heartbeat-covered blind spots: the per-repo memory roots (already behind the 15s
`REPO_SURFACE_REFRESH_TTL_SECONDS`, so their freshness bound is TTL + heartbeat), landing state
(an in-memory 30s git-derived refresher with no file signal), and the worktree checkouts
themselves.

`is_projection_input_event(path)` filters one raw watch event: drops `*.tmp` atomic-write temps,
dot-prefixed sidecar temps, the projection's own outputs (`latest-state.json`/
`latest-metrics.json`, defensive — they also live *outside* every watched subdirectory), and the
`workspace/` non-input churn by name **only when the parent dir is `workspace`** (the raw event
river `events.jsonl` + its cursor/lock files, the `operator-inbox.lock` flock file — opened `a+b`
by every inbox access including each tick's own `read_agent_pickups`, whose boot-time creation
would otherwise emit one spurious change-tick (review hardening) — and the supervisor's own
heartbeat row). A lifecycle's `events.jsonl` is NOT confused with the workspace river.

`ChangePacer` is the wake scheduler; one instance belongs to one projector run loop. The watcher
feeds `notify_change()`/`set_watcher_healthy()`; the run loop awaits `wait()` once per tick, which
returns the wake reason (`"change"`/`"heartbeat"`/`"interval"`). The pure `_next_deadline()` holds
all scheduling rules (monotonic clock): **floor** — never two projections closer than `interval`
(`--interval` keeps its meaning as the fast-path cadence floor); **debounce** — a change projects
`DEBOUNCE_SECONDS` (0.1, clamped to `interval`) after the *last* change of its burst; **max delay**
— a sustained burst still projects within `max_delay = interval` of its *first* change (R2: a
continuously-busy world keeps the former 1s cadence); **heartbeat** — with no changes, project
every `heartbeat` seconds (default `DEFAULT_HEARTBEAT_SECONDS` = 15.0, floored to never undercut
`interval`); **degraded** — while the watcher is unhealthy, tick at the fixed `interval` exactly
like the pre-adaptive loop. The pacer **starts degraded** so there is no detection blind spot
between boot and the watcher establishing its watches. `wait()` consumes pending changes at wake;
changes observed *during* a projection accumulate for the next cycle, so nothing is lost to a tick.

`ProjectionInputWatcher.run(pacer)` is the live watch task (lifecycle mirrors the landing
refresher: created by `create_app` for live serving only, started/cancelled by `Projector.run`).
`watchfiles` missing at import (`watchfiles = None`) logs a loud ERROR and degrades permanently for
that process. Otherwise the retry loop: derive roots **inside** the retry guard (review hardening —
a transient stat/glob failure follows the same loud degrade-and-retry path as a watch failure
instead of escaping `run()` and killing the task for good); zero roots is not an error (a
fresh/empty tree paces at the fixed interval and re-checks every `WATCH_REFRESH_SECONDS` = 30);
`_watch_once` marks the pacer healthy, emits one reconciling `notify_change()` on every
re-establish after the first (inotify has no replay — whatever happened while the watch was down
gets one debounced projection), then feeds `watchfiles.awatch(*roots, recursive=True)` batches
(library batching tightened to `debounce=200ms`/`step=50ms` so first detection never exceeds the
1s max-delay bound) into the pacer until `_stop_when_roots_change` — a 30s re-derivation task —
stops the generation to restart with a fresh root set. Any exception logs
`projection input watcher FAILED` (ERROR + traceback), sets the pacer unhealthy, sleeps 30s, and
retries.

### Conventions

The R-numbered comments (R1 input list, R2 busy-world cadence, R3/R4 heartbeat bounds, R5
freshness/SSE semantics, R7 failure posture) are this leaf's requirement labels, pinned one-for-one
by `test_change_watcher.py`. `WakeTarget` and `ChangeWatch` are structural `Protocol`s — the
projector's seam mirrors `LandingStateRefresh` (the projector owns the task lifecycle, tests inject
fakes, this module ships the live implementation). Debounce/refresh constants are code defaults,
not settings knobs; `--heartbeat` is the only operator-facing knob.

### Invariants And Boundaries

- **Only *when* the projector wakes changes, never *what* a tick does.** The tick body
  (prime, diff/broadcast, ETag revision) is untouched by this module.
- **Failure degrades LOUDLY to the legacy fixed-interval ticking, never crashes and never goes
  silent (R7, fail-open).** Missing wheel, zero watchable roots, derivation failure, or a crashed
  watch all end in `set_watcher_healthy(False)` + ERROR logging, with a 30s retry for the
  recoverable cases. Fixed-interval is exactly the pre-PTS-L3 behaviour.
- **The heartbeat is the staleness bound for everything a watcher cannot see (R3/R4).**
  `/api/state` of a quiet world, the unwatched blind spots, and every time-*derived* field or state
  flip (`ageSeconds`/`staleSeconds` recomputation, stale/overdue decays) advance at heartbeat
  resolution (default 15s). This is a deliberate R4 policy: volatile ages were already stripped
  from the SSE delta stream and advanced client-side (`dashboard/src/data/servedAges.ts`), and a
  derived-state flip needs a full reducer run anyway — so heartbeat-cadence refresh does not change
  what an SSE client displays between emissions.
- **A tick never re-wakes itself.** The projection's own outputs live outside every watched
  subdirectory *and* are name-filtered; the workspace non-input churn is name-filtered;
  TTL-gated writers that run inside a tick cost at most one debounced echo tick per TTL window,
  whose diff emits nothing.
- **A busy world keeps the former cadence.** `max_delay = interval` plus the floor mean sustained
  writes produce exactly one projection per `--interval`, and change-driven deltas in a quiet
  world land within debounce + projection time (measured ~0.2s on the reference tree).
- **Live serving only.** `create_app` wires the watcher iff `before_tick is None`; `--sim` replay
  stays time-driven because the sim feeder writes only *inside* a tick — a change-gated loop would
  never wake.

### Todos

None.

## Docs References

No external Domain Documentation source is configured for this memory repo (`system/sources.md`
has no entries). The `watchfiles` library (the inotify-backed watch backend, new runtime
dependency `watchfiles>=1.1,<2`) is documented at its own upstream site; the load-bearing local
facts (awatch batching defaults, missing-path refusal, `DefaultFilter`) are recorded here and
pinned by the real-backend integration test.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant documentation found after checking live sources; no Domain Documentation entries are configured. | N/A | N/A |

## Repo-Internal References

The watch roots are derived from — and must stay in lock-step with — the reader list of
`project_and_write`; the projector consumes the pacer; `create_app` decides when a watcher exists;
the CLI/daemon own the `--heartbeat` knob's plumbing.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Module docstring: the R1 root-derivation table (root → readers), the deliberate blind spots, self-trigger safety, the R5 freshness bounds, and the R7 failure posture. | L1-L67 | [change_watcher.py](agents-remember/mcp/src/agents_remember/serving/change_watcher.py) |
| Constants (heartbeat 15s, debounce 0.1s, awatch 200/50ms batching, 30s refresh) and the workspace/output name-filter sets. | L97-L131 | [change_watcher.py](agents-remember/mcp/src/agents_remember/serving/change_watcher.py) |
| `projection_input_roots` (existing-dirs-only; nothing under `worktrees/` — container data is unreadable and high-churn) and `is_projection_input_event` (tmp/dotfile/output/workspace-churn filter). | L134-L175 | [change_watcher.py](agents-remember/mcp/src/agents_remember/serving/change_watcher.py) |
| `WakeTarget`/`ChangeWatch` protocols and `ChangePacer` (`_next_deadline` scheduling core, degraded boot state, consume-at-wake). | L178-L279 | [change_watcher.py](agents-remember/mcp/src/agents_remember/serving/change_watcher.py) |
| `ProjectionInputWatcher`: derivation inside the retry guard, empty-roots idle path, reconcile-on-re-establish, awatch generation restart on root-set change, loud degrade + 30s retry. | L282-L384 | [change_watcher.py](agents-remember/mcp/src/agents_remember/serving/change_watcher.py) |
| The tick entry whose readers define the watched input surfaces. | `project_and_write` | [projection_store.py](agents-remember/mcp/src/agents_remember/observer/projection_store.py) |
| The projector side: pacer construction (watcher present ⇒ `ChangePacer`, absent ⇒ legacy `sleep(interval)`), change-or-heartbeat waking, and the `_on_watch_task_done` fail-open callback. | L105-L124; L149-L205 | [projector.py](agents-remember/mcp/src/agents_remember/serving/projector.py) |
| `create_app(cadence=ProjectionCadence(heartbeat=…), live_inputs=LiveProjectionInputs(change_watch=…))`: watcher enabled iff `replay.before_tick is None` (sim replay stays time-driven); since 260731-EFA-L2 the three live-input toggles resolve together in `LiveProjectionInputs.resolved()`. | L467-L505 | [app.py](agents-remember/mcp/src/agents_remember/serving/app.py) |
| The `--heartbeat` flag, `--interval` re-documented as the fast-path cadence floor, and the daemon ensure/spawn heartbeat plumbing. | L59-L78; L190-L196 | [cli/dashboard.py](agents-remember/mcp/src/agents_remember/cli/dashboard.py) |
| The client-side volatile-age advancement that makes heartbeat-resolution time-derived fields acceptable (R4). | `VOLATILE_AGE_FIELDS` mirror | [servedAges.ts](agents-remember/dashboard/src/data/servedAges.ts) |
| The R1-R7 regression suite: root derivation, event filter, pure pacer deadlines, projector integration (heartbeat-only quiet world, debounce-bounded change, burst coalescing, loud degrades, derivation-failure retry), legacy no-watcher pacing, and one real-inotify end-to-end pass. | L1-L435 | [test_change_watcher.py](agents-remember/mcp/tests/test_change_watcher.py) |
| The new runtime dependency this module degrades without. | `watchfiles>=1.1,<2` | [pyproject.toml](agents-remember/mcp/pyproject.toml) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Same-repository serving concern only. | N/A | N/A |

## 260727-CHATS-IM-L2 Current Delta

Accepted watcher paths map to explicit projection reader domains. `ChangePacer` accumulates those
domains through debounce/max-wait and returns a `ProjectionWake`; an unmapped accepted path returns
all domains so correctness fails open to a full refresh.

## Update History

- 2026-07-30T12:51+02:00 — 260727-CHATS-IM-L2 curator: watcher paths now map to
  explicit projection domains and `ChangePacer` coalesces both the wake and its invalidation set.
  An accepted but unmapped path fails open to every domain, preserving correctness while narrow
  known changes avoid a full input rebuild. Verification metadata remains pinned until closeout.

- 2026-07-13T11:15+02:00 — 260712-PTS-L3 post-integration correction: removed the
  `worktrees/*/*/provider-runtime` watch root entirely. It descended (recursive) into each task's
  live container data (Postgres/grepai), which is unreadable to the daemon user — it crashed the
  whole watch on permission-denied against the real coordination tree, falling back to permanent
  1s ticking — and would have re-projected on every container WAL write. Worktree provider-state.json
  is now heartbeat-covered; central provider status stays watched via `logs/providers`. Added
  `ignore_permission_denied=True` to `awatch` and a regression test asserting no watch root falls
  under `worktrees/`. Verified against the live tree with containers: watcher establishes cleanly,
  re-projections dropped ~20/20s → ~3/20s, change latency ~1.2s.
- 2026-07-12T20:24+02:00 — 260712-PTS-L3: created for change-driven projection pacing — the derived
  projection-input watch roots (docstring derivation table; nothing under worktrees/, never
  a worktree-checkout walk), the input-event filter (tmp/dotfile/own-output/workspace-churn +
  `operator-inbox.lock`, review hardening), `ChangePacer` (debounce 0.1s, max-delay = interval so a
  busy world keeps the former cadence, heartbeat default 15s, starts degraded), and
  `ProjectionInputWatcher` on `watchfiles` (30s watch-set re-derivation; loud ERROR +
  fixed-interval fallback on ANY failure with 30s retry — derivation failures follow the same
  retry path after review hardening). Adversarial review verdict INTEGRATE with the two hardenings
  adopted. Verification metadata remains empty until closeout stamps the PTS-L3 code commit.
