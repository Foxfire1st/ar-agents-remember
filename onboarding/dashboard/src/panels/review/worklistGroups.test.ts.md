# dashboard/src/panels/review/worklistGroups.test.ts

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**The worklist grouping cases (2).** The worklist is the real served tree view of the converted scratch leaf
(`../../data/reviewTrees.captured.json`); the unexplained items are built by `hunk()` in exactly the shape of
MIK-R10's `unexplained_hunk` items (`facts.path`, `facts.coverage.state`, `facts.row`), because the captured leaf
has none.

## Code Commentary

### Logic

- **Planning marks and planned effects:** over the real worklist, INV-2TQGXFAX is `planned` and FAM-2HBJREC2
  `unplanned` (`planningMarks` gives `touched invariant · planned`), and the `planned_untouched` items are listed
  apart.
- **Unexplained grouping and the row lookup:** unexplained items across files and coverage states are grouped by
  file, then by coverage state, with a count per file; a history row whose subject is an item's `facts.row` is found
  for that item (`rowSubjects`).

### Conventions

- Pure functions over data; no DOM.

### Invariants And Boundaries

- The derived unexplained items are labelled as shaped after MIK-R10 in the file header; they are not a capture.

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured; the requirement packets live outside the repositories.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The real worklist and the MIK-R10-shaped unexplained items. [1]
- The two cases. [2]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
