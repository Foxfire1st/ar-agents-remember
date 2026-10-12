# dashboard/src/panels/detail-panel/model.ts

## Governing Overview

[panels/ overview](../overview.md)

## Purpose

The pure document-derivation model of the DetailPanel, extracted from
`DetailPanel.tsx` by the 260731-EFA-L8 split. Owns path/slug helpers, the
displayed-reader-doc resolution, the master-document view assembly
(`seriesAsMasterDoc`), sub-task key/label helpers, and form/grouping/ancestry/table/bounded-text mappings for the three fixed reader skeletons.

## Code Commentary

### Logic

Since 260815-DAG-L14 `docPathForTaskRef` resolves a typed `masterRef` against the FULL
projected task-document pool (a sprint commanded master lives in another folder, so
`sliceDocs` can never answer it); undefined when the target is not projected, which is the
caller signal to fall back to the row older behaviors.

`displayedReaderDoc` / `displayedLeafDoc` resolve which task document the reader
shows for a selection; `seriesAsMasterDoc` builds the master view from a series node
(the path whose rows carry `createdAt` for ordering).

### 260928-MIK-L126 Current Delta — Newest-First Decision Ordering

`orderDecisionsNewestFirst` orders decisions by parsed recorded time, newest first, with a
stable fallback: writers stamp `at` as ISO-8601, the finalizer prepends its newest record, and
storage order carries no invariant, so both the preview and the whole-log page order by time.
An unparseable stamp keeps its input position among its peers, never inventing an order.

- Decisions order newest-first by recorded time with a stable fallback. [3]

### Form and bounded-reader model

`docForm` trusts a valid projected form and uses the model rule for an older cache: a master commanding masters is a sprint; any other master is a master; non-masters are tasks. `docIdentity` is the document path or repository-qualified ID, never a transient projection object. Grouping retains unknown statuses as waiting, excludes abandoned rows from live completion totals, and keeps the received task order.

Registers require a register heading and a parseable table; canonical slots are Judgment then Priority. Free-form Further notes exclude structured sections, recognized registers and a byte-identical objective repeat. `boundedText` checks both eight-line and character limits so a single huge paragraph cannot render unbounded. Review summaries read the supplied whole-round count rather than deriving it from a capped list. An ancestry chain uses qualified projected documents and a series fallback, never invented parents.

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
- The master/series view assembly builds the master view from a series node. [2]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.


## 260815-DAG-L12 Execution Graph View

`MasterDocView` (the master-document view assembly) now includes the optional `executionGraphView` field (L12-R4/R5), so the sprint page can open the render-ready whole wave-grid graph from the projected master document in its Order own view.


## 260821-CLIVE Discarded-Subtask Model

`MasterDocView` now carries `discardedCount` and `discardedSubTasks`, and `seriesAsMasterDoc()`
passes both producer-owned values through without folding them into live subtasks or completion.
The existing execution-graph view, repository-qualified `masterRef` resolution, and ordering
behavior are unchanged.
