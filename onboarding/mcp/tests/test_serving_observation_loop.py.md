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

### Logic

`_VirtualClock` replaces `asyncio.sleep` while advancing the same timeline the sweeper reads through
its clock callable: `elapse` moves time without completing a parked sleep (a pass that outran its
tick), `release` completes the oldest parked sleep by its own delay. `_RefreshProbe` records an
ordered call/return/sleep timeline for the `refresh` the observation owner invokes, and
`_ServingFixture` composes the real `TerminalCatalog`, `TerminalCatalogLivenessSweeper`, a live fake
tmux host, and a `SimpleNamespace` serving runtime in which every sibling background loop is parked on
an event instead of being individually faked. `_ServingFixture` records every task the lifespan
creates through the module's own `create_task` patch point, which is what lets a case assert on the
real `asyncio.Task` objects rather than on a mock's call log; `_background_tasks` filters out the
off-loop `to_thread` workers those loops spawn, and `_observer_tasks` selects the owner by its
coroutine's `__qualname__`. The fixture also records the ordered `startup` list — one
`(step, sweeps_completed)` entry per pre-serve step, appended by `_record_startup` — where the sweep
count read off the probe's own callable is the ordering witness a case uses to prove how many
observation passes had completed at each startup step; the sibling startup-prime module reads the same
record. `_Gate` is an `inner` callable for the probe that parks one chosen `refresh` invocation in its
worker thread, so a case names the exact attempt it wants slow without teaching the probe a second
blocking mode: invocation 1 is always the pre-serve prime, so a case that needs the recurring owner's
own first pass to be the slow one gates invocation 2.

`ServingObservationLoopTests` asserts the ordered timeline `call started → call ended →
sleep(DEFAULT_STARTING_SWEEP_INTERVAL_SECONDS)` per attempt; that a pass outrunning three nominal ticks
still yields exactly one follow-up attempt; that 25 one-second attempts against the real sweeper
produce only three full sweeps because the ten-second clock stayed inside the sweeper; that
observation continues at 1.0 s while the real notifier loop runs with `agent_notifier.enabled = False`
and `run_agent_notifier_sweep` is never called; that the refresh runs on a worker thread through
`_to_thread_drained_on_cancel` with no terminal-session route registered; that teardown cancels exactly
one observer task, leaves no parked sleep, and performs no further refresh before `host.shutdown()`;
and that a failed pass neither marks success nor changes cadence. Because the lifespan now takes the
pre-serve prime first, every absolute call index in these timelines counts the prime as call 1 and the
recurring owner's own first pass as call 2; the slow-pass case gates invocation 2 for exactly that
reason, and a case that parked invocation 1 would be parking the prime rather than the owner's attempt.

