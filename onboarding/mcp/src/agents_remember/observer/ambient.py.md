# mcp/src/agents_remember/observer/ambient.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/observer/ambient.py`    |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-07T20:09+02:00                      |
| lastVerifiedCommitHash | `100b40d6be4a7d03eedbb1164ce54e2e8a314038`       |
| lastVerifiedCommitDate | 2026-08-14T08:23:37+02:00|
| governingOverview      | `overview.md`                                    |

## Purpose

`ambient.py` owns the process-scoped *current lifecycle*: the signal state
machine, event emission, the activity-decaying heartbeat ticker, and the
opportunistic TTL sweep. One stdio MCP server process is approximately one harness
session, so the active lifecycle is a process singleton that the `_tool_payload` choke
point reads to tag every tool call by construction (slice 2b of the observable-lifecycle
3.0 design). The heartbeat now reflects agent *activity*, not mere process liveness: it goes
quiet after a span of no real (non-heartbeat) events so an idle/parked lifecycle's log ages
out and becomes cleanable instead of being held alive by its own keepalive.

## Code Commentary

`AmbientLifecycle(store, *, timing=None, clock, id_factory, served_store=None)`
holds the single `current: LifecycleState | None` under a `threading.Lock`; all
state mutation and emission run under that lock because the heartbeat thread and
the request thread both append to the same single-writer per-lifecycle log.

Signals: `start` (guarded — raises `GuardedStartError` while a lifecycle is
active; mints the id, becomes `running`, emits `lifecycle.started`, starts the
ticker, sweeps); `block` (`running`→`blocked`, carrying an optional structured
ask via `build_ask`); `resume` (`blocked`→`running`); `end` (L243-L274 — emits
`lifecycle.ended` *before* clearing the ambient, so the end call's own
`tool.completed` is dropped — the terminal signal is the record — and returns the
terminal snapshot); `phase` (orthogonal phase move); `switch` (leave the current — persistent paused
`switched-away`, fleeting through the save gate — then mint a fresh one). Slice 2c
adds `promote` (fleeting→persistent on `worktree_start`: records the contract
`enclosure`/`repo_id`/`scope` and emits `lifecycle.promoted`) and `attach` (the
`worktree_attach` resume — none-active→adopt + `lifecycle.resumed` (`adopted`);
same id→no-op; persistent→pause+adopt; fleeting→save gate). The save gate lives in
`_leave_current_locked`: `save`⇒`_promote_to_landing_zone_locked` then pause,
`discard`⇒end `abandoned`, and no decision⇒`SaveGateRequired` (it blocks — never a
silent drop). `_emit_locked` stamps the envelope `enclosure`/`repoId` from the
current lifecycle.
Task 25 keeps `block` as the ambient state-machine operation used by the unified
`lifecycle_gate` public tool and by the retained lower-level compatibility
builder; `build_ask` remains the single ask-shape constructor for both paths.

**260731-EFA-L4: `end` no longer holds a copy of the terminal vocabulary.** This
module was the last hand-written copy of the live/terminal split. `end` used to
carry BOTH halves of the classification itself — a literal accept-tuple
`if outcome not in ("completed", "abandoned")` and then a separate outcome→state
conditional `terminal: State = "completed" if outcome == "completed" else "abandoned"`
— which is a copy, and a copy fails silently: a third terminal state would be one
the reducer projects and no session could write, and a renamed one would pass the
guard and then be mapped to the wrong state by the conditional. Both halves now
read `lifecycle_state`: the guard is `if outcome not in TERMINAL_STATES:`
cit:(["if outcome not in TERMINAL_STATES:"], mcp/src/agents_remember/observer/ambient.py:291-291)
(its message built from `'|'.join(sorted(TERMINAL_STATES))`) and the
conversion is `terminal = coerce_end_outcome(outcome)`
cit:(["terminal = coerce_end_outcome(outcome)"], mcp/src/agents_remember/observer/ambient.py:298-298). Membership is
already established by the guard, so that call is the identity conversion — it is
made anyway, rather than `cast`, so the outcome→state rule has exactly one owner
and the write side reads it from the same function the reducer's `_ended_updates`
does.

