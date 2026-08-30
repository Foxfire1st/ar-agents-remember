# dashboard/src/panels/sprint-graph/SprintGraphView.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/sprint-graph/SprintGraphView.tsx` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-20T10:45+02:00                           |
| lastVerifiedCommitHash | `dc03c64a91947cee470622c560c516854eec86b5`       |
| lastVerifiedCommitDate | 2026-08-30T17:41:53+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[sprint-graph overview](overview.md)

## Purpose

The sprint execution graph wave-grid view (260815-DAG-L12 R2/R6). The backend projects a
render-ready per-node model (`executionGraphView`) — kind, master ref + title, leaf ids +
titles, derived wave index, frontier state, execution nature, and predecessors with
reasons — so this component renders projected facts verbatim and never joins raw refs or
re-derives waves.

## Code Commentary

### Logic

`SprintGraphViewImpl` groups `graphView.nodes` (already ordered by derived wave then node
order — the server contract) into a `Map<waveIndex, nodes>`, sorts the rows by wave, and
renders one `<section class="wave">` per wave with a `Wave {n}` heading and a
`waveGrid` div of `GraphBox` elements. `GraphBox` renders the master title header with a
frontier-state badge (`data-frontier` for styling), then either a leaf list (`node.kind ===
"segment"` — one ellipsized `leafIds[i] — leafTitles[i]` line per leaf) or an atomic lump
(`data-testid="graph-lump"`, "atomic unit" — no leaf list), then the textual predecessor
labels (`← {predecessorTitle} — {reason}`, keyed by ref) when present. The component is
memoized; no layout algorithm lives here (coordinates come from the server-derived
`waveIndex` — the documented L12-R3 fallback).

### Conventions

- Deterministic render: nodes arrive ordered; the component preserves that order.
- Test-surface attributes (`data-testid`, `data-node`, `data-frontier`) are part of the
  component contract for the L12-R7 mounted-UI proof.

### Invariants And Boundaries

- Never joins raw refs to titles; never re-derives waves or frontier state.
- A node without predecessors renders no label list (zero-edge graphs show independent
  boxes).

### Todos

None.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The wave-grid component and box renderer. | `SprintGraphView` | dashboard/src/panels/sprint-graph/SprintGraphView.tsx:35-107 |
| The wire model consumed. | `TaskExecutionGraphView` | dashboard/src/types/projection.ts:656-658 |
| The responsive grid/leaf contracts. | `waveGridStyles`; `leafLineStyles` | dashboard/src/panels/sprint-graph/styles.ts:7-12; dashboard/src/panels/sprint-graph/styles.ts:77-87 |
| The component forcing suite. | `SprintGraphView` (describe) | dashboard/src/panels/sprint-graph/SprintGraphView.test.tsx:102-163 |
| The sprint page that mounts it. | `SprintGraphSection` | dashboard/src/panels/detail-panel/taskReader.tsx:246-253 |

## Cross-Repo References

No cross-repository implementation source governs this file.

## Update History

- 2026-08-20T10:45+02:00 — Created for 260815-DAG-L12 (R2/R6): the wave-grid sprint graph

view — wave rows, ≤3 boxes per row, ellipsized leaf lines, atomic lumps, textual

predecessor labels, deterministic from the server contract. Verified at code commit

b7f2c8e2.



- 2026-08-20T10:45+02:00 — Created for 260815-DAG-L12 (R2/R6): the wave-grid sprint graph
  view — wave rows, ≤3 boxes per row, ellipsized leaf lines, atomic lumps, textual
  predecessor labels, deterministic from the server contract. Verified at code commit
  b7f2c8e2.
