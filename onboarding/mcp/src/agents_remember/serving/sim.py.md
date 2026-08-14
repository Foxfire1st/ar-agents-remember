# mcp/src/agents_remember/serving/sim.py

| Field                  | Value                                     |
| ---------------------- | ----------------------------------------- |
| repository             | agents-remember                           |
| path                   | `mcp/src/agents_remember/serving/sim.py`  |
| doc_type               | `file-level-onboarding`                   |
| lastUpdated            | 2026-06-14T11:30+02:00                    |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`|
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `overview.md`                             |

## Governing Overview

[overview.md](overview.md)

## Purpose

`sim.py` builds a deterministic replay setup from recorded observer events:
it loads and sorts a fixture, copies its structural surfaces into a temporary
coordination root, and supplies a replay clock plus feeder for the existing
serving path.

## Code Commentary

`build_sim(config, fixture_dir, *, speed)` loads the sorted fixture events,
creates a fresh temporary root, removes copied observer-log directories, and
returns a `SimSetup` whose replaced config points at that root. An empty
fixture raises `SimError`.

`ReplayClock` maps wall-clock elapsed time to fixture time and freezes at the
start when speed is non-positive. `ReplayFeeder.feed` appends each due event
through `EventStore.append` and reports the remaining tail.

`parse_sim_speed` accepts `paused` or a non-negative numeric multiplier.
`SimSetup` retains the temporary directory along with config, clock, and
feeder so the root remains alive for the setup's lifetime.

## Invariants And Boundaries

- **Fixture never mutated** — the fixture is read and its structural surfaces
  are copied into a throwaway temporary root; observer logs are feeder-owned.
- **Clock and feeder behavior is deterministic for the same inputs.**
- **The module does not create a second event-transport implementation; it
  prepares replay inputs for the existing serving path.**

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture loading and temporary-root setup. | `build_sim`; `load_fixture`; `_materialize_surfaces` | mcp/src/agents_remember/serving/sim.py:64-69; mcp/src/agents_remember/serving/sim.py:123-134; mcp/src/agents_remember/serving/sim.py:137-148 |
| Replay clock and speed parsing. | `ReplayClock`; `parse_sim_speed` | mcp/src/agents_remember/serving/sim.py:51-61; mcp/src/agents_remember/serving/sim.py:72-84 |
| Progressive event feeding and remaining-tail state. | `ReplayFeeder` | mcp/src/agents_remember/serving/sim.py:87-106 |
| Setup lifetime retains the temporary root. | `SimSetup` | mcp/src/agents_remember/serving/sim.py:109-120 |

## Update History
- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-04T08:03:35+02:00 — 260731-EFA-L6 S18-B07 curator: repaired the bounded citation findings from the recovered Avicenna and Kuhn ledgers, splitting or narrowing claims to the frozen source and normalizing scoped citation ranges.

- 2026-06-14T23:30+02:00 — Slice 05 (5c): `build_sim` now calls `_materialize_surfaces` to copy the fixture's structural surfaces (contracts / task docs / provider state / ledgers / drift) into the sim root — not just replay event logs — so the rich sim can exercise the whole projection. Verification metadata pinned until closeout stamps the 5c code commit.
- 2026-06-14T11:30+02:00 — Created for slice 04 commit 4b: sim mode — `build_sim` +
  `ReplayClock` + progressive `ReplayFeeder` + `parse_sim_speed`, driving the live path via the
  projector's `now` / `before_tick` seams over a throwaway temp root. Verification metadata
  pinned until closeout stamps the 4b code commit.
