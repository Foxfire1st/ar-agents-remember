# mcp/tests/_serving_handoff.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/_serving_handoff.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T21:25+02:00 |
| lastVerifiedCommitHash | `806649b91bdce18f7b915bfbbf6727967f4e7a88` |
| lastVerifiedCommitDate | 2026-09-16T12:23:53+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

Reviewed at 2026-09-15T21:25+02:00 against the leaf base `e9678c56`; this module is an uncommitted
candidate at that base, so it does not exist at the commit above and normal closeout owns the final
verification-metadata stamping. The hash records only the base this card was read against.

## Purpose

The virtual-clock harness that drives the two **real** serving loops for the observer-to-notifier
handoff proof (`LOCR-R04@v1`). It is the instrument half of that proof; the oracle it measures is
documented and asserted at the proof site,
[test_serving_notifier_handoff.py](test_serving_notifier_handoff.py.md).

Nothing here replaces production behavior. One disposable serving world enters the real
`_serving_lifespan`, which creates the real `_terminal_observation_loop` and the real
`_agent_notifier_loop`; the real `TerminalCatalogLivenessSweeper.refresh` runs over a real
`TerminalCatalog`; and the real `run_agent_notifier_sweep` runs over the context the notifier loop
builds for itself. Every piece either **records** what production did or **holds** a pass where a case
needs to observe a scheduling phase — no piece substitutes for a production collaborator.

The module is a subclass-and-compose extension of the shared serving fixture: `_HandoffFixture` extends
`_ServingFixture` from [test_serving_observation_loop.py](test_serving_observation_loop.py.md) and
supplies the collaborators the real notifier loop and the real sweep read, so a case fails if
production stops composing the two cadences and also if a hand-aligned harness stops agreeing with
production.

## Code Commentary

### Logic

