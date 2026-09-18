# mcp/tests/test_serving_notifier_handoff.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_serving_notifier_handoff.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T21:25+02:00 |
| lastVerifiedCommitHash | `e963a01c6804570d597e451eaa069eaba66bd3ec` |
| lastVerifiedCommitDate | 2026-09-18T04:45:39+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

Reviewed at 2026-09-15T21:25+02:00 against the leaf base `e9678c56`; this module is an uncommitted
candidate at that base, so it does not exist at the commit above and normal closeout owns the final
verification-metadata stamping. The hash records only the base this card was read against.

## Purpose

The completion-relative proof of the observer-to-notifier handoff (`LOCR-R04@v1`): eight cases that
measure the latency from "terminal evidence became readable" to "a notifier pass actually consumed it"
and assert that latency, and its decomposition, against a stated bound.

The serving lifetime owns two independently scheduled loops and neither can be woken by the other.
`_terminal_observation_loop` polls the canonical liveness sweeper every `P` (1.0 s) **after** each
attempt returns, and the sweeper itself admits one full sweep per `F` (10.0 s) measured from the **start**
of the previous full sweep. `_agent_notifier_loop` evaluates the durable catalog and then sleeps `N`
(10.0 s), also after its pass returns. The relay is correct only if those two cadences compose into a
bounded handoff, and this module is that claim made falsifiable.

**The delivered relation.** With `T` the instant the evidence becomes readable:

```
observer_release = max(previous_full_sweep_start + F,
                       completion of any observer refresh() still in flight and holding the
                       shared sweep lock at that eligibility point)
consuming_sweep  = the first lifecycle poll at or after observer_release, at most P later
commit           = the consuming full sweep's own durable catalog commit
next_notifier    = last_notifier_pass_end + N

worst phase      = F + P + R_observer + D_commit + N + R_notifier
```

`R_observer` is the remaining duration, measured at eligibility, of any refresh holding the shared
sweep lock (the previous full sweep, or a starting-row fast-path pass). `D_commit` is the consuming
sweep's own duration up to its commit, and `R_notifier` the remaining duration of a notifier pass
already in flight at that commit. For the default knobs the fixed part is **21.0 s** of logical
scheduling (`P` + `F` + `N`); everything beyond it is a measured overrun rather than an allowance.

**This is a preservation leaf.** `LOCR-R04@v1` requires zero production change; the deliverable is the
timing oracle and its proof envelope, so this module and its two support modules are the whole artifact
and no file under `mcp/src` is touched by the change set.

The module does not build a harness. It imports `_HandoffCase`, `WORST_PHASE_BOUND`, `P`, `F`, `N`,
`ARMED_EVIDENCE_ID`, `_REAL_SLEEP` and `_wait_until` from
[_serving_handoff.py](_serving_handoff.py.md), which enters the real `_serving_lifespan` under a
deadline-correct virtual clock, so the real loops, the real sweeper, the real catalog commit boundary
and the real notifier sweep are what these cases measure.

## Code Commentary

### Logic

Each case asserts the bound **and** its decomposition from measured terms rather than illustrating it,
and each protects one clause of the oracle. Assertions such as
`handoff.latency == WORST_PHASE_BOUND + overrun + commit_duration + notifier_overrun` are claims over
measured quantities, so a case that met the bound by accident of a different decomposition still fails.

