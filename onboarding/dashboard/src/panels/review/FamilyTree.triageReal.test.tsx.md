# dashboard/src/panels/review/FamilyTree.triageReal.test.tsx

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

## Evidence

### Docs References

No domain documentation source is configured; the requirement packet `MIK-R33@v1` (adopting `ICR-R32@v1`) and the architect's rulings in `33_review-triage-order-and-change-kind-badges.json` live outside the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The suite's statement: real served answers of a scratch copy with scratch-authored knowledge edits. [1]
- The real family badged, changes first, all 24 members kept. [2]
- An incomplete page is not unreturned members; the shared member and the revised guarantee. [3]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
