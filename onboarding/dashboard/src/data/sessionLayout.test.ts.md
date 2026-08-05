# dashboard/src/data/sessionLayout.test.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/sessionLayout.test.ts`       |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-07-18T07:22+02:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`       |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[data overview](overview.md)

## Purpose

The narrow-width/floor/rail-default unit suite (260715-FEUI-L1 S2 R3; eight cases in the current
suite): downward crossings collapse, upward crossings expand, and a user's manual choice below
the threshold is never fought.

## Code Commentary

### Logic

- **autoCollapseTransition** — collapse on a downward crossing / expand on the way back up (both
  thresholds); QUIET while staying on one side (the manual-reopen-respected rule); first-measure
  collapse only when already below.
- **The ~80-col floor** — flags `ptyFloorPx()-1`, not the floor itself, and never a 0-width
  (hidden-layer) stage.
- **railDefaultPercent** (round 2, finding 4) — pixel→percentage conversion (1280/1920/900),
  min/max clamps (2560→12, 400→40), and the unmeasured fallback (0/-5 →
  `RAIL_FALLBACK_PERCENT`).
- **hasPersistedPanelLayout** — reads the library's own `react-resizable-panels:${id}` key via an
  injectable storage and survives a throwing storage (false).

### Invariants And Boundaries

Pure suite; the component-level counterparts (chip re-measure on `onLayout`, one-shot calibration,
persisted-layout skip) live in `SessionsView.test.tsx`. Test-only.

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
| The suite exercises autoCollapseTransition across crossing, quiet, and first-measure cases. | `autoCollapseTransition` | dashboard/src/data/sessionLayout.test.ts:16-32 |
| The component-level floor-chip and calibration counterparts. | `SessionsView` | dashboard/src/panels/session-cockpit/SessionsView.test.tsx:222-298 |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-04T11:42:15+02:00 — 260731-EFA-L6 S18-B04 — same-reviewer residual correction: bound the crossing, quiet, and first-measure
  suite behavior to the complete `autoCollapseTransition` test body through the scoped fixer.

- 2026-07-18T07:22+02:00 — FEUI-L8 manual route refactor: retargeted this direct data file card
  from the packed dashboard/src parent to the new nearest data authority overview. Source behavior
  is unchanged by this memory-only governance move; verification hash/date remain pinned.

- 2026-07-17T00:20+02:00 — Created for 260715-FEUI-L1 S2/S5 (extended in review round 2 with the
  `railDefaultPercent` conversion/clamp/fallback and `hasPersistedPanelLayout` cases): the
  edge-transition, floor-edge, and rail-default decision suite. Verification metadata pinned to
  the task base until closeout stamps the L1 code commit.
