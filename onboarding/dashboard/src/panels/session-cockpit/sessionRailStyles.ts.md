# dashboard/src/panels/session-cockpit/sessionRailStyles.ts

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/session-cockpit/sessionRailStyles.ts` |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated | 2026-08-11T09:45+02:00 |
| lastVerifiedCommitHash | `d9a1eb82849baea6c0b86735e772a932f4bbdc7c`                  |
| lastVerifiedCommitDate | 2026-08-12T00:45:15+02:00|
| governingOverview      | `overview.md`                                               |

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

Defines the one-line visual grammar for the structural Chats hierarchy and its live occupant rows.

## Code Commentary

### Logic

Sprint, master, leaf, and row styles preserve nesting while `rowShell`, `rowLabelGroup`, and
`rowTitle` constrain live labels. The title uses hidden overflow, ellipsis, and no wrapping so a
replacement or long label cannot expand the rail row vertically.

### Conventions

Structural indentation belongs to sprint/master/leaf containers; runtime state appears as compact
chips inside the row.

### Invariants And Boundaries

- Live row labels are single-line CSS ellipsis.
- Structural nesting must remain visible independently of occupant status.
- Styling must not encode an alternate identity or hierarchy.

### Todos

None.

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Master and leaf containers express real task nesting. | `masterBox` | dashboard/src/panels/session-cockpit/sessionRailStyles.ts:114-167 |
| Row layout constrains identity and action segments. | `rowShell` | dashboard/src/panels/session-cockpit/sessionRailStyles.ts:231-260 |
| The live title is clipped to a single ellipsized line. | `rowTitle` | dashboard/src/panels/session-cockpit/sessionRailStyles.ts:299-309 |

## Cross-Repo References

No cross-repository implementation dependency governs this file.

## Update History

- 2026-08-11T19:58+02:00 — Aligned the current dashboard card for `sessionRailStyles.ts` with its task-document, seat-state, and lifecycle interaction boundaries.
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the rail
  styles module extracted from `SessionRail.tsx`. Verification pinned to the leaf
  base until closeout stamps the code commit.
