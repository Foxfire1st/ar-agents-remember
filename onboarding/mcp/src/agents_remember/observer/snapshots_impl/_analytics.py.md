# mcp/src/agents_remember/observer/snapshots_impl/_analytics.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/observer/snapshots_impl/_analytics.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-07T22:45:00+02:00                                            |
| lastVerifiedCommitHash | `b252c42cca200933d5c9c36e26de47a526a569ce`                                        |
| lastVerifiedCommitDate | 2026-08-07T23:58:52+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[overview](../../overview.md)

## Purpose

Analytical file-surface readers: drift, sidecars, setup, routes, tools, ledger. The observers' slice-3b readers plus the shared ledger-window enrichment used by the engine-process facts and the official ledger surface. Every reader reuses the producing subsystem's own parser rather than re-parsing.

## Code Commentary

- `read_start_progress_entries`
- `read_drift_snapshots`
- `read_sidecar_staleness`
- `read_setup_summaries`
- `read_setup_progress_nodes`
- `read_route_coverage`
- `read_tool_reports`
- `read_ledger`
- `_ledger_window`
- `_git_commit_meta`
- `_commit_meta_for`
- `_enrich_ledger_rows`

## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/agents_remember/observer/snapshots_impl/_analytics.py`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module. | — | — |

## Update History

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
