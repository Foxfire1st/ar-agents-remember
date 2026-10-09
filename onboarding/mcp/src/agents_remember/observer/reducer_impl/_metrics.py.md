# mcp/src/agents_remember/observer/reducer_impl/_metrics.py

## Governing Overview

[overview](../overview.md)

## Purpose

Analytical rollups: staleness histogram and workspace metrics. The reducer's slice-3b rollups: the verification-age histogram, the workspace metrics rollup, and the analytics assembly. All remain pure functions of already-read inputs. No token aggregate is computed here; `tool.completed` is liveness-only.

## Code Commentary

- `_metrics`
- `staleness_histogram`
- `_staleness_bucket`
- `build_analytics`
- `_stalest`

## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/agents_remember/observer/reducer_impl/_metrics.py`.

## Evidence

### Repo-Internal References

The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module.
