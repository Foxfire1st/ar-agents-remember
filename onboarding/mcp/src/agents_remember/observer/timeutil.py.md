# mcp/src/agents_remember/observer/timeutil.py

## Governing Overview

[overview.md](overview.md)

## Purpose

`timeutil.py` provides the observer's injectable `Clock` type and shared time boundary. The current
age calculation lives with the observer control-plane stamp implementation, while heartbeat, stale,
and TTL thresholds are owned by their consuming layers rather than by this module.

## Code Commentary

`Clock = Callable[[], datetime]` is the injectable now-source: passing it at the
edges keeps a reduction a pure function of `(events, snapshots, now)` and the
tests deterministic. The `age_seconds` implementation is owned by the observer
control-plane stamp module. The heartbeat/stale/TTL constants are likewise read
from the producer and reducer layers that consume them.

## Invariants And Boundaries

- `Clock` is the shared injectable boundary; age calculation and threshold ownership
  remain with their respective observer control-plane and producer/consumer modules.
- `providers.setup_progress` keeps its *own* `_age_seconds` and
  `STALE_AFTER_SECONDS` (90.0): it predates the observer package and is a
  provider-layer concern, deliberately not consolidated here.
- Pure: no I/O, no package-internal imports beyond the standard library.

## Evidence

### Repo-Internal References

- The write side imports the cadence and TTL, and `_inactive_seconds_locked` ages the last real non-heartbeat event. [1]
- The read side (observer/reducer.py) imports the stale and TTL thresholds from `observer.timeutil` for the inferred layer. [2]
- The provider-layer heartbeat/stale idiom with its own separate copy. [3]
- The design sections describe lifecycle TTL/heartbeat semantics and defer implementation ownership. [4]
