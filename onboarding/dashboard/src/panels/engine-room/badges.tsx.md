# dashboard/src/panels/engine-room/badges.tsx

## Governing Overview

[panels/engine-room overview](overview.md)

## Purpose

The overlay badge and failure-mode primitives of the Engine Room scene, extracted
from `EnclosureCanvas.tsx` by the 260731-EFA-L8 responsibility split. It renders the
canopy frame, blocked-lane gates, attention/reason badges, recovery chips, the
fleeting enclosure box, terminal STOP, refused-conduit flashes, lane flags, the
upstream-moved badge, and the closeout train.

## Code Commentary

### Logic

Every badge is a small SVG group keyed by a projection fact (edge state, node
factState, or landing refs). `FleetingEnclosure` renders the born-blocked provisional
enclosure; `RefusedConduit` renders a one-shot flash whose polarity arrives from
`geometry.refusedPolarityOf`; `CloseoutTrain` renders the five ordered beats
(code → onboard → quality → memory → ledger). Motion enter/exit stays in the calling
layers, so these components are mostly static SVG.

### Conventions

Badges never carry animation CSS; GSAP/Motion own transitions. Colour-as-state is
the engine-room law: `planned` refs never use the `live` register.

### Invariants And Boundaries

These primitives render only projection-derived data and must not decide state. The
scene layers own placement (x/y/w/h); badges own geometry only where the design
requires it (e.g. the fleeting box).

### Todos

None recorded.

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

- The failure-mode overlay primitives extracted from the canvas. [1]
- The closeout-order train and moved/attention badges. [2]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.
