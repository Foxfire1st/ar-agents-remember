# dashboard/src/panels/engine-room/flow.styles.ts

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

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

- The conduit/flow and transient primitives. [1]
- The failure-overlay recipes. [2]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.
