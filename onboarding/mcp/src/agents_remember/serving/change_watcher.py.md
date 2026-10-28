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
heartbeat) fed by the `ProjectionInputWatcher` `watchfiles`/inotify task. The initial L3 change altered pacing, not tick contents. Current projection additionally consumes reader domains and complete path samples and performs independent full healing; byte-identity of today's tick is not claimed.

## Native events and completion-paced live wakes

The existing recursive watcher explicitly passes `force_polling=False` on supported local native POSIX/ext4 roots. Inherited WSL/environment polling selection cannot turn it into periodic recursive scans. Event/domain filtering, root refresh, nested atomic-write delivery, stop/drain and reported retry remain with this owner; no polling/mount fallback is added.

Completion preserves rest through max(existing floor, now + max(interval,min(duration,3s))). Once per rest window, task/host invalidation may spend an early pass at arrival+interval and last-wake floor; a quick tick preserves original rest. Pending domains survive failures and health changes until successful acknowledgement. Heartbeat is scheduling, not total-freshness or periodic host read.



## Code Commentary

One watcher per coordination root and ports-object identity caches by current binding generation/comparison/snapshot, captures only through its comparison owner, filters planning turn-end checks and emits notices without seat wakeups.

Accepted native paths reach the projection refresh, with explicit incompleteness falling back to full reconciliation. Pending own-write effects are judged after completion; completed identity/event-kind checks do not certify unknown foreign writes. Discovery/refresher/native-child death share one reported outage/retry path. Failure origins remain separate: root-refresher loss queues ALL after child drain; native-lane failure before registration preserves ordinary HEALING without adding host activity; registered native loss queues ALL after drain. The existing registration flag, stop/drain, exception reporting, stable downSince and default thirty-second retry retain their owners. If both failure buckets are populated, the root failure is reported first. Independent full healing preempts partial traffic; only successful full publication advances its clock.


### Logic

Existing roots cover `tasks`, the configured host-publication workspace, workspace dismissals, drift, `temp/worktree-start`, `temp/tool-reports` and, when configured, the activity directory, plus since MIK-R200 the `controlplane` activation records and terminal notice store and the temporary held-message queue. Central provider `logs/providers/{status,setup}` are **not** roots: no surviving projection reader reads them and they carry no `projection_domains_for_paths` entry, so an event there would fail open to every domain and rebuild from state nothing displays. Lifecycle logs are not roots. Root refresh admits newly appearing paths.

**Nothing under `worktrees/` is a native watch root.** The source records the reasons: about
50k checkout directories would recreate the scan cost, and each task's `provider-runtime` can
contain Postgres/grepai data unreadable to the daemon and churning on container/WAL writes.
Recursive watching previously crashed on permission-denied and would also wake projection for
those unrelated writes. Central provider status/setup is **not** watched under `logs/providers`, for the
reason the source gives in place: no surviving reader, no domain entry. The independent
provider-safety sampler keeps its own loop and needs no watch root. Worktree
provider/setup files retain their existing non-host safety/heartbeat owners.
`ProjectionInputWatcher._watch_once` additionally passes `ignore_permission_denied=True`, so an
unreadable subdirectory of an admitted root is skipped rather than killing the whole watch.
The original card recorded a dedicated no-worktree-root regression in `test_change_watcher.py`;
that module is absent from the current source tree, so this exclusion is currently supported
by the root constructor and explicit watch arguments, not an advertised surviving test.

Other deliberate non-host blind spots retain their own owners: per-repository memory surfaces
are not watch roots and have a 120-second retained-input/reader TTL, while native landing state
has an in-memory refresher and no file signal. Refresh opportunities also depend on scheduled
wakes and running work; a TTL is not an unconditional end-to-end publication deadline. Host
activity remains startup/explicit-invalidation intake, not a periodic census.

