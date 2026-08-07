# dashboard/src/panels/detail-panel/changeSetBar.tsx

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/detail-panel/changeSetBar.tsx`        |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-07T08:19Z                                           |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f`                  |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
| governingOverview      | `../overview.md`                                            |

## Governing Overview

[panels/ overview](../overview.md)

## Purpose

The change-set bar of the DetailPanel task-document reader, extracted from
`DetailPanel.tsx` by the 260731-EFA-L8 split. `ChangeSetButton` is the per-document
button, `DocChangeSetBar` the compact bar rendered above the reader content.

## Code Commentary

### Logic

The bar renders the change-set summary for the displayed document and exposes the
change-set viewer toggle; selection state stays in the panel's `useDetailPanelState`.

### Conventions

Small presentational components; no data-store imports.

### Invariants And Boundaries

The bar renders only the document currently displayed; it never fetches a change set
itself.

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
| The change-set bar entry points. | `ChangeSetButton`; `DocChangeSetBar` | dashboard/src/panels/detail-panel/changeSetBar.tsx:20-118 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the
  change-set bar extracted from `DetailPanel.tsx`. Verification pinned to the leaf
  base until closeout stamps the code commit.
