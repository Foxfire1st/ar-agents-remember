# dashboard/src/data/keymap/focus.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/keymap/focus.ts`             |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T00:20+02:00                           |
| lastVerifiedCommitHash | `d9a1eb82849baea6c0b86735e772a932f4bbdc7c`       |
| lastVerifiedCommitDate | 2026-08-12T00:45:15+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[data/keymap overview](overview.md)

## Purpose

The **cockpit focus model** (260715-FEUI-L1 S4, design §5.3) — pure region logic. Regions carry a
`data-region` marker; each region exposes ONE primary focus target (`data-focus-target`): rail =
the selected row (roving tabindex arrives with L2), stage = the composer, inspector = the active
tab. F6 cycles forward, Shift+F6 backward; collapsed panels drop out of the cycle. The removed
StatusLine is no longer a region or an F6 stop.

## Code Commentary

### Logic

- `FOCUS_REGIONS`: `rail → stage → inspector`, the canonical cycle order.
- cit:([`nextRegion`], dashboard/src/data/keymap/focus.ts:14-24): filters the canonical order by the
  available set (collapsed panels excluded by the caller), wraps both ways, starts from the
  matching edge when focus is outside every region (`current === null` or the current region
  itself became unavailable), and returns `null` when nothing is available.
- cit:([`regionTargetSelector`], dashboard/src/data/keymap/focus.ts:27-29): `[data-region="…"] [data-focus-target]`.
- cit:([`STAGE_HEADER_SELECTOR`], dashboard/src/data/keymap/focus.ts:32-32): the composer-Esc and PTY-F6-exit landing — deliberately NOT the
  stage's cycle target (the composer), so exiting a pane lands on inert chrome, never back inside
  an editor.
- cit:([`PTY_HOST_SELECTOR`], dashboard/src/data/keymap/focus.ts:35-35): `[data-kbzone="pty"]` — the explicit Focus-terminal command's
  destination.

### Invariants And Boundaries

- Pure and DOM-free: the caller (SessionsView) supplies availability and performs the actual
  `focus()`; this module only decides.
- The cycle order is fixed; later leaves add focusables INSIDE regions (via `data-focus-target`),
  not new regions, without touching this file.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The region cycle, selectors, and the stage-header/PTY landing constants. | `nextRegion`; `regionTargetSelector`; `STAGE_HEADER_SELECTOR`; `PTY_HOST_SELECTOR` | dashboard/src/data/keymap/focus.ts:14-24; dashboard/src/data/keymap/focus.ts:27-29; dashboard/src/data/keymap/focus.ts:32-32; dashboard/src/data/keymap/focus.ts:35-35 |
| The view wires F6/Shift+F6 through `nextRegion` with collapsed panels filtered out. | "const next = nextRegion(current" | dashboard/src/panels/session-cockpit/sessions-view/sessionsViewController.ts:467-467 |
| The cycle suite: forward/backward wrap, edge starts, collapsed dropout, unavailable-current recovery. | "cycles backward with Shift+F6"; "skips collapsed panels (they leave the cycle)"; "recovers when the current region itself is unavailable" | dashboard/src/data/keymap/focus.test.ts:15-18; dashboard/src/data/keymap/focus.test.ts:25-30; dashboard/src/data/keymap/focus.test.ts:32-34 |

## Update History

- 2026-08-02T16:46+02:00 — 260731-EFA-L6 curator W1-B03: repaired 3 citation rows with exact anchors and source paths; scoped citation recheck recorded separately. Verification metadata remains pinned until closeout.

- 2026-07-31T17:48+02:00 — 260731-EFA-L2 curator: re-derived 2 stale self-citations after the
  header comment gained the removed-`statusline`-region note, shifting the whole file down one
  line: `STAGE_HEADER_SELECTOR` L31 → L32 and `PTY_HOST_SELECTOR` L34 → L35. Both constants are
  unchanged.

- 2026-07-24T13:17:50Z — Corrected the stale StatusLine focus-region description after the bar's
  removal; F6 now wraps inspector directly to rail. Verification hash/date remain pinned to the
  pre-commit source stamp.

- 2026-07-17T00:20+02:00 — Created for 260715-FEUI-L1 S4 (R7): the F6 region cycle with
  collapsed-panel dropout plus the stage-header (composer-Esc / PTY-exit landing) and PTY-host
  focus selectors. Verification metadata pinned to the task base until closeout stamps the L1
  code commit.
