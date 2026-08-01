# mcp/src/agents_remember/observer/series_tokens.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/observer/series_tokens.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-01T15:10+02:00                     |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d` |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00                  |
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
| The reducer calls this helper after lifecycle projection and before `build_analytics`, then serves the enriched series list. | L155-L169 | [reducer.py](agents-remember/mcp/src/agents_remember/observer/reducer.py) |
| `SeriesNode` exposes the served `seriesTokenTotal` field that this helper writes. | L662-L688 (`seriesTokenTotal` L684) | [projection.py](agents-remember/mcp/src/agents_remember/observer/projection.py) |
| Projection tests prove two linked leaf lifecycles sum to the master `seriesTokenTotal` and missing rows contribute nothing. | L713-L786 | [test_observer_projection.py](agents-remember/mcp/tests/test_observer_projection.py) |

## Cross-Repo References

No meaningful cross-repo references found; this helper consumes the current
agents-remember workspace projection only.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repo dependency; aggregate tokens are computed from already-projected lifecycle and task-document nodes. | n/a | n/a |

## Update History

- 2026-08-01T15:10+02:00 — 260731-EFA-L4 curator (citation pass): re-verified the three reference
  citations; two were broken and are repaired. `reducer.py` L148-L162 → **L155-L169** — the same
  window the 17:20 entry below describes, moved +7 by later edits to that file: `_attach_gates`
  closes lifecycle projection at L155, `attach_series_token_totals` is called at L163, and
  `build_analytics` spans L164-L169 consuming `series=series_nodes` at L166.
  `test_observer_projection.py` L690-L763 → **L713-L786** —
  `test_series_token_total_sums_linked_leaf_lifecycles` in `WorkspaceTests`, with LC1 at 100 tokens
  (L722), LC2 at 50 (L733), the doc-less `03_c.md` row at L772-L774 and the 150 assertion at L786;
  the old range ended 23 lines before that assertion, so neither number it cites was inside it.
  `projection.py` `SeriesNode` L662-L688 (`seriesTokenTotal` L684) was re-read and left unchanged.
  Every body claim was re-read against the 43-line source and still holds, so no prose changed.
  Squared two ragged frontmatter cells.
- 2026-08-01T10:40+02:00 — 260731-EFA-L4 curator (citation pass): the `projection.py` citation was
  stale by a much larger margin than the rest of the tree. `SeriesNode` L497-L523 was correct
  against an older commit (`b7d38a7`); the class is now L662-L688 with `seriesTokenTotal` at L684,
  so the range is repaired and the field line called out. Also aligned `lastUpdated` with this
  entry — it had lagged behind the 2026-07-31T17:20 entry below. No body text changed.
- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired the 2 approximate cross-file citations
  the previous entry flagged, so the numbers are exact again. `reducer.py` L148-L162 is the real
  window — `_attach_gates` closes lifecycle projection at L148, `attach_series_token_totals` is
  called at L156, and `build_analytics` consumes `series=series_nodes` at L157-L162.
  `test_observer_projection.py` L690-L763 is `test_series_token_total_sums_linked_leaf_lifecycles`
  in `WorkspaceTests`, which asserts 100+50=150 across LC1/LC2 with a third `subTasks` row
  (`03_c.md`) that has no task document and contributes nothing. Both ranges read back verbatim.

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
