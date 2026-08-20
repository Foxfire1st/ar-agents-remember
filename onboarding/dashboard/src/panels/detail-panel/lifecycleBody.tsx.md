# dashboard/src/panels/detail-panel/lifecycleBody.tsx

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/detail-panel/lifecycleBody.tsx`       |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-20T04:36+02:00                                        |
| lastVerifiedCommitHash | `9c3180c133fccf98586a87c4b08824edaa3755a7`                  |
| lastVerifiedCommitDate | 2026-08-20T01:13:12+02:00|
| governingOverview      | `../overview.md`                                            |

## Governing Overview

[panels/ overview](../overview.md)

## Purpose

The lifecycle-detail body of the DetailPanel, extracted from `DetailPanel.tsx` by the
260731-EFA-L8 split. Owns the master/series resolution helpers, the detail head,
phase stepper, gate section, worktree spine, token row, and the exported
`LifecycleDetailBody`.

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

## Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant domain documentation was found. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The lifecycle body entry and its derivation helpers. | `LifecycleDetailBody`; `resolveMasterAndSlices`; `resolveParentLink` | dashboard/src/panels/detail-panel/lifecycleBody.tsx:64-102; dashboard/src/panels/detail-panel/lifecycleBody.tsx:367-412 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-20T04:36+02:00 — 260815-DAG-L14: `DetailBody` threads `docPathForRef` into all three lifecycle-path render branches (seriesDoc, master, TaskContent). Verified at code commit 9c3180c1.

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the
  lifecycle body extracted from `DetailPanel.tsx`. Verification pinned to the leaf
  base until closeout stamps the code commit.
