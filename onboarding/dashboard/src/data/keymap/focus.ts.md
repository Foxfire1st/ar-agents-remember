# dashboard/src/data/keymap/focus.ts

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

## Evidence

### Repo-Internal References

- The region cycle, selectors, and the stage-header/PTY landing constants. [1]
- The view wires F6/Shift+F6 through `nextRegion` with collapsed panels filtered out. [2]
- The cycle suite: forward/backward wrap, edge starts, collapsed dropout, unavailable-current recovery. [3]
