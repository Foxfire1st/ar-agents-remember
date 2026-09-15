# mcp/tests/test_serving_observation_loop.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_serving_observation_loop.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T13:19+02:00 |
| lastVerifiedCommitHash | `163ba8a9798228b7f912eec05646f31e79f6b26e` |
| lastVerifiedCommitDate | 2026-09-15T13:37:09+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

Reviewed at 2026-09-15T13:19+02:00 against the leaf base `67b21aeb`; the module itself is an
uncommitted candidate at that base, so no commit verifies it yet and normal closeout owns the final
verification-metadata stamping.

## Purpose

This hermetic unit-regression module proves that the serving lifespan — not an HTTP route and not the
agent notifier — owns the steady-state terminal-catalog observation clock. It enters the real
`_serving_lifespan` finalizer under a virtual event-loop clock shared with the sweeper's own datetime
clock, so the attempt cadence, attempt non-overlap, and the sweeper's retained rate limits are
observed deterministically with no HTTP request, no browser, and no real second.

## Code Commentary

### Logic

`_VirtualClock` replaces `asyncio.sleep` while advancing the same timeline the sweeper reads through
its clock callable: `elapse` moves time without completing a parked sleep (a pass that outran its
tick), `release` completes the oldest parked sleep by its own delay. `_RefreshProbe` records an
ordered call/return/sleep timeline for the `refresh` the observation owner invokes, and
`_ServingFixture` composes the real `TerminalCatalog`, `TerminalCatalogLivenessSweeper`, a live fake
tmux host, and a `SimpleNamespace` serving runtime in which every sibling background loop is parked on
an event instead of being individually faked.

The cases assert the ordered timeline `call started → call ended → sleep(DEFAULT_STARTING_SWEEP_INTERVAL_SECONDS)`
per attempt; that a pass outrunning three nominal ticks still yields exactly one follow-up attempt;
that 25 one-second attempts against the real sweeper produce only three full sweeps because the
ten-second clock stayed inside the sweeper; that observation continues at 1.0 s while the real
notifier loop runs with `agent_notifier.enabled = False` and `run_agent_notifier_sweep` is never
called; that the refresh runs on a worker thread through `_to_thread_drained_on_cancel` with no
terminal-session route registered; that teardown cancels exactly one observer task, leaves no parked
sleep, and performs no further refresh before `host.shutdown()`; and that a failed pass neither marks
success nor changes cadence.

### Conventions

`unittest.IsolatedAsyncioTestCase` with module-local private harness classes; temporary catalogs and
an in-process runtime rather than a parallel fake of the production seams. The module issues no HTTP
request, starts no process, and publishes nothing, so it is classified in the repository's
`unit-regression` evidence lane (the `test_terminal_liveness_deferred_work.py` /
`test_active_projector_singleflight.py` neighbours, not the `TestClient`-based `test_serving.py`
integration neighbours). Focused host results are development evidence and grant no certification
authority.

### Invariants And Boundaries

The observation sleep must follow each attempt's return, including a failed one, and the attempt
cadence must be read from `DEFAULT_STARTING_SWEEP_INTERVAL_SECONDS`; a fixed-tick (sleep-first)
shape, a literal cadence, a notifier-enabled gate, an overlapping fire-and-forget attempt, or an
observer the lifespan does not cancel each fail a named case. The module claims nothing about the
sweeper's own internals beyond its retained ten-second full-sweep limit, and nothing about the
notifier's pre-existing inline refresh — that remains a second recurring caller whose future is a
separate decision, so no case asserts its presence or absence. Pass-failure retry and error
*semantics* are likewise not claimed: the failure case asserts only cadence and survival.

### Todos

None. The module is complete for its leaf's requirement; a future change to the notifier's inline
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
| The lifespan creates the observer unconditionally and cancels/awaits it with the other background loops. | `_serving_lifespan` | mcp/src/agents_remember/serving/_app_lifespan.py:232-284 |
| The sweeper keeps its own starting-row window and ten-second full-sweep limit behind `refresh`. | `refresh`; `_refresh_starting_rows`; `_starting_rate_limited`; `_rate_limited` | mcp/src/agents_remember/serving/terminal_liveness.py:174-221; mcp/src/agents_remember/serving/terminal_liveness.py:223-268; mcp/src/agents_remember/serving/terminal_liveness.py:270-282 |
| The module drives the real lifespan finalizer, the real sweeper, and its seven cases with a virtual clock and no HTTP surface. | `ServingObservationLoopTests` | mcp/tests/test_serving_observation_loop.py:318-510 |
| The candidate classifies this module once, in the explicit unit-regression lane. | "mcp/tests/test_serving_observation_loop.py" | mcp/tests/test-evidence-lanes.toml:97-97 |

## Cross-Repo References

No meaningful cross-repository implementation boundary is established by this repository-owned
unit-regression module.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History

- 2026-09-15T13:19+02:00 — 260831-LOCR-L01 curator: created this file card for the leaf's new
  steady-state observation suite. Recorded the current contract it protects (a serving-lifespan-owned,
  completion-relative, non-overlapping observation attempt through the drained helper, independent of
  HTTP, dashboard, and notifier enablement), the virtual-clock harness shape, the falsifiable failure
  classes, and the boundaries the module deliberately does not claim (the notifier's inline refresh and
  pass-failure error semantics). Verification remains closeout-owned because the source is an
  uncommitted candidate; no stamp beyond the leaf base was advanced.
