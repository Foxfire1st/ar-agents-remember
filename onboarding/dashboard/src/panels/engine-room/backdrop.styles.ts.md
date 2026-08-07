# dashboard/src/panels/engine-room/backdrop.styles.ts

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/engine-room/backdrop.styles.ts`       |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-07T08:19Z                                           |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f`                  |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
| governingOverview      | `overview.md`                                               |

## Governing Overview

[panels/engine-room overview](overview.md)

## Purpose

The atmospheric backdrop style domain of the Engine Room, split from
`engineRoomStyles.ts` by the 260731-EFA-L8 R6 ruling. Owns the absolutely-positioned
`backdrop` layer, the faint amber-tinted `backdropVideo` (with the radial vignette
mask), and `stageContent`, the scene layer stacked above it.

## Code Commentary

### Logic

`backdrop` pins the layer to the stage (`inset:0`, `pointerEvents:none`,
`overflow:hidden`). `backdropVideo` uses `mixBlendMode:screen` + low opacity and a
radial `maskImage` so faded edges fall back to the dark stage; `stageContent` sits
above it.

### Conventions

Atmosphere only: `aria-hidden` is the component's duty; effects gating is the
caller's (`useShouldAnimate` / effects toggle).

### Invariants And Boundaries

The layer must never intercept pointer events or sit above the scene content.

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
| The backdrop layer recipes. | `backdrop`; `backdropVideo`; `stageContent` | dashboard/src/panels/engine-room/backdrop.styles.ts:4-28 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the backdrop
  style domain split from `engineRoomStyles.ts`. Verification pinned to the leaf base
  until closeout stamps the code commit.
