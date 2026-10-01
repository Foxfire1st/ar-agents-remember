# dashboard/src/panels/detail-panel/lifecycleBody.tsx

## Governing Overview

[panels/ overview](../overview.md)

## Purpose

The lifecycle-detail body of the DetailPanel, extracted from `DetailPanel.tsx` by the
260731-EFA-L8 split. Owns the master/series resolution helpers, the detail head,
phase stepper, gate section, worktree spine, token row, and the exported
`LifecycleDetailBody`.


## 260831-CCR-L23 Task-Artifact Target Import

The `NotesReaderTarget` type import moved from the notes-reader module to the
shared `dashboard/src/data/taskArtifacts.ts` union (aliased as
`NotesReaderTarget`); the payload `DetailBody` forwards into
`TaskContent`/`TaskNotes` is now kind-tagged (notes or requirements).
Selection derivation and render branches are unchanged.

## Code Commentary

Since 260815-DAG-L14 `DetailBody` passes `docPathForRef={state.docPathForRef}` into the series-doc, master, and TaskContent render branches so typed sprint rows can open their commanded master document.

### Logic

`resolveMasterAndSlices` / `resolveSeriesView` / `resolveParentLink` derive the
displayed document and the parent/up-link from the selected selection.
`LifecycleDetailBody` composes the head, stepper, gate section, body, and worktree
spine for a lifecycle selection.

### Conventions

Selection derivation is pure; rendering stays presentational.

### Invariants And Boundaries

The body renders the lifecycle selection only; task-document content rendering lives
in `taskReader.tsx` / `taskDocPanels.tsx`.

### Todos

None recorded.

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

- The lifecycle body entry and its derivation helpers. [1]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.
