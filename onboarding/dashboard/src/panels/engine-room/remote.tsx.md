# dashboard/src/panels/engine-room/remote.tsx

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/engine-room/remote.tsx`               |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-07T08:19Z                                           |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`                  |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `overview.md`                                               |

## Governing Overview

[panels/engine-room overview](overview.md)

## Purpose

The remote/PR strip renderers of the Engine Room scene, extracted from
`EnclosureCanvas.tsx` by the 260731-EFA-L8 responsibility split. `RemoteChip` renders
one origin ref as a colour-as-state chip, `PrBadge` the open/merged PR pill, and
`RemoteStrip` the band that orders refs code-first (`origin-feat → PR → origin-main →
origin-mem-main`).

## Code Commentary

### Logic

Chip tone derives from `LandingRefNode` state (planned dashed/muted · live amber
outline · done mint fill). `RemoteStrip` renders the strip only while an enclosure is
landing and drops missing probe refs; the connector wires come from the remote styles.

### Conventions

Refs are coloured by their actual state only; a planned ref is never shown in the live
register. Labels stay readable at the 0.76× canvas scale.

### Invariants And Boundaries

The strip is render-only: it never probes refs itself; refs arrive from the projection.

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
| The strip/band composition and its chip/badge primitives. | `RemoteStrip`; `RemoteChip`; `PrBadge` | dashboard/src/panels/engine-room/remote.tsx:26-55; dashboard/src/panels/engine-room/remote.tsx:56-83; dashboard/src/panels/engine-room/remote.tsx:84-108 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the new
  remote module extracted from `EnclosureCanvas.tsx`. Verification pinned to the leaf
  base until closeout stamps the code commit.
