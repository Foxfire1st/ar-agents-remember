# dashboard/src/panels/detail-panel/taskDocPanels.tsx

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/detail-panel/taskDocPanels.tsx`       |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-07T08:19Z                                           |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`                  |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `../overview.md`                                            |

## Governing Overview

[panels/ overview](../overview.md)

## Purpose

The task-document panel composition of the DetailPanel, extracted from
`DetailPanel.tsx` by the 260731-EFA-L8 split. `TaskDocumentPanel` renders the selected
task document body (or empty/series variants), `EmptyDetailPanel` the no-selection
state, and `SeriesDetailPanel` the series-as-master reader.

## Code Commentary

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

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the panel
  composition module extracted from `DetailPanel.tsx`. Verification pinned to the
  leaf base until closeout stamps the code commit.
