# dashboard/src/data/sessionLayout.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/sessionLayout.ts`            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-07-18T07:22+02:00 |
| lastVerifiedCommitHash | `ee955085a2010f62e9ad4d2bdc6aa77975daa5f3`       |
| lastVerifiedCommitDate | 2026-07-17T00:42:07+02:00|
| governingOverview | `overview.md` |

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

## Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Thresholds, floor math, rail conversion/clamps, persisted-layout probe, and the edge-transition rule. | `RAIL_AUTO_COLLAPSE_PX`, `railDefaultPercent`, `hasPersistedPanelLayout`, `stageBelowPtyFloor`, `autoCollapseTransition` | dashboard/src/data/sessionLayout.ts:6-6; dashboard/src/data/sessionLayout.ts:36-43; dashboard/src/data/sessionLayout.ts:50-61; dashboard/src/data/sessionLayout.ts:64-66; dashboard/src/data/sessionLayout.ts:74-85 |
| The consumer: root/stage measurement, one-shot `calibrateRail`, and the collapse/expand wiring. | `calibrateRail` | dashboard/src/panels/session-cockpit/SessionsView.tsx:955-962 |
| The unit suite: crossings, quiet-below-threshold, floor edges, conversion/clamps/fallback, storage probing. | "the ~80-col PTY floor", "the ~280px rail default (review round 2, finding 4)" | dashboard/src/data/sessionLayout.test.ts:34-40; dashboard/src/data/sessionLayout.test.ts:42-58 |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-02T20:44:32+02:00 — 260731-EFA-L6 curator W2-B10: repaired 5 citation findings (4 reference rows and 1 prose pointer); scoped recheck clean.

- 2026-07-18T07:22+02:00 — FEUI-L8 manual route refactor: retargeted this direct data file card
  from the packed dashboard/src parent to the new nearest data authority overview. Source behavior
  is unchanged by this memory-only governance move; verification hash/date remain pinned.

- 2026-07-17T00:20+02:00 — Created for 260715-FEUI-L1 S2 (R3): pure narrow-width edge-transition
  rules (collapse on downward, expand on upward crossings — manual reopens respected), the ~80-col
  floor approximation with the 0-width hidden-layer guard, and — review round 2 finding 4 — the
  ~280px rail-target percentage conversion (`railDefaultPercent`) + the library-keyed
  `hasPersistedPanelLayout` probe. Verification metadata pinned to the task base until closeout
  stamps the L1 code commit.
