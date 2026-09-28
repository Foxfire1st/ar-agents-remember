# dashboard/src/panels/review/familyWalkMerge.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/familyWalkMerge.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-28T21:46:34+02:00 |
| lastVerifiedCommitHash |  `ae2fd5c864aa2609ae45b5c7dbbaa693569aefc6`|
| lastVerifiedCommitDate |  2026-09-28T22:11:57+02:00|
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

### Conventions

Pure functions over the review wire types; no React, no state. Only `mergeFamilyContinuation` is exported;
the four helpers are module-private.

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
| Exact member merge: same revision, unchanged recorded content and claims, nothing erased. | `mergeMember` | dashboard/src/panels/review/familyWalkMerge.ts:13-33 |
| Side merge only within the same walk. | `mergeFamilySide`; `sameFamilyWalk` | dashboard/src/panels/review/familyWalkMerge.ts:35-58; dashboard/src/panels/review/familyWalkMerge.ts:60-72 |
| The admission conditions on the whole payload. | `admittedFamilyContinuation` | dashboard/src/panels/review/familyWalkMerge.ts:74-100 |
| The exported merge, and its statement that it is presentation, not authority. | `mergeFamilyContinuation` | dashboard/src/panels/review/familyWalkMerge.ts:102-157 |
| The read cycle's one caller: a `null` merge becomes a failed read. | `familyContinuationRead`; `mergeFamilyContinuation` | dashboard/src/panels/review/ReviewReadCycle.ts:249-270 |
| The mounted continuation cases that pin it. | "retains the coherent display and fails a rejected continuation, including a structured page refusal" | dashboard/src/panels/review/ReviewReadCycle.family.test.tsx:137-205 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-28T21:46:34+02:00 — 260921-ICR-L48 curator (uncommitted candidate tree `ac73216e2a763b72844a63b8c36c81f9a8b5f0e8` over code base `cb1b942af60a7ed5006ac992075d2bf96aeb9fa7`): **created this one-to-one card for the roster-walk merge moved out of `ReviewReadCycle.ts` (L47-R1-F5 budget).** The curator verified each of the five functions is identical to its base declaration in the read cycle (only `export` added to `mergeFamilyContinuation`). The L38 contract the read-cycle card carried (exact member merge, independent side walks, presentation not authority) is restated here as current intent; its history stays on the read-cycle card. The verification hash and date are blank because no commit contains this file yet; closeout owns the stamp.
