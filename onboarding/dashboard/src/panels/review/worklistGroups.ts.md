# dashboard/src/panels/review/worklistGroups.ts

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**The leaf's MIK-R08 worklist as the reviewer reads it: grouping only (MIK-R25 rule 3, MIK-R11 rule 7, MIK-R10).**
Every item is shown as the worklist recorded it, with the history rows about the subject it answers to; nothing here
decides whether a row answers an item. `LeafKnowledgeChanges.tsx` renders the groups, and `FamilyReviewCenter.tsx`
takes the cards' planning marks from `planningMarks`.

## Code Commentary

### Logic

- **`worklistGroups`** splits the items into: knowledge items (those carrying MIK-R11's `planning` mark),
  `planned_untouched` items (the declared effects no row delivered), unexplained items (`unexplained_hunk` and
  `unexplained_file`) and every other kind, listed by kind.
- **Unexplained grouping (carried from L10, ruling 2026-09-30T01:56:39).** Items can be numerous (160 on ICR L47), so
  `unexplainedGroups` groups them by `facts.path` and then by `facts.coverage.state` (`coverage not recorded` when
  absent), sorted, with a count per file. Since MIK-L32 the unexplained-changes lane shows an opened file's groups
  from here (`LaneFileFocus.GateItems` filters `unexplained` by path); MIK-R32 excludes any disposition, so nothing
  here or there offers one. The module header says so too: the items are answered by MIK-R10's history rows, which
  the closeout gate enforces, and this structure and the lane only list them.
- **Rows by `facts.row` (PS-1, accepted at 05:36:19).** `rowSubjects` returns the item's own subject and, when
  different, the subject its `facts.row` names: an unexplained hunk is answered by a `hunk:…` row, so the row is
  found by that subject. The server's `_row_subjects` does the same when it collects the rows.
- **`planningMarks`** maps each invariant or family subject with a planning mark to `<kind> · <planning>` (for
  example `touched invariant · planned`), for the card voices.
- **`hunkLinkage`** counts a changed file's linked hunks and reads its file-level link.

### Conventions

- Snake_case wire keys throughout (`history_rows`, `satisfied_by`, `file_level`).

### Invariants And Boundaries

- Grouping only: no disposition is offered or decided. MIK-L32's lane reuses the grouping for display and adds none
  (MIK-R32's Exclusions forbid assessment, approval or waiver of unexplained changes).
- Card planning marks come from here only through `FamilyReviewCenter.pinnedWorklist`, which passes the worklist of a
  leaf-wide read of the same comparison and nothing otherwise (see the candidate invariant on that card).

### Todos

- **Resolved by MIK-L32:** the lane consumes the unexplained groups for display only and adds no disposition control
  (MIK-R32's Exclusions).
- **Resolved in MIK-L32 (the coordinator's comment-only fix):** the module header (lines 9-10) now says the
  unexplained items "are answered by history rows (MIK-R10) that the closeout gate enforces; this structure and the
  MIK-R32 lane only list them", which matches MIK-R32's Exclusions.

## Evidence

### Docs References

No domain documentation source is configured; the requirement packets and rulings live outside the code and memory
repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The lane's gate items for one opened file, from the unexplained groups (MIK-L32). [1]
- The module's own statement: grouping only, the four groups, and that history rows answer the unexplained items while this structure and the lane only list them. [2]
- The group shapes. [3]
- Rows found by the item's subject and by its `facts.row`. [4]
- Unexplained items by file, then coverage state. [5]
- The four groups. [6]
- The cards' planning marks and the hunk linkage. [7]
- The server's matching row lookup. [8]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
