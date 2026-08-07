# dashboard/src/panels/engine-room/stage.styles.ts

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/engine-room/stage.styles.ts`          |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-07T08:19Z                                           |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f`                  |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
| governingOverview      | `overview.md`                                               |

## Governing Overview

[panels/engine-room overview](overview.md)

## Purpose

The pod-stage scene style domain of the Engine Room, split from `engineRoomStyles.ts`
by the 260731-EFA-L8 R6 ruling. Owns the scene SVG/world labels, enclosure border,
SVG node boxes, pruned-node register, engine gauge frame/charge/petals, official and
worktree wires, canopy stroke, lane flags, and warp-coupler geometry.

## Code Commentary

### Logic

`sceneSvg` carries layout only (no global transition substrate — motion is
GSAP/Motion). `engineGaugeOut` is a constant gold bezel with `down` as the one
fault-coloured frame; `enginePetal` is constant gold with per-state opacity.
`prunedNode` is the dormant/desaturated stale-base register.

### Conventions

CSS is static; property-split law: a class opacity must never shadow a Motion-owned
value (see `worktreeWire`, which deliberately carries no opacity).

### Invariants And Boundaries

This domain contains no animations and no dynamic per-beat styles.

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
| The scene/wire recipes. | `sceneSvg`; `officialWire`; `worktreeWire`; `canopyStroke` | dashboard/src/panels/engine-room/stage.styles.ts:5-14; dashboard/src/panels/engine-room/stage.styles.ts:171-198 |
| The engine gauge/pruned-node recipes. | `engineGaugeOut`; `engineCharge`; `prunedNode` | dashboard/src/panels/engine-room/stage.styles.ts:72-105; dashboard/src/panels/engine-room/stage.styles.ts:125-139 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the stage
  style domain split from `engineRoomStyles.ts`. Verification pinned to the leaf base
  until closeout stamps the code commit.