The **asymmetry is deliberate**: `coerce_end_outcome` defaults an unrecognized
outcome to `abandoned`, but `end` refuses one. That leniency exists for the
reducer, which reads logs it did not write; a session ending *itself* must not
have a typo silently recorded as an abandonment.

One literal `"abandoned"` deliberately remains, in the `discard` branch of
`_leave_current_locked` cit:([`_leave_current_locked`], mcp/src/agents_remember/observer/ambient.py:467-496): that branch is *naming one outcome*, not
classifying, so the literal is the decision. It is deliberately not
`DEFAULT_END_OUTCOME`, which is the separate policy for coercing a free-form
outcome at the tool boundary — discard would follow that constant anywhere it
moved, and there is no reason it should.

Task 28 adds the **NOTIFY-AND-CONTINUE turn end** — the new ACTIVE turn-end path,
modeled on `block`/`resume` but with no gate and no wait: `await_developer(*,
summary)` (`running`→`awaiting-developer`, emitting `lifecycle.awaiting-developer`
with the `summary` on the event data so the model can declare the turn complete
and stop) and `resume_from_await` (`awaiting-developer`→`running`, emitting
`lifecycle.resumed`). `resume_from_await` is a *separate* method from `resume`
precisely so the parked gate stack keeps its strict "only blocked resumes" guard —
`block`/`resume` are unchanged. The `_tool_payload` choke point calls
`resume_from_await` automatically when any tool other than the turn-end
notification fires while awaiting (the auto-dismiss that makes the notification a
*stop*, not a stall), so `awaiting-developer` is a notification, not a barrier.
The old `lifecycle_gate`/inbox stack is parked (kept, un-hinted).

`emit_tool(tool_name, payload)` is the choke-point hook: under the lock it
appends one `observed` `tool.completed` (tool/tokens/ok) to the active lifecycle,
or drops it when none is active — a lifecycle-less call is never misattributed.
It is wrapped in `contextlib.suppress(ValidationError, OSError)` so audit
emission can never break the tool it observes.

`emit_read_packet(repo_id, files)` is the slice-07 peer of `emit_tool`: it
appends one `observed` `read.packet` for the active lifecycle (dropped when none
is active, suppressing `ValidationError`/`OSError` so it never breaks the read).
Its **facts-only guarantee is structural**: every caller entry is projected to
the fixed allowlist `_READ_PACKET_FACTS` (`{path, lines, status, bytes}`) by
building a new dict that picks only those keys, so any other key — including file
content smuggled in by the caller — is dropped here regardless of input.
`Event`'s `extra="forbid"` only governs top-level Event fields, not the contents
of `data`, so the projection (not the envelope) is the privacy invariant. The
packet `data` also carries the read's `repoId` (slice 07b — the repo the files
belong to; a fact, distinct from the lifecycle's top-level Event `repoId` stamped
by `_emit_locked`). Riding the same ambient choke gives the packet the chat's
fleeting identity (or the adopted worktree lifecycle) by construction.

The **served-onboarding dedup ledger** (slice 07) lives beside the event logs:
the constructor takes an optional `served_store` (defaulting to
`ServedStore(store.root)`) and keeps a `_served: dict[str, set[str]]` in-memory
hot path. `_served_for_locked` hydrates a lifecycle's key set from `served.jsonl`
on first use, so the dedup survives a context compaction (the same process keeps
running). `served_keys` returns a copy of the set; `is_served(lifecycle_id, kind,
path, content_hash)` tests membership by `served_key`; `record_served(...,
ts=...)` adds the key in memory and appends a `ServedRecord` to disk
(`OSError`-suppressed so durability never breaks the read, while the in-memory set
still advances so the same call does not re-serve within one process);
`reset_served(lifecycle_id)` is the compaction/refresh reset — it drops the
in-memory set and deletes the on-disk `served.jsonl` so the next read re-serves
every piece (the single live owner deleting its own ledger keeps the
single-writer invariant). The served set is also pruned whenever the lifecycle
is left: `end` and the `discard` branch of `_leave_current_locked`
(`self._served.pop(...)`), and `_pause_locked` (switched-away).

