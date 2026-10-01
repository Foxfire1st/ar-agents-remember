# dashboard/src/panels/review/familyWalkMerge.ts

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

The merge of one admitted family roster walk: **what** an admitted continuation page looks like once it is
folded into the family context already on screen. The read cycle (`ReviewReadCycle.ts`) decides **when** a
continuation is admitted; this module owns the merge. Moved verbatim out of the read cycle in
`260921-ICR-L48` to bring `ReviewReadCycle.ts` under the file-size rail (539 → 471 lines); the behaviour was
introduced by `260921-ICR-L38` and its history is on [ReviewReadCycle.ts](ReviewReadCycle.ts.md).

## Code Commentary

### Logic

`mergeFamilyContinuation(previous, next, cursor)` is the only export. It returns `null` unless
`admittedFamilyContinuation` holds: the page is a `family_members` continuation continued from exactly
`cursor`, carries no page refusal and is not stale, and the comparison, candidate and primary revision
selection are identical and the family-context entry count matches. It then merges family by family:
`mergeFamilySide` merges a side only when `sameFamilyWalk` holds (same family, side, state, family
revision, guarantee digest and page scope) and otherwise refuses; `mergeMember` keeps the same invariant
revision, refuses a changed recorded payload digest or a changed claim, adds new claims by `claim_id`, and
never lets a sparse later page erase content already delivered. Any refusal returns `null`, which the read
cycle turns into a failed read that keeps the coherent display.

**Change facts across the walk (MIK-L33).** On a tree comparison each admitted page carries the change facts of the
members it returned. `walkedChangeKinds` unions the displayed entry's `change_kinds` with the continuation's through
`changeTriage.mergeChangeKinds`: every occurrence either delivery described is kept and the newer family-level facts
apply, so the tree's badges and breakdown cover every member the walk has returned. A dataset review's entries carry
no facts and gain none.

### Conventions

Pure functions over the review wire types; no React, no state. Only `mergeFamilyContinuation` is exported;
the five helpers are module-private (`walkedChangeKinds` since MIK-L33).

### Invariants And Boundaries

- Presentation of one admitted walk, never another dataset or selection authority: the latest response
  still owns the primary statements, source inventory, evidence and assessments.
- A continuation that does not continue exactly the displayed walk is refused, never partially applied.
- Earlier exact content is never erased by a later sparse page.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- **The module's own statement of the split: the read cycle decides when, this module owns what.** [1]
- Exact member merge: same revision, unchanged recorded content and claims, nothing erased. [2]
- Side merge only within the same walk. [3]
- The admission conditions on the whole payload. [4]
- The exported merge, and its statement that it is presentation, not authority. [5]
- The read cycle's one caller: a `null` merge becomes a failed read. [6]
- The mounted continuation cases that pin it. [7]
- The walk keeps the change facts of every returned member (MIK-L33). [8]
- The union rule it applies. [9]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
