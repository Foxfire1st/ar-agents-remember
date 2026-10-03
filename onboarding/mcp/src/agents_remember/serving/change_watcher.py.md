# mcp/src/agents_remember/serving/change_watcher.py

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

## Native events and completion-paced live wakes

The existing recursive watcher explicitly passes `force_polling=False` on supported local native POSIX/ext4 roots. Inherited WSL/environment polling selection cannot turn it into periodic recursive scans. Event/domain filtering, root refresh, nested atomic-write delivery, stop/drain and reported retry remain with this owner; no polling/mount fallback is added.

After real live tick completion or cancellation drain, `projection_completed` imposes `max(interval, min(duration, 3 seconds))` rest. The default adds one to three seconds; larger configured intervals keep their larger floor. Completion, failure and health transitions never clear accumulated domains: work/rest notifications participate in the next eligible tick. Degraded watches request full refresh and retain the same rest; the quiet heartbeat's existing 15-second scheduling interval remains. Native batching, running/next tick computation and publication add to total lag; this is no three-second total-freshness promise.


- Native registration is explicit and retains watcher lifecycle. [10]
- The real completion floor preserves accumulated domains. [11]
- Completion rest participates in change/degraded/heartbeat deadlines. [12]

## Code Commentary

### Logic

`projection_input_roots(config)` derives the watch roots reader-by-reader from what
`serving.projections.projection_store.project_and_write` reads (the authoritative derivation table with the
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
dot-prefixed sidecar temps, **every control-plane lockfile, by suffix, in any watched directory**
(see below), the projection's own outputs (`latest-state.json`/
`latest-metrics.json`, defensive — they also live *outside* every watched subdirectory), and the
`workspace/` non-input churn by name **only when the parent dir is `workspace`** (the raw event
river `events.jsonl` + its cursor/lock files and the supervisor's own heartbeat row). A lifecycle's
`events.jsonl` is NOT confused with the workspace river.

### 260731-EFA-L5 The Lockfile Exclusion Is Derived, Not Spelled Out

`_DURABLE_LOG_LOCK_SUFFIX = lock_path_for(Path("log.jsonl")).name.removeprefix("log")` — the suffix
that `kernel.file_lock.lock_path_for` gives a `.jsonl` control-plane log, **derived from
that function** rather than written down. `is_projection_input_event` suffix-matches it and returns
`False` before any of the name checks.

**Spelling it out is what broke.** This filter carried the literal `"operator-inbox.lock"` in
`_EXCLUDED_WORKSPACE_NAMES` while `lock_path_for` had moved to `operator-inbox.jsonl.lock`, so the
exclusion silently stopped matching anything — a filter that looks correct and filters nothing. The
name is now out of that set entirely; the set keeps only `events.jsonl`, the workspace cursor and
lock, and the supervisor heartbeat.

**Suffix-and-everywhere is what the old list structurally could not express.** Five of the six
durable logs live only under `workspace/`, but `gates.jsonl` lives there **and once per lifecycle**
under `<obs>/lifecycles/<id>/` — so `gates.jsonl.lock` appears in every lifecycle directory too, and
a basename list scoped to `parent == "workspace"` could never have covered it. A suffix rule also
needs no list to keep in step with the stores as they are added.

**Why it matters for pacing:** every append and every rewrite of the six durable logs opens its
lockfile `a+b` (including each projection tick's own `read_agent_pickups`), which makes these the
highest-frequency writes in the watched tree, and none of them is a projection input. The rule is
safe because no projection input is named `*.jsonl.lock` — the inputs are the `.jsonl` logs
themselves and `.json` sidecars.

`ChangePacer` is the wake scheduler; one instance belongs to one projector run loop. The watcher
feeds `notify_change()`/`set_watcher_healthy()`; the run loop awaits `wait()` once per tick, which
returns a `ProjectionWake` carrying reason (`"change"`/`"heartbeat"`/`"interval"`) and accumulated reader domains. Interval wakes request every domain; heartbeat wakes carry an empty invalidation set. The pure `_next_deadline()` holds
all scheduling rules (monotonic clock): **floor** — never two projections closer than `interval`
(`--interval` keeps its meaning as the fast-path cadence floor); **debounce** — a change projects
`DEBOUNCE_SECONDS` (0.1, clamped to `interval`) after the *last* change of its burst; **max delay**
— a sustained burst requests its deadline within `max_delay = interval` of its *first* change, subject to interval/completion floors; **heartbeat** — with no changes, project
every `heartbeat` seconds (default `DEFAULT_HEARTBEAT_SECONDS` = 15.0, floored to never undercut
`interval`); **degraded** — while the watcher is unhealthy, request interval-driven full refreshes, subject to the same completion rest. The pacer **starts degraded** so there is no detection blind spot
between boot and the watcher establishing its watches. `wait()` consumes pending changes at wake;
changes observed *during* a projection accumulate for the next cycle, so nothing is lost to a tick.

`ProjectionInputWatcher.run(pacer)` is the live watch task (lifecycle mirrors the landing
refresher: created by `create_app` for live serving only, started/cancelled by `Projector.run`).
`watchfiles` missing at import (`watchfiles = None`) logs a loud ERROR and degrades permanently for
that process. Otherwise the retry loop: derive roots **inside** the retry guard (review hardening —
a transient stat/glob failure follows the same loud degrade-and-retry path as a watch failure
instead of escaping `run()` and killing the task for good); zero roots is not an error (a
fresh/empty tree requests interval-driven full refreshes with completion rest and re-checks every `WATCH_REFRESH_SECONDS` = 30);
`_watch_once` marks the pacer healthy, emits one reconciling `notify_change()` on every
re-establish after the first (inotify has no replay — whatever happened while the watch was down
gets one debounced projection), then feeds `watchfiles.awatch(*roots, recursive=True)` batches
(library batching tightened to `debounce=200ms`/`step=50ms` so first detection never exceeds the
1s max-delay bound) into the pacer until `_stop_when_roots_change` — a 30s re-derivation task —
stops the generation to restart with a fresh root set. Any exception logs
`projection input watcher FAILED` (ERROR + traceback), sets the pacer unhealthy, sleeps 30s, and
retries.

### Conventions

The original input/filter/heartbeat/failure protections remain in `test_change_watcher.py`; completion-relative rest and retained-domain timelines are additionally pinned by the serving owner tests. `WakeTarget` and `ChangeWatch` are structural `Protocol`s — the
projector's seam mirrors `LandingStateRefresh` (the projector owns the task lifecycle, tests inject
fakes, this module ships the live implementation). Debounce/refresh constants are code defaults,
not settings knobs; `--heartbeat` is the only operator-facing knob.

### Invariants And Boundaries

- **Only *when* the projector wakes changes, never *what* a tick does.** The tick body
  (prime, diff/broadcast, ETag revision) is untouched by this module.
- **Failure reports LOUDLY and requests interval-driven full refreshes with completion rest.** Missing wheels, derivation failures and crashed watches log loudly and mark the watcher unhealthy; recoverable failures retry after 30s. Zero watchable roots is explicitly not an error: it keeps interval pacing and retries discovery without logging an ERROR.
- **Quiet heartbeat is a scheduling interval.** With no pending domains the next heartbeat deadline is based on the existing 15-second interval and the completion floor. A running tick and its publication can extend the elapsed gap; the heartbeat is not an unconditional maximum publication lag. Unwatched sources retain their existing TTL/heartbeat ownership, and volatile ages still advance through the frontend's existing served-age owner.
- **A tick never re-wakes itself.** The projection's own outputs live outside every watched
  subdirectory *and* are name-filtered; the workspace non-input churn is name-filtered; the
  control-plane lockfiles are suffix-filtered in every watched directory;
  TTL-gated writers that run inside a tick cost at most one debounced echo tick per TTL window,
  whose diff emits nothing.
- **The lockfile exclusion must stay derived from `lock_path_for`, never re-spelled.** A literal
  copy of the lock name is what silently stopped matching once the naming moved, and a basename list
  cannot reach the per-lifecycle `gates.jsonl.lock` at all. This module importing
  `kernel.file_lock` is the point of the rule, not an incidental dependency.
- **A busy world is completion-paced.** Change debounce and max-delay remain subject to the completed tick's bounded rest. Added rest, native batching, running/next tick time and publication are separate lag components; no exact interval-only throughput or total-freshness bound is claimed.
- **Live serving only.** `create_app` wires the watcher iff `before_tick is None`; `--sim` replay
  stays time-driven because the sim feeder writes only *inside* a tick — a change-gated loop would
  never wake.

### Todos

None.

## Evidence

### Docs References

No external Domain Documentation source is configured. This card records the repository's explicit `watchfiles` call arguments, retry policy and dependency declaration; it makes no claim to have checked upstream platform behavior.

No configured external domain documentation source.

### Repo-Internal References

The watch roots are derived from — and must stay in lock-step with — the reader list of
`project_and_write`; the projector consumes the pacer; `create_app` decides when a watcher exists;
the CLI/daemon own the `--heartbeat` knob's plumbing.

- Reader-derived roots and every-directory input filtering; live provider-runtime trees are excluded. [1]
- Accepted paths map to reader domains; unknown accepted paths request every domain. [2]
- Typed wake reason/domains, structural watcher seams and complete pacer scheduling. [3]
- Watcher root discovery, degraded empty-root behavior, explicit awatch arguments and retry lifecycle. [4]
- Shared lock naming and transaction mechanics keep filtering aligned. [5]
- Projection source readers determine the input surface. [6]
- Projector wiring and fail-open watcher completion retain actual ownership. [7]
- The live-input model selects actual watcher participation. [8]
- Dashboard reload entry carries the pacing configuration. [9]

| Derived suffix uses the same whole-log naming owner. | `_DURABLE_LOG_LOCK_SUFFIX` | mcp/src/agents_remember/serving/change_watcher.py:158-158 |
| Frontend advances volatile ages between heartbeat snapshots. | `VOLATILE_AGE_FIELDS` | dashboard/src/data/servedAges.ts:16-22 |
| Runtime dependency is explicitly version bounded. | "watchfiles>=1.1,<2" | mcp/pyproject.toml:28-28; mcp/pyproject.toml:34-34 |

### Cross-Repo References

No meaningful cross-repo references found.

Same-repository serving concern only.

## 260727-CHATS-IM-L2 Current Delta

Accepted watcher paths map to explicit projection reader domains. `ChangePacer` accumulates those
domains through debounce/max-wait and returns a `ProjectionWake`; an unmapped accepted path returns
all domains so correctness fails open to a full refresh.
