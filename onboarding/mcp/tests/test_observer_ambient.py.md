# test_observer_ambient.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_observer_ambient.py`             |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-01T09:18+02:00                           |
| lastVerifiedCommitHash | `e52edaf5b655f495580efd93306afdf922b19b51`       |
| lastVerifiedCommitDate | 2026-08-01T11:01:51+02:00|
| governingOverview      | `../overview.md`                              |

## Governing Overview

[mcp overview](../overview.md) — there is no route-local `mcp/tests/overview.md`.

## Purpose

`test_observer_ambient.py` covers the ambient lifecycle (slices 2b-2c): the
signal state machine, guarded start, switch transitions, the choke-point
emission, the TTL project-and-prune sweep, the heartbeat ticker (2b), and the
promotion, attach/resume, and save gate (2c). Since 260731-EFA-L4 it also pins
the **structure** of the `end` signal: that it holds no private copy of the
terminal-state vocabulary.

## Code Commentary

### 260707-HFX2-L13 Heartbeat-Sidecar Compatibility

The activity-decay heartbeat test now reads the coalesced sidecar timestamp rather than scanning
`events.jsonl`. It still proves the same behavioral contract: active lifecycle beats advance, idle
time does not mint new heartbeats, and the next real signal resumes the ticker.

### Logic

`StateMachineTests` assert running/fleeting start + the guard, the
started→phase-changed→blocked→resumed→ended event order, the block/resume
state guards, that `end` clears the ambient and lifts the guard, the bad-outcome
rejection, a phase move, and that a signal without an active lifecycle raises.
Task 28 adds the NOTIFY-AND-CONTINUE turn-end guards:
`test_await_developer_only_from_running` (`running`→`awaiting-developer` emits
`lifecycle.awaiting-developer` carrying the `summary` on its event data; a second
`await_developer` from `awaiting-developer` raises) and
`test_resume_from_await_only_from_awaiting` (the strict `resume()` stays
blocked-only and raises on an await; `resume_from_await()`→`running` emits
`lifecycle.resumed`, and calling it from `running` raises).

`EndSignalVocabularyTests` (L157-L186) is the one class here that asserts against the *shape* of
the production method rather than its behaviour. `observer/ambient.py::end` held the last
hand-written copy of the live/terminal split — a literal `("completed", "abandoned")` accept-tuple
plus an outcome→state conditional — and now guards on `TERMINAL_STATES` and converts through
`coerce_end_outcome` (both from `observer/lifecycle_state.py`, L139 and L149).
`test_the_end_signal_names_no_terminal_state_of_its_own` intersects the string constants compiled
into `AmbientLifecycle.end` with `TERMINAL_STATES` and requires the intersection empty;
`test_the_end_signal_converts_through_the_vocabulary` requires **both** `coerce_end_outcome` and
`TERMINAL_STATES` in `end.__code__.co_names`, because a bare `cast` would also name no state and
would pass the first test alone. Reading the code object rather than the source text is the point:
a comment or a docstring promising the vocabulary is shared satisfies neither assertion. The
behavioural pin lives elsewhere — `test_the_ambient_end_signal_accepts_exactly_the_terminal_states`
in `test_observer_projection.py` — and a copy that happens to agree with today's vocabulary passes
it, which is exactly what the removed copy did for as long as it existed; these pin the structure
so a third or renamed terminal state cannot desynchronise silently.

`SwitchTests` assert that leaving a fleeting current now needs an explicit
`on_unsaved` (no decision raises `SaveGateRequired`; `discard` ends it then starts
fresh; `save` promotes then pauses), and that switching from a persistent current
pauses it. `PromoteTests` assert `promote` makes the lifecycle persistent, records
the scope, emits `lifecycle.promoted`, and that later events carry the envelope
`enclosure`/`repoId`. `AttachTests` assert the §1.3 table (none→adopt+`resumed`;
same→no-op; persistent→pause+adopt; fleeting→save gate). `SaveGateUnitTests` cover
`compute_scope` and `coerce_save_decision`. `EmissionTests` assert
`emit_tool` tags exactly one `observed` `tool.completed` on the active lifecycle,
that a lifecycle-less call writes nothing, and that the `end` signal leaves no
trailing `tool.completed`. `TtlSweepTests` seed logs with old timestamps and
assert dormant fleeting logs are pruned while persistent, fresh, and promoted
ones are kept, and that `start`'s opportunistic sweep keeps the fresh current.
`HeartbeatTests` run a short-interval ticker and assert `lifecycle.heartbeat`
events appear, plus the task-34 **activity-decay** coverage:
`test_inactive_seconds_tracks_real_activity_not_heartbeats` (a deterministic clock proves real events
reset `_inactive_seconds_locked()` to 0 while an emitted heartbeat does not) and
`test_heartbeat_ticker_goes_quiet_when_idle_and_resumes_on_activity` (the ticker beats while active,
goes silent once the clock jumps past `inactivity_cutoff_seconds`, and resumes the moment a real
`emit_tool` resets the activity clock). `AskTests` cover `build_ask` pruning and `coerce_phase` validation.

### Conventions

Inserts `mcp/src` on `sys.path` (the suite idiom). `_AmbientCase` builds an
`AmbientLifecycle` over a `tempfile.TemporaryDirectory` `EventStore` with a long
heartbeat for determinism — the cadence rides one `timing=AmbientTiming(...)`
parameter object rather than loose keywords — and calls `shutdown()` in `tearDown`
to stop the ticker; the heartbeat tests deliberately use a short interval then stop
before reading. The task-34 decay tests inject a list-backed mutable clock (still a
separate `clock=` argument) plus an explicit
`AmbientTiming(heartbeat_seconds=..., inactivity_cutoff_seconds=...)` so they can step
time deterministically across the cutoff.

