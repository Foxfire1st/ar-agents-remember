# dashboard/src/panels/detail-panel/lifecycleBody.tsx

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/detail-panel/lifecycleBody.tsx`       |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-07T08:19Z                                           |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`                  |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `../overview.md`                                            |

## Governing Overview

[panels/ overview](../overview.md)

## Purpose

The lifecycle-detail body of the DetailPanel, extracted from `DetailPanel.tsx` by the
260731-EFA-L8 split. Owns the master/series resolution helpers, the detail head,
phase stepper, gate section, worktree spine, token row, and the exported
`LifecycleDetailBody`.

## Code Commentary

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

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the
  lifecycle body extracted from `DetailPanel.tsx`. Verification pinned to the leaf
  base until closeout stamps the code commit.
