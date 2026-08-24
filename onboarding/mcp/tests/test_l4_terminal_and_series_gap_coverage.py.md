# mcp/tests/test_l4_terminal_and_series_gap_coverage.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_l4_terminal_and_series_gap_coverage.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:48+02:00 |
| lastVerifiedCommitHash | `f95487ec993b58d34911bba0206a7fa6ef9684eb` |
| lastVerifiedCommitDate | 2026-08-24T15:28:18+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[governing overview](../overview.md)

## Purpose

Forces the atomic child terminal census and series closeout/publication guards across invalid,
concurrent, and exact named-ref facts.

## Code Commentary

Terminal cases cover malformed/foreign child enclosures and residual worktree/ref ownership.
Series cases cover standalone publication, graph/blocker/candidate races, exact leaf-chain tips,
atomic task completion, dirty integration checkouts, and external-memory ledger mapping/reachability.

## Invariants And Boundaries

- Series refs retire only after child ownership is terminal.
- Atomic closeout publication remains under exact task/ref authority.
- External-memory ledgers must map and reach the exact landed content.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The suite owns rare terminal and atomic-series refusal branches. | `TerminalChildCensusCoverageTests`; `AtomicSeriesAuthorityCoverageTests` | mcp/tests/test_l4_terminal_and_series_gap_coverage.py:21-127; mcp/tests/test_l4_terminal_and_series_gap_coverage.py:130-418 |

## Documentation References

No configured domain-documentation or cross-repository source applies to this file.

## Current Contract — 260821 CLIVE Final

This is the current source-backed contract for this test card. It supersedes any earlier
queue-lifecycle, blocker-row, replan/drain, or compatibility-reader wording where present.

Forces terminal child-census and atomic-series authority refusal branches, including unreadable or conflicting evidence.

### Current Invariants

- Terminal cleanup and successor admission require exact archive/receipt proof.
- Atomic-series authority remains contract/ref-owned and fail-closed.

## Update History

- 2026-08-24T14:48+02:00 — DAGQC cumulative CLIVE final-gap curation: reconciled this test card to current source while preserving prior history and verification provenance.

- 2026-08-24T00:51+02:00 — No content impact: 260821-CLIVE-L2 the test only patches the extracted `initial_queue_state` name instead of its former private alias; the forced assertion is unchanged. Verified at code commit `1d446724`.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-19T22:32+02:00 — No content impact: 260815-DAG-L13 extended topology mocks with the resolve/parent seams the effective-nature resolution consumes; documented gap coverage is unchanged. Verification remains closeout-owned.

- 2026-08-19T04:05+02:00 — No content impact: 260815-DAG-L10 updated expectations to the new
  series worktree-group check (the refusal now matches "worktree group"; the missing/empty
  enclosure cases replace only `task_root` and keep the group valid). The documented terminal and
  atomic-series coverage is unchanged; the class-range citation was re-pointed to the shifted
  spans (`21-127`; `130-418`). Verification metadata stamped at the landed code commit
  `e41ea31d`.

- 2026-08-18T09:05+02:00 — Renamed the atomic 'barrier' concept to 'blocker' throughout (terminology unification; no behavioral change). Verification remains closeout-owned.

- 2026-08-16T08:12+02:00 — Created focused terminal and atomic-series forcing during targeted Dagger coverage repair.
