# dashboard/src/panels/review/changeTriage.test.ts

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**The pure triage rules over the store-authored comparison's served bodies** (`triage.family`, `triage.familyPage`,
`triage.familyContinued`, `triage.shared`; the world `mcp/tests/test_review_change_kinds.py` asserts the facts of). 12
cases check that the tree orders, counts and merges the delivered facts and never decides one.

## Code Commentary

### Logic

- **Family triage (5):** counts by delivered primary kind; a partial page scoped to its returned members with the total
  named; a complete-looking family whose total is unknown scoped as "(total unknown)" and weighing at least `unknown`
  (SYNTHETIC: no total; review R1 F2); a family weighed by its own revised guarantee (SYNTHETIC: every member
  unchanged; mutation R-C3); the total said to be unknown rather than invented.
- **Tree order (5):** changes first by weight then authored position, every sibling kept; pure authored order is the
  family record's `members` list; families by their highest member or guarantee weight, then context order; a partial
  family above a complete unchanged one (SYNTHETIC facts); a dataset review (no facts) in its landed order.
- **Roster walk (2):** `mergeFamilyContinuation` keeps the facts of every member the walk returned (strengthened with a
  SYNTHETIC gap after the walk-merge mutation first survived); two deliveries unioned with the newer family facts.

### Conventions

Vitest over captured JSON read from the test's own directory; SYNTHETIC variations are labelled in the case names.

### Invariants And Boundaries

Proves part of the candidate invariant recorded on `changeTriage.ts.md` (order never hides siblings; partial pages scoped).

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured; the requirement packet `MIK-R33@v1` (adopting `ICR-R32@v1`) and the architect's rulings in `33_review-triage-order-and-change-kind-badges.json` live outside the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The suite's statement and its bodies. [1]
- Family triage: counts, partial and scoped breakdowns, the guarantee's weight. [2]
- Tree order: changes first with every sibling kept, pure authored order, families by weight, a dataset review untouched. [3]
- The roster walk keeps every returned member's facts. [4]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
