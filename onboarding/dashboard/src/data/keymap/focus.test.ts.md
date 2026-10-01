# dashboard/src/data/keymap/focus.test.ts

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

## Evidence

### Repo-Internal References

- The cycle logic under test. [1]
- The DOM-level F6/Shift+F6 counterpart over the rendered view. [2]
