# dashboard/src/data/keymap/focus.test.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/keymap/focus.test.ts`        |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T00:20+02:00                           |
| lastVerifiedCommitHash | `ee955085a2010f62e9ad4d2bdc6aa77975daa5f3`       |
| lastVerifiedCommitDate | 2026-07-17T00:42:07+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[data/keymap overview](overview.md)

## Purpose

The F6 region-cycle suite (260715-FEUI-L1 S4, design §5.3, 7 cases): rail → stage → inspector →
statusline, wrapping both ways, with collapsed panels dropping out of the cycle.

## Code Commentary

### Logic

Pins `nextRegion`'s full forward cycle, the Shift+F6 backward cycle, edge starts when focus is
outside every region (`null` current → first/last), collapsed-panel dropout (a filtered
`available` set skips the missing region), recovery when the CURRENT region itself is unavailable,
and `null` when nothing is available. Plus `regionTargetSelector`'s
`[data-region="…"] [data-focus-target]` shape.

### Invariants And Boundaries

Pure logic only — the DOM-level F6 behavior (real focus moves across the rendered regions) is
pinned separately in `SessionsView.test.tsx`. Test-only.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The cycle logic under test. | L13-L28 | [focus.ts](focus.ts) |
| The DOM-level F6/Shift+F6 counterpart over the rendered view. | L210-L246 | [../../panels/session-cockpit/SessionsView.test.tsx](../../panels/session-cockpit/SessionsView.test.tsx) |

## Update History

- 2026-07-17T00:20+02:00 — Created for 260715-FEUI-L1 S4: the pure F6 cycle suite (both
  directions, edge starts, collapsed dropout, unavailable-current recovery, empty-set null).
  Verification metadata pinned to the task base until closeout stamps the L1 code commit.