The oracle's four scheduling constants are read from production declarations rather than written as
literals: `P` from `DEFAULT_STARTING_SWEEP_INTERVAL_SECONDS` (1.0 s, the observer's
completion-relative poll delay), `F` from `DEFAULT_LIVENESS_HYSTERESIS.sweep_interval_seconds` (10.0 s,
the full-sweep rate limit measured from the previous full sweep's **start**), `N` from
`DEFAULT_AGENT_NOTIFIER_INTERVAL_SECONDS` (10.0 s, the notifier's completion-relative interval), and
`WORST_PHASE_BOUND = F + P + N` — 21.0 s of logical scheduling for the default knobs, before any
measured overrun. `_REAL_SLEEP` captures `asyncio.sleep` before the fixture swaps it for the virtual
clock, so the few places that genuinely need real wall time can still get it.

The recording layer is a set of thin wrappers around real objects. `_SweepWitness` **is** the
`runtime.liveness_sweeper` attribute, so it sees every caller — the startup prime, the observation
owner, and the notifier pass's own inline refresh — without changing what any of them does; attempt
numbers and the entry snapshot are allocated under one lock together with the finished record, because
`measure()` compares that index to choose the consuming sweep and a torn number would let two attempts
share one. `_WitnessCatalog` subclasses the real `TerminalCatalog` and records at `_write_disk` — the
store's single durable write, which inside a batch **is** the commit — so `batch()`, the RLock spanning
it and the atomic replace all stay production code while the commit instant, order and rows become
observable. `_CatalogReads` **is** `AgentNotifierContext.catalog`, so the notifier's real predicate
reads land in it and `list()` returns exactly what the real store returned. `_NotifierPasses` records
the window around the real `run_agent_notifier_sweep`. `_HeartbeatWitness` records the real heartbeat
store's end-of-pass tick, which is the last act of a real sweep and therefore the exact instant at which
a pass "has finished evaluating its snapshot and has not consumed the new truth".

`_Adapter` holds the one terminal fact a case can make readable, plus the three gates that park a pass
where a scenario needs it: inside a full sweep after the evidence row was already read (`overrun`),
inside a one-second starting-row fast-path pass (`fastpath`), and inside the consuming sweep's own
pre-commit work (`commit`). Terminal truth is produced outside the dashboard, so the observer is the
only reader that can turn it into catalog truth — which is why the fact lives on the adapter and
becomes readable only when a case arms it.

`_World` composes those recordings over three seeded rows in the order a full sweep observes them
(evidence, second steady seat, starting row) and wires `_HandoffFixture`, which supplies the recorded
catalog, host and heartbeat store and then overrides the settings loader: the shared fixture patches one
settings object, but the loop must receive a **fresh frozen snapshot per load**, which is what
production's loader returns and what makes a loop that reads its settings once observably different
from one that re-reads them. That override is what lets a case flip notifier enablement in place.

`_Handoff` reads the oracle's terms back out of the recordings — `overrun` (`R_observer`, the in-flight
refresh's remaining duration at eligibility), `poll_delay`, `commit_duration` (`D_commit`),
`wait`, `notifier_overrun` (`R_notifier`), `latency` and `bound` — and `_HandoffCase` is the driver.
Its primitives release exactly one parked sleep each: `observer_poll` for the observation owner and
`notifier_poll` for the notifier loop. Only the loop whose sleep was released moves, so a case chooses
each pass's exact virtual instant instead of racing two cadences, and every measurement is a difference
of virtual timestamps or sequence numbers.

The driver waits for the released loop to **re-park** rather than for the record alone, which is what
proves an attempt settled without racing the loop back to its own cadence; a disabled notifier loop
re-parks without running a pass at all, so re-parking — not a new pass — is what proves that interval
was consumed. `poll_until` is bounded by `_STEP_LIMIT = 2 * ceil(F / P) + 2`, sized from the observer's
own grid so a genuinely late full sweep reaches `measure()` and fails on the bound assertion instead of
aborting the driver with "never reached the requested state" — an attribution failure rather than a
verdict.

`assert_oracle` asserts the bound and its decomposition term by term. Three relations are deliberately
**documented rather than asserted**, each named with the reason it is unfalsifiable: the telescoping
decomposition `latency = (release - T) + poll_delay + D_commit + wait` holds by the terms' own
definitions in every state, reachable or not; the observer phase is at most `F + R_observer` for the
same reason, since `release = previous.entered_at + F + R_observer` makes the phase
`F + R_observer - (T - previous.entered_at)` for every `T` at or after the previous sweep's start, and
only arming before that start reverses it — a state the oracle's premise excludes; and `bound` is by
definition the sum compared to `latency`. The assertions that remain each name the state that breaks
them: the consuming pass is the **first** eligible full sweep after the release (minimality), the commit
cannot precede the consuming sweep's start, the next notifier pass starts one whole interval after the
last pass that could not have seen the fact finished, and `poll_delay` is at most `P`.

### Conventions

Module-local private harness classes with a leading underscore, matching the sibling support modules in
this directory, plus the `MCP_SRC` source-root preamble they share. The harness starts no process,
opens no socket and issues no HTTP request; it is ordinary version-controlled test support in the
`unit-regression` lane, not a governed evidence artifact.

### Invariants And Boundaries

- Every production collaborator is the real object. The wrappers record and park; none reimplements the
  sweeper's rate limits, the notifier's predicate reads, or the store's commit path.
- The notifier's committed-truth read is scoped to the notifier's own `list(include_terminated=True)`.
  `_WitnessCatalog.committed_holds` therefore reads with `include_terminated=True` too: a filtered read
  would answer about a strictly narrower collection than the claim and would report "not durable" for a
  fact whose row had terminated.
- `upsert`'s in-batch hook fires only for the evidence row's own projection **while a batch is open**,
  which is the one instant an in-memory observation exists that no reader may treat as truth yet.
- The harness constrains only what its recordings can see. A scheduling property production expresses
  outside the sweeper, the notifier pass, the catalog write path or the heartbeat tick is not measured
  here.
- No production module imports this file, and the candidate change set touches no file under `mcp/src`.

### Todos

None. The instrument covers the oracle's terms and its three park points; a scenario needing a fourth
would add a gate beside these rather than a second harness.

## Docs References

No Domain Documentation entries are configured in the resolved memory root. Every claim on this card is
about repository-owned serving behaviour, so no external domain source is cited.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

The declarations below establish the current instrument and the production seams it drives; this
inventory is not execution evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| The oracle's four scheduling terms are read from production declarations, not literals: 21.0 s of logical scheduling before any measured overrun. | `P`; `F`; `N`; `WORST_PHASE_BOUND` | mcp/tests/_serving_handoff.py:86-96 |
| The real `asyncio.sleep`, captured before the fixture swaps it for the virtual clock. | `_REAL_SLEEP` | mcp/tests/_serving_handoff.py:83-83 |
| The driver's step budget is sized from the observer's grid so a late sweep fails on the bound rather than aborting the driver with an attribution error. | `_STEP_LIMIT` | mcp/tests/_serving_handoff.py:113-121 |
| One `refresh()` attempt's window and how many rows it probed, which is how a full sweep is told apart from a fast-path pass. | `_SweepCall`; `full_sweep` | mcp/tests/_serving_handoff.py:127-139 |
| The one entry point both loops call; attempt numbers and records are allocated under one lock because `measure()` compares that index. | `_SweepWitness`; `refresh` | mcp/tests/_serving_handoff.py:183-241; mcp/tests/_serving_handoff.py:216-229 |
| The last refresh still running at a moment: the pass that can delay the next sweep. | `in_flight_at` | mcp/tests/_serving_handoff.py:235-241 |
| The real catalog with its single durable write path recorded, so the commit's instant, order and rows are observable while `batch()` and the atomic replace stay production code. | `_WitnessCatalog`; `_write_disk` | mcp/tests/_serving_handoff.py:244-293; mcp/tests/_serving_handoff.py:261-267 |
| Durable truth is read with `include_terminated=True`, matching the notifier's own read scope rather than a narrower filtered one. | `committed_holds` | mcp/tests/_serving_handoff.py:281-293 |
| The one in-batch hook, which holds a sweep inside its own open batch after it projected the fact. | `upsert` | mcp/tests/_serving_handoff.py:269-274 |
| The adapter readers a sweep consumes, the one terminal fact a case can make readable, and the three park points. | `_Adapter`; `make_readable` | mcp/tests/_serving_handoff.py:296-364; mcp/tests/_serving_handoff.py:318-322 |
| The notifier loop's own catalog port, delegated in full and recorded on every `list()` read. | `_CatalogReads`; `list` | mcp/tests/_serving_handoff.py:367-403; mcp/tests/_serving_handoff.py:389-395 |
| One notifier pass recorded around the real `run_agent_notifier_sweep`, so "this pass actually read the fact" is decidable per pass. | `_NotifierPasses`; `observed` | mcp/tests/_serving_handoff.py:406-428; mcp/tests/_serving_handoff.py:177-180 |
| The real heartbeat store's end-of-pass tick, which is where a pass is parked as in-flight-but-not-consumed. | `_HeartbeatWitness`; `tick` | mcp/tests/_serving_handoff.py:431-450; mcp/tests/_serving_handoff.py:444-447 |
| A fresh frozen settings snapshot per load, which is what makes in-place enablement observable. | `_SettingsSource`; `set_enabled` | mcp/tests/_serving_handoff.py:453-471; mcp/tests/_serving_handoff.py:466-468 |
| Three seeded rows in the order a full sweep observes them: evidence, second steady seat, starting row. | `_seed_rows` | mcp/tests/_serving_handoff.py:496-503 |
| One disposable world composing the recordings, the adapter and the real fixture. | `_World` | mcp/tests/_serving_handoff.py:507-540 |
| The shared serving fixture extended with the real notifier loop's collaborators, rather than a second harness. | `_HandoffFixture` | mcp/tests/_serving_handoff.py:543-600 |
| Every oracle term read back out of recorded events, with `bound` composed from the measured terms. | `_Handoff`; `bound` | mcp/tests/_serving_handoff.py:604-666; mcp/tests/_serving_handoff.py:663-666 |
| The driver releasing one parked sleep at a time so a case chooses each pass's exact instant. | `_HandoffCase`; `observer_poll`; `notifier_poll` | mcp/tests/_serving_handoff.py:669-886; mcp/tests/_serving_handoff.py:699-710; mcp/tests/_serving_handoff.py:712-723 |
| Re-parking, not a new record, is what proves an interval was consumed — a disabled loop re-parks without running a pass. | `settle`; `poll_until` | mcp/tests/_serving_handoff.py:694-697; mcp/tests/_serving_handoff.py:725-732 |
| The arming choices that make the observer phase strict rather than maximal. | `arm_the_fact_after`; `arm_the_fact_at` | mcp/tests/_serving_handoff.py:769-779; mcp/tests/_serving_handoff.py:759-767 |
| Every term of the bound asserted against the recorded events, with the three unfalsifiable relations documented instead of asserted. | `assert_oracle` | mcp/tests/_serving_handoff.py:827-886 |
| The production loops and sweeper this harness enters rather than replaces. | `_terminal_observation_loop`; `_serving_lifespan` | mcp/src/agents_remember/serving/_app_lifespan.py:109-126; mcp/src/agents_remember/serving/_app_lifespan.py:288-352 |
| The sweeper's retained starting-row window and ten-second full-sweep limit behind `refresh`. | `refresh` | mcp/src/agents_remember/serving/terminal_liveness.py:174-221 |
| The fixture this harness extends, and the clock its sleep primitive replaces. | `_ServingFixture`; `_VirtualClock` | mcp/tests/test_serving_observation_loop.py:259-370; mcp/tests/test_serving_observation_loop.py:115-159 |
| The proof site that owns the oracle's documentation and its eight cases. | `ServingNotifierHandoffTests` | mcp/tests/test_serving_notifier_handoff.py:52-376 |

## Cross-Repo References

No separate cross-repository authority is established by this repository-owned test-support module.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History

- 2026-09-15T21:25+02:00 — 260831-LOCR-L04 curator (uncommitted change set on `ar/260831-locr-l04`,
  base `e9678c56`, `mcp/tests/_serving_handoff.py` new, 886 lines, sha256 `6ab4455a…`): created this
  card for the leaf's new handoff harness. It is the instrument half of a preservation leaf's proof
  envelope — the leaf changes no production file, so the harness and the oracle are the whole
  deliverable, and the card records what the instrument actually is rather than a one-line stub. Four
  properties are recorded because each is load-bearing and none is visible from a passing run: the
  scheduling constants are read from production declarations so the bound cannot drift from the knobs;
  the wrappers **are** the production collaborators (the sweeper attribute, the notifier's catalog port,
  the heartbeat tick) so no production behaviour is reimplemented; the settings loader hands out a fresh
  frozen snapshot per load, which is what makes a cached-settings loop observably different from a
  re-reading one; and `assert_oracle` documents its three unfalsifiable relations instead of asserting
  them, because an assertion that cannot fail in any reachable state is not evidence. The committed-truth
  read is scoped to the notifier's own `include_terminated=True` collection for the reason recorded in
  the body: a filtered read would answer about a narrower collection than the claim. Verification
  metadata is pinned to the leaf base only; the source is an uncommitted candidate, so normal closeout
  owns the final stamping.
