# dashboard/src/panels/sprint-graph/ — Sprint Graph View Overview

| Field | Value |
| --- | --- |
| sourceRoute | `dashboard/src/panels/sprint-graph/` |

## Governing Overview

[panels overview](../overview.md)

## Purpose

This directory presents a sprint's execution graph as a responsive wave grid. Each derived wave has a labeled section containing master boxes: segmented masters show one ellipsized ID-and-title line per leaf, while atomic masters show an atomic-unit lump without a leaf list. Each box displays its master title, projected frontier state, and textual predecessor labels with dependency reasons.

## Hot Path Summary

The sprint/master fixed reader's Order block (in `detail-panel/orderGraph.tsx`) shows bounded
producer-ordered rows and opens the complete `SprintGraphView` in an own view. The sprint-scoped
`CloseoutQueue` remains an independent taskReader section, including graphless sprints; opening the
graph does not own/reset that queue. The view groups `graphView.nodes` by received `waveIndex` and
renders one `GraphBox` per node with segment leaves or an atomic lump, frontier and textual reasons.
Rest has no active/master or focus/leaf mark; a qualified hover/focus changes visual marks without
re-deriving edges, waves or counts. Start at `SprintGraphView.tsx`, `styles.ts` and the shell tests.
The former always-inline `SprintGraphSection` integration is retired, not another page shell.

Start at `SprintGraphView.tsx` for rendering, `styles.ts` for layout declarations, and `SprintGraphPage.test.tsx` for reachability through the real `DetailPanel`.

## How It Is Built

- `SprintGraphView.tsx` exports the memoized `SprintGraphViewImpl`. `GraphBox` renders segment leaves or an atomic lump, a frontier badge, and predecessor titles and reasons.
- `styles.ts` exports `waveGridStyles` and `leafLineStyles`. The grid has three columns before wrapping and one column at viewport widths of 720px or less. Leaf lines use ellipsis with maximum widths of 30ch, 48ch at `sm`, and 72ch at `lg`, each bounded by the available width.
- The serving layer walks the persisted graph, derives waves, resolves predecessor endpoints, joins titles, and supplies master facts to the observer's render-ready graph builder. The resulting `TaskExecutionGraphView` carries the facts needed by this route.
- `SprintGraphView.test.tsx` covers independent zero-edge boxes, segmented masters across waves, predecessor reasons, frontier state attributes, responsive grid declarations, and ellipsis declarations. The declaration checks establish the CSS contract; jsdom does not evaluate media queries or character-unit sizing.
- `SprintGraphPage.test.tsx` renders the real `DetailPanel` to check graph and queue reachability, sprint scoping, graphless queue access, and mounted canonical-reset clearance. Its reset case seeds a matching authoritative store queue, establishes visible queue metadata and a candidate path, invokes the store reset while the panel remains mounted, then checks unfiltered store emptiness and disappearance of the derived UI.

The document-rendering sibling is `_execution_graph_lines` in `tasks/render.py`: it emits a deterministic Mermaid diagram alongside machine-readable node, dependency, and derived-wave lists. `dev/sprintGraphPage.tsx` supplies a deterministic mounted evidence surface by applying a seeded projection and opening the real `DetailPanel` on the sprint document.

## Invariants And Boundaries

The route consumes projected facts without joining raw task references or deriving waves or frontier states. It groups and orders existing wave indices for presentation; CSS determines box placement rather than a client graph-layout algorithm.

Pure CSS grid with textual dependency labels is the [recorded L12-R3 rendering choice](/home/firefox/projects/ar-coordination/tasks/agents-remember/260815_dependency-aware-sprint-execution/12_visual-graph-rendering.md#decision-log). Ready-made rendering alternatives were evaluated, and `@xyflow/react` was proposed but deferred; it is not declared in the current dashboard package. This historical authority link is not a code-source citation and does not authorize installing the proposed dependency.

The narrow layout preserves box grouping, wave order, and predecessor information while changing the grid's column count. Frontier styling supports the projected landed, ready, waiting, in-flight, and abandoned states.

Scenario reset uses the canonical dashboard-store reset rather than a second reset owner. The mounted reset proof must establish a visible matching queue before reset and verify both store and UI clearance afterward. This is dev/test scenario infrastructure; it supplies no production queue-ingestion, scheduling, or lifecycle authority.

## Evidence

- The sprint reader retains its scoped CloseoutQueue independently of the optional Order preview and graph own view. [3]

- The wave-grid component groups projected nodes into wave rows, preserves node order within each wave, and renders segment or lump boxes with frontier and predecessor information. [1]
- The exported responsive layout contracts specify three columns, a narrow single column, and viewport-growing ellipsis caps; frontier styling includes abandoned. The proposed graph dependency remains undeclared. [2]
- The shell suite proves graph/queue reachability, sprint scoping, graphless queue access, and mounted canonical-reset clearance. Component tests pin the rendering and responsive declarations; the canonical store reset clears closeout queues. [4]
- The render-ready wire model this route consumes includes nodes, wave indices, frontier states, leaf titles, and predecessor reasons; current serving and observer callers construct those projected facts. [5]
- The deterministic Mermaid document-diagram sibling of this view also preserves machine-readable nodes, dependencies, and derived waves. [6]
- The one-shot mounted-UI evidence surface applies a seeded projection and opens the real sprint detail panel. [7]
