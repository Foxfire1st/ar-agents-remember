# mcp/tests/test_worktree_support_benchmark.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_worktree_support_benchmark.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-29T18:29+02:00                                            |
| lastVerifiedCommitHash | `60e429d17e9fcbca3ab1c02563afcaa5761b8c5a`                                        |
| lastVerifiedCommitDate | 2026-08-29T20:33:10+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Part of the 260731-EFA-L7 in-place split family for `test_worktree_support_benchmark.py`'s source module; covers the behaviours named by its test classes.

## Code Commentary

- `BenchmarkRunnerPortabilityTests`
- `RequireUpdatedSidecarContentTests` proves exact candidate acceptance can clear an unchanged
  stale sidecar.
- `RequireUpdatedRouteOverviewContentTests` proves exact candidate acceptance can clear an
  unchanged stale governing overview but cannot hide an untraced body edit.

## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/tests/test_worktree_support_benchmark.py`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module. | — | — |

## Update History

- 2026-08-29T18:29+02:00 — Added the candidate-bound no-impact acceptance cases and the forcing
  case that keeps untraced route content closed. Verification remains closeout-owned.
- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
