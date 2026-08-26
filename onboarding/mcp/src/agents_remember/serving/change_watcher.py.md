# mcp/src/agents_remember/serving/change_watcher.py

| Field                  | Value                                                |
| ---------------------- | ---------------------------------------------------- |
| repository             | agents-remember                                      |
| path                   | `mcp/src/agents_remember/serving/change_watcher.py`  |
| doc_type               | `file-level-onboarding`                              |
| lastUpdated | 2026-08-01T19:45+02:00 |
| lastVerifiedCommitHash |                                                      `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d`|
| lastVerifiedCommitDate |                                                      2026-08-26T08:10:26+02:00|
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
dot-prefixed sidecar temps, **every control-plane lockfile, by suffix, in any watched directory**
(see below), the projection's own outputs (`latest-state.json`/
`latest-metrics.json`, defensive — they also live *outside* every watched subdirectory), and the
`workspace/` non-input churn by name **only when the parent dir is `workspace`** (the raw event
river `events.jsonl` + its cursor/lock files and the supervisor's own heartbeat row). A lifecycle's
`events.jsonl` is NOT confused with the workspace river.

### 260731-EFA-L5 The Lockfile Exclusion Is Derived, Not Spelled Out

`_DURABLE_LOG_LOCK_SUFFIX = lock_path_for(Path("log.jsonl")).name.removeprefix("log")` — the suffix
that `controlplane.durable_store.lock_path_for` gives a `.jsonl` control-plane log, **derived from
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
  subdirectory *and* are name-filtered; the workspace non-input churn is name-filtered; the
  control-plane lockfiles are suffix-filtered in every watched directory;
  TTL-gated writers that run inside a tick cost at most one debounced echo tick per TTL window,
  whose diff emits nothing.
- **The lockfile exclusion must stay derived from `lock_path_for`, never re-spelled.** A literal
  copy of the lock name is what silently stopped matching once the naming moved, and a basename list
  cannot reach the per-lifecycle `gates.jsonl.lock` at all. This module importing
  `controlplane.durable_store` is the point of the rule, not an incidental dependency.
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

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant documentation found after checking live sources; no Domain Documentation entries are configured. | N/A | N/A |

## Repo-Internal References

The watch roots are derived from — and must stay in lock-step with — the reader list of
`project_and_write`; the projector consumes the pacer; `create_app` decides when a watcher exists;
the CLI/daemon own the `--heartbeat` knob's plumbing.

| Finding | Anchor | Source |
| --- | --- | --- |
| Module docstring: the R1 root-derivation table (root → readers), the deliberate blind spots, self-trigger safety (now naming the suffix-filtered lockfiles), the R5 freshness bounds, and the R7 failure posture. | "Failure posture (R7)" | mcp/src/agents_remember/serving/change_watcher.py:68-68 |
| Constants (heartbeat 15s L109, debounce 0.1s L113, awatch 200/50ms batching L118-L119, 30s refresh L123), the output/workspace name-filter sets (L126, L133-L140), and `_DURABLE_LOG_LOCK_SUFFIX` with the rationale comment that says why it is derived (L142-L156). | `_DURABLE_LOG_LOCK_SUFFIX` | mcp/src/agents_remember/serving/change_watcher.py:158-158 |
| `projection_input_roots` (existing-dirs-only, nothing under `worktrees/` — container data is unreadable and high-churn) and `is_projection_input_event` (tmp/dotfile/lockfile-suffix/output/workspace-churn filter). | `projection_input_roots`, `is_projection_input_event` | mcp/src/agents_remember/serving/change_watcher.py:159-184; mcp/src/agents_remember/serving/change_watcher.py:187-205 |
| `projection_domains_for_paths` — accepted paths mapped to reader domains, unmapped ⇒ every domain. | `projection_domains_for_paths` | mcp/src/agents_remember/serving/change_watcher.py:208-252 |
| `ProjectionWake`, the `WakeTarget`/`ChangeWatch` protocols, and `ChangePacer` (`_next_deadline` scheduling core, degraded boot state, consume-at-wake). | `ProjectionWake`, `ChangePacer` | mcp/src/agents_remember/serving/change_watcher.py:255-260; mcp/src/agents_remember/serving/change_watcher.py:283-376 |
| `ProjectionInputWatcher`: derivation inside the retry guard, empty-roots idle path, reconcile-on-re-establish, awatch generation restart on root-set change (`_stop_when_roots_change`), loud degrade + 30s retry. | `ProjectionInputWatcher` | mcp/src/agents_remember/serving/change_watcher.py:379-487 |
| `lock_path_for` — the single source this module derives its lockfile suffix from, so the filter cannot drift out of step with the stores again. | `lock_path_for` | mcp/src/agents_remember/controlplane/durable_store.py:334-341 |
| The tick entry whose readers define the watched input surfaces. | `project_and_write` | mcp/src/agents_remember/serving/projections/projection_store.py:212-275 |
| The projector side: `ProjectionRefreshers` (all three live inputs enabled together), pacer construction (watcher present ⇒ `ChangePacer`, absent ⇒ legacy `sleep(self._interval)`), change-or-heartbeat waking in `run`, and the `_on_watch_task_done` fail-open callback. | `ProjectionRefreshers`, `_on_watch_task_done` | mcp/src/agents_remember/serving/projector.py:112-123; mcp/src/agents_remember/serving/projector.py:262-273 |
| `create_app(cadence=ProjectionCadence(heartbeat=…), live_inputs=LiveProjectionInputs(change_watch=…))`: watcher enabled iff `replay.before_tick is None` (sim replay stays time-driven) via `change_watcher=ProjectionInputWatcher(config) if enabled.change_watch else None`; the three live-input toggles resolve together in `LiveProjectionInputs.resolved()`. | "class LiveProjectionInputs:" | mcp/src/agents_remember/serving/_app_common.py:395-395 |
| The `--interval` flag re-documented as the fast-path cadence floor (L101-L109) and the `--heartbeat` flag (L110-L118), plus the reload/daemon heartbeat plumbing (`_dev_app` L76-L80, the reload env hand-off L218-L221, `serving_daemon.ensure` L294). | `_dev_app` | mcp/src/agents_remember/cli/dashboard.py:52-81 |
| The client-side volatile-age advancement that makes heartbeat-resolution time-derived fields acceptable (R4). | `VOLATILE_AGE_FIELDS` | dashboard/src/data/servedAges.ts:16-22 |
| The R1-R7 regression suite: root derivation, event filtering including lockfile-suffix cases, domain mapping, pure pacer deadlines, projector integration (heartbeat-only quiet world, debounce-bounded change, burst coalescing, loud degrades, derivation-failure retry, legacy no-watcher pacing), and one real-inotify end-to-end pass. | `ProjectionInputRootsTests`, `InputEventFilterTests`, `ProjectionDomainMappingTests`, `ChangePacerDeadlineTests`, `AdaptiveProjectorTests`, `RealWatchfilesIntegrationTests` | mcp/tests/test_change_watcher.py:48-95; mcp/tests/test_change_watcher.py:98-139; mcp/tests/test_change_watcher.py:142-170; mcp/tests/test_change_watcher.py:173-221; mcp/tests/test_change_watcher.py:252-441; mcp/tests/test_change_watcher.py:444-485 |
| The new runtime dependency this module degrades without. | "watchfiles>=1.1" | mcp/pyproject.toml:31-31 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| Same-repository serving concern only. | N/A | N/A |

## 260727-CHATS-IM-L2 Current Delta

Accepted watcher paths map to explicit projection reader domains. `ChangePacer` accumulates those
domains through debounce/max-wait and returns a `ProjectionWake`; an unmapped accepted path returns
all domains so correctness fails open to a full refresh.

## Update History

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-02T21:14+02:00 — W2-B03 curator: resolved 16 initial citation findings (8 anchor, 0 prose, 8 source); scoped recheck PASS (0 findings). Verification metadata unchanged.

- 2026-08-01T19:45+02:00 — 260731-EFA-L5 (durable store integrity). The card described the
  lockfile exclusion as a name in `_EXCLUDED_WORKSPACE_NAMES` (`operator-inbox.lock`), which is both
  gone and was the defect: the literal had stopped matching once `lock_path_for` moved to
  `operator-inbox.jsonl.lock`, so the filter looked correct and filtered nothing. Recorded the
  replacement — `_DURABLE_LOG_LOCK_SUFFIX`, **derived** from `lock_path_for(Path("log.jsonl"))` and
  suffix-matched in **every watched directory** — and why suffix-and-everywhere is what a basename
  list structurally could not express: `gates.jsonl` lives under `workspace/` *and* once per
  lifecycle, so `gates.jsonl.lock` appears in every lifecycle directory. Recorded that these are the
  highest-frequency writes in the watched tree (every durable-store append and rewrite opens one
  `a+b`) and that the rule is safe because no projection input is named `*.jsonl.lock`. Added the
  invariant that the exclusion must stay derived. Re-anchored **every** citation in the table
  against the current source, since the earlier ranges predated three leaves: module docstring
  `L1-L67` → **L1-L71** (the old range stopped three lines short of the R7 failure posture the same
  claim names); constants `L97-L131` → **L107-L156** (it stopped short of both
  `_EXCLUDED_WORKSPACE_NAMES` and `_DURABLE_LOG_LOCK_SUFFIX`); `L134-L175` → **L159-L205**;
  `L178-L279` → **L255-L376**; `L282-L384` → **L379-L487**; added a row for
  `projection_domains_for_paths` (**L208-L252**), which the table never had. Off-file citations
  likewise: `projector.py` `L105-L124; L149-L205` → **L107-L119; L145-L160; L193-L250** (neither old
  range contained `_on_watch_task_done` or the legacy `sleep(self._interval)` the claim names);
  `app.py` `L467-L505` → **L606-L688** (`L467` is now a `TerminalLandedCleanupRequest` field);
  `cli/dashboard.py` `L59-L78; L190-L196` → **L101-L118; L76-L80; L218-L221**;
  `test_change_watcher.py` `L1-L435` → **L1-L489**. Added a `lock_path_for` reference row.
  Verification metadata untouched and still pinned.
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
