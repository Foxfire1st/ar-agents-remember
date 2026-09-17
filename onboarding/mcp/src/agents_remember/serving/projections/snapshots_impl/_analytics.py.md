# mcp/src/agents_remember/serving/projections/snapshots_impl/_analytics.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/serving/projections/snapshots_impl/_analytics.py` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-07T22:45:00+02:00                                            |
| lastVerifiedCommitHash | `997305a9ced4caea67edb826224bf0351264fd56`                                        |
| lastVerifiedCommitDate | 2026-09-17T19:54:27+02:00|
| governingOverview      | `../overview.md`                                          |

## Governing Overview

[serving projections overview](../overview.md)

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

- The card mirrors the source file one-to-one at `mcp/src/agents_remember/serving/projections/snapshots_impl/_analytics.py`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module. | — | — |

## Update History

- 2026-09-17T19:30+02:00 — 260915-CAPS-L20 curator: **both governing declarations repaired.** The field named `overview.md` and the body link named `overview.md`; each resolved card-relatively to nothing, and they did not agree with each other. Both now name `../overview.md`, the route-local overview of this card's own directory. Recorded under `260915-CAPS-L20` as this leaf's **S3** (D3, the packaged `l-01-agent-lifecycles` family) and **S4** (D16, govern-or-remove per card). The checker that previously reported this corpus clean now resolves both declarations, so this card reaches the curator's gated repair set instead of passing silently; that is the gap this leaf closed. Superseded history entries above stand unedited — including any entry that asserted an earlier repair this card did not in fact carry, which is the finding rather than an error to erase. No prose, anchor, range or verification stamp was otherwise changed.
- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
