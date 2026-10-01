# mcp/tests/_serving_handoff.py

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

## Evidence

### Docs References

No Domain Documentation entries are configured in the resolved memory root. Every claim on this card is
about repository-owned serving behaviour, so no external domain source is cited.

### Repo-Internal References

The declarations below establish the current instrument and the production seams it drives; this
inventory is not execution evidence.

- The oracle's four scheduling terms are read from production declarations, not literals: 21.0 s of logical scheduling before any measured overrun. [1]
- The real `asyncio.sleep`, captured before the fixture swaps it for the virtual clock. [2]
- The driver's step budget is sized from the observer's grid so a late sweep fails on the bound rather than aborting the driver with an attribution error. [3]
- One `refresh()` attempt's window and how many rows it probed, which is how a full sweep is told apart from a fast-path pass. [4]
- The one entry point both loops call; attempt numbers and records are allocated under one lock because `measure()` compares that index. [5]
- The last refresh still running at a moment: the pass that can delay the next sweep. [6]
- The real catalog with its single durable write path recorded, so the commit's instant, order and rows are observable while `batch()` and the atomic replace stay production code. [7]
- Durable truth is read with `include_terminated=True`, matching the notifier's own read scope rather than a narrower filtered one. [8]
- The one in-batch hook, which holds a sweep inside its own open batch after it projected the fact. [9]
- The adapter readers a sweep consumes, the one terminal fact a case can make readable, and the three park points. [10]
- The notifier loop's own catalog port, delegated in full and recorded on every `list()` read. [11]
- One notifier pass recorded around the real `run_agent_notifier_sweep`, so "this pass actually read the fact" is decidable per pass. [12]
- The real heartbeat store's end-of-pass tick, which is where a pass is parked as in-flight-but-not-consumed. [13]
- A fresh frozen settings snapshot per load, which is what makes in-place enablement observable. [14]
- Three seeded rows in the order a full sweep observes them: evidence, second steady seat, starting row. [15]
- One disposable world composing the recordings, the adapter and the real fixture. [16]
- The shared serving fixture extended with the real notifier loop's collaborators, rather than a second harness. [17]
- Every oracle term read back out of recorded events, with `bound` composed from the measured terms. [18]
- The driver releasing one parked sleep at a time so a case chooses each pass's exact instant. [19]
- Re-parking, not a new record, is what proves an interval was consumed — a disabled loop re-parks without running a pass. [20]
- The arming choices that make the observer phase strict rather than maximal. [21]
- Every term of the bound asserted against the recorded events, with the three unfalsifiable relations documented instead of asserted. [22]
- The production loops and sweeper this harness enters rather than replaces. [23]
- The sweeper's retained starting-row window and ten-second full-sweep limit behind `refresh`. [24]
- The fixture this harness extends, and the clock its sleep primitive replaces. [25]
- The proof site that owns the oracle's documentation and its eight cases. [26]

### Cross-Repo References

No separate cross-repository authority is established by this repository-owned test-support module.
