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


## Current enclosure-only composition

The Markdown primitive list does not name ProviderBlock, so that list is still valid. Source deletes ProviderBlock and ENGINE import only; Gate, NodeBlock, FleetingEnclosure, TerminalStop, RefusedConduit, recovery/attention/moved/lane/closeout primitives survive. RefusedConduit returns null when no conduitPathD.

### Maintenance boundaries

Keep the listed generic badge responsibilities. Add a precise retirement boundary for ProviderBlock, and qualify RefusedConduit by geometry: the polarity helper admits only integration/integration-mem, and old provider seed/clone kinds yield no polarity; integration flashes survive when shared geometry is present. Refresh shifted evidence locators without claiming all failure badges were deleted.

Source/test/fixture inspection is not a fresh mounted capture or a passing test run.
Historical provider-shaped input data and retained compatibility definitions do not
restore removed provider visuals or tool exposure.

- The Markdown primitive list does not name ProviderBlock, so that list is still valid. Source deletes ProviderBlock and E — source ownership, not executed visual proof. [3]
- The Markdown primitive list does not name ProviderBlock, so that list is still valid. Source deletes ProviderBlock and E — source ownership, not executed visual proof. [4]
- The Markdown primitive list does not name ProviderBlock, so that list is still valid. Source deletes ProviderBlock and E — source ownership, not executed visual proof. [5]

- Provider seed/clone kinds yield no refused polarity; the surviving integration flash also requires a shared conduit path. [6]
