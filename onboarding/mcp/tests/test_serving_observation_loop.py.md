# mcp/tests/test_serving_observation_loop.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_serving_observation_loop.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T15:02+02:00 |
| lastVerifiedCommitHash | `99534dc5880e979b98930ead9809bbdcad936033` |
| lastVerifiedCommitDate | 2026-09-15T15:04:53+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

Reviewed at 2026-09-15T15:02+02:00 against the leaf base `d868486c`; the module itself
remains an uncommitted candidate at that base, so no commit verifies it yet and normal closeout owns
the final verification-metadata stamping.

## Purpose

This hermetic unit-regression module pins two distinct guarantees about the same serving background
owner. Its first class proves that the serving lifespan — not an HTTP route and not the agent
notifier — owns the steady-state terminal-catalog observation clock. Its second class proves that one
unexpected failure inside a single observation pass is contained: the recurring observer survives and
retries, unrelated serving loops keep running, and no durable truth is lost or invented. Both enter
the real `_serving_lifespan` finalizer under a virtual event-loop clock shared with the sweeper's own
datetime clock, so cadence, attempt non-overlap, the sweeper's retained rate limits, and the failure
boundary are observed deterministically with no HTTP request, no browser, and no real second.

The module also owns the **shared fixture** for the serving-startup seam. `_ServingFixture` is
imported by [test_serving_startup_prime.py](test_serving_startup_prime.py.md), which owns the one
pre-serve observation prime (`LOCR-R18@v1`), so a change to the fixture's timeline or to its `startup`
record reaches that module too. This card stays the fixture's owner of record; the prime's own
ordering contract lives on the sibling card.

## Code Commentary

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
(every durable file under the case root as relative path → sha256), `_background_tasks`,
`_serving_probe_route`, `_seed_emitted_signal_marker` and `_seed_workspace_cursor`. Its five cases
drive the real lifespan task collection and the real sweeper over a real catalog: five sibling loops
stay alive across a failed pass while the real notifier loop keeps reaching its own cadence with its
sweep uncalled, an in-process ASGI request through the same app object still answers 200, and teardown
then cancels every task and calls `host.shutdown()` exactly once; the durable tree is byte-identical
across the failed pass with a control proving the preceding *successful* pass did change it; the retry
is triggered by the cadence alone, on the same task object, with the tree still byte-identical so no
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
surface intact, publish nothing durable, and retry from the current persisted catalog on the next
cadence without any external trigger. The boundary is `except Exception`, which is load-bearable only
because `asyncio.CancelledError` derives from `BaseException`: the module asserts that inheritance
directly, and widening the boundary to `BaseException` fails the cancellation case alone. A durable
tree that is byte-identical across the failure path is only meaningful because the same case proves a
*surviving* pass does change it, so the identity is a result about the failure and not about a tree
nothing writes.

The module claims nothing about the sweeper's own internals beyond its retained ten-second full-sweep
limit, and nothing about the notifier's pre-existing inline refresh — that remains a second recurring
caller whose future is a separate decision, so no case asserts its presence or absence. It also claims
nothing about the shape, content, retention or log format of observer-failure *publication*: a
structured observer-failure surface is a different requirement's contract, and no case here asserts on
log text. It claims nothing about the pre-serve prime's own ordering either — that is
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

## Docs References

No Domain Documentation entries are configured in the resolved memory root. The module tests
repository-owned serving behavior, so no external domain claim is needed.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

The cases are grounded in the production observation loop and in the sweeper's retained clocks; these
references describe the behavior under test and do not claim a certification result.

| Finding | Anchor | Source |
| --- | --- | --- |
| The serving lifetime owns one completion-relative, non-overlapping observation attempt that sleeps after each call returns, including a failed one. | `_terminal_observation_loop` | mcp/src/agents_remember/serving/_app_lifespan.py:76-93 |
| That attempt cadence is the sweeper's own starting-row interval constant, read at its declaration. | "DEFAULT_STARTING_SWEEP_INTERVAL_SECONDS = 1.0" | mcp/src/agents_remember/serving/terminal_liveness.py:57-57 |
| The lifespan creates the observer unconditionally and cancels/awaits it with the other background loops, and it takes the one pre-serve observation prime before the projection is built. | `_serving_lifespan` | mcp/src/agents_remember/serving/_app_lifespan.py:255-310 |
| The sweeper keeps its own starting-row window and ten-second full-sweep limit behind `refresh`. | `refresh`; `_refresh_starting_rows`; `_starting_rate_limited`; `_rate_limited` | mcp/src/agents_remember/serving/terminal_liveness.py:174-221; mcp/src/agents_remember/serving/terminal_liveness.py:223-268; mcp/src/agents_remember/serving/terminal_liveness.py:270-282 |
| The module drives the real lifespan finalizer, the real sweeper, and its cadence cases with a virtual clock and no HTTP surface; every absolute call index counts the pre-serve prime as call 1. | `ServingObservationLoopTests` | mcp/tests/test_serving_observation_loop.py:439-657 |
| One failed pass is isolated: the owner stays scheduled, five sibling loops and the HTTP surface survive, nothing durable is published, the retry resumes from the current catalog, and cancellation still ends the task. | `ServingObservationFailureIsolationTests` | mcp/tests/test_serving_observation_loop.py:660-874 |
| The failure boundary is `except Exception` and therefore cannot absorb cancellation, because `CancelledError` is a `BaseException`. | `_terminal_observation_loop` | mcp/src/agents_remember/serving/_app_lifespan.py:88-93 |
| The shared fixture and its ordered `startup` witness, imported by the startup-prime module as well as used here. | `_ServingFixture`; `_record_startup` | mcp/tests/test_serving_observation_loop.py:246-354 |
| The probe's parkable inner callable, used to place a slow pass on a chosen invocation rather than always on the first. | `_Gate` | mcp/tests/test_serving_observation_loop.py:223-243 |
| The sibling module that owns the pre-serve prime's own ordering contract and imports this fixture. | `ServingStartupPrimeTests` | mcp/tests/test_serving_startup_prime.py:93-352 |
| The candidate classifies this module once, in the explicit unit-regression lane. | "mcp/tests/test_serving_observation_loop.py" | mcp/tests/test-evidence-lanes.toml:97-97 |

