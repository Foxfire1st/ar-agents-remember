# dashboard/src/panels/engine-room/geometry.ts

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/engine-room/geometry.ts`              |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-07T08:19Z                                           |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f`                  |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
| governingOverview      | `overview.md`                                               |

## Governing Overview

[panels/engine-room overview](overview.md)

## Purpose

The pure geometry and derivation layer of the Engine Room scene, extracted from
`EnclosureCanvas.tsx` by the 260731-EFA-L8 responsibility split. It owns the canvas
coordinate constants, conduit path math, state vocabulary narrowing, and the small
formatting/derivation helpers the scene layers render.

## Code Commentary

### Logic

The column layout is fixed by `COL_MAIN_CX` / `COL_FEAT_CX` / `COL_WT_CX`, and all
node, coupler, and wire positions derive from `POS` / `ENGINE` / `COUPLER_X` /
`OFFICIAL_COUPLER_X` / `EDGE_GEOM`. `conduitState` and `runtimeState` narrow
untrusted server strings to the render vocabulary. `conduitPathD` builds SVG paths
per edge, `refusedPolarityOf` derives the flash polarity from edge state alone
(failed → red, stale → amber), and `branchEnter` computes the build-up materialisation
opacity/dx. `isBlocked`, `truncate`, `alertProps`, and `CLOSEOUT_BEATS` are the shared
render helpers.

### Conventions

Everything here is pure: no DOM, no React, no animation state. Motion properties are
owned by GSAP/Motion in the layer components, never by these constants.

### Invariants And Boundaries

This module must stay free of component imports. `RuntimeState` includes `missing`
(an expected-but-unobserved provider slot) and `unknown`; both render as drained,
not faulting.

### Todos

None recorded.

## Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant domain documentation was found. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The scene-wide coordinate constants and conduit-path builder consumed by the layers. | `COL_MAIN_CX`; `conduitPathD` | dashboard/src/panels/engine-room/geometry.ts:47-50; dashboard/src/panels/engine-room/geometry.ts:97-123 |
| The runtime/state vocabulary narrowing shared by gauges and conduits. | `runtimeState`; `conduitState` | dashboard/src/panels/engine-room/geometry.ts:16-38 |
| The materialisation/block derivations this module feeds. | `branchEnter`; `isBlocked` | dashboard/src/panels/engine-room/geometry.ts:141-157; dashboard/src/panels/engine-room/geometry.ts:176-183 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the new
  geometry module extracted from `EnclosureCanvas.tsx`. Verification pinned to the
  leaf base until closeout stamps the code commit.
