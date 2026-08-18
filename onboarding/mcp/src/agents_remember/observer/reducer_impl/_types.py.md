# mcp/src/agents_remember/observer/reducer_impl/_types.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/observer/reducer_impl/_types.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-07T22:45:00+02:00                                            |
| lastVerifiedCommitHash | `2597ff98306ba7c7963005092ac597c4972e63ce`                                        |
| lastVerifiedCommitDate | 2026-08-18T15:45:32+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[overview](../../overview.md)

## Purpose

Input bundles shared by the reducer's assembly and its split builders. ``WorkspaceStructure`` is the slice-3a pre-image (enclosures + providers + admitted worktree groups); ``AnalyticalInputs`` is the slice-3b pre-image the analytical surfaces are built from. Both are the design's own two slices, so they live together and are re-exported by :mod:`agents_remember.observer.reducer`.

## Code Commentary

- `WorkspaceStructure`
- `AnalyticalInputs`

## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/agents_remember/observer/reducer_impl/_types.py`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module. | — | — |

## Update History

- 2026-08-18T13:00+02:00 — No content impact: 260815-DAG-L8 added the closeout-queue projection surface (closeoutQueues); the behavior this card describes is unchanged.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
