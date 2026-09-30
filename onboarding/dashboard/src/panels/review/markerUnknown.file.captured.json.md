# dashboard/src/panels/review/markerUnknown.file.captured.json

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/markerUnknown.file.captured.json` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T20:26:08+02:00 |
| lastVerifiedCommitHash | `d3a22213ad3124603b0210afb7e3d049c5589b82`|
| lastVerifiedCommitDate | 2026-09-30T20:52:55+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**A real `GET /api/review/trees?comparison=3&file=mcp/src/agents_remember/serving/notes.py` body of the MIK-L34 scratch
leaf after `break-family`** (10,172 bytes; test evidence for `ReviewSurface.markers.test.tsx` and
`MarkerTargetState.test.tsx`).

## Code Commentary

### Logic

- The same two hunks as comparison 2, now with unknown memberships: in L124, INV-Z66EMHMH's before-side FAM-4V4GSQCS
  occurrence and its after-side occurrence (no family) are `membership_unknown`; INV-413DC8XE is `confirmed_no_family`
  before and `membership_unknown` after, so the four occurrences of ruling Q3 sit in one list. In L210 the two
  FAM-4V4GSQCS occurrences are unknown and INV-SMYSQKTJ stays confirmed.
- The after knowledge side's index is `partial`, naming the unparsable family record.

### Conventions

Keep the captured bytes and their receipt intact; a recapture rewrites both.

### Invariants And Boundaries

The body describes the scratch copies under `/tmp/mik-l34-real` (code `59daf505` with the scratch leaf's edits; memory `76f5e91e1` converted with the L34 worktree's `knowledge-convert` and committed as scratch `main` `2e3810ed`), not current project knowledge; its line numbers, blobs and keys are the scratch tree's.

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
| The per-file response with the unknown memberships. | "file_classification"; "\"state\": \"membership_unknown\"" | dashboard/src/panels/review/markerUnknown.file.captured.json:42-204 |
| The partial after index and its problem. | "\"index_state\": \"partial\""; "FAM-4V4GSQCS-Bounded-notes-listing-with-unchanged-meaning.json" | dashboard/src/panels/review/markerUnknown.file.captured.json:379-402 |
| The receipt row for this body. | "src/panels/review/markerUnknown.file.captured.json" | dashboard/src/panels/review/markerUnknown.capture-provenance.json:43-43 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T20:26:08+02:00 — 260928-MIK-L34 curator (staged change set on `ar/260928-mik-l34`, code base `904e804b07a598d5d6c66f06b7e67ddab64d9b8e`; reviews R1 to R3 changes-required, each followed by a fix round): created this card for the new captured `notes.py` classification (comparison 3). The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
