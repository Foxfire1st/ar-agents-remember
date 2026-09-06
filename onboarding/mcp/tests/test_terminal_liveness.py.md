# test_terminal_liveness.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_terminal_liveness.py`            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-09-06T21:45:53+00:00 |
| lastVerifiedCommitHash | `f2b7c648f540efb9d64ceea22e11e651cb5cc914`       |
| lastVerifiedCommitDate | 2026-08-31T15:32:32+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

Retains the transient-failure-storm regression: sessions stay running while the liveness hysteresis window has not elapsed. Fake probes and clock-driven setup model that boundary. Historical fleet-scaling, landed-row cost and broad false-exit recovery claims are no longer the retained assertions in this module.

## Code Commentary

### Logic

The current evidence boundary is the source-listed behavior below. Earlier coverage claims in
history describe prior populations and must not be used to recreate removed tests or claim they
still run. The retained behavior and its fixture limits, described above, govern this card.

### Conventions

The table lists retained test definitions, not collected parametrized or subtest counts.
Inspect the cited setup and collaborators before treating a focused result as end-to-end evidence.

### Invariants And Boundaries

Preserve exact refusal, identity, and cleanup assertions rather than adding overlapping helper
cases. Coverage percentages are diagnostic and production CRAP 20 prompts review; neither implies
an obligation to restore removed cases. Full suites and whole-candidate review remain master-end
work. This source inspection does not claim a newly executed test or acceptance result.

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
| Transient failure storm leaves sessions running until window elapsed | `test_transient_failure_storm_leaves_sessions_running_until_window_elapsed` | mcp/tests/test_terminal_liveness.py:184-196 |

## Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external evidence is needed for these assertions. | N/A | N/A |

## Update History

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