`ServingObservationFailureIsolationTests` extends the same harness additively —
`_RefreshProbe.fail_on` fails exactly one later attempt while `.outcomes` records each attempt's own
verdict, and `_LiveHost.probed` records which tmux name each sweep probed — and adds `_durable_tree`
(every durable file under the case root as relative path → sha256), `_durable_tree_without_observer_health`
(the same map minus exactly this lifetime's observer-health row), `_background_tasks`,
`_serving_probe_route`, `_seed_emitted_signal_marker` and `_seed_workspace_cursor`. Its five cases
drive the real lifespan task collection and the real sweeper over a real catalog: five sibling loops
stay alive across a failed pass while the real notifier loop keeps reaching its own cadence with its
sweep uncalled, an in-process ASGI request through the same app object still answers 200, and teardown
then cancels every task and calls `host.shutdown()` exactly once; every durable artifact **outside the
observer-health row** is byte-identical across the failed pass, with two like-scoped halves proving it
— the filtered map against the filtered map, and the health row's own key before against after — plus
a control proving the preceding *successful* pass did change the full tree; the retry is triggered by
the cadence alone, on the same task object, with the non-health tree still byte-identical so no
catalog edit and no HTTP request was needed; rows, an emitted-signal marker and the workspace cursor
committed ahead of an independent later failure survive it, and the retry then probes the row committed
ahead of the failure (`host.probed == ["ar-seat-1", "ar-seat-1", "ar-seat-2"]`); and a cancellation
still ends the task, drains the in-flight pass, and never resumes the loop.

Four of those five cases plus five of `ServingObservationLoopTests`' seven were **re-anchored** by
`LOCR-R18@v1`, which inserted one observation prime at the head of every lifespan timeline. Each
re-anchoring is a pure index shift — `+1` on the `probe.calls` predicates and the related
`probe.outcomes` expectations, plus moving the injected failure back onto the pass the case is about
(`failures=1` → `fail_on=2`, `fail_on=2` → `3`) so the failing pass is once again the recurring
owner's own and not the prime. No assertion was relaxed, removed, skipped, weakened or made
conditional, no case was dropped or renamed, and the shared helpers stayed byte-identical, so the
properties each case proved are the same properties at shifted indices. A reader who sees these cases
modified in an `R18` diff is looking at that mechanical shift, not at a re-adjudication of
`LOCR-R11@v1`, which remains accepted and untouched.

### Conventions

`unittest.IsolatedAsyncioTestCase` with module-local private harness classes; temporary catalogs and
an in-process runtime rather than a parallel fake of the production seams. The module issues no HTTP
request except the one in-process ASGI probe that asserts the serving surface stays up, starts no
process, and publishes nothing, so it is classified in the repository's `unit-regression` evidence
lane (the `test_terminal_liveness_deferred_work.py` / `test_active_projector_singleflight.py`
neighbours, not the `TestClient`-based `test_serving.py` integration neighbours). Focused host results
are development evidence and grant no certification authority.

### Invariants And Boundaries

The observation sleep must follow each attempt's return, including a failed one, and the attempt
cadence must be read from `DEFAULT_STARTING_SWEEP_INTERVAL_SECONDS`; a fixed-tick (sleep-first) shape,
a literal cadence, a notifier-enabled gate, an overlapping fire-and-forget attempt, or an observer the
lifespan does not cancel each fail a named case.

A pass that raises must leave the owner scheduled, leave every sibling background loop and the HTTP
surface intact, publish nothing durable **of its own**, and retry from the current persisted catalog
on the next cadence without any external trigger. The boundary is `except Exception`, which is
load-bearable only because `asyncio.CancelledError` derives from `BaseException`: the module asserts
that inheritance directly, and widening the boundary to `BaseException` fails the cancellation case
alone. The durable-tree identity across the failure path is only meaningful because of two
compensating halves: the same case proves a *surviving* pass does change the full tree, so the
identity is a result about the failure and not about a tree nothing writes, and the identity itself
is asserted between LIKE-SCOPED maps — the filtered map against the filtered map for "nothing outside
the health row moved", and the health row's own key before against after for "the diagnostic row did
move". `LOCR-R17@v1` is why the exclusion exists and why the scope matters: every completed observer
call — successful or failed — atomically rewrites exactly
`observer_root/workspace/terminal-observer-health.json`, so a failed pass legitimately changes that
ONE path and nothing else. Weakening the claim to "almost nothing changed" was rejected; the
exclusion keeps it exact for every other artifact.

**Vacuous-assertion lesson (recorded because it cost a review round and is invisible to a passing
run).** `LOCR-R17@v1`'s first repair to
`ServingObservationFailureIsolationTests::test_a_failed_pass_publishes_no_durable_fact_at_all`
compared the **full** tree map against the **filtered** one. The extra key made the inequality hold
in every reachable state — including the state where the health row never moved at all — so the
assertion could not fail and proved nothing. It now reads in two like-scoped halves as described
above, and the non-vacuity is what makes it evidence: an assertion whose two sides are differently
scoped is not a stronger form of the same claim, it is a different and empty one.

The module claims nothing about the sweeper's own internals beyond its retained ten-second full-sweep
limit, and nothing about the notifier's pre-existing inline refresh — that remains a second recurring
caller whose future is a separate decision, so no case asserts its presence or absence. It also claims
nothing about the shape, content, retention or log format of observer-failure *publication*: those are
`LOCR-R17@v1`'s contract and live in
[test_terminal_observer_health.py](test_terminal_observer_health.py.md). What this module does assert
about that publication is deliberately narrow and is not a second contract for it: the health row
moved, and it carries the `steady-state-refresh-failed` category. No case here asserts log text, a
payload field set, or the health module's own lifecycle. It claims nothing about the pre-serve prime's
own ordering either — that is
[test_serving_startup_prime.py](test_serving_startup_prime.py.md)'s contract — but it owns the fixture
both modules read, so the timeline's call numbering is a shared contract: **call 1 is the pre-serve
prime and call 2 is the recurring owner's own first pass.** A case that parks or fails invocation 1
addresses the prime, not the owner, and would silently stop testing the owner's attempt; that failure
mode is not hypothetical, since
`ServingObservationFailureIsolationTests.test_cancellation_still_passes_through_the_failure_boundary`
had become vacuous for exactly that reason — its `block_first` probe parked invocation 1, so it
cancelled an owner task that had never started and passed even under a mutation that makes the
observer boundary swallow cancellation, while burning the probe's park timeout — until
`LOCR-R18@v1` re-anchored it onto the owner's own in-flight pass. That is a fact about the shared
fixture's instrumentation contract, not about the production boundary it exercises.

Two instrument limits on the shared fixture are recorded rather than implied, both measured by the
`LOCR-R18@v1` independent review: the `startup` witness records no `(step, ...)` entry for
`migrate_control_plane_identity_logs` or `compact_workspace_river`, because `running()` patches both
with plain un-recording mocks — so it constrains prime-versus-projection, prime-versus-tasks,
prime-versus-yield and multiplicity but **not** prime-versus-migration/compaction; and the failure
boundary's inheritance claim is asserted here directly (`CancelledError` is a `BaseException`) while
the prime's own cancellation property has no falsifying case in either module.

### Todos

None. The module is complete for its leaves' requirements; a future change to the notifier's inline
refresh belongs to the leaf that decides it.

## Evidence

- The module docstring: the real lifespan under a virtual clock, and the failure isolation. [14]
- The shared virtual timeline. [15]
- The attempt timeline of the refresh calls. [16]
- The runtime with one real loop, and the assertion that the worklist shutdown runs once, off the main thread. [17]
- The cadence cases. [18]
- The failure isolation cases. [19]
- The lifespan under test calls the shutdown callable first. [20]

### Docs References

No Domain Documentation entries are configured in the resolved memory root. The module tests
repository-owned serving behavior, so no external domain claim is needed.

### Repo-Internal References

The cases are grounded in the production observation loop and in the sweeper's retained clocks; these

references describe the behavior under test and do not claim a certification result.

- The serving lifetime owns one completion-relative, non-overlapping observation attempt that sleeps after each call returns, including a failed one. [21]
- That attempt cadence is the sweeper's own starting-row interval constant, read at its declaration. [22]
- The lifespan creates the observer unconditionally and cancels/awaits it with the other background loops, and it takes the one pre-serve observation prime before the projection is built. [23]
- The sweeper keeps its own starting-row window and ten-second full-sweep limit behind `refresh`. [24]
- The module drives the real lifespan finalizer, the real sweeper, and its cadence cases with a virtual clock and no HTTP surface; every absolute call index counts the pre-serve prime as call 1. [25]
- One failed pass is isolated: the owner stays scheduled, five sibling loops and the HTTP surface survive, nothing durable of its own is published, the retry resumes from the current catalog, and cancellation still ends the task. [26]
- The failure boundary is `except Exception` and therefore cannot absorb cancellation, because `CancelledError` is a `BaseException`. [27]
- The like-scoped exclusion that keeps the R11 identity exact while accounting for the one row R17 must rewrite on every completed observer call. [28]
- The health row's own path and the category a failed steady pass must publish, asserted by the failure case. [29]
- The shared fixture and its ordered `startup` witness, imported by the startup-prime module as well as used here. [30]
- The probe's parkable inner callable, used to place a slow pass on a chosen invocation rather than always on the first. [31]
- The sibling module that owns the pre-serve prime's own ordering contract and imports this fixture. [32]
- The candidate classifies this module once, in the explicit unit-regression lane. [33]

### Cross-Repo References

No meaningful cross-repository implementation boundary is established by this repository-owned
unit-regression module.
