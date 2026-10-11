# dashboard/src/panels/review/LeafKnowledgeChanges.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

Render the leaf's worklist in its own open reading view and the selected record's applicable worklist
items in subject review. The comparison-bound tree read supplies currentness and worklist facts, not
knowledge-file patches. Missing, incomplete, unbound and unavailable measurements stay explicit.

The leaf's worklist as its own open view, plus the worklist items about the selected record under a subject's review. The view reports recorded facts one line per item in open groups, with status, currentness, gate linkage and file lines that open the change-set page. It lists no knowledge file and draws no patch; identifiers close into one list per group.
## Code Commentary

### Read and measurement states

`ReadNotice` renders loading, not-converted, unavailable/recovery and fallback-unavailable states as open
status content. `completeWorklist` requires non-absent source, complete state, comparison binding and no
incomplete entries. `WorklistProblems` names the missing measurement; it never infers no applicable item
or complete gate linkage from an incomplete answer.

### Own worklist view and subject items

- **Status line.** State, item measurement, source and comparison binding; absent/unavailable is not an
  empty measured result. A comparison mismatch is named rather than silently adopted.
- **Degraded sides.** One line for each knowledge side that is not available or was read from a partial
  index (`degradedKnowledgeSides`).
- **No embedded diff.** Neither `KnowledgeDiff` nor the old `LeafKnowledgeChanges`/`LeafKnowledgeNotice`
  exports remain. Memory patches are comparison change-set reads, not worklist content.
- **Currentness** (`Currentness`). Open per-side counts/reasons and non-current invariants not already
  named by worklist items, with their non-current entries and reasons.
- **Worklist groups** (`WorklistGroupsView`). Open knowledge, planned-undelivered, other-kind and
  unexplained-file groups. One line per item exposes recorded state, history and facts; identifiers are
  collected into one disclosure per group. File buttons call `onOpenPath` into the comparison viewer.
- **Gate linkage** (`GateLinkage`). Complete and partial linkage have different text; an absent/incomplete
  measurement does not claim all hunks measured.
- **Subject items** (`SubjectWorklistItems`). Canonical record identity and comparison must match before
  filtering items. Only a complete bound measurement can assert that no item names the selected record.
- The panel offers no disposition of an item. The grouping (`worklistGroups`) and the linkage counts
  (`hunkLinkage`) come from `worklistGroups.ts`; this file renders them.

## Evidence

- The module renders own-view worklist and subject items without patches; history remains recorded fact, not a UI disposition. [11]
- LeafWorklistView composes open status, degraded sides, worklist groups, currentness and gate linkage. [12]
- ReadNotice exposes loading, not-converted and unavailable/recovery states as status content. [13]
- Status distinguishes absent source, complete bound item counts and partial/unbound reported items. [14]
- Open currentness names non-current invariants not already represented in worklist items and their entry reasons. [16]
- Open unexplained groups preserve coverage state and link their paths to the comparison viewer. [17]
- Worklist groups and linkage remain recorded facts, with complete and incomplete measurement distinguished. [18]

- One-line rendering of a worklist entry with facts and state [22]
- Completeness rule for the worklist measurement [23]
- Items about the selected record under a subject review [24]
- Items about the record on the worklist view path [25]
- Grouped open worklist with status, currentness and linkage [26]
- One-line gate linkage of changed hunks to recorded knowledge [27]
- The worklist as its own view in the main page [28]
