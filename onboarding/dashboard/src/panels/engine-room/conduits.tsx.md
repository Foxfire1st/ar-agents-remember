# dashboard/src/panels/engine-room/conduits.tsx

## Governing Overview

[panels/engine-room overview](overview.md)


## Current enclosure-only composition

Conduit returns null for edge kinds without EDGE_GEOM; all supported paths are straight, replay only changes title/data-strategy. Opacity is 0 while retiring or planned, otherwise 1 with no clone-specific delay. Running draw/marker/packet and inner-path ghosting plus landing progression survive.

### Maintenance boundaries

Replace provider-edge and replay-shape assertions with geometry-gated worktree/ledger/sync/integration paths. Remove clone arc/transient-delay rules; document zero-delay opacity, running markers/packets and retained LandingFlows. Correct the already-stale replay-bend claim rather than preserve it through L112.

Source/test/fixture inspection is not a fresh mounted capture or a passing test run.
Historical provider-shaped input data and retained compatibility definitions do not
restore removed provider visuals or tool exposure.

- Conduit returns null for edge kinds without EDGE_GEOM; all supported paths are straight, replay only changes title/data- — source ownership, not executed visual proof. [3]
- Conduit returns null for edge kinds without EDGE_GEOM; all supported paths are straight, replay only changes title/data- — source ownership, not executed visual proof. [4]
- Conduit returns null for edge kinds without EDGE_GEOM; all supported paths are straight, replay only changes title/data- — source ownership, not executed visual proof. [5]

## Historical superseded account (non-operative)

The prior onboarding below is retained for provenance and unrelated design history.
It is not current provider-render, fallback, prototype-parity or execution guidance.
Current behavior and its limits are the operative contract above.



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
