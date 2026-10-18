# mcp/src/agents_remember/observer/reducer_impl/_metrics.py

## Governing Overview

[overview](../overview.md)

## Purpose

Pure analytical assembly over already-read retained inputs. Verification-age histogram and stalest-sidecar ranking functions are removed. Native task stage/activity counts belong to task-entry production; the old lifecycle `_metrics` function is not present here. This module computes no token aggregate.

## Code Commentary

- `build_analytics`

Analytics retains supplied drift, setup, route coverage, tool reports and ledgers, with caller-derived attention and Engine Room process surfaces. It emits no verification-age sidecar list, lifecycle buckets, taskDocuments, series, pickup or expectation collection and owns no task-stage/action authority. The former lifecycle metrics and tool.completed liveness account belongs to the predecessor, not this current assembly function.

## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/agents_remember/observer/reducer_impl/_metrics.py`.

## Evidence

- Historical predecessor only: lifecycle metrics derived vocabulary-owned counts without age histograms; that `_metrics` target is no longer in this module. [1]
- Analytics assembles retained feeds and caller-derived overrides without sidecar ranking. [2]



### Repo-Internal References
