# mcp/src/agents_remember/observer/series_tokens.py

## Governing Overview

[observer/overview.md](overview.md)

## Purpose

Attaches aggregate token totals to projected series masters by summing the tokens
from their linked leaf lifecycles. This keeps the reducer's `Analytics.series`
surface useful as a master-level readout without changing per-lifecycle token
gauges.

## Code Commentary

### Logic

`attach_series_token_totals(series, task_documents, lifecycles)` first indexes
lifecycle token totals by lifecycle id, then indexes non-master `TaskDocNode`s by
their series directory and markdown filename. For each `SeriesNode`, it walks the
master `subTasks[]`, finds the sibling leaf task doc by `ref.file`, and adds that
doc's bound lifecycle token count when one exists. The return value is a new list
of `SeriesNode` copies with `seriesTokenTotal` set.

### Conventions

The join key intentionally matches the master row's markdown `file` field against
the projected leaf task document path converted from `.json` to `.md`. No file I/O
happens here; all inputs are already-projected nodes.

### Invariants And Boundaries

- Master task docs are skipped when building the leaf-doc index, so a master never
  contributes its own synthetic reader row to the aggregate.
- Missing leaf docs and unbound leaf docs contribute zero. The aggregate is an
  observed lifecycle-token sum, not a declaration from the master.
- The helper returns copied `SeriesNode`s and does not mutate the input list.

### Todos

No known local todos.

## Evidence

### Docs References

No relevant external documentation found after checking the observer projection
scope; this file implements an internal projection rollup.

No relevant external documentation found; behavior is defined by repo projection contracts and tests.

### Repo-Internal References

- The reducer returns an enriched `WorkspaceProjection` from the lifecycle projection path. [1]
- The reducer module defines `build_analytics` for analytics enrichment. [2]
- SeriesNode exposes the served seriesTokenTotal field, defaulting to zero. [3]

### Cross-Repo References

No meaningful cross-repo references found; this helper consumes the current
agents-remember workspace projection only.

No cross-repo dependency; aggregate tokens are computed from already-projected lifecycle and task-document nodes.
