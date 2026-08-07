# dashboard/src/panels/detail-panel/styles.ts

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/detail-panel/styles.ts`               |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-07T08:19Z                                           |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f`                  |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
| governingOverview      | `../overview.md`                                            |

## Governing Overview

[panels/ overview](../overview.md)

## Purpose

The Panda CSS recipes of the DetailPanel, extracted from `DetailPanel.tsx` by the
260731-EFA-L8 split. Owns sizing, the phase stepper, state badges, series/sub-task
slice list, cross-master button, breadcrumb, worktree spine lanes, and reader
typography.

## Code Commentary

### Logic

Static atoms are `css({...})`; `step` and `lane` are `cva` keyed on state. All colours
go through `token(colors.*)`.

### Conventions

Styles stay co-located with the panel; no animation in this domain.

### Invariants And Boundaries

The `sizing` flex rule preserves the panel's fill behavior.

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
| The panel layout/stepper/badge recipes. | `sizing`; `stepper`; `step`; `badge` | dashboard/src/panels/detail-panel/styles.ts:5-52 |
| The slice/cross/spine recipes. | `slice`; `sliceButton`; `crossButton`; `lane` | dashboard/src/panels/detail-panel/styles.ts:55-66; dashboard/src/panels/detail-panel/styles.ts:69-88; dashboard/src/panels/detail-panel/styles.ts:91-110; dashboard/src/panels/detail-panel/styles.ts:133-145 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the styles
  module extracted from `DetailPanel.tsx`. Verification pinned to the leaf base until
  closeout stamps the code commit.
