# dashboard/src/panels/review/markerReturn.cards.captured.json

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/markerReturn.cards.captured.json` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T20:26:08+02:00 |
| lastVerifiedCommitHash | `d3a22213ad3124603b0210afb7e3d049c5589b82`|
| lastVerifiedCommitDate | 2026-09-30T20:52:55+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**A real `GET /api/review/trees?comparison=2&invariants=<five keys>` body of the MIK-L34 scratch leaf: the tree view's
entries INV-Z66EMHMH's view asks for** (20,035 bytes; captured in the rulings round; test evidence for
`ReviewSurface.markers.test.tsx`'s card-excerpt assertions, ruling Q4).

## Code Commentary

### Logic

- Seven `notes.py` entries, all resolved on both sides at blobs `e3e6f8d4` → `9019bea5`: RLZ-7X2C4VRQ (INV-Z66EMHMH,
  L113–127, the `_confined_stat` card holding the L124 edit), RLZ-7RNSV7PG and RLZ-9YY9Y1E1 (the shared `list_notes`
  range L209–220 holding the L210 deletion), RLZ-5KCQCHVQ (INV-Z66EMHMH, L165–193, an unchanged range), and three more
  (INV-DA7D417G, INV-QR24S1VH twice).
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
| The entries, including the changed `_confined_stat` range and the unchanged range. | "\"id\": \"RLZ-7X2C4VRQ\""; "\"id\": \"RLZ-5KCQCHVQ\"" | dashboard/src/panels/review/markerReturn.cards.captured.json:41-283 |
| The receipt row for this body. | "src/panels/review/markerReturn.cards.captured.json" | dashboard/src/panels/review/markerUnknown.capture-provenance.json:104-104 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T20:26:08+02:00 — 260928-MIK-L34 curator (staged change set on `ar/260928-mik-l34`, code base `904e804b07a598d5d6c66f06b7e67ddab64d9b8e`; reviews R1 to R3 changes-required, each followed by a fix round): created this card for the new captured card entries (comparison 2, rulings round). The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