`is_projection_input_event(path)` filters one raw watch event: drops `*.tmp` atomic-write temps,
dot-prefixed sidecar temps, **every control-plane lockfile, by suffix, in any watched directory**
(see below), the projection's own outputs (`latest-state.json`/
`latest-metrics.json`, defensive — they also live *outside* every watched subdirectory), and the
`workspace/` non-input churn by name **only when the parent dir is `workspace`** (the raw event
river `events.jsonl` + its cursor/lock files with no supervisor heartbeat input). Host publication paths map to HOST_ACTIVITY; workspace River records are not task-status inputs.

### 260731-EFA-L5 The Lockfile Exclusion Is Derived, Not Spelled Out

`_DURABLE_LOG_LOCK_SUFFIX = lock_path_for(Path("log.jsonl")).name.removeprefix("log")` — the suffix
that `kernel.file_lock.lock_path_for` gives a `.jsonl` control-plane log, **derived from
that function** rather than written down. `is_projection_input_event` suffix-matches it and returns
`False` before any of the name checks.

**Spelling it out is what broke.** This filter carried the literal `"operator-inbox.lock"` in
`_EXCLUDED_WORKSPACE_NAMES` while `lock_path_for` had moved to `operator-inbox.jsonl.lock`, so the
exclusion silently stopped matching anything — a filter that looks correct and filters nothing. The
name is now out of that set entirely; the set keeps only `events.jsonl`, the workspace cursor and
lock, with no supervisor heartbeat name.

The derived whole-log lock suffix applies in every watched directory. Legacy gate-log placement does not reinstate lifecycle-log watching or a per-session projection domain; sibling lock creation is not an input.

**Why it matters for pacing:** every append and every rewrite of a retained durable log opens its
lockfile `a+b` (including each projection tick's attention-dismissal reconciliation), which makes these the
highest-frequency writes in the watched tree, and none of them is a projection input. The rule is
safe because no projection input is named `*.jsonl.lock` — the inputs are the `.jsonl` logs
themselves and `.json` sidecars.

`ChangePacer` is the monotonic wake scheduler, one instance per projector run loop.
`notify_change()` accumulates pending domains and path completeness, and `wait()` snapshots them
into a `ProjectionWake` rather than clearing them. Its retained scheduling rules are:

- **Floor:** ordinary eligibility is at least `last_wake + interval` and the completed tick's
  rest floor. `projection_completed` retains the later existing floor or
  `now + max(interval, min(duration, 3 seconds))`.
- **Debounce:** settle after the last change by `DEBOUNCE_SECONDS` (default 0.1 seconds,
  clamped to a positive interval). **Max delay:** a sustained burst uses
  `first_pending + max_delay`, default `max_delay = interval`; both remain subject to the
  interval/completion floors and the existing one-use task/host early-pass exception.
- **Heartbeat:** with no pending changes, use `DEFAULT_HEARTBEAT_SECONDS` (15 seconds),
  floored to never undercut `interval` and still subject to completion rest and due full healing.
  Heartbeat wakes carry no domain invalidations.
- **Degraded:** before watch establishment and while unhealthy, request interval-paced full
  refreshes with the same completion rest. The pacer starts degraded, closing the boot-to-watch
  detection gap. Due independent full healing preempts partial traffic.

Change wakes carry pending domains; interval/full wakes carry
`HEALING_PROJECTION_DOMAINS` plus pending domains (no `HOST_ACTIVITY` unless pending).
Only unchanged-generation successful publication acknowledges work; failed wakes retain domains
and paths. Degradation heals/retries loudly without host polling. These are scheduling rules,
not an interval-only throughput or total-freshness guarantee.

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
(library batching tightened to `debounce=200ms`/`step=50ms` to shorten native batching; this configuration alone does not establish a one-second total detection bound) into the pacer until `_stop_when_roots_change` — a 30s re-derivation task —
stops the generation to restart with a fresh root set. Any exception logs
`projection input watcher FAILED` (ERROR + traceback), sets the pacer unhealthy, sleeps 30s, and
retries.

### Conventions

The original card attributed input/filter/heartbeat/failure regressions to the historical
`test_change_watcher.py`; that module is not present in the current tree. Current scheduling
and native-watch claims here are grounded in the owning implementation. Completion-relative rest
and retained-domain timelines are additionally pinned by the surviving serving-owner tests:
`test_serving.py` covers the one-use task/host early pass, ordinary-domain rest, an earlier
normal deadline, capped slow-tick rest with work/rest arrivals, and completion callbacks on startup
and failure. `test_pacer_healing.py` asserts failed change wakes retain their domains and arrivals
before acknowledgement keep the merged set. These are inspected source assertions, not a new
execution result or a surviving dedicated no-worktree-root regression. `WakeTarget` and `ChangeWatch` are structural `Protocol`s — the
projector's seam mirrors `LandingStateRefresh` (the projector owns the task lifecycle, tests inject
fakes, this module ships the live implementation). Debounce/refresh constants are code defaults,
not settings knobs; `--heartbeat` is the only operator-facing knob.

