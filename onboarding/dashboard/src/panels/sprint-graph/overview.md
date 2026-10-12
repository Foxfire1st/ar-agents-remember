# dashboard/src/panels/sprint-graph/ — Sprint Graph View Overview

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| sourceRoute            | `dashboard/src/panels/sprint-graph/`             |

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

The sprint/master fixed reader's Order block (in `detail-panel/orderGraph.tsx`) shows bounded
producer-ordered rows and opens the complete `SprintGraphView` in an own view. The sprint-scoped
`CloseoutQueue` remains an independent taskReader section, including graphless sprints; opening the
graph does not own/reset that queue. The view groups `graphView.nodes` by received `waveIndex` and
renders one `GraphBox` per node with segment leaves or an atomic lump, frontier and textual reasons.
Rest has no active/master or focus/leaf mark; a qualified hover/focus changes visual marks without
re-deriving edges, waves or counts. Start at `SprintGraphView.tsx`, `styles.ts` and the shell tests.
The former always-inline `SprintGraphSection` integration is retired, not another page shell.

## Route Model

- `SprintGraphView.tsx` — the memoized wave-grid component (`SprintGraphViewImpl` +
  `GraphBox`); deterministic wave grouping from the server contract.
- `styles.ts` — the exported `waveGridStyles` (≤3 boxes/row, narrow single-column) and
  `leafLineStyles` (ch-based ellipsis caps stepped up at sm/lg), pinned by tests.
- `SprintGraphView.test.tsx` — component tests: zero-edge, segmented-master, frontier
  badges, narrow declarations, ellipsis contract (L12-R7 scenario evidence).
- `SprintGraphPage.test.tsx` — shell-level reachability (L12-R5) plus scenario-reset proof: the real
  `DetailPanel` opens the graph from Order and retains the independently sprint-scoped `CloseoutQueue`, keeps the queue reachable
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

## Evidence

### Repo-Internal References

- The wave-grid component groups projected nodes into wave rows. [1]
- The exported responsive layout contracts. [2]

- The sprint reader retains its scoped CloseoutQueue independently of the optional Order preview and graph own view. [3]

- The shell suite proves graph/queue reachability, graphless queue access, and mounted canonical-reset clearance. [4]
- The render-ready wire model this route consumes. [5]
- The deterministic mermaid document-diagram sibling of this view. [6]
- The one-shot mounted-UI evidence surface. [7]
