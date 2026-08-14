# dashboard/src/panels/engine-room/flow.styles.ts

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/engine-room/flow.styles.ts`           |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-07T08:19Z                                           |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`                  |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `overview.md`                                               |

## Governing Overview

[panels/engine-room overview](overview.md)

## Purpose

The flow and failure-overlay style domain of the Engine Room, split from
`engineRoomStyles.ts` by the 260731-EFA-L8 R6 ruling. Owns conduit/flow-packet
recipes, the scan ring, ghosted lane, refused-conduit flashes, engine dropout,
moved-badge trio, fleeting-enclosure box, gates, reason/attention badges, recovery
chips, stop bar, and the abandon/cleanup records.

## Code Commentary

### Logic

`flowConduit` is a static stroke recipe (running solid, planned dashed); the packet
and scan-ring rest at `opacity: 0` because GSAP owns the transient beats.
`refusedConduit` is a `cva` keyed on `polarity` (amber reroute / red fault).
`dissolveShell` is the flex passthrough; Motion owns the abandon fade.

### Conventions

Transient overlays end GONE (no settled state); CSS never animates. Colour-as-state.

### Invariants And Boundaries

`ghostedLane` applies to the inner conduit path, never the Motion group.

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
| The conduit/flow and transient primitives. | `flowConduit`; `flowPacket`; `scanRing`; `ghostedLane` | dashboard/src/panels/engine-room/flow.styles.ts:5-63 |
| The failure-overlay recipes. | `refusedConduit`; `fleetingBox`; `stopBar`; `abandonRecord` | dashboard/src/panels/engine-room/flow.styles.ts:65-93; dashboard/src/panels/engine-room/flow.styles.ts:102-141; dashboard/src/panels/engine-room/flow.styles.ts:143-177 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the flow
  style domain split from `engineRoomStyles.ts`. Verification pinned to the leaf base
  until closeout stamps the code commit.
