# mcp/src/agents_remember/observer/reducer_impl/_metrics.py

## Governing Overview

[overview](../overview.md)

## Purpose

Pure analytical assembly over already-read retained inputs. Verification-age histogram and stalest-sidecar ranking functions are removed. Native task stage/activity counts belong to task-entry production; the old lifecycle `_metrics` function is not present here. This module computes no token aggregate.

## Code Commentary

- `build_analytics`

Analytics retains supplied drift, route coverage, tool reports and ledgers, with caller-derived attention and Engine Room process surfaces. No setup surface is retained. It emits no verification-age sidecar list, lifecycle buckets, taskDocuments, series, pickup or expectation collection and owns no task-stage/action authority. The former lifecycle metrics and tool.completed liveness account belongs to the predecessor, not this current assembly function.

## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/agents_remember/observer/reducer_impl/_metrics.py`.

## Evidence


- Analytics assembles retained feeds and caller-derived overrides without sidecar ranking. [2]




### Repo-Internal References
