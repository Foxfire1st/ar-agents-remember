# dashboard/src/panels/engine-room/layout.styles.ts

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/engine-room/layout.styles.ts`         |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-07T08:19Z                                           |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`                  |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `overview.md`                                               |

## Governing Overview

[panels/engine-room overview](overview.md)

## Purpose

The room-layout and health/fact style domain of the Engine Room, split from
`engineRoomStyles.ts` by the 260731-EFA-L8 R6 ruling. Owns the full-bleed room
shell/grid/stage/zones/header, the left enclosure stack (with `stackList` top-aligned
so single rows keep intrinsic height), health dots, phase/fact chips, node boxes, and
the official strip labels.

## Code Commentary

### Logic

Static atoms are `css({...})`; stateful treatments are `cva` keyed on one semantic
axis (`stackItem`, `healthDot`, `phaseChip`, `factChip`, `nodeBox`, `roomCaution`).
All colours go through `token(colors.*)`.

### Conventions

Colour-as-state; no animation in this domain (motion lives in GSAP/Motion).

### Invariants And Boundaries

`stackList` keeps `overflowX:hidden` + `minWidth:0` so the repo label ellipsizes and
the phase pill never clips.

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
| The room layout recipes. | `roomShell`; `roomGrid`; `roomStage` | dashboard/src/panels/engine-room/layout.styles.ts:6-41 |
| The stack/health/fact recipes. | `stackList`; `stackItem`; `healthDot`; `nodeBox` | dashboard/src/panels/engine-room/layout.styles.ts:112-186; dashboard/src/panels/engine-room/layout.styles.ts:194-216; dashboard/src/panels/engine-room/layout.styles.ts:308-340 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the layout
  style domain split from `engineRoomStyles.ts`. Verification pinned to the leaf base
  until closeout stamps the code commit.
