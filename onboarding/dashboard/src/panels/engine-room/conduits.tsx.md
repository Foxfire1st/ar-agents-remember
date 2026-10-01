# dashboard/src/panels/engine-room/conduits.tsx

## Governing Overview

[panels/engine-room overview](overview.md)

## Purpose

The SVG conduit and landing-flow renderers of the Engine Room scene, extracted from
`EnclosureCanvas.tsx` by the 260731-EFA-L8 responsibility split. `Conduit` draws a
single provider/landing edge with its draw-on, packet, marker, and ghosted/retiring
treatments; `LandingFlows` renders the landing-tier arcs derived from landing refs.

## Code Commentary

### Logic

Conduit opacity/title/draw/packet visibility are derived per edge from its state and
the integration strategy (replay bends, ff-only stays straight). The GSAP draw-on and
packet motion are gated by `animate`; the inner path can carry the ghosted-lane
treatment while the Motion group opacity stays untouched (the property-split law).
`LandingFlows` resolves refs (`landingRefResolved`, `landingPrMerged`,
`landingMemPushed`) to a flow state.

### Conventions

CSS never animates: the conduit path is static, and GSAP owns the draw/packet. The
`worktreeWire`-style opacity rule applies — a class opacity would shadow Motion.

### Invariants And Boundaries

Conduit state is read from `edge.state` only; "refused" is a beat, never a state.
Ghosting applies to the held memory lane while its code sibling stays solid.

### Todos

None recorded.

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

- The per-edge conduit renderer with replay/ghost handling. [1]
- The landing-tier flow renderer and its ref resolution. [2]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.