| # | Case | Clause it protects |
| --- | --- | --- |
| 1 | `test_the_default_phase_handoff_stays_inside_the_worst_phase_bound` | The nominal 21.0 s handoff, with no injected overrun, plus the **strict** form of the observer-phase bound and the sleeping-notifier branch (`wait < N`). |
| 2 | `test_an_in_flight_full_sweep_overrun_delays_the_consuming_sweep` | The previous full sweep's own overrun (`R_observer`): the sweep is parked inside its batch after it already read the evidence row unarmed, and the bound is met exactly rather than merely satisfied. |
| 3 | `test_a_starting_row_fast_path_pass_counts_toward_the_same_overrun` | The one-second starting-row fast-path pass as an overrun source, plus a nonzero `D_commit`: the observed latency is exactly the oracle's sum. |
| 4 | `test_an_in_flight_notifier_pass_finishes_before_its_interval_starts` | `R_notifier`: a pass in flight at the commit reads a pre-fact snapshot, exits after the commit, and its interval starts at its own completion — so `wait == N + F/2`, not `N`. |
| 5 | `test_the_notifier_reads_only_committed_catalog_truth` | Committed-truth-only reads: the notifier reaches the catalog while the consuming batch is still open, its read is attempted before the commit and returns after it, carries the committed rows exactly, and could not have carried the uncommitted in-memory observation. |
| 6 | `test_missed_ticks_coalesce_instead_of_queueing_a_catch_up_burst` | Coalesced missed ticks, for both loops: three nominal ticks expiring behind one parked pass queue nothing and launch no second in-flight attempt; the next attempt is one whole delay after the parked one returned. |
| 7 | `test_a_live_pass_that_did_not_observe_the_fact_does_not_satisfy_the_stage` | The stage's negative control: rate-limited observer polls and a live notifier pass exist while the fact is readable, none reads it, and none is the consuming pass — being alive is not the claim. |
| 8 | `test_a_disabled_notifier_pauses_signal_derivation_only` | Notifier disablement and in-place re-enabling: observation keeps sweeping and commits the fact with signal derivation off, the loop re-parks without running a pass, and re-enabling makes the already-committed truth visible on the next completion-relative pass with no external traffic and no restart. |

Two properties of the proof are recorded as its **design** rather than as decoration, because a passing
run cannot show either. First, case 1's strict observer-phase assertion
(`observer_term < F + overrun`) is a constraint on **that case's scenario** — it arms the fact `P / 2`
after the previous sweep's start — and not a claim about production behaviour; its failing state is the
tight arming (`delay = 0`) the other cases use, and the arithmetic identity that would restate the arming
constant has no such state, so it is not asserted. Second, the boundary between the two arming helpers is
the difference between "the worst phase" and "a phase strictly inside its own maximum": `arm_the_fact_at`
arms at `T = previous_full_sweep_start`, which is the state the oracle bounds, while `arm_the_fact_after`
arms later and is the packet's conforming example.

### Conventions

`unittest.IsolatedAsyncioTestCase` through the shared `_HandoffCase` base, one class, eight cases. The
module issues no HTTP request, starts no process, opens no socket and publishes nothing durable outside
the disposable temporary case root, so it is classified in the repository's `unit-regression` evidence
lane at `mcp/tests/test-evidence-lanes.toml:97`. Focused host results are development evidence and grant
no certification authority; lane membership is classification, not execution or acceptance evidence, and
the verification stamps remain closeout-owned.

### Invariants And Boundaries

