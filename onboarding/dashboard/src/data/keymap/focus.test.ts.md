# dashboard/src/data/keymap/focus.test.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/keymap/focus.test.ts`        |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T00:20+02:00                           |
| lastVerifiedCommitHash | `842b487b854503d95c9c2d9dce1841198ba93c7d`       |
| lastVerifiedCommitDate | 2026-07-24T17:08:25+02:00|
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

### 2026-07-24 Curator Delta

The focus-cycle tests now assert the three-region rail/stage/inspector loop after StatusLine removal,
including forward/backward wrapping and collapsed-region handling.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The cycle logic under test. | L13-L28 | [focus.ts](focus.ts) |
| The DOM-level F6/Shift+F6 counterpart over the rendered view. | L210-L246 | [../../panels/session-cockpit/SessionsView.test.tsx](../../panels/session-cockpit/SessionsView.test.tsx) |

## Update History

- 2026-07-24T13:17:50Z — Updated F6-cycle regression coverage for the removed StatusLine region.
  Verification hash/date remain pinned to the pre-commit source stamp.

- 2026-07-17T00:20+02:00 — Created for 260715-FEUI-L1 S4: the pure F6 cycle suite (both
  directions, edge starts, collapsed dropout, unavailable-current recovery, empty-set null).
  Verification metadata pinned to the task base until closeout stamps the L1 code commit.
