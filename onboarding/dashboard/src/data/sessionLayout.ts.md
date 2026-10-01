# dashboard/src/data/sessionLayout.ts

## Governing Overview

[data overview](overview.md)

## Purpose

The **narrow-width + ~80-col-floor + rail-default rules** for the Sessions cockpit view
(260715-FEUI-L1 S2, R3) — pure decisions so vitest covers the thresholds without a layout engine.
The React side (`panels/session-cockpit/SessionsView.tsx`) feeds measured widths in; this module
answers "collapse / expand / show the floor chip / what rail percentage".

## Code Commentary

### Logic

- Thresholds cit:([`RAIL_AUTO_COLLAPSE_PX`], dashboard/src/data/sessionLayout.ts:6-6): the rail auto-collapses below `RAIL_AUTO_COLLAPSE_PX` (900), the inspector
  below `INSPECTOR_AUTO_COLLAPSE_PX` (1100) — both reopenable (R3).
- The ~80-col floor (L11-L23, L63-L66): `ptyFloorPx()` = `PTY_MIN_COLS` (80) ×
  `APPROX_CELL_PX` (8 — an APPROXIMATION by design: ≈7.8px mono advance at the terminal's 13px
  font plus a per-cell chrome share; the chip is a hint, not a measurement — real cols arrive with
  the xterm stage, L6). `stageBelowPtyFloor(width)` is true only for a POSITIVE width below the
  floor — a 0-width (hidden keep-alive layer) never false-alarms.
- The ~280px rail default (L25-L43, review round 2 finding 4): react-resizable-panels v3 is
  percentage-only, so `railDefaultPercent(rootWidthPx, min=12, max=40)` converts
  `RAIL_TARGET_PX` (280) to a width-relative percentage clamped to the panel's bounds
  (1280→21.9%, 1920→14.6%, 2560→12 min-clamped, 400→40 max-clamped); unmeasured (≤0) widths keep
  `RAIL_FALLBACK_PERCENT` (22 — the 1280px design reference).
- cit:([`hasPersistedPanelLayout`], dashboard/src/data/sessionLayout.ts:50-61): reads the library's OWN key format
  (`react-resizable-panels:${autoSaveId}` — `getPanelGroupKey`); injectable storage for tests,
  throw-safe (a denying storage reports false). Calibration must never override a user's saved
  layout.
- cit:([`autoCollapseTransition`], dashboard/src/data/sessionLayout.ts:74-85) — the **transition-edge
  semantics**: collapse fires only on a DOWNWARD threshold crossing, expand only on an UPWARD one,
  so a user who reopens a panel below the threshold is respected (staying below produces no new
  crossing) and a user who closed it above stays closed. First measure (`previousWidth: null`)
  collapses only when already below.

### Invariants And Boundaries

- Pure module — no DOM, no store, no persistence writes; the view owns measurement and the
  imperative panel API.
- `APPROX_CELL_PX` is honest scaffolding: when L6 lands real xterm cols, the chip should switch to
  measured columns rather than tuning this constant.
- The persisted-layout key format belongs to react-resizable-panels; if the library changes it,
  `hasPersistedPanelLayout` must follow (the unit test pins the current format).

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- Thresholds, floor math, rail conversion/clamps, persisted-layout probe, and the edge-transition rule. [1]
- The consumer: root/stage measurement, one-shot `calibrateRail`, and the collapse/expand wiring. [2]
- The unit suite: crossings, quiet-below-threshold, floor edges, conversion/clamps/fallback, storage probing. [3]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.