- The bound is stated over **measured** terms. `assert_oracle` asserts term relations that can fail in a
  state this harness can reach, and documents the three that cannot (the telescoping decomposition, the
  observer phase's maximum, and `bound` as the sum) with the reason each is unfalsifiable. A future
  reader must not "strengthen" the file by asserting them: an assertion that holds in every reachable
  state is not evidence, and the vacuity failure mode is invisible to a passing run.
- The consuming pass is chosen by **minimality** among eligible full sweeps, not by first match: the
  selection may not skip an earlier eligible poll and report a later one's window.
- The oracle claims the two loops compose within the bound. It does not claim the sweeper's internals
  beyond its retained ten-second full-sweep limit, the notifier's internal predicate set, or the catalog's
  on-disk format.
- The notifier's committed read is compared against `list_committed(include_terminated=True)` — the
  notifier's **own** read scope. Comparing against a filtered read would compare a full collection to a
  narrower one and would hold only while no catalog row is terminated.
- Case 8 asserts that observation continues with signal derivation disabled; it does not assert anything
  about how enablement is persisted or surfaced.
- No case edits, mocks, or imports a production module's internals; every case measures production
  through the harness's recordings. No file under `mcp/src` is changed by this leaf.

### Todos

None. The eight cases cover the oracle's terms and its two negative controls; a clause added to the
requirement needs its own case here rather than a widened assertion in an existing one.

## Docs References

No Domain Documentation entries are configured in the resolved memory root. The module tests
repository-owned serving behaviour, so no external domain claim is needed.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

The declarations below establish the behaviour under test and the oracle's own terms; this inventory is
not execution evidence and is not a certification result.

| Finding | Anchor | Source |
| --- | --- | --- |
| The two independently scheduled loops neither of which can wake the other: the observer's completion-relative poll and the notifier's completion-relative interval. | `_terminal_observation_loop`; `_serving_lifespan` | mcp/src/agents_remember/serving/_app_lifespan.py:109-126; mcp/src/agents_remember/serving/_app_lifespan.py:288-352 |
| The observer's poll delay, read from the production declaration rather than written as a literal. | `DEFAULT_STARTING_SWEEP_INTERVAL_SECONDS` | mcp/src/agents_remember/serving/terminal_liveness.py:57-57 |
| The sweeper's retained starting-row window and ten-second full-sweep limit measured from the previous full sweep's start. | `refresh` | mcp/src/agents_remember/serving/terminal_liveness.py:174-221 |
| The full-sweep rate limit the oracle's `F` term is read from, declared with the hysteresis the sweeper applies. | `TerminalCatalogLivenessConfig`; `DEFAULT_LIVENESS_HYSTERESIS` | mcp/src/agents_remember/models/terminal_catalog.py:729-744 |
| The notifier interval the oracle's `N` term is read from. | `DEFAULT_AGENT_NOTIFIER_INTERVAL_SECONDS` | mcp/src/agents_remember/kernel/_agentic_settings_core.py:111-111 |
| The real notifier sweep each recorded pass runs, and the durable store whose commit boundary the harness records. | `run_agent_notifier_sweep`; `TerminalCatalog` | mcp/src/agents_remember/serving/agent_notifier.py:96-192; mcp/src/agents_remember/serving/terminal_catalog.py:65-433 |
| The instrument: the deadline-correct virtual clock, the recorded worlds, and the oracle's terms read back out of them. | `_HandoffCase`; `_Handoff`; `assert_oracle` | mcp/tests/_serving_handoff.py:669-886; mcp/tests/_serving_handoff.py:604-666; mcp/tests/_serving_handoff.py:827-886 |
| The oracle's fixed part and the class that carries all eight cases. | `WORST_PHASE_BOUND`; `ServingNotifierHandoffTests` | mcp/tests/_serving_handoff.py:95-96; mcp/tests/test_serving_notifier_handoff.py:52-376 |
| The default-phase handoff with no injected overrun, and the strict observer-phase form asserted where its arming actually happens. | `test_the_default_phase_handoff_stays_inside_the_worst_phase_bound` | mcp/tests/test_serving_notifier_handoff.py:53-99 |
| The previous full sweep's own overrun as the `R_observer` term, with the bound met exactly. | `test_an_in_flight_full_sweep_overrun_delays_the_consuming_sweep` | mcp/tests/test_serving_notifier_handoff.py:101-146 |
| The starting-row fast-path overrun and a nonzero commit duration, with the observed latency equal to the oracle's sum. | `test_a_starting_row_fast_path_pass_counts_toward_the_same_overrun` | mcp/tests/test_serving_notifier_handoff.py:148-204 |
| A notifier pass in flight at the commit: its interval starts at its own completion, not at the commit. | `test_an_in_flight_notifier_pass_finishes_before_its_interval_starts` | mcp/tests/test_serving_notifier_handoff.py:206-237 |
| Committed-truth-only reads: attempted before the commit, returned after it, carrying the committed rows in the notifier's own scope. | `test_the_notifier_reads_only_committed_catalog_truth` | mcp/tests/test_serving_notifier_handoff.py:239-280 |
| Missed ticks coalesce for both loops: no queued catch-up burst and no second in-flight attempt. | `test_missed_ticks_coalesce_instead_of_queueing_a_catch_up_burst` | mcp/tests/test_serving_notifier_handoff.py:282-323 |
| A live pass that did not read the fact cannot be the pass that satisfies the stage. | `test_a_live_pass_that_did_not_observe_the_fact_does_not_satisfy_the_stage` | mcp/tests/test_serving_notifier_handoff.py:325-354 |
| Notifier disablement pauses signal derivation only, and re-enabling in place consumes already-committed truth on the next pass. | `test_a_disabled_notifier_pauses_signal_derivation_only` | mcp/tests/test_serving_notifier_handoff.py:356-376 |
| The shared fixture this module extends rather than duplicating. | `_ServingFixture` | mcp/tests/test_serving_observation_loop.py:259-370 |
| The candidate classifies this module once, in the explicit unit-regression lane. | "mcp/tests/test_serving_notifier_handoff.py" | mcp/tests/test-evidence-lanes.toml:120-120 |

## Cross-Repo References

No meaningful cross-repository implementation boundary is established by this repository-owned
unit-regression module.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History
- 2026-09-18T02:37:44+00:00: Generated citation repair: "mcp/tests/test_serving_notifier_handoff.py" repointed to mcp/tests/test-evidence-lanes.toml:120-120. No content impact: mechanical anchor-range projection bound to citation source snapshot d211cfd02f11c0600198b11c621aa5574ac8743db6e0ca1d2c92936e561c5146; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T22:33:10+00:00: Generated citation repair: "mcp/tests/test_serving_notifier_handoff.py" repointed to mcp/tests/test-evidence-lanes.toml:118-118. No content impact: mechanical anchor-range projection bound to citation source snapshot 82f9228826d64da5e61d4da1a77adecab55752bad9f20116de62f870f7abd93f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T06:49:47+00:00: Generated citation repair: "mcp/tests/test_serving_notifier_handoff.py" repointed to mcp/tests/test-evidence-lanes.toml:114-114. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-15T21:25+02:00 — 260831-LOCR-L04 curator (uncommitted change set on `ar/260831-locr-l04`,
  base `e9678c56`, `mcp/tests/test_serving_notifier_handoff.py` new, 376 lines, one class, eight cases,
  sha256 `01070bca…`): created this card for the leaf's new handoff proof module. `LOCR-R04@v1` is a
  **preservation** requirement — the change set touches no file under `mcp/src` — so the proof envelope
  is the deliverable and the card records the oracle it makes falsifiable rather than a case list: the
  delivered latency relation, the fixed 21.0 s of logical scheduling (`P` + `F` + `N`) with every
  further term measured (`R_observer`, `D_commit`, `R_notifier`), and the clause each of the eight cases
  protects. Two design properties are recorded as boundaries rather than claims, because a passing run
  cannot distinguish them: case 1's strict observer-phase assertion is a constraint on that case's own
  arming scenario and not a statement about production behaviour, and `assert_oracle`'s three
  unfalsifiable relations are documented rather than asserted — an assertion that holds in every
  reachable state is not evidence. The committed-truth case compares against the notifier's own
  `include_terminated=True` collection for the reason recorded in the body. The module is registered in
  the `unit-regression` lane at `mcp/tests/test-evidence-lanes.toml:97`, which is also the row whose
  insertion re-derived the lane citations across this card's siblings. No requirement verdict is
  recorded here: acceptance is the independent review's, and verification metadata stays closeout-owned
  because the source is an uncommitted candidate.
