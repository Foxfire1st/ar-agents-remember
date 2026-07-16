# dashboard/src/data/sessionLayout.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/sessionLayout.ts`            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T00:20+02:00                           |
| lastVerifiedCommitHash | `ee955085a2010f62e9ad4d2bdc6aa77975daa5f3`       |
| lastVerifiedCommitDate | 2026-07-17T00:42:07+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

The **narrow-width + ~80-col-floor + rail-default rules** for the Sessions cockpit view
(260715-FEUI-L1 S2, R3) — pure decisions so vitest covers the thresholds without a layout engine.
The React side (`panels/session-cockpit/SessionsView.tsx`) feeds measured widths in; this module
answers "collapse / expand / show the floor chip / what rail percentage".

## Code Commentary

### Logic

- Thresholds (L5-L9): the rail auto-collapses below `RAIL_AUTO_COLLAPSE_PX` (900), the inspector
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
- `hasPersistedPanelLayout(autoSaveId, storage?)` (L50-L61): reads the library's OWN key format
  (`react-resizable-panels:${autoSaveId}` — `getPanelGroupKey`); injectable storage for tests,
  throw-safe (a denying storage reports false). Calibration must never override a user's saved
  layout.
- `autoCollapseTransition(previousWidth, width, threshold)` (L74-L85) — the **transition-edge
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

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Thresholds, floor math, rail conversion/clamps, persisted-layout probe, and the edge-transition rule. | L5-L85 | [sessionLayout.ts](sessionLayout.ts) |
| The consumer: root/stage measurement, one-shot `calibrateRail`, and the collapse/expand wiring. | L300-L355 | [../panels/session-cockpit/SessionsView.tsx](../panels/session-cockpit/SessionsView.tsx) |
| The unit suite: crossings, quiet-below-threshold, floor edges, conversion/clamps/fallback, storage probing. | L16-L73 | [sessionLayout.test.ts](sessionLayout.test.ts) |

## Update History

- 2026-07-17T00:20+02:00 — Created for 260715-FEUI-L1 S2 (R3): pure narrow-width edge-transition
  rules (collapse on downward, expand on upward crossings — manual reopens respected), the ~80-col
  floor approximation with the 0-width hidden-layer guard, and — review round 2 finding 4 — the
  ~280px rail-target percentage conversion (`railDefaultPercent`) + the library-keyed
  `hasPersistedPanelLayout` probe. Verification metadata pinned to the task base until closeout
  stamps the L1 code commit.
