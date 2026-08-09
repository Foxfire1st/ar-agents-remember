# mcp/src/agents_remember/observer/series_tokens.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/observer/series_tokens.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-01T15:10+02:00                     |
| lastVerifiedCommitHash | `2dea095cd68454a7a68893e37c07dbd8daa86d32` |
| lastVerifiedCommitDate | 2026-08-09T18:00:39+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation found; behavior is defined by repo projection contracts and tests. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The reducer returns an enriched `WorkspaceProjection` from the lifecycle projection path. | "class WorkspaceProjection(BaseModel):" | mcp/src/agents_remember/observer/projection.py:992-992 |
| The reducer module defines `build_analytics` for analytics enrichment. | "def build_analytics(" | mcp/src/agents_remember/observer/reducer_impl/_metrics.py:129-129 |
| `SeriesNode` exposes the served `seriesTokenTotal` field. | `seriesTokenTotal` | mcp/src/agents_remember/observer/projection.py:709-709 |
| The projection test module includes a `seriesTokenTotal` regression case. | `seriesTokenTotal` | mcp/tests/test_observer_projection.py:681-681 |

## Cross-Repo References

No meaningful cross-repo references found; this helper consumes the current
agents-remember workspace projection only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo dependency; aggregate tokens are computed from already-projected lifecycle and task-document nodes. | n/a | n/a |

## Update History

- 2026-08-04T12:41:53+00:00 — 260731-EFA-L6 S18-B09 curator: split the reducer return and analytics call/order claims onto their frozen-source owners; the landing provenance mismatch remains an explicit Tier-3 item.
- 2026-08-02T16:20:23+02:00 — 260731-EFA-L6 curator: repaired the remaining history citation for the
  current `SeriesNode` and `seriesTokenTotal` projection source; the source behavior and card body
  remain unchanged.

- 2026-08-01T15:10+02:00 — 260731-EFA-L4 curator (citation pass): re-verified the three reference
  citations after source movement; the reducer and observer-projection references were repaired.
  The current `SeriesNode` and `seriesTokenTotal` projection source (cit:([`SeriesNode`, `seriesTokenTotal`], mcp/src/agents_remember/observer/projection.py:685-711)) was re-read and left unchanged.
  Every body claim was re-read against the source and still holds, so no prose changed.
  Squared two ragged frontmatter cells.
- 2026-08-01T10:40+02:00 — 260731-EFA-L4 curator (citation pass): the `projection.py` citation was
  stale after source movement; the range was repaired and the field line called out. Also aligned
  `lastUpdated` with this entry. No body text changed.
- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired the two approximate cross-file citations
  flagged by the previous entry. The reducer and observer-projection assertions now read back
  verbatim, including the 100+50=150 token total and the doc-less `03_c.md` row.

- 2026-07-31T16:35+02:00 — No content impact: the only change to
  `mcp/src/agents_remember/observer/series_tokens.py` since the L2 base commit is the whole-tree
  `ruff format` pass in `00e8379`, which re-wrapped 3 line(s), touching only magic trailing
  commas. Checked by parsing both revisions and comparing the abstract syntax trees (identical)
  and the comment tokens (identical), so no symbol, signature, default, decorator, control-flow
  branch, docstring, or assertion this card describes has moved, and every claim this card makes
  about its own source still holds. Noted while checking: the references table also cites line
  ranges inside `reducer.py`, `test_observer_projection.py`; those ranges shifted because this
  task edited those files, so treat the cited numbers as approximate and the linked cards as
  authoritative.

- 2026-07-31T00:00+02:00 — 260731-EFA-L2 attestation: this file was touched ONLY by the
  whole-tree `ruff format` pass (commit `00e8379`) — line reflow, no behaviour, contract,
  structure or responsibility change. The sidecar was re-read against the current source and
  every claim in it still holds, so it was deliberately not rewritten. Verification metadata
  pinned until closeout stamps the L2 commit.
- 2026-06-26T20:18+02:00 — Created for Task 21: documents the series-token aggregate join from master `subTasks[]` rows to sibling leaf task documents and their lifecycle token totals. Verification metadata left blank until closeout stamps the first code commit for this new file.
