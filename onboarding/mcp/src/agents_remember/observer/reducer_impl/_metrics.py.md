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

The metrics vocabulary buckets and staleness histogram/ranking remain pure. Analytics assembly retains the caller-derived series/attention/engine surfaces but no longer projects agentPickups or expectationRows; removal of those fields is not restoration of old session/gate machinery.

## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/agents_remember/observer/reducer_impl/_metrics.py`.

## Evidence

- Pure metrics and analytics assembly retain surviving inputs, not removed pickup/expectation projections. [1]



### Repo-Internal References

The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module.
