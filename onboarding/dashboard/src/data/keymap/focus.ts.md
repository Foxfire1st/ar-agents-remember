# dashboard/src/data/keymap/focus.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/keymap/focus.ts`             |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T00:20+02:00                           |
| lastVerifiedCommitHash | `ee955085a2010f62e9ad4d2bdc6aa77975daa5f3`       |
| lastVerifiedCommitDate | 2026-07-17T00:42:07+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[data/keymap overview](overview.md)

## Purpose

The **cockpit focus model** (260715-FEUI-L1 S4, design §5.3) — pure region logic. Regions carry a
`data-region` marker; each region exposes ONE primary focus target (`data-focus-target`): rail =
the selected row (roving tabindex arrives with L2), stage = the composer, inspector = the active
tab, statusline = the summary. F6 cycles forward, Shift+F6 backward; collapsed panels drop out of
the cycle.

## Code Commentary

### Logic

- `FOCUS_REGIONS` (L8): `rail → stage → inspector → statusline`, the canonical cycle order.
- `nextRegion(current, direction, available)` (L13-L23): filters the canonical order by the
  available set (collapsed panels excluded by the caller), wraps both ways, starts from the
  matching edge when focus is outside every region (`current === null` or the current region
  itself became unavailable), and returns `null` when nothing is available.
- `regionTargetSelector(region)` (L26-L28): `[data-region="…"] [data-focus-target]`.
- `STAGE_HEADER_SELECTOR` (L31): the composer-Esc and PTY-F6-exit landing — deliberately NOT the
  stage's cycle target (the composer), so exiting a pane lands on inert chrome, never back inside
  an editor.
- `PTY_HOST_SELECTOR` (L34): `[data-kbzone="pty"]` — the explicit Focus-terminal command's
  destination.

### Invariants And Boundaries

- Pure and DOM-free: the caller (SessionsView) supplies availability and performs the actual
  `focus()`; this module only decides.
- The cycle order is fixed; later leaves add focusables INSIDE regions (via `data-focus-target`),
  not new regions, without touching this file.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The region cycle, selectors, and the stage-header/PTY landing constants. | L8-L34 | [focus.ts](focus.ts) |
| The view wires F6/Shift+F6 through `nextRegion` with collapsed panels filtered out. | L218-L233 | [../../panels/session-cockpit/SessionsView.tsx](../../panels/session-cockpit/SessionsView.tsx) |
| The cycle suite: forward/backward wrap, edge starts, collapsed dropout, unavailable-current recovery. | L7-L45 | [focus.test.ts](focus.test.ts) |

## Update History

- 2026-07-17T00:20+02:00 — Created for 260715-FEUI-L1 S4 (R7): the F6 region cycle with
  collapsed-panel dropout plus the stage-header (composer-Esc / PTY-exit landing) and PTY-host
  focus selectors. Verification metadata pinned to the task base until closeout stamps the L1
  code commit.
