# dashboard/src/panels/engine-room/remote.styles.ts

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/engine-room/remote.styles.ts`         |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-07T08:19Z                                           |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`                  |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `overview.md`                                               |

## Governing Overview

[panels/engine-room overview](overview.md)

## Purpose

The remote/PR strip style domain of the Engine Room, split from `engineRoomStyles.ts`
by the 260731-EFA-L8 R6 ruling. Owns the strip header, code-chain and carryover
connectors, and the chip/badge recipes (`remoteChip`, `remoteChipLabel`,
`remoteChipState`, `prBadge`, `prBadgeLabel`, `prBadgeSub`).

## Code Commentary

### Logic

`remoteChip` is a `cva` keyed on tone: planned dashed/muted, live amber outline,
done mint fill. `prBadge` is keyed on open/merged. Connectors are solid amber (code
chain) vs dashed muted (carryover handoff).

### Conventions

Static styles only; the sole motion is the gated fill/stroke transition on a
projection state flip.

### Invariants And Boundaries

These recipes style the strip only; state derivation stays in `remote.tsx`.

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
| The strip/connector recipes. | `remoteStripHeader`; `remoteConnector`; `remoteConnectorCarry` | dashboard/src/panels/engine-room/remote.styles.ts:4-23 |
| The chip and PR badge recipes. | `remoteChip`; `prBadge` | dashboard/src/panels/engine-room/remote.styles.ts:25-80 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the remote
  style domain split from `engineRoomStyles.ts`. Verification pinned to the leaf base
  until closeout stamps the code commit.