The heartbeat ticker is a daemon `threading.Thread` (generalizing the
`setup_progress` idiom) that appends `lifecycle.heartbeat` every
`HEARTBEAT_SECONDS` until stopped on end/switch/`shutdown`; a stale last
heartbeat is how the projection reducer infers `paused (quiet)`. The ticker now
**decays with activity**: `_heartbeat_tick` skips the emit (returns True, keeping the loop
alive) whenever `_inactive_seconds_locked()` exceeds `_inactivity_cutoff_seconds`
(`INACTIVITY_CUTOFF_SECONDS`, 10 min) and returns False — ending the loop — when no lifecycle
is active or the current one is terminal; emitting resumes the moment a real event resets the clock.
`_inactive_seconds_locked()` is the age of `self._last_activity_iso`, which `_emit_locked`
stamps for every kind except the module-level `_HEARTBEAT_KIND` (heartbeats are liveness
theater, so they never refresh it). Since 260731-EFA-L2 the cutoff is pinned through the frozen
`AmbientTiming(heartbeat_seconds, ttl_seconds, inactivity_cutoff_seconds)` parameter object rather
than three separate constructor keywords — the three durations are one timing policy (a heartbeat
longer than the TTL keeps nothing alive), and passing `timing=AmbientTiming(...)` is how a test
overrides any of them; omitting it takes all three module defaults. The constructor still unpacks
them onto `_heartbeat_seconds` / `_ttl_seconds` / `_inactivity_cutoff_seconds`, so every internal
read is unchanged. Net: a parked lifecycle
stops beating and its dashboard log ages out under `event_retention`'s inactivity TTL instead
of being kept alive forever by its own keepalive.

**260731-EFA-L8 (round 13): the ticker wait is a monotonic-deadline recheck loop.** The loop body
is now `while not self._ticker_wait(stop, interval): if not self._heartbeat_tick(): return` — one
beat per wait return, with `_heartbeat_tick` owning the activity cutoff and the gone/terminal exit.
`_default_ticker_wait(stop, interval)` replaces `Event.wait`/`Condition.wait`: CPython's
waiter-lock handoff can overrun the timeout and leave the thread parked with no recheck or escape,
so the production wait chunks `time.sleep` against a monotonic deadline, re-reads the stop flag on
every wake, and returns deterministically when the interval expires — there is no wedged-wait path.
Tests inject a grant-stepping fake through the keyword-only `start(ticker_wait=...)` seam (stored
as `self._ticker_wait`) instead of racing a short interval.
`_reap_stale_fleeting` is the project-and-prune TTL sweep — it deletes the log
directory of any dormant (`> TTL_SECONDS`), never-promoted fleeting lifecycle (a
directory deletion, never a non-owner append) and runs opportunistically on
start/switch, since a dead process cannot reap itself.

