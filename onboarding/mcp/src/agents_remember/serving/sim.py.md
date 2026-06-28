# mcp/src/agents_remember/serving/sim.py

| Field                  | Value                                     |
| ---------------------- | ----------------------------------------- |
| repository             | agents-remember                           |
| path                   | `mcp/src/agents_remember/serving/sim.py`  |
| doc_type               | `file-level-onboarding`                   |
| lastUpdated            | 2026-06-14T11:30+02:00                    |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`|
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `overview.md`                             |

## Governing Overview

[overview.md](overview.md)

## Purpose

`sim.py` is **sim mode** (slice 4b): it replays a recorded observer fixture through the
byte-identical live serving path so the frontend cannot tell sim from live. It reuses the two
`Projector` seams (note 15 Loop C) — a replay clock drives `now`, and a before-tick feeder
appends the next due fixture events into a throwaway sim coordination root — so as sim-time
advances the sim log grows, the projection evolves, and the same delta + raw-event SSE
machinery fires.

## Code Commentary

- `build_sim(config, fixture_dir, *, speed)` loads the fixture's recorded events
  (`load_fixture` → `read_lifecycle_logs` under `<fixture>/logs/observer`, sorted by ts),
  creates a fresh `tempfile.TemporaryDirectory`, **materializes the fixture's structural surfaces**
  into it (`_materialize_surfaces`: copies the tree except the observer event logs, which the feeder
  replays — so contracts, task docs, provider state, ledgers, and drift snapshots are read like a
  live root), and returns a `SimSetup` whose `config` is
  `dataclasses.replace(config, coordination_root=<temp>)` — so the shipped fixture is never mutated
  and all sim reads/writes land in the temp root. An empty fixture raises `SimError`.
- `ReplayClock(start, *, speed)` maps wall-clock elapsed onto fixture time at `speed`
  (`speed <= 0` ⇒ frozen at `start`, i.e. paused).
- `ReplayFeeder(store, events).feed(moment)` appends every not-yet-fed event whose ts is
  `<= moment` (progressive materialization through `EventStore.append`); `remaining` reports
  the un-fed tail.
- `parse_sim_speed("paused" | <float>)` → a non-negative multiplier (`SimError` otherwise).
- `SimSetup` holds `config`, `clock`, `feeder`, and `temp_dir` (held so the temp root lives for
  the server's lifetime); the CLI passes `clock.now` as `now` and `feeder.feed` as `before_tick`
  to `create_app`.

## Invariants And Boundaries

- **No new transport** — sim is a clock + root swap over the existing projector/SSE path; only
  `now` and `coordination_root` differ from live.
- **Fixture never mutated** — events are read once and fed into a throwaway temp root.
- **Deterministic** — same fixture fed to the same moment ⇒ same log ⇒ same projection ⇒ same
  delta sequence (the reducer + diff are already pure).
- **Reducer unchanged** — the *log* grows over replay time; the reducer keeps its live
  "fold the whole log" behaviour.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The replay clock / before-tick seams consumed here. | [projector.py](agents-remember/mcp/src/agents_remember/serving/projector.py) |
| The `project_and_write(now=…)` re-projection it drives + the fixture loader it reuses. | [observer/projection_store.py](agents-remember/mcp/src/agents_remember/observer/projection_store.py) |
| The event store the feeder appends through. | [observer/store.py](agents-remember/mcp/src/agents_remember/observer/store.py) |
| The fixture-root resolution (`observer_logs_root` / `observer_root`, NS #5). | [observer/paths.py](agents-remember/mcp/src/agents_remember/observer/paths.py) |
| The CLI `--sim` / `--sim-speed` wiring. | [cli/dashboard.py](agents-remember/mcp/src/agents_remember/cli/dashboard.py) |

## Update History

- 2026-06-14T23:30+02:00 — Slice 05 (5c): `build_sim` now calls `_materialize_surfaces` to copy the fixture's structural surfaces (contracts / task docs / provider state / ledgers / drift) into the sim root — not just replay event logs — so the rich sim can exercise the whole projection. Verification metadata pinned until closeout stamps the 5c code commit.
- 2026-06-14T11:30+02:00 — Created for slice 04 commit 4b: sim mode — `build_sim` +
  `ReplayClock` + progressive `ReplayFeeder` + `parse_sim_speed`, driving the live path via the
  projector's `now` / `before_tick` seams over a throwaway temp root. Verification metadata
  pinned until closeout stamps the 4b code commit.
