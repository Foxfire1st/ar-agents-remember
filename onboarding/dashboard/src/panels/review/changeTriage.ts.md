# dashboard/src/panels/review/changeTriage.ts

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**The family tree's triage rules as pure functions over the delivered change facts (MIK-R33, ICR-R32@v1 rules 2 to 5).**
Weights, labels and meanings; a family's counts, returned and total, partial and scoped state and weight; the breakdown
text; family and member order; and the union of two deliveries across an admitted roster walk. Nothing here decides a
fact; an entry without `change_kinds` (a dataset review) is left exactly as the landed tree shows it.

## Code Commentary

### Logic

- **Weights and words.** `CHANGE_WEIGHT` (intent 4 > implementation 3 > membership 2 > unknown 1 > unchanged 0),
  `CHANGE_LABEL` (`impl`; "same revision; text differs"), `CHANGE_MEANING` (each kind's accessible meaning).
- **`occurrenceKind`.** A returned member the facts do not describe reads `unknown`, never `unchanged`.
- **`familyTriage`.** Counts the distinct returned occurrences by primary kind. `partial` (members unreturned) is
  `returned < members_total`; only without a total does an incomplete page count as unreturned members, because a
  roster page can be incomplete with every member returned (ruling 16:22:22 item 8). `scoped` is `partial` or no total
  (review R1 F2): the breakdown then covers only the returned members, and the family weighs at least `unknown`. The
  weight is the highest of the guarantee's, the members' and that floor (ruling 16:22:22 item 3; rule 5).
- **`breakdownText`.** "`a` intent · `b` impl · `c` membership · `d` unknown of T", or "… of N returned (T total)",
  or "… of N returned (total unknown)" (review R1 F2).
- **`orderFamilies`.** By weight, then the context's order; `authored` or no facts keeps the landed order.
- **`orderMemberRows`.** By weight (triage order only), then `authored_position` (the family record's `members` list,
  ruling 16:22:22 item 7), then the landed row order; the rows of one occurrence stay together, and no sibling is
  removed. Used by the tree and, on a tree comparison, by the centre's member list (review R1 note: the centre follows
  the tree).
- **`mergeChangeKinds`.** Every occurrence either delivery described is kept; the newer family-level facts apply.

### Conventions

Pure, typed functions exported for the tree, the badges, the centre and the walk merge; 200 lines.

### Invariants And Boundaries

- **Candidate invariant (not ingested): triage order never hides unchanged siblings, and traversal never forces
  unreturned pages to load.** Realized here by `orderFamilies` and `orderMemberRows` (reorder only) and by
  `familyTriage`'s `partial`/`scoped` over the returned members only; with `changeTraversal.ts` (which walks the
  rendered nodes and stops at a partial family's continuation control without activating it). Proved by
  `changeTriage.test.ts` ("lists changes first … keeping every sibling", "scopes a partial page…", "sorts a partial
  family above a complete unchanged one"), `FamilyTree.triage.test.tsx` ("lists changes first and keeps unchanged
  siblings…", "stops at the continuation control…"), `FamilyTree.triageReal.test.tsx` (all 24 members kept; an
  incomplete page is not unreturned members), and the mutations "members ordered without weight", "an incomplete roster
  page counts as unreturned members", "a walk merge forgets earlier facts" and "no stop at a partial family's
  continuation", all caught.
- A total the server could not read never lets the returned members pass for the whole family (`scoped`).

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured; the requirement packet `MIK-R33@v1` (adopting `ICR-R32@v1`) and the architect's rulings in `33_review-triage-order-and-change-kind-badges.json` live outside the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The module's statement: pure functions over the delivered facts; a dataset entry is left as landed. [1]
- Precedence and sort weight, the labels and the accessible meanings. [2]
- An undescribed returned member reads unknown. [3]
- A family's counts, partial and scoped state and weight (item 8; review R1 F2). [4]
- The breakdown text, never the intent count. [5]
- Families and member rows ordered, siblings kept, one occurrence's rows together. [6]
- The union of two deliveries across a roster walk. [7]
- The centre's member list follows the tree's order. [8]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
