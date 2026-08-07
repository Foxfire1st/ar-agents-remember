# dashboard/src/panels/detail-panel/state.ts

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/detail-panel/state.ts`                |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-07T08:19Z                                           |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f`                  |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
| governingOverview      | `../overview.md`                                            |

## Governing Overview

[panels/ overview](../overview.md)

## Purpose

The selection-state hook of the DetailPanel, extracted from `DetailPanel.tsx` by the
260731-EFA-L8 split. `useDetailPanelState` resolves the selected task/lifecycle/series
and derives the viewed-leaf key and direct document set from props.

## Code Commentary

### Logic

The pure resolvers (`resolveSelectedTaskDoc`, `resolveLifecycleId`,
`resolveDirectDocs`, `isRootTaskSelection`, `resolveSelectedSeries`,
`resolveViewedLeafKey`) narrow the prop selection; the hook memoizes the derived state
the render tree consumes.

### Conventions

State derivation is pure and unit-testable.

### Invariants And Boundaries

The hook never mutates server data; it only projects the current selection.

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
| The state hook and its pure resolvers. | `useDetailPanelState`; `resolveSelectedTaskDoc`; `resolveViewedLeafKey` | dashboard/src/panels/detail-panel/state.ts:27-61; dashboard/src/panels/detail-panel/state.ts:80-166 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the state
  module extracted from `DetailPanel.tsx`. Verification pinned to the leaf base until
  closeout stamps the code commit.