### Invariants And Boundaries

- **The original L3 pacing-only boundary is historical.** Current wakes also select reader domains/path-directed refresh or full reconciliation; publication, diff/broadcast and ETag ownership remains with the projector.
- **Failure reports LOUDLY and requests interval-driven full refreshes with completion rest.** Missing wheels, derivation failures and crashed watches log loudly and mark the watcher unhealthy; recoverable failures retry after 30s. Zero watchable roots is explicitly not an error: it keeps interval pacing and retries discovery without logging an ERROR.
- **Quiet heartbeat is a scheduling interval.** With no pending domains the next heartbeat deadline is based on the existing 15-second interval and the completion floor. A running tick and its publication can extend the elapsed gap; the heartbeat is not an unconditional maximum publication lag. Unwatched non-host sources retain their existing TTL/heartbeat ownership, and volatile ages still advance through the frontend's existing served-age owner.
- **A tick never re-wakes itself.** The projection's own outputs live outside every watched
  subdirectory *and* are name-filtered; the workspace non-input churn is name-filtered; the
  control-plane lockfiles are suffix-filtered in every watched directory;
  TTL-gated writers that run inside a tick cost at most one debounced echo tick per TTL window,
  whose diff emits nothing.
- **The lockfile exclusion must stay derived from `lock_path_for`, never re-spelled.** A literal
  copy of the lock name is what silently stopped matching once the naming moved, and a basename list
  would not cover sibling locks wherever a retained store lives. This module importing
  `kernel.file_lock` is the point of the rule, not an incidental dependency.
- **A busy world is completion-paced.** Change debounce and max-delay retain completion rest, except the one-use task/host early pass described above; that pass preserves the original rest for later arrivals. Added rest, native batching, running/next tick time and publication are separate lag components; no exact interval-only throughput or total-freshness bound is claimed.
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

- The source records why recursive worktree watching would repeat scan cost, crash on container permissions and react to WAL churn; admitted roots exclude that tree. 
- Native watching skips unreadable subdirectories as defence-in-depth. [14]
- Defaults are 0.1-second debounce and 15-second heartbeat; max delay defaults to interval and the pacer starts degraded. [15]
- Debounce/max-delay/heartbeat deadlines retain interval and completion floors, subject to the one-use task/host rest exception and due full healing. [16]
- Change, full and heartbeat wakes preserve their distinct domain selection; full healing does not reread host activity unless pending. [17]

- Serving-owner assertions allow one early task/host pass per original rest window; a quick early tick preserves that rest. [18]
- Other domains retain rest without spending the task exception; a task arrival merges the pending set and may use it. [19]
- The task exception never delays an earlier ordinary deadline. [20]
- Capped completion rest retains work/rest arrivals and keeps degraded and recovery-full deadlines completion-paced. [21]
- Prime and failed live ticks invoke the completion callback; replay has no pacer. [22]
- A failed change wake retries its outstanding domains until acknowledgement. [23]
- An arrival before acknowledgement advances generation and re-wakes the merged set. [24]

The watch roots are derived from — and must stay in lock-step with — the reader list of
`project_and_write`; the projector consumes the pacer; `create_app` decides when a watcher exists;
the CLI/daemon own the `--heartbeat` knob's plumbing.


