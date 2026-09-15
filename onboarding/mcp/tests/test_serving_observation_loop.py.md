# mcp/tests/test_serving_observation_loop.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_serving_observation_loop.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T20:42+02:00 |
| lastVerifiedCommitHash | `8ee51cc2cea0be7326937a3b1bbfdad6cafdbd33` |
| lastVerifiedCommitDate | 2026-09-15T21:57:55+02:00|
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
| The serving lifetime owns one completion-relative, non-overlapping observation attempt that sleeps after each call returns, including a failed one. | `_terminal_observation_loop` | mcp/src/agents_remember/serving/_app_lifespan.py:109-126 |
| That attempt cadence is the sweeper's own starting-row interval constant, read at its declaration. | "DEFAULT_STARTING_SWEEP_INTERVAL_SECONDS = 1.0" | mcp/src/agents_remember/serving/terminal_liveness.py:57-57 |
| The lifespan creates the observer unconditionally and cancels/awaits it with the other background loops, and it takes the one pre-serve observation prime before the projection is built. | `_serving_lifespan` | mcp/src/agents_remember/serving/_app_lifespan.py:288-352 |
| The sweeper keeps its own starting-row window and ten-second full-sweep limit behind `refresh`. | `refresh`; `_refresh_starting_rows`; `_starting_rate_limited`; `_rate_limited` | mcp/src/agents_remember/serving/terminal_liveness.py:174-221; mcp/src/agents_remember/serving/terminal_liveness.py:223-268; mcp/src/agents_remember/serving/terminal_liveness.py:270-282 |
| The module drives the real lifespan finalizer, the real sweeper, and its cadence cases with a virtual clock and no HTTP surface; every absolute call index counts the pre-serve prime as call 1. | `ServingObservationLoopTests` | mcp/tests/test_serving_observation_loop.py:469-688 |
| One failed pass is isolated: the owner stays scheduled, five sibling loops and the HTTP surface survive, nothing durable of its own is published, the retry resumes from the current catalog, and cancellation still ends the task. | `ServingObservationFailureIsolationTests` | mcp/tests/test_serving_observation_loop.py:690-924 |
| The failure boundary is `except Exception` and therefore cannot absorb cancellation, because `CancelledError` is a `BaseException`. | `_terminal_observation_loop` | mcp/src/agents_remember/serving/_app_lifespan.py:109-126 |
| The like-scoped exclusion that keeps the R11 identity exact while accounting for the one row R17 must rewrite on every completed observer call. | `_durable_tree_without_observer_health` | mcp/tests/test_serving_observation_loop.py:429-441 |
| The health row's own path and the category a failed steady pass must publish, asserted by the failure case. | `terminal_observer_health_path`; `TerminalObserverHealthStore` | mcp/src/agents_remember/serving/terminal_observer_health.py:110-113; mcp/src/agents_remember/serving/terminal_observer_health.py:239-279 |
| The shared fixture and its ordered `startup` witness, imported by the startup-prime module as well as used here. | `_ServingFixture`; `_record_startup` | mcp/tests/test_serving_observation_loop.py:259-371 |
| The probe's parkable inner callable, used to place a slow pass on a chosen invocation rather than always on the first. | `_Gate` | mcp/tests/test_serving_observation_loop.py:236-257 |
| The sibling module that owns the pre-serve prime's own ordering contract and imports this fixture. | `ServingStartupPrimeTests` | mcp/tests/test_serving_startup_prime.py:93-352 |
| The candidate classifies this module once, in the explicit unit-regression lane. | "mcp/tests/test_serving_observation_loop.py" | mcp/tests/test-evidence-lanes.toml:98-98 |

## Cross-Repo References

No meaningful cross-repository implementation boundary is established by this repository-owned
unit-regression module.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History

- 2026-09-15T20:42+02:00 — 260831-LOCR-L17 curator (uncommitted change set on `ar/260831-locr-l17`,
  base `99534dc5`, `mcp/tests/test_serving_observation_loop.py` +86, 924 lines, final candidate
  `git diff | sha256sum` = `b75a785d…`): this landed **L11** module was modified by this leaf, so the
  card records what changed about its meaning rather than a routine refresh. `LOCR-R17@v1` makes every
  completed observer call — successful or failed — atomically rewrite exactly
  `observer_root/workspace/terminal-observer-health.json`, so R11's three "nothing durable moved"
  identities can no longer hold verbatim. They now run over
  `_durable_tree_without_observer_health` (the full map minus exactly that one path), which keeps the
  claim exact for every OTHER durable artifact instead of weakening it to "almost nothing changed",
  and the failure case additionally asserts positively that the row moved and carries
  `steady-state-refresh-failed`. **The module's own wording changed with it**: it now says a failed
  pass "publishes nothing durable **of its own**", and the card's invariant and negative-boundary
  sections were corrected to match — the previous "publishes nothing durable" and "claims nothing
  about observer-failure publication" sentences would now overstate the boundary, since the case does
  assert that one row's movement and category (never log text or the health module's own field set,
  which stay `LOCR-R17@v1`'s contract in the sibling card). **A vacuity defect found after the review
  round is recorded as negative knowledge**: the first form of that assertion compared the FULL map
  against the FILTERED one, so the extra key made the inequality hold in every reachable state,
  including the one where the row never moved; it now reads in two like-scoped halves. An assertion
  whose two sides are differently scoped is not a stronger form of the same claim but an empty one,
  and a passing run cannot see the difference. Class anchors re-derived against the 924-line candidate
  (`ServingObservationLoopTests` `439-657` → `469-688`, `ServingObservationFailureIsolationTests`
  `660-874` → `690-924`, `_ServingFixture` `246-354` → `259-371`, `_Gate` `223-243` → `236-257`), the
  `_serving_lifespan` citation moved with the production file (`255-310` → `288-352`), and rows were
  added for the two helpers this leaf introduced. The module's lane row (`test-evidence-lanes.toml:97`)
  is unchanged — the L17 insertion is the new sibling module at `:122`, below it — so L11's
  classification is untouched. Verification metadata remains closeout-owned; no stamp advanced.

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
