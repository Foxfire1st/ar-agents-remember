# dashboard/src/panels/engine-room/sceneLayers.tsx

## Governing Overview

[panels/engine-room overview](overview.md)


## Current enclosure-only composition

OfficialLineLayer now composes OfficialCoupler only; WorktreeEngineLayer name survives but renders Worktree WarpCoupler only. Provider gauges/wires/wireMotion, DropoutOverlay and ProviderBlock branch are deleted; PointerOverlays is source/node/edge based and FxOverlay passes attention/surgeXs only.

### Maintenance boundaries

Keep layer composition/Motion/static-CSS boundary but rename documented responsibilities to official/worktree ledger links. Delete dropout/provider-wire/gauge layers from inventory; specify surviving pointers, memory flags, landing/closeout and integration refusal/STOP/attention. Do not delete the surviving WorktreeEngineLayer merely because its name is historical.

Source/test/fixture inspection is not a fresh mounted capture or a passing test run.
Historical provider-shaped input data and retained compatibility definitions do not
restore removed provider visuals or tool exposure.

- OfficialLineLayer now composes OfficialCoupler only; WorktreeEngineLayer name survives but renders Worktree WarpCoupler  — source ownership, not executed visual proof. [3]
- OfficialLineLayer now composes OfficialCoupler only; WorktreeEngineLayer name survives but renders Worktree WarpCoupler  — source ownership, not executed visual proof. [4]

## Historical superseded account (non-operative)

The prior onboarding below is retained for provenance and unrelated design history.
It is not current provider-render, fallback, prototype-parity or execution guidance.
Current behavior and its limits are the operative contract above.



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

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

- The shell and wire/engine layer entry points. [1]
- The overlay/failure layer entry points. [2]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.
