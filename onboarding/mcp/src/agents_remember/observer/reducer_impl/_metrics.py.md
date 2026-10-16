# mcp/src/agents_remember/observer/reducer_impl/_metrics.py

## Governing Overview

[overview](../overview.md)

## Purpose

Pure analytical assembly, verification-age staleness histogram and stalest-sidecar ranking over already-read inputs. Task stage/activity counts belong to task-entry production, not lifecycle buckets here.

## Code Commentary

- `staleness_histogram`
- `_staleness_bucket`
- `build_analytics`
- `_stalest`

Analytics retains drift, sidecar staleness, setup, route, tool-report, ledger, attention and Engine Room surfaces. It emits no lifecycle buckets, taskDocuments, series, pickup or expectation collections and owns no task-stage or action authority.

## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/agents_remember/observer/reducer_impl/_metrics.py`.

## Evidence

- Pure staleness/ranking and analytics assembly consume already-read surviving inputs. [1]



### Repo-Internal References

The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module.