- Projector wiring and fail-open watcher completion retain actual ownership. [7]


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


- Reader-derived roots and every-directory input filtering; live provider-runtime trees are excluded. [1]


- Accepted paths map to reader domains; unknown accepted paths request every domain.


- Typed wake reason/domains, structural watcher seams and complete pacer scheduling. [3]


- Watcher root discovery, degraded empty-root behavior, explicit awatch arguments and retry lifecycle. 


- Shared lock naming and transaction mechanics keep filtering aligned. [5]


- Projection source readers determine the input surface. [6]


- The live-input model selects actual watcher participation. [8]

- Dashboard reload entry carries the pacing configuration.

Retired at the fifth freeze d59c3493: mcp/src/agents_remember/cli/dashboard.py:101-153 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 20624f979e2b89067a3e42019c9611a8e18ff848. Retired means the anchor no longer stands, not that the cited subject was deleted [9]

- Native registration is explicit and retains watcher lifecycle.  Anchor: `ProjectionInputWatcher._watch_once` [10]


- The real completion floor preserves accumulated domains.  Anchor: `ChangePacer.projection_completed` [11]


- Completion rest participates in change/degraded/heartbeat deadlines.  Anchor: `ChangePacer._next_deadline` [12]


- After child drain, root-refresher loss or established native-watch loss reconciles all domains; pre-registration native failure keeps ordinary degraded healing. The existing outage and retry owner remains.

Retired at the fifth freeze d59c3493: mcp/src/agents_remember/serving/change_watcher.py:852-889 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit a66314c555d873dd01b4dbefbe18fb3f2ee44d4b; mcp/src/agents_remember/serving/change_watcher.py:891-951 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 87992ce842079a7a4f161bd4bfcc4aed5307178b; mcp/src/agents_remember/serving/change_watcher.py:886-923 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 5e34b4fe25c386dde75b04f6b63d3c64e62afe39; mcp/src/agents_remember/serving/change_watcher.py:925-985 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit a414bf4725215f2cf236d6d492bc070a973bce08. Retired means the anchor no longer stands, not that the cited subject was deleted [25]

- One watcher per coordination root and ports-object identity caches by current binding generation/comparison/snapshot, captures only through its comparison owner, filters planning turn-end checks and emits notices without seat wakeups. [26]

- The source records why recursive worktree watching would repeat scan cost, crash on container permissions and react to WAL churn; admitted roots exclude that tree. [13]

- Retired at the fifth freeze d59c3493: mcp/src/agents_remember/serving/change_watcher.py:234-280 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit a414bf4725215f2cf236d6d492bc070a973bce08; mcp/src/agents_remember/serving/change_watcher.py::ProjectionInputWatcher - the bytes it recorded now occur 2 times in the file, so no single home can be named and it is not given to the likelier one; mcp/src/agents_remember/serving/change_watcher.py::projection_input_roots - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit a414bf4725215f2cf236d6d492bc070a973bce08. Retired means the anchor no longer stands, not that the cited subject was deleted.

## Retirements

- Retired at the fifth freeze d59c3493: mcp/src/agents_remember/serving/change_watcher.py:852-889 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit a66314c555d873dd01b4dbefbe18fb3f2ee44d4b; mcp/src/agents_remember/serving/change_watcher.py:891-951 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 87992ce842079a7a4f161bd4bfcc4aed5307178b; mcp/src/agents_remember/serving/change_watcher.py:886-923 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 5e34b4fe25c386dde75b04f6b63d3c64e62afe39; mcp/src/agents_remember/serving/change_watcher.py:925-985 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit a414bf4725215f2cf236d6d492bc070a973bce08. Retired means the anchor no longer stands, not that the cited subject was deleted.

- Retired at the fifth freeze d59c3493: mcp/src/agents_remember/cli/dashboard.py:101-153 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 20624f979e2b89067a3e42019c9611a8e18ff848. Retired means the anchor no longer stands, not that the cited subject was deleted.