# dashboard/src/panels/review/familyWalkMerge.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/familyWalkMerge.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T22:35:02+02:00 |
| lastVerifiedCommitHash |  `3dc2ab0cf59cdc87ec478f6563d4ac6696871076`|
| lastVerifiedCommitDate |  2026-09-30T23:11:04+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

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

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| **The module's own statement of the split: the read cycle decides when, this module owns what.** | "decides WHEN a continuation is admitted" | dashboard/src/panels/review/familyWalkMerge.ts:1-5 |
| Exact member merge: same revision, unchanged recorded content and claims, nothing erased. | `mergeMember` | dashboard/src/panels/review/familyWalkMerge.ts:15-35 |
| Side merge only within the same walk. | `mergeFamilySide`; `sameFamilyWalk` | dashboard/src/panels/review/familyWalkMerge.ts:37-60; dashboard/src/panels/review/familyWalkMerge.ts:62-74 |
| The admission conditions on the whole payload. | `admittedFamilyContinuation` | dashboard/src/panels/review/familyWalkMerge.ts:76-102 |
| The exported merge, and its statement that it is presentation, not authority. | `mergeFamilyContinuation` | dashboard/src/panels/review/familyWalkMerge.ts:116-170 |
| The read cycle's one caller: a `null` merge becomes a failed read. | `familyContinuationRead`; `mergeFamilyContinuation` | dashboard/src/panels/review/ReviewReadCycle.ts:249-270 |
| The mounted continuation cases that pin it. | "retains the coherent display and fails a rejected continuation, including a structured page refusal" | dashboard/src/panels/review/ReviewReadCycle.family.test.tsx:145-213 |
| The walk keeps the change facts of every returned member (MIK-L33). | `walkedChangeKinds`; "...walkedChangeKinds(known, entry)," | dashboard/src/panels/review/familyWalkMerge.ts:104-112; dashboard/src/panels/review/familyWalkMerge.ts:149-149 |
| The union rule it applies. | `mergeChangeKinds` | dashboard/src/panels/review/changeTriage.ts:192-200 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-30T22:35:02+02:00 — 260928-MIK-L33 curator (staged change set on `ar/260928-mik-l33`, code base `c052b2593b85d9baf425cc1d5c46f384b13fc9ea`; review R1 changes-required, R2 and R3 pass-with-notes, each followed by a fix round, with the merge round after MIK-L34): **body updated for MIK-R33:** `walkedChangeKinds` unions the change facts of an admitted continuation with the displayed entry's through `changeTriage.mergeChangeKinds` (a dataset review gains none); Logic and Conventions updated, two rows added. The other moved rows were re-pointed by the installed fixer or the exact base-to-staged line shift.
- 2026-09-28T21:46:34+02:00 — 260921-ICR-L48 curator (uncommitted candidate tree `ac73216e2a763b72844a63b8c36c81f9a8b5f0e8` over code base `cb1b942af60a7ed5006ac992075d2bf96aeb9fa7`): **created this one-to-one card for the roster-walk merge moved out of `ReviewReadCycle.ts` (L47-R1-F5 budget).** The curator verified each of the five functions is identical to its base declaration in the read cycle (only `export` added to `mergeFamilyContinuation`). The L38 contract the read-cycle card carried (exact member merge, independent side walks, presentation not authority) is restated here as current intent; its history stays on the read-cycle card. The verification hash and date are blank because no commit contains this file yet; closeout owns the stamp.
