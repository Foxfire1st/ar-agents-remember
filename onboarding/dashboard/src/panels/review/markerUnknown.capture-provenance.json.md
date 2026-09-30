# dashboard/src/panels/review/markerUnknown.capture-provenance.json

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/markerUnknown.capture-provenance.json` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T20:26:08+02:00 |
| lastVerifiedCommitHash | `d3a22213ad3124603b0210afb7e3d049c5589b82`|
| lastVerifiedCommitDate | 2026-09-30T20:52:55+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**The receipt of the rulings round's seven bodies: six of comparison 3 and the comparison-2 card entries.** It names
the capture time (2026-09-30T14:30:58Z), the producer (`notes/reports/260928-MIK-L34-evidence/capture_rulings_fixtures.py`)
and its command, the route (`create_app` over a FastAPI `TestClient`), the source tree (the L34 worktree on base
`904e804b` with its uncommitted changes; no server file changed), the scratch (as in `markerReturn.capture-provenance.json`,
then `setup_leaf.py break-family`: the leaf's FAM-4V4GSQCS record made `{}` on the after side, so the after memory
tree is not read whole, which is comparison 3), the comparisons per file set, the attempts, and one row per body.

## Code Commentary

### Logic

- Six comparison-3 rows: the task-context review, the lane, `notes.py`'s classification, its source content (the same
  bytes as comparison 2's), INV-Z66EMHMH's review (`memberUnknown`) and INV-413DC8XE's review (`noFamily`).
- One comparison-2 row: the tree view's entries for the five invariants INV-Z66EMHMH's view asks for
  (`invariants=` their keys), captured for the card-excerpt assertions (`markerReturn.cards.captured.json`).

### Conventions

Keep the captured bytes and their receipt intact; a recapture rewrites both.

### Invariants And Boundaries

These are scratch-copy captures, not current project knowledge. All seven sha256 values match the fixtures (checked by this curation).

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
| When, by what command, at which source tree and over which broken scratch record the bodies were captured. | "captured_at"; "source_tree"; "break-family" | dashboard/src/panels/review/markerUnknown.capture-provenance.json:2-12 |
| One receipt row per captured body, the card entries last. | "\"fixtures\": ["; "src/panels/review/markerReturn.cards.captured.json" | dashboard/src/panels/review/markerUnknown.capture-provenance.json:13-118 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T20:26:08+02:00 — 260928-MIK-L34 curator (staged change set on `ar/260928-mik-l34`, code base `904e804b07a598d5d6c66f06b7e67ddab64d9b8e`; reviews R1 to R3 changes-required, each followed by a fix round): created this card for the new capture receipt of the rulings round's seven bodies. The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
