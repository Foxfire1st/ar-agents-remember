# dashboard/src/panels/detail-panel/model.ts

## Governing Overview

[panels/ overview](../overview.md)

## Purpose

The pure document-derivation model of the DetailPanel, extracted from
`DetailPanel.tsx` by the 260731-EFA-L8 split. Owns path/slug helpers, the
displayed-reader-doc resolution, the master-document view assembly
(`seriesAsMasterDoc`, `masterDocWithSeriesTokens`), and sub-task key/label helpers.

## Code Commentary

### Logic

Since 260815-DAG-L14 `docPathForTaskRef` resolves a typed `masterRef` against the FULL
projected task-document pool (a sprint commanded master lives in another folder, so
`sliceDocs` can never answer it); undefined when the target is not projected, which is the
caller signal to fall back to the row older behaviors.

`displayedReaderDoc` / `displayedLeafDoc` resolve which task document the reader
shows for a selection; `seriesAsMasterDoc` builds the master view from a series node
(the path whose rows carry `createdAt` for ordering); `masterDocWithSeriesTokens`
merges series tokens into a master document.

### Conventions

Pure functions only — no React, no stores.

### Invariants And Boundaries

The cross-series `→` jump is reachable only when `linkedLifecycleId` is present on a
`TaskSubTaskRefNode`; this module keeps that guard.

### Todos

None recorded.

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

- The reader-doc resolution entry points. [1]
- The master/series view assembly. [2]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.


## 260815-DAG-L12 Execution Graph View

`MasterDocView` (the master-document view assembly) now includes the optional `executionGraphView` field (L12-R4/R5), so the sprint page can render the render-ready wave-grid graph directly from the projected master document.


## 260821-CLIVE Discarded-Subtask Model

`MasterDocView` now carries `discardedCount` and `discardedSubTasks`, and `seriesAsMasterDoc()`
passes both producer-owned values through without folding them into live subtasks or completion.
The existing execution-graph view, repository-qualified `masterRef` resolution, ordering, and token
rollup behavior are unchanged.
