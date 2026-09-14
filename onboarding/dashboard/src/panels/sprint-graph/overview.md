# dashboard/src/panels/sprint-graph/ — Sprint Graph View Overview

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| sourceRoute            | `dashboard/src/panels/sprint-graph/`             |
| doc_type               | `route-local-overview`                           |
| lastUpdated | 2026-09-14T20:00+02:00 |
| lastVerifiedCommitHash | `bb65a2073228c5e143b055a470f39c6c9e2f4d9d`       |
| lastVerifiedCommitDate | 2026-09-14T19:36:04+02:00|
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
| The wave-grid component groups projected nodes into wave rows. | `SprintGraphView` | dashboard/src/panels/sprint-graph/SprintGraphView.tsx:107-107 |
| The exported responsive layout contracts. | `waveGridStyles`; `leafLineStyles` | dashboard/src/panels/sprint-graph/styles.ts:7-12; dashboard/src/panels/sprint-graph/styles.ts:80-90 |
| The master reader mounts the scoped queue independently of its optional graph section. | `MasterOverview`; `SprintGraphSection` | dashboard/src/panels/detail-panel/taskReader.tsx:189-266; dashboard/src/panels/detail-panel/taskReader.tsx:270-277; dashboard/src/panels/detail-panel/taskReader.tsx:246-253 |
| The shell suite proves graph/queue reachability, graphless queue access, and mounted canonical-reset clearance. | "sprint page shell (L12-R5)" | dashboard/src/panels/sprint-graph/SprintGraphPage.test.tsx:53-174 |
| The render-ready wire model this route consumes. | "export interface TaskExecutionGraphView {" | dashboard/src/types/projection.ts:720-720 |
| The deterministic mermaid document-diagram sibling of this view. | `_execution_graph_lines` | mcp/src/agents_remember/tasks/render.py:216-257 |
| The one-shot mounted-UI evidence surface. | `SprintGraphPage` | dashboard/src/dev/sprintGraphPage.tsx:16-21 |

## Update History

- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (drift re-verification): the
  `dashboard/src/panels/sprint-graph/` route changed since the recorded verification commit. Re-read
  the card against the frozen on-disk source and re-checked its claims and cited ranges: nothing
  this card asserts is falsified by the change, so no wording changed. Verification metadata remains
  closeout-owned; no verification stamp advanced.
- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (citation pass): re-derived the source ranges of 1
  claim(s) whose anchor no longer sat in its cited range and normalised 4 further range(s) in this
  card from their anchors against the frozen source snapshot (`agents-remember memory-citations
  --fix --document`, snapshot 188b8ecd). 1 claim(s) were declined as ambiguous or not the subject
  and were left for a reading curator. No claim wording changed; every rewritten range was read back
  at its current position. Verification metadata remains closeout-owned.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `_execution_graph_lines` repointed to mcp/src/agents_remember/tasks/render.py:216-257. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.


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
