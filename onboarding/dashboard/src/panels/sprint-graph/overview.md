# dashboard/src/panels/sprint-graph/ — Sprint Graph View Overview

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| sourceRoute            | `dashboard/src/panels/sprint-graph/`             |
| doc_type               | `route-local-overview`                           |
| lastUpdated            | 2026-08-20T10:45+02:00                           |
| lastVerifiedCommitHash | `b7f2c8e2c7020642780e2c9b997ffb035a782e62`       |
| lastVerifiedCommitDate | 2026-08-20T10:42:29+02:00                        |
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[panels/ overview](../overview.md)

## Purpose

The sprint execution graph wave-grid view (260815-DAG-L12 R2/R6): one row per derived
wave; within a wave, boxes in a grid of at most 3 per row before wrapping. Each box shows
the master title header and one ellipsized leaf line per leaf (the character range grows
with the viewport); an atomic master renders as a lump box with no leaf list. Edges render
as textual dependency labels under each box — the documented pure-CSS fallback chosen in
the L12-R3 decision (no ready-made layout library installed). The narrow/phone layout
collapses the grid to a single wave-ordered column while preserving box grouping and
predecessor info. The backend projects a render-ready per-node model
(`executionGraphView`), so this route renders projected facts verbatim and never joins raw
refs or re-derives waves.

## Hot Path Summary

`SprintGraphSection` (in `detail-panel/taskReader.tsx`) mounts `SprintGraphView` plus the
sprint-scoped `CloseoutQueue` on the sprint page; the view groups `graphView.nodes` by
`waveIndex` into rows and renders one `GraphBox` per node — a segment box with leaf lines
or an atomic lump, a frontier badge, and textual predecessor labels with reasons. Start at
`SprintGraphView.tsx` for the component, `styles.ts` for the declarative grid/leaf-line
contracts, and `SprintGraphPage.test.tsx` for the shell-level reachability proof.

## Route Model

- `SprintGraphView.tsx` — the memoized wave-grid component (`SprintGraphViewImpl` +
  `GraphBox`); deterministic wave grouping from the server contract.
- `styles.ts` — the exported `waveGridStyles` (≤3 boxes/row, narrow single-column) and
  `leafLineStyles` (ch-based ellipsis caps stepped up at sm/lg), pinned by tests.
- `SprintGraphView.test.tsx` — component tests: zero-edge, segmented-master, frontier
  badges, narrow declarations, ellipsis contract (L12-R7 scenario evidence).
- `SprintGraphPage.test.tsx` — shell-level reachability (L12-R5): the real DetailPanel
  mounts the graph view AND the sprint-scoped CloseoutQueue; fails if a panel is exported
  but unmounted.

## Invariants And Boundaries

- The route renders projected facts only; no raw-path joins, no wave re-derivation, no
  layout algorithm (coordinates come from the server-derived `waveIndex`).
- Ready-made rendering was evaluated and the documented fallback chosen (pure CSS grid +
  textual dependency labels); `@xyflow/react` was proposed but NOT installed (L12-R3
  decision).
- The narrow layout preserves box grouping and predecessor info; only the column count
  changes.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The wave-grid component groups projected nodes into wave rows. | `SprintGraphView` | dashboard/src/panels/sprint-graph/SprintGraphView.tsx:81-107 |
| The exported responsive layout contracts. | `waveGridStyles`; `leafLineStyles` | dashboard/src/panels/sprint-graph/styles.ts:7-12; dashboard/src/panels/sprint-graph/styles.ts:77-87 |
| The sprint page mounts the view plus the scoped queue. | `SprintGraphSection` | dashboard/src/panels/detail-panel/taskReader.tsx:220-233 |
| The render-ready wire model this route consumes. | `TaskExecutionGraphView` | dashboard/src/types/projection.ts:561-565 |
| The deterministic mermaid document-diagram sibling of this view. | `_execution_graph_lines` | mcp/src/agents_remember/tasks/render.py:173-213 |
| The one-shot mounted-UI evidence surface. | `SprintGraphPage` | dashboard/src/dev/sprintGraphPage.tsx:16-20 |

## Update History

- 2026-08-20T10:45+02:00 — Created for 260815-DAG-L12 (R2/R3/R5/R6): the sprint graph

wave-grid route — ≤3 boxes per row, ellipsized leaf lines, atomic lumps, textual

predecessor labels, narrow single-column fallback, and the mounted sprint-page surface.

Verified at code commit b7f2c8e2.



- 2026-08-20T10:45+02:00 — Created for 260815-DAG-L12 (R2/R3/R5/R6): the sprint graph
  wave-grid route — ≤3 boxes per row, ellipsized leaf lines, atomic lumps, textual
  predecessor labels, narrow single-column fallback, and the mounted sprint-page surface.
  Verified at code commit b7f2c8e2.
