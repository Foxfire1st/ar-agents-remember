# dashboard/src/panels/review/markerReturn.source.captured.json

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/markerReturn.source.captured.json` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T20:26:08+02:00 |
| lastVerifiedCommitHash | `d3a22213ad3124603b0210afb7e3d049c5589b82`|
| lastVerifiedCommitDate | 2026-09-30T20:52:55+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**A real `GET /api/review/intent/source-content` body for `serving/notes.py` of the MIK-L34 scratch leaf at trees
`59daf505` → `db68db54`** (28,591 bytes; test evidence for `ReviewSurface.markers.test.tsx`). Its bytes are identical
to `markerUnknown.source.captured.json` (the same content at the same trees).

## Code Commentary

### Logic

- `content`, status `modified`, `current`: the before blob `e3e6f8d4` (12,923 bytes) and the after blob `9019bea5`
  (12,848 bytes), both `present` with their whole texts, the exact objects the classification names, so
  `describesDrawn` holds and the marks are placed.

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
| The expansion: both sides present with the object ids the classification names. | "\"object_id\": \"9019bea5a3b9ace22947a516a78718f1a2d8f123\""; "\"object_id\": \"e3e6f8d4c246e066532296e69563c435200ae08b\"" | dashboard/src/panels/review/markerReturn.source.captured.json:2-36 |
| The receipt row for this body. | "src/panels/review/markerReturn.source.captured.json" | dashboard/src/panels/review/markerReturn.capture-provenance.json:55-55 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T20:26:08+02:00 — 260928-MIK-L34 curator (staged change set on `ar/260928-mik-l34`, code base `904e804b07a598d5d6c66f06b7e67ddab64d9b8e`; reviews R1 to R3 changes-required, each followed by a fix round): created this card for the new captured `notes.py` source content (comparison 2). The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
