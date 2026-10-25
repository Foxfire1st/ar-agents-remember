# dashboard/src/panels/detail-panel/taskDocPanels.tsx

## Governing Overview

[panels/ overview](../overview.md)

## Purpose

TaskDocumentPanel composes one selected entry; EmptyDetailPanel owns no-selection. There is no separate SeriesDetailPanel or synthetic series-as-master body.


## 260831-CCR-L23 Task-Artifact Target Import

The onOpenNotes callback carries the kind-tagged task-artifact reader union from data/taskArtifacts.ts; taskReader receives it unchanged.

## Code Commentary

Parent navigation follows the served parent entry, and each entry-bound worktree renders WorktreeSpine. No masterRef/slug drill path is inferred.

### Logic

An addressed entry with summary renders TaskReader; an unauthored entry shows the honest document-not-authored notice and shared task status. The entry’s own stage/activity is never replaced by body content.

Selected-document panel chrome owns Back/parent navigation only. The authored reader owns one ID/title/objective, not a duplicate Panel title. EmptyDetailPanel retains its separate
empty-selection title/backdrop. Reader-local own views and expansion reset on document identity,
not on the arrival of another projection object.

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
