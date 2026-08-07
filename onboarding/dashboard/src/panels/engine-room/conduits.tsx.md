# dashboard/src/panels/engine-room/conduits.tsx

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/engine-room/conduits.tsx`             |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-07T08:19Z                                           |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f`                  |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
| governingOverview      | `overview.md`                                               |

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

## Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant domain documentation was found. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The per-edge conduit renderer with replay/ghost handling. | `Conduit` | dashboard/src/panels/engine-room/conduits.tsx:70-138 |
| The landing-tier flow renderer and its ref resolution. | `LandingFlows` | dashboard/src/panels/engine-room/conduits.tsx:192-205 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the new
  conduits module extracted from `EnclosureCanvas.tsx`. Verification pinned to the
  leaf base until closeout stamps the code commit.
