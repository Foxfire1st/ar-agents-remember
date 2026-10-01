# dashboard/src/panels/detail-panel/state.ts

## Governing Overview

[panels/ overview](../overview.md)

## Purpose

The selection-state hook of the DetailPanel, extracted from `DetailPanel.tsx` by the
260731-EFA-L8 split. `useDetailPanelState` resolves the selected task/lifecycle/series and derives
the canonical viewed-task document reference, optional compatibility leaf key, and direct document
set from props.

## Code Commentary

Since 260815-DAG-L14 `useDetailPanelState` exposes `docPathForRef` — resolves a sub-task row typed `masterRef` against the full projected task-document pool and dispatches it through `jump(taskDocSelectionKey(...))`, the same mechanism the parent-series crumb uses.

### Logic

The pure resolvers (`resolveSelectedTaskDoc`, `resolveLifecycleId`,
`resolveDirectDocs`, `isRootTaskSelection`, `resolveSelectedSeries`,
`resolveViewedLeafKey`) narrow the prop selection; `taskDocumentRefForDoc` supplies the primary
viewed-task identity passed through `onViewTask`. The hook memoizes the derived state the render
tree consumes.

### Conventions

State derivation is pure and unit-testable.

### Invariants And Boundaries

The hook never mutates server data; it only projects the current selection.

### Todos

None recorded.

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

- The state hook and its pure resolvers. [1]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.
