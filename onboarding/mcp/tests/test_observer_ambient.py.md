# test_observer_ambient.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_observer_ambient.py`             |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-10T01:14+02:00                           |
| lastVerifiedCommitHash | `5b49fa85a51d527a5a216a88c361c08246c759d0`       |
| lastVerifiedCommitDate | 2026-07-10T05:00:02+02:00|
| governingOverview      | `../overview.md`                              |

## Governing Overview

[mcp overview](../overview.md) — there is no route-local `mcp/tests/overview.md`.

## Purpose

`test_observer_ambient.py` covers the ambient lifecycle (slices 2b-2c): the
signal state machine, guarded start, switch transitions, the choke-point
emission, the TTL project-and-prune sweep, the heartbeat ticker (2b), and the
promotion, attach/resume, and save gate (2c).

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
heartbeat for determinism and calls `shutdown()` in `tearDown` to stop the
ticker; the heartbeat tests deliberately use a short interval then stop before
reading. The task-34 decay tests inject a list-backed mutable clock and an explicit
`inactivity_cutoff_seconds` so they can step time deterministically across the cutoff.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The ambient lifecycle under test. | [ambient.py](agents-remember/mcp/src/agents_remember/observer/ambient.py) |
| The state vocabulary, errors, and `coerce_phase` under test. | [lifecycle_state.py](agents-remember/mcp/src/agents_remember/observer/lifecycle_state.py) |
| The store events are written to and read back from. | [store.py](agents-remember/mcp/src/agents_remember/observer/store.py) |
| Task 34 heartbeat activity-decay coverage (L265-L316): inactivity tracks real activity not heartbeats; the ticker goes quiet past the cutoff and resumes on activity. | [test_observer_ambient.py](agents-remember/mcp/tests/test_observer_ambient.py) |

## Series-Contract Notes

Ambient observer tests use leaf enclosure paths when lifecycle promotion records an enclosure, matching the durable anchor consumed by dashboard projection.

## Update History

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
