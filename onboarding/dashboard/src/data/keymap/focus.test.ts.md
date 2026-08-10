# dashboard/src/data/keymap/focus.test.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/keymap/focus.test.ts`        |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T00:20+02:00                           |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb`       |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| The cycle logic under test. | `FOCUS_REGIONS`; `nextRegion` | dashboard/src/data/keymap/focus.ts:9-9; dashboard/src/data/keymap/focus.ts:14-24 |
| The DOM-level F6/Shift+F6 counterpart over the rendered view. | "F6 from the pty zone exits to chrome (the stage header)"; "F6 skips the default-closed inspector"; "Shift+F6 cycles backward" | dashboard/src/panels/session-cockpit/sessions-view/focus.test.tsx:31-31; dashboard/src/panels/session-cockpit/sessions-view/shell.test.tsx:265-265; dashboard/src/panels/session-cockpit/sessions-view/focus.test.tsx:254-254 |

## Update History

- 2026-08-04T13:00:51+02:00 — 260731-EFA-L6 S18-B11 curator: converted the focus references to exact source anchors and supplied scoped fixer input for generated ranges. Verification metadata unchanged.

- 2026-07-24T13:17:50Z — Updated F6-cycle regression coverage for the removed StatusLine region.
  Verification hash/date remain pinned to the pre-commit source stamp.

- 2026-07-17T00:20+02:00 — Created for 260715-FEUI-L1 S4: the pure F6 cycle suite (both
  directions, edge starts, collapsed dropout, unavailable-current recovery, empty-set null).
  Verification metadata pinned to the task base until closeout stamps the L1 code commit.
