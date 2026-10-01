# mcp/src/agents_remember/serving/projections/snapshots_impl/_analytics.py

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

## Evidence

### Repo-Internal References

The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module.
