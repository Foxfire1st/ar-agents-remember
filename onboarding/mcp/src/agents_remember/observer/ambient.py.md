# mcp/src/agents_remember/observer/ambient.py

## Governing Overview

[overview.md](overview.md)

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
*stop*, not a stall), so `awaiting-developer` is a notification, not a blocker.
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

## Evidence

### Repo-Internal References

- The state/phase vocabulary, `LifecycleState`, and typed errors this module drives — and, since 260731-EFA-L4, the `TERMINAL_STATES` / `coerce_end_outcome` pair `end` reads instead of restating (`TERMINAL_STATES` L139, `coerce_end_outcome` L149-L158). [1]
- The append-only store the ambient writes events to. [2]
- The `ar-observer-event/v1` envelope every signal emits. [3]
- The application response boundary finalizes the payload and emits the completed tool call when an ambient lifecycle exists. [4]
- The optional stale-notifier banner reads the ambient root and contains errors before response enrichment. [5]
- The agent-notifier heartbeat store this `.root` accessor lets the tool choke point locate (260707-HFX2-L2 R5). [6]
- The served-onboarding ledger store this owns (per-lifecycle `served.jsonl`). [7]
- The `read_ar_files` application entry point that calls `emit_read_packet` + the `amb.served.is_served`/`record`/`reset` dedup surface. [8]
- The heartbeat/stale idiom this generalizes. [9]
- The shared timing thresholds + `Clock` this imports (the `age_seconds` stamp-ager now lives in `controlplane.stamps`). [10]
- The projection reducer that consumes the heartbeat/TTL signals (paused/abandoned). [11]
- The dashboard retention policy whose inactivity TTL ages out a log once its heartbeat decays. [12]
- The design: state machine (§1.2-1.6), v1 event set (§2.2), TTL prune (§1.5), config (§8). [13]
