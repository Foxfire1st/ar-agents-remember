# dashboard/src/panels/review/familyWalkMerge.ts

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

The merge of one admitted family roster walk: **what** an admitted continuation page looks like once it is folded into the family context already on screen. The read cycle (`ReviewReadCycle.ts`) decides **when** a continuation is admitted; this module owns the merge. Its member merge is also used by the walked family tree.

## Code Commentary

### The continuation merge

`mergeFamilyContinuation(previous, next, cursor)` is the merge the read cycle calls. It returns `null` unless `admittedFamilyContinuation` holds: the page is a `family_members` page in state `continued`, continued from exactly `cursor`, carries no page refusal and is not stale, and the comparison, the candidate and the primary revision selection are identical and the number of family entries matches.

It then merges family by family:

- A family of the continuation must be a family on screen with the same selection; otherwise the merge is refused.
- `mergeFamilySide` merges a side only when `sameFamilyWalk` holds (same family, side, state, family revision, guarantee digest and page scope). A side whose page is not a continuation is another walk resent at its first page and leaves the side on screen as it is. An exact replay of the same page is accepted without change.
- `mergeMember` keeps the same invariant revision, refuses a changed recorded payload digest or a changed claim, adds new claims by `claim_id`, and keeps the member content already recorded, so a sparse later page never erases content already delivered.
- Exactly one side must have continued from the cursor; otherwise the merge is refused.
- A family is marked `recorded` only when every side is complete with all members recorded.

Any refusal returns `null`, which the read cycle turns into a failed read that keeps the coherent display.

`walkedChangeKinds` unions the change facts of the entry on screen with the continuation's through `mergeChangeKinds` of `changeTriage.ts`, so the tree's badges and breakdown cover every member the walk has returned. A dataset review's entries carry no change facts and gain none.

### The member merge is shared

`mergeMember` is exported. The walked tree (`walkedTree.ts`, `mergeSide`) calls it to merge two reads of one member of a family that two answers of one comparison both carry. The rule is the same there: the same invariant revision, no changed recorded payload digest, claims united by `claim_id`, and nothing already delivered erased. When `mergeMember` returns `null` there, the walked tree takes the newer member.

### Conventions

Pure functions over the review wire types; no React, no state. `mergeFamilyContinuation` and `mergeMember` are exported; `mergeFamilySide`, `sameFamilyWalk`, `admittedFamilyContinuation` and `walkedChangeKinds` are module-private. The file is 170 lines.

### Boundaries

- The merge is presentation of one admitted walk, not another dataset or selection authority: the latest response still owns the primary statements, the source inventory, the evidence and the assessments.
- A continuation that does not continue exactly the displayed walk is refused, never partially applied.

## Evidence

- The module's own statement of the split: the read cycle decides when, this module owns what. [11]
- Exact member merge, exported: same revision, unchanged recorded content and claims, nothing erased. [12]
- Side merge only within the same walk. [13]
- The admission conditions on the whole payload. [14]
- The exported merge, and its statement that it is presentation, not authority. [15]
- The walk keeps the change facts of every returned member. [16]
- The union rule it applies. [17]
- The read cycle's caller: a `null` merge becomes a failed read. [18]
- The walked tree's caller of the member merge. [19]
- The mounted continuation case of a rejected continuation that keeps the coherent display. [20]
