# dashboard/src/panels/sprint-graph/ — Sprint Graph View Overview

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| sourceRoute            | `dashboard/src/panels/sprint-graph/`             |
| doc_type               | `route-local-overview`                           |
| lastUpdated | 2026-09-05T06:21+00:00 |
| lastVerifiedCommitHash | `dc03c64a91947cee470622c560c516854eec86b5`       |
| lastVerifiedCommitDate | 2026-08-30T17:41:53+02:00|
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
- `SprintGraphPage.test.tsx` — shell-level reachability (L12-R5) plus scenario-reset proof: the real
  `DetailPanel` mounts the graph view and sprint-scoped `CloseoutQueue`, keeps the queue reachable
  for graphless sprints, and proves the canonical dev/test reset clears both a seeded authoritative
  queue and its mounted derived UI without introducing a second reset owner.

## Invariants And Boundaries

- The route renders projected facts only; no raw-path joins, no wave re-derivation, no
  layout algorithm (coordinates come from the server-derived `waveIndex`).
- Ready-made rendering was evaluated and the documented fallback chosen (pure CSS grid +
  textual dependency labels); `@xyflow/react` was proposed but NOT installed (L12-R3
  decision).
- The narrow layout preserves box grouping and predecessor info; only the column count
  changes.
- Mounted reset proof must begin with a visible matching queue, invoke the canonical store reset
  while `DetailPanel` remains mounted, and assert both unfiltered store emptiness and derived UI
  absence. This is dev/test scenario infrastructure; production queue ingestion, filtering,
  scheduling, and lifecycle authority remain unchanged.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The wave-grid component groups projected nodes into wave rows. | `SprintGraphView` | dashboard/src/panels/sprint-graph/SprintGraphView.tsx:81-107 |
| The exported responsive layout contracts. | `waveGridStyles`; `leafLineStyles` | dashboard/src/panels/sprint-graph/styles.ts:7-12; dashboard/src/panels/sprint-graph/styles.ts:77-87 |
| The master reader mounts the scoped queue independently of its optional graph section. | `MasterOverview`; `SprintGraphSection` | dashboard/src/panels/detail-panel/taskReader.tsx:167-242; dashboard/src/panels/detail-panel/taskReader.tsx:246-253 |
| The shell suite proves graph/queue reachability, graphless queue access, and mounted canonical-reset clearance. | "sprint page shell (L12-R5)" | dashboard/src/panels/sprint-graph/SprintGraphPage.test.tsx:53-174 |
| The render-ready wire model this route consumes. | "export interface TaskExecutionGraphView {" | dashboard/src/types/projection.ts:721-723 |
| The deterministic mermaid document-diagram sibling of this view. | `_execution_graph_lines` | mcp/src/agents_remember/tasks/render.py:173-213 |
| The one-shot mounted-UI evidence surface. | `SprintGraphPage` | dashboard/src/dev/sprintGraphPage.tsx:16-20 |

## Update History


- 2026-09-05T06:21+00:00 — Re-read the affected source declarations and repaired citation ranges shifted by CCR additions. Preserved the route contract and existing history; literal anchors identify the exact current construct where shared identifiers were ambiguous.

- 2026-08-26T10:44:52+02:00 — No route impact: refreshed master-reader and projection-type anchors after component/source movement; the sprint graph and independently reachable queue contract are unchanged.

- 2026-08-24T12:59+02:00 — 260821-DAGQC-L3 curator: added the mounted forcing boundary for the
  canonical dev/test reset: a visible seeded queue clears from both authoritative store state and
  the real `DetailPanel`-derived surface while the component remains mounted. Production queue
  behavior is unchanged, and no second reset authority was introduced. Verification metadata
  remains pinned until governed closeout stamps the code commit.

- 2026-08-20T10:45+02:00 — Created for 260815-DAG-L12 (R2/R3/R5/R6): the sprint graph

wave-grid route — ≤3 boxes per row, ellipsized leaf lines, atomic lumps, textual

predecessor labels, narrow single-column fallback, and the mounted sprint-page surface.

Verified at code commit b7f2c8e2.



- 2026-08-20T10:45+02:00 — Created for 260815-DAG-L12 (R2/R3/R5/R6): the sprint graph
  wave-grid route — ≤3 boxes per row, ellipsized leaf lines, atomic lumps, textual
  predecessor labels, narrow single-column fallback, and the mounted sprint-page surface.
  Verified at code commit b7f2c8e2.
