# mcp/src/agents_remember/observer/reducer_impl/_metrics.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/observer/reducer_impl/_metrics.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-07T22:45:00+02:00                                            |
| lastVerifiedCommitHash | `b252c42cca200933d5c9c36e26de47a526a569ce`                                        |
| lastVerifiedCommitDate | 2026-08-07T23:58:52+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[overview](../../overview.md)

## Purpose

Analytical rollups: token series, staleness histogram, and workspace metrics. The reducer's slice-3b rollups: the bounded cumulative token series, the verification-age histogram, the workspace metrics rollup, and the analytics assembly. All remain pure functions of already-read inputs.

## Code Commentary

- `_metrics`
- `_decimate_token_series`
- `token_series`
- `staleness_histogram`
- `_staleness_bucket`
- `build_analytics`
- `_stalest`

## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/agents_remember/observer/reducer_impl/_metrics.py`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module. | — | — |

## Update History

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
