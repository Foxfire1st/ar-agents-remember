# test_terminal_liveness.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_terminal_liveness.py`            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-09-10T10:12:00+02:00 |
| lastVerifiedCommitHash | `a5c29cb63dcb6f0d1ca32d0cf7822457df43cfa4`       |
| lastVerifiedCommitDate | 2026-09-11T18:44:06+02:00|| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

Retains the liveness behavior at the sweeper boundary: transient failures stay within the hysteresis window, full catalog probes remain rate-limited by the configured interval, and starting rows use the one-second bounded path. Fake probes, snapshots, and a controlled clock model those boundaries. These tests do not claim lifecycle caller ownership or production wiring.
## Code Commentary

### Logic

The current evidence boundary is the source-listed behavior below. The transient-failure case
keeps sessions running while the hysteresis window has not elapsed. The full-sweep case keeps the
configured ten-second admission gate intact. The starting-row case proves the one-second
eligibility boundary, four-row targeted cap, and persisted readiness transition for a fifth row on
the following tick. Earlier coverage claims in history describe prior populations and must not be
used to recreate removed tests or claim they still run.

The current evidence boundary is the source-listed behavior below. `_FakeHost` parks inside
`probe_session` on events so the first sweep holds the sweeper lock and the catalog batch while a
contender runs; `_RaisingHost` raises on its first probe to force the lock-release path. The
contended-full case asserts the contender returns before its 0.25 s join, that the host was probed
only once across both callers, and that a later `refresh()` probes again. The contended-starting
case drives the one-second starting fast path with the full-sweep rate limit in force and asserts
the first sweep was the only probe across both callers. The clean-hosted case wraps
`catalog._write_disk` and asserts one replacement on the first sweep and zero on an identical
second sweep. 
### Conventions

The table lists retained test definitions, not collected parametrized or subtest counts.
Inspect the cited setup and collaborators before treating a focused result as end-to-end evidence.
This inventory covers the composed module: siblings `260831-LOCR-L12` and `260831-LOCR-L21` and this
leaf `260831-LOCR-L22` have all landed on the LOCR master integration branch, so the rows above are
the module's complete retained case set and every cited range was derived from that composed file.
### Invariants And Boundaries

Preserve exact refusal, identity, and cleanup assertions rather than adding overlapping helper
cases. Keep full-sweep rate limiting inside `TerminalCatalogLivenessSweeper` and keep the
one-second starting-row path bounded at four rows; the lifecycle cadence and production wiring
remain owned by the assembled L01/R16/R18 candidate. Coverage percentages are diagnostic and
production CRAP 20 prompts review; neither implies an obligation to restore removed cases. Full
suites and whole-candidate review remain master-end work. This source inspection does not claim a
newly executed test or acceptance result.
### Todos

No additional implementation scope is opened by this memory reconciliation.

## Docs References

The repository has no configured Domain Documentation source. These claims concern its own test
fixtures and assertions, so the exact retained source is the direct evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain claim is required. | N/A | N/A |

## Repo-Internal References

Each current definition below can be inspected in the exact source file. Historical references
to removed methods are superseded by this current inventory.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fake fixtures configure and drive the existing host/control-read seams | `_Clock`; `_FakeHost`; `_sweeper`; `_starting_sweeper` | mcp/tests/test_terminal_liveness.py:44-81 |
| The raising probe double that forces the lock-release path | `_RaisingHost` | mcp/tests/test_terminal_liveness.py:114-124 |
| Host failures retain the count-plus-window gate, exit-mark and immediate pane-gone transition | `test_transient_failure_storm_leaves_sessions_running_until_window_elapsed` | mcp/tests/test_terminal_liveness.py:203-231 |
| Full sweeps remain rate-limited by the configured interval | `test_full_sweep_rate_limit_is_preserved` | mcp/tests/test_terminal_liveness.py:233-250 |
| Starting rows use the one-second path and four-row cap | `test_starting_rows_use_one_second_fast_path_and_four_row_cap` | mcp/tests/test_terminal_liveness.py:252-292 |
| Host failure evidence survives reload and clears after a successful probe | `test_host_failure_series_survives_restart_and_success_resets` | mcp/tests/test_terminal_liveness.py:295-334 |
| Connected bridge failures require three strikes across reload and reset on success | `test_connected_control_reads_require_three_strikes_across_restart_and_reset` | mcp/tests/test_terminal_liveness.py:336-405 |
| Alive starting rows remain eligible through delayed bridge reads | `test_alive_starting_row_survives_delayed_bridge_reads` | mcp/tests/test_terminal_liveness.py:407-439 |
| A contended full sweep returns without waiting and without a second probe | `test_contended_full_sweep_returns_committed_snapshot_without_second_probe` | mcp/tests/test_terminal_liveness.py:442-479 |
| The sweep lock releases after an observation exception so a later cadence retries | `test_sweep_lock_releases_after_observation_exception_for_later_retry` | mcp/tests/test_terminal_liveness.py:481-491 |
| A contended starting-row sweep reads the committed snapshot before any catalog list | `test_contended_starting_sweep_reads_committed_snapshot_before_any_catalog_list` | mcp/tests/test_terminal_liveness.py:493-534 |
| A repeated clean hosted sweep performs zero physical replacements | `test_repeated_clean_hosted_sweep_does_not_replace_catalog` | mcp/tests/test_terminal_liveness.py:536-572 |

## Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external evidence is needed for these assertions. | N/A | N/A |

## Update History

- 2026-09-11T18:45+02:00 — 260831-LOCR-L22 curator composition: resolved this card's sync merge
  against the landed L12 and L21 lines and re-derived the inventory and every range from the composed
  ten-case module. Two merge hazards were handled semantically rather than line-wise: this leaf and
  L21 both open new cases with the same `TerminalCatalogLivenessSweeper(...)` boilerplate, so a
  line-based union splices one side's case into the other's, and this leaf's `_RaisingHost` helper
  and `TerminalEvidenceRead` import sit outside the case bodies. All three lines' contributions are
  present in their correct owners, and the composed module plus the catalog suite were executed
  (nineteen cases passed) before these ranges were written. The composition boundary is now closed:
  no sibling case additions to this module remain unlanded. Verification metadata remains
  closeout-owned.

- 2026-09-11T18:40+02:00 — 260831-LOCR-L21 curator composition: resolved this card's sync merge
  against the landed L12 line and re-derived every row above from the composed module. The merge was
  semantic rather than textual: this leaf extends `test_transient_failure_storm_leaves_sessions_
  running_until_window_elapsed` with its window-elapsed and pane-gone tail, while L12 inserts two new
  cases immediately after that same anchor, so a line-wise union splices one side's tail into the
  other's case. Both contributions are kept in their correct owners and the composed module was
  executed (six cases passed) before the ranges above were written. Row ownership: L12 contributes
  the full-sweep and starting-row cases; this leaf contributes the host-restart, connected-
  three-strike and alive-starting cases plus the storm tail. Verification metadata remains
  closeout-owned.

- 2026-09-10T10:12:00+02:00 — 260831-LOCR-L12 curator: re-verified every cited range against the
  current source tree and made the composition boundary explicit. Sibling leaves `260831-LOCR-L21`
  (three further cases) and `260831-LOCR-L22` (four further cases) modify this same file and had not
  landed, so this inventory is bounded by what this tree contains and is not the file's final case
  count. Verification metadata remains pinned until closeout stamps the leaf code commit.

- 2026-09-08T14:23:36+02:00 — 260831-LOCR-L12 curator: reconciled the retained liveness test
  inventory with the worker's two focused additions. The sidecar now records the configured
  full-sweep gate and the one-second starting-row/cap behavior, while preserving the boundary
  that lifecycle ownership and production wiring require the assembled L01/R16/R18 candidate.
  Verification metadata remains pinned until closeout stamps the leaf code commit.

- 2026-09-10T11:53:11+02:00 — LOCR-R21 curator reconciliation against the relocated base (code `bb38d04e`, memory `e26b55db`) after sibling LOCR-L28 landed: LOCR-L28 did not touch this module, so all five cited ranges were re-checked against the unchanged candidate file and kept; the four collected cases and the 363-line file are unchanged. The composition boundary was re-confirmed — L12 and L22 remain unlanded and their case additions to this module are still absent — and the card now also records that the module is registered in the `integration` lane of `mcp/tests/test-evidence-lanes.toml`, whose declared budget is 150 collected cases. The candidate stays test-only. Verification metadata remains closeout-owned.

