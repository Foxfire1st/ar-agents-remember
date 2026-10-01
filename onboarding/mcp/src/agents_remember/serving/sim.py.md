# mcp/src/agents_remember/serving/sim.py

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

## Evidence

### Repo-Internal References

- Fixture loading and temporary-root setup. [1]
- Replay clock and speed parsing. [2]
- Progressive event feeding and remaining-tail state. [3]
- Setup lifetime retains the temporary root. [4]