## Cross-Repo References

No meaningful cross-repository implementation boundary is established by this repository-owned
unit-regression module.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History

- 2026-09-15T15:02+02:00 — 260831-LOCR-L18 curator (uncommitted test change set on `ar/260831-locr-l18`,
  base `d868486c`, `+117/−44`, 874 lines): the module's body was corrected rather than annotated,
  because `LOCR-R18@v1`'s pre-serve prime changed the meaning of every absolute call index it asserts
  and gave the shared fixture a second consumer. Recorded the current contract: the fixture now also
  carries the ordered `startup` witness (`_record_startup`, one `(step, sweeps_completed)` entry per
  pre-serve step) and `_Gate`, a parkable probe `inner` so a case can make a chosen invocation slow;
  **call 1 is the pre-serve prime and call 2 is the recurring owner's own first pass**, which is the
  numbering contract both this module and its new sibling depend on. Nine landed cases were
  re-anchored by `+1` for that shift (five of `ServingObservationLoopTests`, four of
  `ServingObservationFailureIsolationTests`) with the injected failure moved back onto the owner's own
  pass; no assertion was relaxed, dropped, skipped or made conditional and the shared helpers stayed
  byte-identical, so this is a mechanical index shift and **not** a re-adjudication of `LOCR-R11@v1`,
  which remains accepted and untouched. One case was additionally repaired for **vacuity**:
  `test_cancellation_still_passes_through_the_failure_boundary` had been parking invocation 1, which
  the prime now occupies, so it cancelled an owner task that never started and passed even under a
  mutation that swallows cancellation; it now gates the owner's own in-flight pass. That is a
  test-integrity fact about this fixture, not a production defect. Class anchors were re-derived
  against the 874-line candidate (`ServingObservationLoopTests` `399-591` → `439-657`,
  `ServingObservationFailureIsolationTests` `594-801` → `660-874`) and the `_serving_lifespan`
  citation moved with the production file (`232-284` → `255-310`). Two fixture instrument limits are
  recorded as boundaries, not resolved claims, both measured by this leaf's independent review: the
  `startup` witness records no entry for the two patched migration/compaction steps, so it does not
  constrain prime-versus-migration/compaction (`L18-RV-3`), and the prime's own cancellation property
  has no falsifying case in either module (`L18-RV-2`). Verification metadata remains closeout-owned;
  no stamp advanced.

- 2026-09-15T14:10+02:00 — 260831-LOCR-L11 curator (uncommitted test-only change set on
  `ar/260831-locr-l11`, base `163ba8a9`): the module gained `ServingObservationFailureIsolationTests`
  (five cases) plus additive harness members (`_RefreshProbe.fail_on`/`.outcomes`, `_LiveHost.probed`,
  `_durable_tree`, `_background_tasks`, `_serving_probe_route`, `_seed_emitted_signal_marker`,
  `_seed_workspace_cursor`), so this card's three stale assertions were corrected in the body rather
  than overridden: the case census is **12** in two classes (not seven in one), the class anchors are
  `399-591` and `594-801` (not `318-510`), and the module **does** now pin pass-failure retry and error
  semantics — the previous "likewise not claimed" sentence was inverted by this change set. Recorded
  the new current contract (one failed pass leaves the owner scheduled, five sibling loops and the
  serving surface intact, publishes nothing durable under a control proving a successful pass does
  change the tree, and retries from the current persisted catalog on the cadence alone) together with
  the boundary-safety invariant that makes the isolation compatible with shutdown:
  `except Exception` cannot swallow `CancelledError`, so widening it to `BaseException` fails the
  cancellation case alone. Also recorded the negative boundary that the module still does not claim
  structured observer-failure *publication* — that belongs to a separate requirement — so a future
  reader does not read this card as evidence for an observer-health surface. Production is byte-unchanged
  by this change set (`_app_lifespan.py` sha256 `7c36ea83…`, the identity the L01 reviewer recorded);
  this leaf's deliverable is the proof envelope, not a production edit. Verification metadata remains
  closeout-owned; no stamp advanced.

- 2026-09-15T13:19+02:00 — 260831-LOCR-L01 curator: created this file card for the leaf's new
  steady-state observation suite. Recorded the current contract it protects (a serving-lifespan-owned,
  completion-relative, non-overlapping observation attempt through the drained helper, independent of
  HTTP, dashboard, and notifier enablement), the virtual-clock harness shape, the falsifiable failure
  classes, and the boundaries the module deliberately does not claim (the notifier's inline refresh and
  pass-failure error semantics). Verification remains closeout-owned because the source is an
  uncommitted candidate; no stamp beyond the leaf base was advanced.
