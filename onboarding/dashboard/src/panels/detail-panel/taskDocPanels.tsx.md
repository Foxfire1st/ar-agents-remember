# dashboard/src/panels/detail-panel/taskDocPanels.tsx

## Governing Overview

[panels/ overview](../overview.md)

## Purpose

The task-document panel composition of the DetailPanel, extracted from
`DetailPanel.tsx` by the 260731-EFA-L8 split. `TaskDocumentPanel` renders the selected
task document body (or empty/series variants), `EmptyDetailPanel` the no-selection
state, and `SeriesDetailPanel` the series-as-master reader.


## 260831-CCR-L23 Task-Artifact Target Import

The `NotesReaderTarget` type import moved from the notes-reader module to the
shared `dashboard/src/data/taskArtifacts.ts` union (aliased as
`NotesReaderTarget`); the `onOpenNotes` callback forwarded through
`TaskDocBody`/`SeriesDetailPanel` now carries the kind-tagged artifact
target.

## Code Commentary

Since 260815-DAG-L14 `TaskDocBody` and `SeriesDetailPanel` thread `docPathForRef` from panel state into the task readers so typed `masterRef` sprint rows can open their commanded master document.

### Logic

`TaskDocBody` maps the displayed document kind to the reader surface; the panel
variants wire the reader to the panel chrome (header, stepper, back-link).

### Conventions

Composition only — reader rendering lives in `taskReader.tsx`.

### Invariants And Boundaries

The panel renders only what the state/model layers resolved; it never fetches.

### Todos

None recorded.

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

- The task-document panel variants. [1]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.
