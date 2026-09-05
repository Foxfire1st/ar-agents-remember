# dashboard/src/panels/detail-panel/taskDocPanels.tsx

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/detail-panel/taskDocPanels.tsx`       |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-09-04T01:06+02:00 |
| lastVerifiedCommitHash | `1993dd25bdf8331a2c1e28171dff2bf92ea090e2` |
| lastVerifiedCommitDate | 2026-09-04T00:57:29+02:00 |
| governingOverview      | `../overview.md`                                            |

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

## Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant domain documentation was found. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The task-document panel variants. | `TaskDocumentPanel`; `EmptyDetailPanel`; `SeriesDetailPanel` | dashboard/src/panels/detail-panel/taskDocPanels.tsx:73-135; dashboard/src/panels/detail-panel/taskDocPanels.tsx:137-145; dashboard/src/panels/detail-panel/taskDocPanels.tsx:147-214 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-09-04T01:06+02:00 — 260831-CCR-L23 Gate-5 memory pass: recorded the shared task-artifact target import (`data/taskArtifacts.ts`) replacing the notes-reader-owned type.

- 2026-08-20T04:36+02:00 — 260815-DAG-L14: `TaskDocBody`/`SeriesDetailPanel` thread `docPathForRef` into the task readers for the sprint → master drill-down. Verified at code commit 9c3180c1.

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the panel
  composition module extracted from `DetailPanel.tsx`. Verification pinned to the
  leaf base until closeout stamps the code commit.
