# dashboard/src/panels/engine-room/engines.tsx

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/engine-room/engines.tsx`              |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-07T08:19Z                                           |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f`                  |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
| governingOverview      | `overview.md`                                               |

## Governing Overview

[panels/engine-room overview](overview.md)

## Purpose

The branch-node and engine-gauge renderers of the Engine Room scene, extracted from
`EnclosureCanvas.tsx` by the 260731-EFA-L8 responsibility split. `BranchNode` draws a
repository branch node (including the pruned/stale-base register); `EngineGauge` draws
the provider engine podracer gauge with its charge, petals, and runtime-state palette.

## Code Commentary

### Logic

`BranchNode` composes label, flags, detach slide, and materialisation opacity from a
`CommitRefNode` plus the landing/detaching/pruned flags. `EngineGauge` maps
`RuntimeState` to the gauge frame/charge/petal treatments (nominal mint, indexing
cyan, down alarm, configured/unknown/missing drained or dashed). Branch-label
truncation and detach delays are computed here as pure helpers.

### Conventions

Colour-as-state: the gauge body carries runtime state; the frame is a constant gold
bezel except `down`, which re-colours red.

### Invariants And Boundaries

These components render only projection data and must never fake a state. Motion
transitions (charge, fault breathe) are driven by GSAP/Motion in the layers, not by
CSS animation in these components.

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
| The branch-node renderer with landing/pruned registers. | `BranchNode` | dashboard/src/panels/engine-room/engines.tsx:72-135 |
| The runtime-state gauge renderer. | `EngineGauge` | dashboard/src/panels/engine-room/engines.tsx:136-196 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the new
  engines module extracted from `EnclosureCanvas.tsx`. Verification pinned to the
  leaf base until closeout stamps the code commit.
