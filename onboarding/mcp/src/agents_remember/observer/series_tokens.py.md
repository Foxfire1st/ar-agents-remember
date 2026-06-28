# mcp/src/agents_remember/observer/series_tokens.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/observer/series_tokens.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-26T20:18+02:00                     |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`                                         |
| lastVerifiedCommitDate |                                            2026-06-28T18:49:06+02:00|
| governingOverview      | `overview.md`                              |

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

## Docs References

No relevant external documentation found after checking the observer projection
scope; this file implements an internal projection rollup.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found; behavior is defined by repo projection contracts and tests. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The reducer calls this helper after lifecycle projection and before `build_analytics`, then serves the enriched series list. | L118-L150 | [reducer.py](agents-remember/mcp/src/agents_remember/observer/reducer.py) |
| `SeriesNode` exposes the served `seriesTokenTotal` field that this helper writes. | L497-L523 | [projection.py](agents-remember/mcp/src/agents_remember/observer/projection.py) |
| Projection tests prove two linked leaf lifecycles sum to the master `seriesTokenTotal` and missing rows contribute nothing. | L420-L490 | [test_observer_projection.py](agents-remember/mcp/tests/test_observer_projection.py) |

## Cross-Repo References

No meaningful cross-repo references found; this helper consumes the current
agents-remember workspace projection only.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repo dependency; aggregate tokens are computed from already-projected lifecycle and task-document nodes. | n/a | n/a |

## Update History

- 2026-06-26T20:18+02:00 — Created for Task 21: documents the series-token aggregate join from master `subTasks[]` rows to sibling leaf task documents and their lifecycle token totals. Verification metadata left blank until closeout stamps the first code commit for this new file.
