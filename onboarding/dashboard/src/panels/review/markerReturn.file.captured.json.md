# dashboard/src/panels/review/markerReturn.file.captured.json

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/markerReturn.file.captured.json` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T20:26:08+02:00 |
| lastVerifiedCommitHash | `d3a22213ad3124603b0210afb7e3d049c5589b82`|
| lastVerifiedCommitDate | 2026-09-30T20:52:55+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**A real `GET /api/review/trees?comparison=2&file=mcp/src/agents_remember/serving/notes.py` body of the MIK-L34 scratch
leaf: one per-file classification** (10,089 bytes; test evidence for `ReviewSurface.markers.test.tsx`,
`hunkMarkers.test.ts` and `intentMarkerScope.test.ts`).

## Code Commentary

### Logic

- `attributed`, 2 hunks, both `linked`. The L124 edit (before 124,1 / after 124,1) meets INV-Z66EMHMH (RLZ-7X2C4VRQ,
  FAM-4V4GSQCS `member`) and INV-413DC8XE (RLZ-DCXK7W7T, `confirmed_no_family`) on both sides: the marker `2 intents`.
- The L210 deletion (before 210,1 / after 209,0) meets three entries through the before side only: INV-EJW15DXA
  (FAM-4V4GSQCS `member`), INV-ZJS1XY4R (`removed_or_reassigned`) and INV-SMYSQKTJ (`confirmed_no_family`): the
  marker `3 intents`.
- Both knowledge sides' indexes are `complete`.

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
| The per-file response and its two hunks. | "file_classification"; "\"start\": 124"; "\"start\": 210" | dashboard/src/panels/review/markerReturn.file.captured.json:42-207 |
| The two knowledge sides, both indexes complete. | "knowledge_sides" | dashboard/src/panels/review/markerReturn.file.captured.json:382-400 |
| The receipt row for this body. | "src/panels/review/markerReturn.file.captured.json" | dashboard/src/panels/review/markerReturn.capture-provenance.json:40-40 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T20:26:08+02:00 — 260928-MIK-L34 curator (staged change set on `ar/260928-mik-l34`, code base `904e804b07a598d5d6c66f06b7e67ddab64d9b8e`; reviews R1 to R3 changes-required, each followed by a fix round): created this card for the new captured `notes.py` classification (comparison 2). The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
