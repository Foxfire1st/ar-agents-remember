# dashboard/src/panels/review/FamilyTree.triageReal.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/FamilyTree.triageReal.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T22:21:58+02:00 |
| lastVerifiedCommitHash | `3dc2ab0cf59cdc87ec478f6563d4ac6696871076`|
| lastVerifiedCommitDate | 2026-09-30T23:11:04+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**The family tree over real served answers** of the MIK-L33 worker's converted scratch copy of the real repositories
(`triageReal.family`, `triageReal.shared`; provenance `triageReal.capture-provenance.json`), with scratch-authored
knowledge edits and the changed files' entries re-recorded as a curator does. 3 cases.

## Code Commentary

### Logic

- **FAM-R6R095RW:** all 24 members kept (25 rows: the revised member's two rows); triage order starts
  INV-2E8MG43K `intent` (with "same revision; text differs"), INV-ZS9ZS878 `intent` (`+impl`, both rows), six
  `implementation`, INV-2TQGXFAX `membership`, then unchanged; INV-21SDZECS's repaired stale entry reads "re-anchored
  (stale at base)" in its title; the carried INV-ZY0YMXMQ stays `unchanged`; INV-VPX81HXV reads `implementation` with
  `+unknown` and names RLZ-YRVX77Q4 first (review R2-3); the breakdown reads "2 intent · 6 impl · 1 membership · 0
  unknown of 24".
- **An incomplete roster page is not unreturned members** (ruling 16:22:22 item 8): the family's pages are
  `complete: false` while all 24 are returned, so `j` never stops at its continuation.
- **The shared member and the revised guarantee:** INV-2TQGXFAX `membership` in FAM-R6R095RW and `unchanged` in
  FAM-2HBJREC2, whose own row shows the guarantee `intent`.

### Conventions

Vitest with Testing Library over the two real bodies.

### Invariants And Boundaries

The bodies describe a scratch copy, not current project knowledge; the facts are the scratch leaf's.

### Todos

No additional work is asserted by this card.

## Docs References

No domain documentation source is configured; the requirement packet `MIK-R33@v1` (adopting `ICR-R32@v1`) and the architect's rulings in `33_review-triage-order-and-change-kind-badges.json` live outside the code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The suite's statement: real served answers of a scratch copy with scratch-authored knowledge edits. | "SCRATCH-AUTHORED"; "blob as a curator does" | dashboard/src/panels/review/FamilyTree.triageReal.test.tsx:1-23 |
| The real family badged, changes first, all 24 members kept. | "badges the real family, lists its changes first and keeps all 24 members"; "realization RLZ-4BD3B78H re-anchored (stale at base)" | dashboard/src/panels/review/FamilyTree.triageReal.test.tsx:66-126 |
| An incomplete page is not unreturned members; the shared member and the revised guarantee. | "does not treat an incomplete roster page as unreturned members, so j never stops there"; "shows the shared member where it joined and the revised guarantee on its own row" | dashboard/src/panels/review/FamilyTree.triageReal.test.tsx:128-176 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T22:21:58+02:00 — 260928-MIK-L33 curator (staged change set on `ar/260928-mik-l33`, code base `c052b2593b85d9baf425cc1d5c46f384b13fc9ea`; review R1 changes-required, R2 and R3 pass-with-notes, each followed by a fix round, with the merge round after MIK-L34): created this card for the new real-data tree test (3 cases), recording rulings 2026-09-30T16:22:22 (items 5 and 8) and 18:57:45 ("re-anchored (stale at base)", R2-3). The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
