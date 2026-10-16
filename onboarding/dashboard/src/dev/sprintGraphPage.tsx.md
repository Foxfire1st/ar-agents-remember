# dashboard/src/dev/sprintGraphPage.tsx

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

A deterministic mounted-UI surface for the sprint execution graph (260815-DAG-L12 R7
evidence): the real sprint page (the Operations DetailPanel) opened against seeded
sprint-graph data, so a reviewer can screenshot the mounted wave-grid view and its closeout
queue at one URL (`/dev/sprint-graph`).

## Code Commentary

### Logic

SprintGraphPage seeds native tasks and SPRINT_GRAPH_QUEUE, then selects the qualified entry key in the real DetailPanel. These deterministic DEV graph/queue inputs are not mutable scheduling or lifecycle authority.

### Invariants And Boundaries

- Dev-only route; the store snapshot is applied on mount and never persisted.
- One-shot reviewer surface — the L12-R7 screenshot leg for a browser-capable seat.

## Evidence

### Repo-Internal References

- The dev sprint-graph page. [1]
- The page seeds the native sprint entry and its closeout queue. [2]
- The real page surface rendered. [3]
- The dev route dispatch. [4]

### Cross-Repo References

No cross-repository implementation source governs this file.
