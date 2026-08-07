# dashboard/src/panels/session-cockpit/sessionRailStyles.ts

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/session-cockpit/sessionRailStyles.ts` |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-07T08:19Z                                           |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f`                  |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
| governingOverview      | `overview.md`                                               |

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

The Panda CSS recipes of the session rail, extracted from `SessionRail.tsx` by the
260731-EFA-L8 split. Owns the rail body, stale banner, attention strip/buttons,
sprint rows, bulk confirm, master box/head/body, leaf groups, and done fold.

## Code Commentary

### Logic

Static atoms plus `attnButton`/`row` `cva` variants; the done-fold collapses
completed leaves.

### Conventions

Tokens; no animation.

### Invariants And Boundaries

The rail must stay vertically scrollable with `minWidth:0` so names ellipsize.

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
| The rail recipes. | `railBody`; `attnButton`; `bulkButton`; `doneFold` | dashboard/src/panels/session-cockpit/sessionRailStyles.ts:3-180 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the rail
  styles module extracted from `SessionRail.tsx`. Verification pinned to the leaf
  base until closeout stamps the code commit.
