# mcp/tests/test_serving_observation_loop.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

Tests of the serving lifespan's recurring terminal observation under a virtual clock. The cases enter the
real `_serving_lifespan` without an HTTP request, a browser or a real second, and observe the cadence of
the observation attempts, that attempts never overlap, the sweeper's own full-sweep rate limit, and that a
failed pass is isolated, retried and leaves every other durable artifact unchanged.

## Code Commentary

### The harness

- `_VirtualClock` is one timeline for `asyncio.sleep` and for the sweeper's datetime clock: a sleep parks
  its caller until the case releases it, and releasing advances the virtual time.
- `_RefreshProbe` records the timeline of the `refresh` calls and can delegate to a real sweeper or fail a
  chosen attempt. `_Gate` parks one chosen invocation in its worker thread. `_LiveHost` is a host whose
  catalog rows are alive.
- `_ServingFixture` builds one serving runtime in which only the observation loop is real; the projector,
  metrics, notifier, death-watch and compaction loops are parked coroutines. Its runtime carries a
  `review_trees_shutdown` callable that records the thread it runs on. Every time the fixture's lifespan
  ends, the fixture asserts that this callable was called exactly once more and never on the main thread.
  Every case of the module therefore also checks that the lifespan invokes the provided shutdown callback
  exactly once, on a worker thread; the actual child and Git-process reclamation is proven by the
  real-process cases, and the accepted A1 wiring limitation stands.

### The cases

- `ServingObservationLoopTests`: each attempt sleeps the observation interval after the call returns; a
  slow attempt delays the next pass instead of queueing ticks; the sweeper keeps its own full-sweep rate
  limit; observation continues while the agent notifier is disabled and needs no HTTP request; the
  observer task is registered and cancelled by the lifespan's teardown; a failed pass keeps the loop alive
  on the same cadence.
- `ServingObservationFailureIsolationTests`: a failed pass leaves every sibling loop and the shutdown
  intact, publishes no durable fact other than the observer-health record, needs no request, restart or
  catalog edit for its retry, resumes from the persisted catalog, and lets cancellation pass through.

## Evidence

- The module docstring: the real lifespan under a virtual clock, and the failure isolation. [14]
- The shared virtual timeline. [15]
- The attempt timeline of the refresh calls. [16]
- The runtime with one real loop, and the assertion that the worklist shutdown runs once, off the main thread. [17]
- The cadence cases. [18]
- The failure isolation cases. [19]
- The lifespan under test calls the shutdown callable first. [20]
