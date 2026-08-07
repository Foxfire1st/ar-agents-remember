# dashboard/src/panels/engine-room/sceneLayers.tsx

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/engine-room/sceneLayers.tsx`          |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-07T08:19Z                                           |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f`                  |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
| governingOverview      | `overview.md`                                               |

## Governing Overview

[panels/engine-room overview](overview.md)

## Purpose

The composed scene layers of the Engine Room canvas, extracted from
`EnclosureCanvas.tsx` by the 260731-EFA-L8 responsibility split. Each layer owns one
vertical slice of the SVG scene: header, enclosure shell, conduits, branch tier,
official line, worktree engines, lane flags, landing dock, closeout train, and the
failure overlays (fleeting, refused, stop/attention, dropout, pointers, FX).

## Code Commentary

### Logic

Layers take the resolved scene packet plus motion flags and compose the primitives
from `badges.tsx`, `engines.tsx`, `ledger.tsx`, `conduits.tsx`, and `remote.tsx`.
`FxOverlay` hosts the GSAP `data-fx` elements; `PointerOverlays` anchors the
verify/block pointers on repository nodes. Motion enters/exits live in `motion.*`
components and `AnimatePresence`; CSS stays static.

### Conventions

One layer per scene slice; layers never decide state. Motion gates flow from
`useShouldAnimate` via the canvas.

### Invariants And Boundaries

The layers must not import data stores or mutating handlers — they render the scene
packet only.

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
| The shell and wire/engine layer entry points. | `EnclosureShell`; `OfficialLineLayer`; `WorktreeEngineLayer` | dashboard/src/panels/engine-room/sceneLayers.tsx:99-132; dashboard/src/panels/engine-room/sceneLayers.tsx:272-295; dashboard/src/panels/engine-room/sceneLayers.tsx:337-385 |
| The overlay/failure layer entry points. | `FleetingOverlay`; `RefusedOverlay`; `FxOverlay` | dashboard/src/panels/engine-room/sceneLayers.tsx:517-534; dashboard/src/panels/engine-room/sceneLayers.tsx:535-551; dashboard/src/panels/engine-room/sceneLayers.tsx:684-719; dashboard/src/panels/engine-room/sceneLayers.tsx:30-30 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the new
  scene-layers module extracted from `EnclosureCanvas.tsx`. Verification pinned to
  the leaf base until closeout stamps the code commit.
