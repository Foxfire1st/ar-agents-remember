# test_supervisor.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/tests/test_supervisor.py`             |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-08T18:45+02:00                     |
| lastVerifiedCommitHash | `8b7c1933611a13ada98dcd6fc3476c0457e136ac` |
| lastVerifiedCommitDate | 2026-07-08T07:43:47+02:00|
| governingOverview      | `../overview.md`                           |

## Purpose

`test_supervisor.py` covers the deterministic supervisor sweep (`serving/supervisor.py` +
`serving/supervisor_heartbeat.py`, 260707-HFX2-L2 R2-R6): one unit test per predicate family, the
heartbeat's own read/tick/staleness behavior, and one integration test that seeds drift across every
predicate simultaneously and asserts the full finding→action→heartbeat chain — no model in the loop
anywhere; every fixture is a plain store write or a fake pane capturer/paster.

## Code Commentary

### Logic

Sixteen tests, `NOW = datetime(2026, 7, 8, 12, 0, 0, tzinfo=UTC)` as the shared fixed clock:

- **Pane predicate (R2a):** `test_mid_turn_pane_fires_a_finding`, `test_normal_pane_fires_nothing`,
  `test_terminal_kind_rows_are_never_pane_classified` (a `kind="terminal"` row is skipped
  regardless of its captured text — the predicate only ever classifies `kind="harness"` rows).
- **Expectation predicate (R2b):** `test_overdue_briefed_by_row_fires`,
  `test_not_yet_due_row_is_silent` (a row whose deadline has not yet passed produces no finding).
- **Turn-report predicate (R2c):** `test_missing_report_fires_when_row_is_overdue`,
  `test_present_report_does_not_fire` (an overdue row whose artifact DOES exist and has content is
  silent — pins that `missing_artifact()` is a real second check, not a rubber stamp on
  overdue-ness), `test_malformed_leaf_key_is_skipped_not_guessed`
  (`turn_report_path_for_leaf_key` returns `None` for a key not in the `repo/master/leaf-id` shape,
  and the predicate skips rather than guessing a path).
- **Inbox predicate (R2d):** `test_pending_row_with_no_next_attempt_is_immediately_redeliverable`.
- **Seat-liveness predicate (R2e):** `test_stale_turn_state_past_cutoff_fires`,
  `test_recently_stale_does_not_fire_yet` (stale but still inside the grace window is silent),
  `test_degraded_row_with_no_turn_state_uses_liveness_failures` (the graceful-degradation path: a
  row the L8 prober never classified falls back to the L5 `liveness_failures > 0` signal alone).
- **Sweep integration:** `test_seeded_drift_produces_expected_actions_and_ticks_heartbeat` seeds
  drift across pane-signal, expectation-overdue, inbox-redeliverable, AND seat-liveness
  simultaneously in one sweep and asserts the expected action set, delivery outcomes, the
  `mark_missed` side effect, and the heartbeat tick — the R6-mandated "seeded drift → expected
  actions" integration case.
- **Edge cases:** `test_finding_with_no_routable_owner_skips_its_action` (a finding whose owner
  cannot be derived produces a `"skipped"`/`"no routable owner"` result rather than raising —
  covers `_signal_emit`'s no-owner branch specifically, added after the CRAP-Calculator flagged its
  low coverage), `test_zero_drift_sweep_still_ticks_the_heartbeat` (R5: a sweep with zero findings
  still ticks), `test_second_sweep_bumps_sweep_count`.

`_entry(...)` is the shared `TerminalCatalogEntry` fixture builder, typed against the catalog's own
`Literal` aliases (`TerminalSessionKind`/`TerminalSessionStatus`/`SeatTurnState`) per `pyright`'s
finding during this leaf.

### Conventions

Standard suite bootstrap (`MCP_SRC` path insert), `tempfile` for every store (`ExpectationRowStore`,
`OperatorInboxStore`, `OrchestrationNudgeStore`, `EventStore`) so no test touches real coordination
state. `cast(TerminalHost, fake)` for the duck-typed fake host, matching the existing project
convention from `test_terminal_ws.py`.

### Invariants And Boundaries

- No test touches the real coordination root or a real tmux session; every store is temp-rooted and
  every pane capturer/paster is a fixture double.
- The integration test's fake `TerminalPaster` tracks a MONOTONICALLY-GROWING chip counter (not a
  single shared landed/not-landed boolean) precisely because the sweep can issue two INDEPENDENT
  deliveries (redeliver + the auto-nudge's owner-signal post) against one fake instance in the same
  sweep — a shared boolean made the second delivery's origin capture already show the first
  delivery's chip, masking growth detection (a live instance of the F-V/N1 problem
  `terminal_paste.py`'s own docstring documents). Any future test adding a third concurrent delivery
  path must preserve this per-call-plus-monotonic counting, not regress to a shared flag.
- Predicate-family tests are independent of the integration test — each can fail in isolation and
  point at exactly one `evaluate_*_findings` function.

### Todos

No known follow-up in this file. The builder report's "Issues Hit" documents two now-resolved
findings from writing this suite (the fake-paster chip-sharing bug above, and `_signal_emit`'s
initial 11% coverage/CRAP-threshold trip) — both fixed in the version this sidecar documents, not
open follow-ups.

## Docs References

No relevant external documentation found after checking the repo Domain Documentation; this is a
same-repository unit/integration-test suite for internal control-plane plumbing with no external
spec.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No external/domain document defines the supervisor sweep; the leaf task doc (R1-R6) and the P-15 pilot-observer log are the source of truth this suite pins. | L1-L449 | [test_supervisor.py](test_supervisor.py) |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The module under test: every predicate, the action dispatcher, and the sweep entry point. | whole module | [../src/agents_remember/serving/supervisor.py](../src/agents_remember/serving/supervisor.py) |
| The heartbeat store the zero-drift and second-sweep tests exercise directly. | `SupervisorHeartbeatStore` | [../src/agents_remember/serving/supervisor_heartbeat.py](../src/agents_remember/serving/supervisor_heartbeat.py) |
| The catalog entry fixture builder's typed fields come from this module's `Literal` aliases. | `TerminalCatalogEntry` | [../src/agents_remember/serving/terminal_catalog.py](../src/agents_remember/serving/terminal_catalog.py) |
| The fake-host casting convention this suite reuses rather than inventing its own duck-typing idiom. | `cast(TerminalHost, fake)` | [test_terminal_ws.py](test_terminal_ws.py.md) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Sweep-local behavior only. | — | — |

## Update History

- 2026-07-08T18:45+02:00 — Created for 260707-HFX2-L2 (supervisor sweep + predicates, R2-R6):
  sixteen tests — one per predicate family (pane/expectation/turn-report/inbox/seat-liveness, each
  with its fire + silent + edge-case variants), one seeded-drift sweep integration test asserting
  the full finding→action→heartbeat chain, a no-routable-owner edge case, and two heartbeat-specific
  cases (zero-drift still ticks; sweep count increments). Documents the fake-paster
  monotonic-chip-counter fix (a live F-V/N1 instance found while writing this suite) as a preserved
  invariant for future test additions. Verification metadata pinned until closeout stamps the
  260707-HFX2-L2 commit.