`EndSignalVocabularyTests` is the exception to every convention above: it is a plain
`unittest.TestCase`, not an `_AmbientCase`, because it never instantiates an `AmbientLifecycle` —
it reads the unbound `AmbientLifecycle.end` function object. Its instrument is the module-level
`_string_constants(function)` helper (L140-L154), which walks `function.__code__.co_consts` with an
explicit stack, flattening nested `tuple | frozenset | set | list` constants so a vocabulary folded
into a literal container is still seen.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The ambient lifecycle under test. | [ambient.py](agents-remember/mcp/src/agents_remember/observer/ambient.py) |
| The state vocabulary (`TERMINAL_STATES` L139), `coerce_end_outcome` (L149), the errors, and `coerce_phase` under test. | [lifecycle_state.py](agents-remember/mcp/src/agents_remember/observer/lifecycle_state.py) |
| The store events are written to and read back from. | [store.py](agents-remember/mcp/src/agents_remember/observer/store.py) |
| Task 34 heartbeat activity-decay coverage (L315-L372): inactivity tracks real activity not heartbeats; the ticker goes quiet past the cutoff and resumes on activity. | [test_observer_ambient.py](agents-remember/mcp/tests/test_observer_ambient.py) |
| `_string_constants` (L140-L154) + `EndSignalVocabularyTests` (L157-L186): the `end` signal names no terminal state of its own and converts through `coerce_end_outcome`. | [test_observer_ambient.py](agents-remember/mcp/tests/test_observer_ambient.py) |

## Series-Contract Notes

Ambient observer tests use leaf enclosure paths when lifecycle promotion records an enclosure, matching the durable anchor consumed by dashboard projection.

## Update History

- 2026-08-01T09:18+02:00 — 260731-EFA-L4 curator: the suite gained a module-level
  `_string_constants` helper (L140-L154) and `EndSignalVocabularyTests` (L157-L186, two tests), and
  a `TERMINAL_STATES` import, after `observer/ambient.py::end` gave up its hand-written
  live/terminal split. The card had no trace of either, so the Purpose, Logic and Conventions
  sections now name them and say what makes them structural rather than behavioural — they read
  `AmbientLifecycle.end.__code__` (`co_consts` for the first, `co_names` for the second), so a
  comment or docstring cannot satisfy them, and the second is what stops a bare `cast` from passing
  the first. Verified the production side directly: `end` (L237-L268 of `ambient.py`) guards on
  `TERMINAL_STATES` and calls `coerce_end_outcome`, defined at `lifecycle_state.py` L139 and L149.
  Re-anchored the task-34 heartbeat citation from L265-L322 to **L315-L372** — the 50 inserted
  lines pushed it down exactly that far; `test_inactive_seconds_tracks_real_activity_not_heartbeats`
  now opens at L315 and `AskTests` at L374 — and added a self-citation row for the new class.
  Counted the file: 39 tests across 11 classes. No existing test was renamed and no assertion in
  them changed.

- 2026-07-31T16:50+02:00 — 260731-EFA-L2 curator, code-quality hardening sweep. `AmbientLifecycle`
  now takes its cadence as one
  `timing=AmbientTiming(heartbeat_seconds=..., inactivity_cutoff_seconds=...)` parameter object,
  so `_AmbientCase.setUp` and all three
  `HeartbeatTests` constructions changed shape while `clock=` stayed a separate argument.
  Rewrote the Conventions paragraph to name `AmbientTiming` instead of describing
  `inactivity_cutoff_seconds` as a direct constructor keyword, and corrected the task-34
  activity-decay reference range from L265-L316 to L265-L322 (the two rewrapped constructor calls
  pushed the end of `test_heartbeat_ticker_goes_quiet_when_idle_and_resumes_on_activity` down four
  lines; `AskTests` now opens at L324). No test was added, removed, or renamed and no assertion
  changed.

- 2026-07-10T01:14+02:00 — 260707-HFX2-L13 F7: repointed heartbeat ticker assertions to the
  coalesced sidecar while preserving active/idle/resume semantics. Verification metadata remains
  pinned until closeout stamps the eventual L13 code commit.

- 2026-06-28T13:54+02:00 — Task 34: added two `HeartbeatTests` for the activity-decaying heartbeat —
  `test_inactive_seconds_tracks_real_activity_not_heartbeats` (deterministic clock: real events reset the
  inactivity clock, heartbeats do not) and
  `test_heartbeat_ticker_goes_quiet_when_idle_and_resumes_on_activity` (the ticker stops past the cutoff
  and resumes on activity). Verification metadata pinned until closeout stamps the task-34 code commit.
- 2026-06-27T22:00+02:00 — Task 28 (NOTIFY-AND-CONTINUE turn end): `StateMachineTests` gained `test_await_developer_only_from_running` (`running`→`awaiting-developer`, emits `lifecycle.awaiting-developer` with `summary`; a second await raises) and `test_resume_from_await_only_from_awaiting` (`resume()` stays blocked-only and raises on an await; `resume_from_await()`→`running` emits `lifecycle.resumed`; calling it from `running` raises). Verification metadata pinned until closeout stamps the code commit.
- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: ambient observer tests now use leaf `series-contract.md` enclosure paths for promoted lifecycle records. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-13T18:45+02:00: Slice 2c — updated `SwitchTests` for the save gate and
  added `PromoteTests`, `AttachTests`, and `SaveGateUnitTests` (promotion, the
  attach §1.3 table, scope/decision validation). Verification metadata is pinned
  until closeout stamps the 2c code commit.
- 2026-06-13T16:41+02:00: Created for slice 2b — tests for the ambient lifecycle
  state machine, emission, TTL sweep, and heartbeat. Verification metadata is
  pinned until closeout stamps the 2b code commit.
