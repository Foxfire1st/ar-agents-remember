# dashboard/src/panels/session-cockpit/sessionRailParts.tsx

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/session-cockpit/sessionRailParts.tsx` |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-07T08:19Z                                           |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f`                  |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
| governingOverview      | `overview.md`                                               |

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

The session-rail render parts, extracted from `SessionRail.tsx` by the
260731-EFA-L8 split. Owns the rail row (`RailRow`), bulk confirm, master head/body
blocks, attention markers, and the `BulkTarget` type.

## Code Commentary

### Logic

`RailRow` renders one seat row with chip tone/derived state and action buttons;
`BulkConfirm` renders the sprint/master bulk confirm surface; `RailMasterBlock`
composes the master attention badge/head/body.

### Conventions

Presentational; data comes from the rail model and store.

### Invariants And Boundaries

Actions always route through the rail/seat handlers; no direct store mutation here.

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
| The rail row and bulk parts. | `RailRow`; `BulkConfirm`; `RailMasterBlock` | dashboard/src/panels/session-cockpit/sessionRailParts.tsx:337-411; dashboard/src/panels/session-cockpit/sessionRailParts.tsx:433-467; dashboard/src/panels/session-cockpit/sessionRailParts.tsx:567-650; dashboard/src/panels/session-cockpit/sessionRailParts.tsx:62-62 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the rail
  parts module extracted from `SessionRail.tsx`. Verification pinned to the leaf
  base until closeout stamps the code commit.
