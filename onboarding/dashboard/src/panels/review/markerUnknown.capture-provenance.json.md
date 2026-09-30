# dashboard/src/panels/review/markerUnknown.capture-provenance.json

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/markerUnknown.capture-provenance.json` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T22:35:02+02:00 |
| lastVerifiedCommitHash | `3dc2ab0cf59cdc87ec478f6563d4ac6696871076`|
| lastVerifiedCommitDate | 2026-09-30T23:11:04+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**The receipt of the rulings round's seven bodies (six of comparison 3 and the comparison-2 card entries), as
re-captured in MIK-L33's merge round.** It names the capture time (2026-09-30T19:12:06Z; MIK-L34's own capture was
14:30:58Z), the producer (MIK-L34's `capture_rulings_fixtures.py` re-run by the MIK-L33 worker from
`notes/reports/260928-MIK-L33-evidence/merge-round/l34-scenario/`) and its command, the route (`create_app` over a
FastAPI `TestClient`), the source tree (the L33 worktree on base `d3a22213`, MIK-L34 landed, with MIK-L33's changes),
the scratch (`/tmp/mik-l33-merge`, as in `markerReturn.capture-provenance.json`,
then `setup_leaf.py break-family`: the leaf's FAM-4V4GSQCS record made `{}` on the after side, so the after memory
tree is not read whole, which is comparison 3), the comparisons per file set, the attempts, one row per body, and a
closing `merge_round` note: `markerUnknown.memberUnknown` now carries FAM-4V4GSQCS's `change_kinds`, every member's
membership unknown with the unparseable after-side record as its reason; the other bodies differ only by scratch
paths, the memory commit, timestamps and comparison digests. MIK-L33's `triageMarker.cards.captured.json` (comparison
3's cards) has its own receipt, `triageMarker.capture-provenance.json`.

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
| One receipt row per captured body, the card entries last, and the merge-round note (MIK-L33). | "\"fixtures\": ["; "src/panels/review/markerReturn.cards.captured.json"; "merge_round" | dashboard/src/panels/review/markerUnknown.capture-provenance.json:13-119 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T22:35:02+02:00 — 260928-MIK-L33 curator (staged change set on `ar/260928-mik-l33`, code base `c052b2593b85d9baf425cc1d5c46f384b13fc9ea`; review R1 changes-required, R2 and R3 pass-with-notes, each followed by a fix round, with the merge round after MIK-L34): **body updated for MIK-L33's merge round** (review R3-3): the receipt now names the merge round's re-capture (time 19:12:06Z, producer, source tree `d3a22213` with MIK-L33's changes, scratch `/tmp/mik-l33-merge`) and its `merge_round` note; the Purpose points to MIK-L33's own `triageMarker` receipt. The fixtures row reworded to name the note and re-measured (`13-118` → `13-119`). All seven sha256 values and byte counts match the bodies (checked by this curation).
- 2026-09-30T20:26:08+02:00 — 260928-MIK-L34 curator (staged change set on `ar/260928-mik-l34`, code base `904e804b07a598d5d6c66f06b7e67ddab64d9b8e`; reviews R1 to R3 changes-required, each followed by a fix round): created this card for the new capture receipt of the rulings round's seven bodies. The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
