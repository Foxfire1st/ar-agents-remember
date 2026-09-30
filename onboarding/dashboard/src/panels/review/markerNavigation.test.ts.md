# dashboard/src/panels/review/markerNavigation.test.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/markerNavigation.test.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T20:26:08+02:00 |
| lastVerifiedCommitHash | `d3a22213ad3124603b0210afb7e3d049c5589b82`|
| lastVerifiedCommitDate | 2026-09-30T20:52:55+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**The workspace's moves for an intent marker (4 cases).** Recording stand-ins for the workspace state's setters and the
navigation's `onSelect` show exactly what a follow selects and what a return restores, in order. Added because the
real review's default selection coincided with the target and let mutation M8 escape.

## Code Commentary

### Logic

- **Following (2).** The invariant's own review at its member row of the named family (`onSelect` with
  `{ kind: 'invariant', id }` and `{ familyId, memberRevisionId }`, after `setOpenPath null`); the invariant alone when
  no family records it.
- **The return (2).** The subject and family, then the lane, the opened file, the layout and the full-file choice, with
  the tree's focus request cleared; without navigation the family selection is restored directly.

### Conventions

- `workspace()` and `navigation()` record each call as a line.

### Invariants And Boundaries

- Pins ICR-R34 rules 2 and 3's workspace moves (mutation M8).

### Todos

No additional work is asserted by this card.

## Docs References

No domain documentation source is configured; the requirement packet `MIK-R34@v1` (adopting `ICR-R34@v1`), the adopted `ICR-R24@v3` item 2 and the architect's rulings live outside the code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Following a marker. | "selects the invariant's own review at its member row of the named family"; "selects the invariant alone when no family records it" | dashboard/src/panels/review/markerNavigation.test.ts:43-68 |
| The return. | "restores the subject, then the lane, the opened file, the layout and the full-file choice" | dashboard/src/panels/review/markerNavigation.test.ts:70-94 |
| The moves under test. | `workspaceMarkerMoves` | dashboard/src/panels/review/markerNavigation.ts:24-42 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T20:26:08+02:00 — 260928-MIK-L34 curator (staged change set on `ar/260928-mik-l34`, code base `904e804b07a598d5d6c66f06b7e67ddab64d9b8e`; reviews R1 to R3 changes-required, each followed by a fix round): created this card for the new moves test module MIK-R34 adds (4 cases). The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
