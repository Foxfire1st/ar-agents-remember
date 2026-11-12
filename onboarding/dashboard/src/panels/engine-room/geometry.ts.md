# dashboard/src/panels/engine-room/geometry.ts

## Governing Overview

[panels/engine-room overview](overview.md)


## Current enclosure-only composition

ConduitState/conduitState retain conduit vocabulary narrowing. Provider positions, ENGINE, RuntimeState/runtimeState and chargeMotion are removed. EDGE_GEOM retains intake, sync and integration lanes; conduitPathD returns a straight line for known geometry or null. refusedPolarityOf accepts only failed or stale integration/integration-mem edges.

### Maintenance boundaries

Remove active provider position/wire/gauge render guarantees. Document surviving branch/coupler/landing constants, conduit narrowing and null-path rejection of unknown kinds. Runtime/gauge/charge helpers and seed refusal arms are removed; failed/stale integration refusal is still geometry-backed.

Source/test/fixture inspection is not a fresh mounted capture or a passing test run.
Historical provider-shaped input data and retained compatibility definitions do not
restore removed provider visuals or tool exposure.

- ConduitState and conduitState retain the conduit vocabulary and normalize unknown values. [4]
- Branch/coupler coordinates and intake/sync/integration geometry remain; conduitPathD returns a straight known lane or null. [5]
- Landing flow state remains derived from the observed landing references. [6]
- Refused polarity is derived only for failed or stale integration/integration-mem lanes. [7]

## Historical superseded account (non-operative)

The prior onboarding below is retained for provenance and unrelated design history.
It is not current provider-render, fallback, prototype-parity or execution guidance.
Current behavior and its limits are the operative contract above.



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

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References


- The scene-wide coordinate constants and conduit-path builder consumed by the layers. [1]

- `runtimeState` and the gauge runtime vocabulary are removed; only the conduit narrowing survives. [2]
- The materialisation/block derivations this module feeds. [3]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.
