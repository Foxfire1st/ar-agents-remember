# mcp/src/agents_remember/serving/projections/snapshots_impl/_analytics.py

## Governing Overview

[serving projections overview](../overview.md)

## Purpose

Analytical file-surface readers for drift snapshots, blocked-start progress, routes, tool reports and ledger. Shared ledger-window enrichment serves engine-process facts and the official ledger surface. Existing producer parsers and tolerant reader boundaries remain; the verification-date sidecar reader and its discovery/metadata imports are removed.

## Code Commentary

- `read_start_progress_entries`
- `read_drift_snapshots`
- `read_route_coverage`
- `read_tool_reports`
- `read_ledger`
- `_ledger_window`
- `_git_commit_meta`
- `_commit_meta_for`
- `_enrich_ledger_rows`

Attention-producing readers also collect per-kind `AttentionObservation` proof. Fixed-level enumeration or malformed progress/snapshot reads make the observation incomplete, not healthy. Drift joins the native branch census and shared strict parser; missing fingerprint supplies no changed/recovery proof and complete censuses suppress orphan snapshots even if unlink failed. Retired provider start-progress gates are skipped without marking the observation incomplete and reach neither attention nor the process map. Blocked-start uses full worktreeGroup identity and native progress/cleared-source evidence. Existing sidecar, coverage, tool and ledger enrichment stays independent.

## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/agents_remember/serving/projections/snapshots_impl/_analytics.py`.

## Evidence

### Repo-Internal References


- Persisted drift, blocked-start, route, tool and ledger readers and ledger enrichment remain; setup-summary/setup-progress readers and onboarding verification-age input are absent. The start reader skips retired provider gates without treating them as unreadable observations. [1]
