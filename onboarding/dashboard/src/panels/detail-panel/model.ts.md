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

`orderDecisionsNewestFirst` orders entries by parsed recorded time, newest first, independently of storage order. Equal timestamps retain input order. Unparseable timestamps follow parseable entries and retain their input order among invalid peers. The preview and whole-log reader call this shared helper; its comparator does not establish how a backend writer stores records.



### Form and bounded-reader model

`docForm` trusts a valid projected form and uses the model rule for an older cache: a master commanding masters is a sprint; any other master is a master; non-masters are tasks. `docIdentity` is the document path or repository-qualified ID, never a transient projection object. Grouping retains unknown statuses as waiting, excludes abandoned rows from live completion totals, and keeps the received task order.

Registers require a register heading and a parseable table; canonical slots are Judgment then Priority. Free-form Further notes exclude structured sections, recognized registers and a byte-identical objective repeat. `boundedText` checks both eight-line and character limits so a single huge paragraph cannot render unbounded. Review summaries read the supplied whole-round count rather than deriving it from a capped list. An ancestry chain uses qualified projected documents and a series fallback, never invented parents. MasterDocView includes optional nonGoals, acceptance, completedAt and waitsFor; seriesAsMasterDoc does not invent those absent fields. stepMarkStates emits one state per major step, not nested marks. A done parent stays done; otherwise an inProgress or done child promotes the parent to current before blocked/next fallback. taskStepProgress returns served done/total counts unchanged; full nested rendering stays with taskBlocks.

### Execution-graph and discarded-subtask view fields

MasterDocView retains the optional executionGraphView field for projected Order rendering on sprint and master pages. The series-only adapter does not fabricate that graph. MasterDocView also retains discardedCount and discardedSubTasks; seriesAsMasterDoc passes those served audit values through separately from live subTasks and completion. Its creation-ordering safety net and qualified task-reference resolution remain in this model.

### Conventions

Pure functions only — no React, no stores.

### Invariants And Boundaries

The cross-series `→` navigation guard belongs to `indexRows.tsx::resolveRowTarget`: only rows carrying linkedLifecycleId take that branch, after exact commanded-master resolution and before local slice fallback. This model retains pure key/label and document-resolution helpers.

### Todos

None recorded.

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

- Decision ordering is parsed-time descending, stable for ties and invalid peers, with invalid timestamps after valid ones. [3]




- displayedReaderDoc and displayedLeafDoc resolve projected selections through their shared lifecycle/series helpers without fabricating a leaf for an overview. [1]



- seriesAsMasterDoc adapts a series as a master, creation-orders its rows, passes discarded audit values and leaves absent document blocks absent. [2]



### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.
