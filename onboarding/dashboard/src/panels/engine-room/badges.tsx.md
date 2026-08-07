# dashboard/src/panels/engine-room/badges.tsx

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/engine-room/badges.tsx`               |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-07T08:19Z                                           |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f`                  |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
| governingOverview      | `overview.md`                                               |

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

## Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant domain documentation was found. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The failure-mode overlay primitives extracted from the canvas. | `FleetingEnclosure`; `TerminalStop`; `RefusedConduit` | dashboard/src/panels/engine-room/badges.tsx:193-236; dashboard/src/panels/engine-room/badges.tsx:237-283 |
| The closeout-order train and moved/attention badges. | `CloseoutTrain`; `MovedBadge`; `Gate` | dashboard/src/panels/engine-room/badges.tsx:61-79; dashboard/src/panels/engine-room/badges.tsx:127-145; dashboard/src/panels/engine-room/badges.tsx:315-342 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the new
  badge module extracted from `EnclosureCanvas.tsx`. Verification pinned to the leaf
  base until closeout stamps the code commit.