- 2026-09-10T10:32:23+02:00 — LOCR-R21 curator reconciliation against the synced base (code `6096941f`, memory `71d7f73a`): re-verified every range cited by this card against the current candidate file and kept each one unchanged — the fixture range spans `_Clock`/`_FakeHost` through `_control_sweeper`, and each of the four case ranges ends on its method's final assertion. The candidate is test-only: `mcp/tests/test_terminal_liveness.py` is the sole changed source, and no production module, threshold, or persisted field moves with it. Recorded the module's composition boundary (L12 and L22 add cases to this same file from their own unlanded worktrees) and the retained-but-uncalled `_control_sweeper` builder. Verification metadata remains closeout-owned.

- 2026-09-08T14:25+02:00 — LOCR-R21 curator: refreshed the card for the current test-only proof boundary. The retained storm now asserts definitive pane-gone exit, and dedicated cases cover persisted host reset, connected three-strike reset, and alive-starting bridge delay. Production liveness thresholds, state fields, and ownership remain unchanged; closeout owns verification stamping.

- 2026-09-10T09:30+02:00 — 260831-LOCR-L22 curator: refreshed the card for the retained
  non-overlap and single-write proof — full and starting contention, exception-driven lock release
  with later retry, and one-replacement-then-zero for a repeated clean hosted sweep. Cadence (`R12`)
  and hysteresis (`R21`) ownership is explicitly preserved; closeout owns verification stamping.
- 2026-09-06T21:45:53+00:00 — Reconciled the retained IAS test/helper population and exact citation ranges, preserving prior history and verification provenance; no tests or review were run.


- 2026-08-25T15:44+02:00 — PDLS whole-system reconciliation updated the implementation summary
  above after source and requirement review. Verification remains closeout-owned.

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-04T11:43:39+02:00 — 260731-EFA-L6 S18-B03 curator: rebound the production stderr-classifier
  reference to the exact terminal-tmux symbols and completed the catalog copier, probe-record, and
  observer-caller ownership chain.

- 2026-07-31T16:50+02:00 — 260731-EFA-L2 curator, code-quality hardening sweep.
  `TerminalCatalogLivenessSweeper` now takes one `probe=LivenessProbe(...)` argument in place of
  the separate `config=`, `pane_capturer=`, and `snapshot_reader=` keywords, so every sweeper
  construction in the suite changed shape. Rewrote the sentence describing the three sweeper
  builders to name `LivenessProbe`, its `hysteresis=TerminalCatalogLivenessConfig(...)` slot, and
  the two injected doubles that now ride inside it. The threshold-3 / window-5s / pane-gone-1 /
  interval values are passed unchanged, and none of the eight enumerated cases gained, lost, or
  altered an assertion.

- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: refreshed the regression-coverage record for the current backend/shared behavior and preserved the pre-commit verification stamp.

- 2026-07-09T19:31+02:00 — 260707-HFX2-L12: documented the CS-6 scaling/reclamation change for this file. Verification metadata pinned until closeout stamps the HFX2-L12 commit.
- 2026-07-09T14:05+02:00 — HFX2-L11 (landed chat archive), round-2 F1 fix: added
  `test_landed_rows_do_not_add_per_row_sweep_probe_or_catalog_reads`, a flat-cost scaling
  regression run at 5 vs 500 `landed`-status rows plus one `running` row. Both sizes assert the
  exact same result — one host probe call (`host.calls == 1`), one pane capture (only for the
  running row), and exactly 3 `_read()` calls on the catalog — proving `refresh()` no longer
  fans out per-row tmux/catalog work across landed rows (the round-1 BLOCK: landed seats were
  silently enrolled into the sweeper's O(N)-subprocess/O(N^2)-catalog-read per-cycle cost as they
  accumulated by design — the 3rd CS-6-class catch on this master after L7/L9). Uses a new
  `_CountingCatalog` subclass to count `_read()` calls and a `status=` kwarg added to `_entry(...)`.
  Verification metadata pinned until closeout stamps the 260707-HFX2-L11 commit.
- 2026-07-07T23:45+02:00 — Created for 260707-HFX-L5 (catalog liveness hysteresis): pins the
  14-session transient command-failure storm staying `running`, pane-gone marking immediately,
  alive-again self-heal of a false exit, sweep rate limiting (1 probe across 3 fast ticks), and
  overlapping-sweep suppression (real threads + events); the L5R2 fix round added the two
  stderr-classification regressions driving the REAL `_tmux_probe_session` with `subprocess.run`
  mocked (non-missing nonzero stderr ⇒ hysteresis; missing-session stderr ⇒ pane-gone).
  Verification metadata pinned until closeout stamps the HFX-L5 commit.