Timing config + the age helper moved to `timeutil` (shared write↔read, slice
3a): `ambient` imports `HEARTBEAT_SECONDS` (15.0) and `TTL_SECONDS` (3600.0) for
the ticker and the TTL sweep, plus `age_seconds`/`Clock`; `STALE_AFTER_SECONDS`
(180.0, the projection's paused-by-dormancy threshold) is consumed by the
`reducer`, not here. The singleton lives on `_AmbientRegistry` (a class
attribute, not a module `global`); `ambient()` / `install_ambient` /
`require_ambient` / `reset_ambient` read and set it.

**260707-HFX2-L2 R5:** `AmbientLifecycle` gained a read-only `root` property returning
`self._store.root` (the observer store root, `logs/observer`) — a one-line accessor, no new state.
It exists so the `mcp/tools/base.py::_tool_payload` choke point can resolve the observer root and
check the agent-notifier sweep's heartbeat row (`serving/agent_notifier_heartbeat.py`) opportunistically on
every tool call, without constructing its own `McpRuntimeConfig` just to find that path. `ambient()`
was already the process-singleton entry point every tool call goes through, so this reuses that
existing seam rather than adding a second one.

## Invariants And Boundaries

- **The model never handles ids.** `start` is guarded; ids are minted and tracked
  server-side; `switch`/`attach` carry a target reference resolved from the
  worktree contract server-side, never a raw id from the model.
- **This module states no terminal vocabulary of its own (260731-EFA-L4).** `end`
  reads `TERMINAL_STATES` for the guard and `coerce_end_outcome` for the
  conversion; a new terminal state is added by filing it on `lifecycle_state`'s
  terminal half and nothing here changes. The one surviving `"abandoned"` literal
  (the `discard` branch, L462) names a single outcome as a decision and is not a
  classification — do not route it through `DEFAULT_END_OUTCOME`.
- **The write side refuses; the read side coerces.** `end` raises
  `LifecycleError` on an unknown outcome even though `coerce_end_outcome` would
  have defaulted it. Keep that asymmetry: the reducer reads foreign logs, a
  session ends only itself.
- **Two resume paths, two guards (task 28).** `resume` resumes only `blocked` (the
  parked gate stack); `resume_from_await` resumes only `awaiting-developer`. They
  are kept separate so the NOTIFY-AND-CONTINUE turn end can auto-resume at the
  choke point without loosening the gate's blocked-only guard. Both emit
  `lifecycle.resumed`.
- **Lifecycle-less calls are dropped, not misattributed** — the emission peer of
  "never pretend declared is observed". Holds for `tool.completed` and
  `read.packet` alike.
- **The `read.packet` facts-only guarantee is structural.** `emit_read_packet`
  projects every entry to `{path, lines, status, bytes}` by construction, so no
  source/onboarding/overview content can reach `Event.data` regardless of the
  caller — the projection, not `Event`'s `extra="forbid"`, is the privacy
  invariant. Alongside the per-file facts, `data.repoId` carries the read's repo
  (the repo the files belong to — a fact, distinct from the envelope `repoId`).
- **The served ledger is single-writer.** The one live lifecycle owner appends to
  and deletes its own `served.jsonl`; the in-memory set is hydrated from disk and
  pruned on end/discard/pause.
- **Single-writer-per-log is preserved:** the TTL sweep prunes a directory; it
  never appends to a log it does not own.
- **The heartbeat reflects activity, not liveness (task 34).** The ticker stops emitting
  after `_inactivity_cutoff_seconds` of no real event and resumes on the next real event; only
  non-heartbeat kinds stamp `_last_activity_iso`, so a heartbeat can never keep its own
  lifecycle's log alive. This is what lets `event_retention` age out an idle/parked log.
- **The ticker wait never wedges (260731-EFA-L8 round 13).** The production wait is
  `_default_ticker_wait`: chunked sleeps against a monotonic deadline with the stop flag re-read
  on every wake; the test seam (`start(ticker_wait=...)`) grants ticks deterministically, and the
  loop exits when `_heartbeat_tick` reports no active or terminal lifecycle.
- All mutation/emission is lock-guarded; the heartbeat ticker is a daemon thread
  stopped via `shutdown()` / end / switch.
- State *types* live in `lifecycle_state.py`; this module is behavior, threading,
  and the process registry. Durable gate records/enforcement and the projection
  read side belong to later slices.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The state/phase vocabulary, `LifecycleState`, and typed errors this module drives — and, since 260731-EFA-L4, the `TERMINAL_STATES` / `coerce_end_outcome` pair `end` reads instead of restating (`TERMINAL_STATES` L139, `coerce_end_outcome` L149-L158). | `TERMINAL_STATES`; `coerce_end_outcome`; `LifecycleState` | mcp/src/agents_remember/observer/lifecycle_state.py:108-108; mcp/src/agents_remember/observer/lifecycle_state.py:118-127; mcp/src/agents_remember/observer/lifecycle_state.py:156-179 |
| `end` is pinned to hold no string constant from `TERMINAL_STATES` and to convert through the shared function — a structural test, because a copy that happens to agree passes a behavioural one. | `test_the_end_signal_names_no_terminal_state_of_its_own` | mcp/tests/test_observer_ambient.py:181-189 |
| The append-only store the ambient writes events to. | `EventStore` | mcp/src/agents_remember/observer/store.py:103-171 |
| The `ar-observer-event/v1` envelope every signal emits. | `OBSERVER_EVENT_SCHEMA` | mcp/src/agents_remember/observer/events.py:23-23 |
| `mcp/tools/base.py::_tool_payload` delegates to `application/tool_response.py::complete_tool_response`, the choke point that calls `ambient().emit_tool(...)` for every public tool and (260707-HFX2-L2) reads `.root` to check the agent-notifier heartbeat. | "def complete_tool_response("; "amb.emit_tool(" | mcp/src/agents_remember/application/tool_response.py:53-53; mcp/src/agents_remember/application/tool_response.py:66-66 |
| The agent-notifier heartbeat store this `.root` accessor lets the tool choke point locate (260707-HFX2-L2 R5). | "the watcher must be code AND watched" | mcp/src/agents_remember/serving/agent_notifier_heartbeat.py:1-1 |
| The served-onboarding ledger store this owns (per-lifecycle `served.jsonl`). | `ServedStore` | mcp/src/agents_remember/observer/served_store.py:78-121 |
| The `read_ar_files` application entry point that calls `emit_read_packet` + the `amb.served.is_served`/`record`/`reset` dedup surface. | `emit_read_packet`; `is_served` | mcp/src/agents_remember/application/read_files.py:141-141; mcp/src/agents_remember/application/read_files.py:310-310 |
| The heartbeat/stale idiom this generalizes. | `SetupProgressFile` | mcp/src/agents_remember/providers/setup_progress.py:54-170 |
| The shared timing thresholds + `Clock` this imports (the `age_seconds` stamp-ager now lives in `controlplane.stamps`). | `HEARTBEAT_SECONDS`; `age_seconds` | mcp/src/agents_remember/observer/timeutil.py:29-29; mcp/src/agents_remember/controlplane/stamps.py:22-35 |
| The projection reducer that consumes the heartbeat/TTL signals (paused/abandoned). | `project_lifecycle`; `_project_inferred` | mcp/src/agents_remember/observer/reducer.py:120-147; mcp/src/agents_remember/observer/reducer.py:431-445 |
| The dashboard retention policy whose inactivity TTL ages out a log once its heartbeat decays. | `FLEETING_INACTIVE_TTL_SECONDS`; `prune_expired_lifecycle_event_logs` | mcp/src/agents_remember/observer/event_retention.py:37-37; mcp/src/agents_remember/observer/event_retention.py:73-107 |
| The design: state machine (§1.2-1.6), v1 event set (§2.2), TTL prune (§1.5), config (§8). | `### 1.2 States and the state machine`; `### 2.2 The v1 kind families (four, plus heartbeat)`; `## 8. Deferred to Implementation Phases` | docs/design/observable-lifecycle.md:40-133; docs/design/observable-lifecycle.md:156-171; docs/design/observable-lifecycle.md:391-402 |

## Update History

- 2026-08-08T22:10+02:00 — 260713-TES-L1 completion round (curator): refreshed this sidecar body for the supervisor -> agent-notifier rename (module paths, identifiers, settings keys, wire keys, prose) and the compat seams; verification metadata pinned until closeout stamps the 260713-TES-L1 commit.
- 2026-08-07T20:09+02:00 — 260731-EFA-L8 curator (bounded delta 2): recorded the round-13
  production fix — `_default_ticker_wait`'s monotonic-deadline chunked wait with stop recheck
  replaces `Event.wait` (no wedged-wait path), `start(ticker_wait=...)` is the keyword-only
  seam, and `_heartbeat_tick` owns the activity cutoff plus the gone/terminal loop exit.
  Verification metadata stays pinned until closeout stamps the code commit.
- 2026-08-04T18:16+02:00 — 260731-EFA-L6 S18-B16 curator: repaired all 13 citation rows and converted 5 superseded prose line citations to cit: forms against the frozen source (end guard L260-L263, conversion L267, discard branch L436-L465, end L243-L274). Three claims re-bound to moved code: the choke point now lives in application/tool_response.py (`complete_tool_response`, delegated from mcp/tools/base.py L73-L75), the served dedup surface is `amb.served.is_served`/`record`/`reset`, and `age_seconds` now lives in controlplane/stamps.py. Two unflagged stale line numbers in touched sentences corrected. Scoped fixer + non-fixing recheck green under the frozen snapshot; verification metadata unchanged.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-01T00:28+02:00 — 260731-EFA-L4 curator: the card described `end` only as "emits
  `lifecycle.ended` before clearing the ambient" and never mentioned that this method held the
  last hand-written copy of the live/terminal split. Verified against the diff and the current
  source and corrected it: the accept-tuple `("completed", "abandoned")` is now
  `if outcome not in TERMINAL_STATES:`
  cit:(["if outcome not in TERMINAL_STATES:"], mcp/src/agents_remember/observer/ambient.py:291-291)
  (message from `sorted(TERMINAL_STATES)`) and
  the outcome→state conditional is now `terminal = coerce_end_outcome(outcome)`
  cit:(["terminal = coerce_end_outcome(outcome)"], mcp/src/agents_remember/observer/ambient.py:298-298) — the
  identity conversion, called anyway rather than `cast`, so the rule has one owner. Recorded the
  deliberate asymmetry (`end` refuses an unknown outcome; `coerce_end_outcome` defaults it,
  because the reducer reads foreign logs), and the one surviving `"abandoned"` literal in the
  `discard` branch of `_leave_current_locked`
  cit:([`_leave_current_locked`], mcp/src/agents_remember/observer/ambient.py:467-496), which names one outcome as a decision and
  is deliberately not `DEFAULT_END_OUTCOME`. Added `end`'s line range
  cit:([`end`], mcp/src/agents_remember/observer/ambient.py:243-274), two invariants,
  and a reference row for the structural test that pins `end` to hold no such string constant.
- 2026-07-31T00:00+02:00 — 260731-EFA-L2 (gate honesty, `PLR0913` armed with no exemptions):
  the `AmbientLifecycle` constructor's `heartbeat_seconds` / `ttl_seconds` /
  `inactivity_cutoff_seconds` keywords were replaced by one frozen `AmbientTiming` parameter
  object passed as `timing=` (defaulting to `AmbientTiming()`, i.e. the same module constants).
  Callers that pinned a duration for tests must now build an `AmbientTiming`. Nothing about the
  state machine, the emission path, the ticker or the TTL sweep changed. Verification metadata
  pinned until closeout stamps the L2 commit.
- 2026-07-08T18:45+02:00 — 260707-HFX2-L2 (supervisor sweep, R5): added a read-only `root` property
  (`self._store.root`) so `mcp/tools/base.py`'s `_tool_payload` choke point can resolve the observer
  root and surface a stale-supervisor banner on any tool call without its own `McpRuntimeConfig`.
  No other behavior changed. Verification metadata pinned until closeout stamps the 260707-HFX2-L2
  commit.
- 2026-06-28T13:54+02:00 — Task 34: the heartbeat ticker now DECAYS with activity. Added
  `_inactive_seconds_locked()` and the `inactivity_cutoff_seconds` ctor param (+ module consts
  `INACTIVITY_CUTOFF_SECONDS`=600 and `_HEARTBEAT_KIND`); `_emit_locked` stamps `_last_activity_iso`
  for every non-heartbeat kind, and `_heartbeat_loop` skips the emit past the cutoff and resumes on
  real activity — so an idle/parked lifecycle's log ages out and becomes cleanable instead of being
  held alive by its own keepalive. Verification metadata pinned until closeout stamps the task-34 code commit.
- 2026-06-27T22:00+02:00 — Task 28 (NOTIFY-AND-CONTINUE turn end): added
  `await_developer(*, summary)` (`running`→`awaiting-developer`, emits
  `lifecycle.awaiting-developer` carrying `summary`) and `resume_from_await`
  (`awaiting-developer`→`running`, emits `lifecycle.resumed`). Modeled on
  `block`/`resume` but with no gate/inbox and no wait; `resume_from_await` is
  deliberately a separate method so `resume` keeps its blocked-only guard and the
  parked gate path is untouched. The choke point auto-resumes via
  `resume_from_await` on the next non-notification tool call. Verification metadata
  pinned until closeout stamps the code commit.
- 2026-06-26T14:16+02:00 — Task 25: clarified that `AmbientLifecycle.block`/`build_ask` now serve `lifecycle_gate` as the public gate path while the lower-level lifecycle-block builder remains compatibility-only.
- 2026-06-23T01:40+02:00 — Slice 07b v1: `emit_read_packet` now takes the read's `repo_id` (signature `emit_read_packet(repo_id, files)`) and carries it as `data.repoId` on the `read.packet` (a fact — the repo the files belong to, distinct from the envelope `repoId`); the facts-only per-file projection is unchanged. Body and invariant note only — verification metadata pinned until closeout stamps the slice-07b code commit.
- 2026-06-22T22:33+02:00 — Slice 07: documented `emit_read_packet` (the facts-only, allowlist-projected `read.packet` emitter — the privacy invariant is the structural projection, not `Event.extra`) and the per-lifecycle served-onboarding dedup ledger (`is_served`/`record_served`/`reset_served`/`served_keys`, the optional `served_store` ctor arg + in-memory `_served` set hydrated from `served.jsonl`, and the prune on end/discard/pause). Body and references only — verification metadata pinned until closeout stamps the slice-07 code commit.
- 2026-06-13T19:30+02:00: Slice 3a — the timing thresholds
  (`HEARTBEAT_SECONDS`/`STALE_AFTER_SECONDS`/`TTL_SECONDS`) and `_age_seconds` +
  the `Clock` alias moved to the shared `timeutil` leaf; this module now imports
  `HEARTBEAT_SECONDS`/`TTL_SECONDS` + `age_seconds`/`Clock` from it (behavior
  unchanged). Verification metadata is pinned until closeout stamps the 3a code commit.
- 2026-06-13T18:45+02:00: Slice 2c — added `promote`, `attach`, and the save gate
  (`_leave_current_locked` / `_promote_to_landing_zone_locked` / `_pause_locked`);
  `switch` now routes leave-from-fleeting through the save gate (explicit
  `on_unsaved`; blocking `SaveGateRequired`), and `_emit_locked` carries the
  envelope `enclosure`/`repoId`. The pure save-gate vocabulary moved to
  `save_gate.py`. Verification metadata is pinned until closeout stamps the 2c
  code commit.
- 2026-06-13T16:41+02:00: Created for slice 2b — the ambient lifecycle: signal
  state machine, choke-point emission, heartbeat ticker, TTL project-and-prune
  sweep, and the process registry. Verification metadata is pinned until closeout
  stamps the 2b code commit.
