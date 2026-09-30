# dashboard/src/panels/review/worklistGroups.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/worklistGroups.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T20:14:26+02:00 |
| lastVerifiedCommitHash | `d3a22213ad3124603b0210afb7e3d049c5589b82`|
| lastVerifiedCommitDate | 2026-09-30T20:52:55+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

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

## Docs References

No domain documentation source is configured; the requirement packets and rulings live outside the code and memory
repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The lane's gate items for one opened file, from the unexplained groups (MIK-L32). | "const groups = worklistGroups(gate.worklist).unexplained.filter((group) => group.path === path);" | dashboard/src/panels/review/LaneFileFocus.tsx:473-473 |
| The module's own statement: grouping only, the four groups, and that history rows answer the unexplained items while this structure and the lane only list them. | "Grouping only"; "They are answered by history rows"; "(MIK-R10) that the closeout gate enforces; this structure and the MIK-R32 lane only list them." | dashboard/src/panels/review/worklistGroups.ts:1-11 |
| The group shapes. | `WorklistEntry`; `UnexplainedGroup`; `WorklistGroups` | dashboard/src/panels/review/worklistGroups.ts:22-25; dashboard/src/panels/review/worklistGroups.ts:27-31; dashboard/src/panels/review/worklistGroups.ts:33-38 |
| Rows found by the item's subject and by its `facts.row`. | `rowSubjects`; `entryOf` | dashboard/src/panels/review/worklistGroups.ts:41-44; dashboard/src/panels/review/worklistGroups.ts:46-49 |
| Unexplained items by file, then coverage state. | `coverageState`; `unexplainedGroups` | dashboard/src/panels/review/worklistGroups.ts:51-56; dashboard/src/panels/review/worklistGroups.ts:58-76 |
| The four groups. | `worklistGroups` | dashboard/src/panels/review/worklistGroups.ts:78-99 |
| The cards' planning marks and the hunk linkage. | `planningMarks`; `hunkLinkage` | dashboard/src/panels/review/worklistGroups.ts:102-109; dashboard/src/panels/review/worklistGroups.ts:112-123 |
| The server's matching row lookup. | `_row_subjects` | mcp/src/agents_remember/application/review_tree_knowledge.py:552-558 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History
- 2026-09-30T20:14:26+02:00 — 260928-MIK-L34 curator (staged change set on `ar/260928-mik-l34`, code base `904e804b07a598d5d6c66f06b7e67ddab64d9b8e`; reviews R1 to R3 changes-required, each followed by a fix round): No content impact: MIK-R34 inserted lines above `GateItems` in `LaneFileFocus.tsx`, so the generated repair above re-points the lane's grouping-call row (`374-391` → `473-473`). The claim is unchanged. No stamp advanced.
- 2026-09-30T18:07:22+00:00: Generated citation repair: "const groups = worklistGroups(gate.worklist).unexplained.filter((group) => group.path === path);" repointed to dashboard/src/panels/review/LaneFileFocus.tsx:473-473. No content impact: mechanical anchor-range projection bound to citation source snapshot dd511ab0f1e150e6e017fdffb93a370d587225cb8c691b071ace179d457746ab; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T14:52:40+02:00 — 260928-MIK-L32 curator (staged change set on `ar/260928-mik-l32`, now 35 files over code base `07d6584afba8a9504e4a3cf2e80eac41f68b28a9`): **body update; this card's source is now a change of this leaf.** The coordinator corrected the stale module header (lines 9-10, comment text only, line count unchanged): the unexplained items "are answered by history rows (MIK-R10) that the closeout gate enforces; this structure and the MIK-R32 lane only list them." The stale-comment Todo is resolved and Logic records the header's statement. **The header row is reworded and re-anchored:** its old quote "(MIK-R32) owns their disposition" no longer exists, so it is anchored on the new line-exact quotes, range unchanged (`1-11`). No other row moved: the line count is unchanged. No verification stamp was advanced.
- 2026-09-30T14:18:54+02:00 — 260928-MIK-L32 curator (staged change set on `ar/260928-mik-l32`, code base `07d6584afba8a9504e4a3cf2e80eac41f68b28a9`; review R1 pass-with-notes, fixes, R2 pass): this card's source is unchanged. **Body update: the L32 Todo is resolved and a claim corrected.** Logic and Invariants no longer say MIK-R32's lane owns the unexplained groups' disposition, and the module header that still says so is recorded as a stale-comment Todo: the lane (`LaneFileFocus.GateItems`) shows an opened file's groups for display only, and MIK-R32's adopted Exclusions forbid assessment, approval or waiver. One row added. The server-lookup row was re-pointed by the installed fixer (its bullet kept). No verification stamp was advanced.
- 2026-09-30T12:05:49+00:00: Generated citation repair: `_row_subjects` repointed to mcp/src/agents_remember/application/review_tree_knowledge.py:552-558. No content impact: mechanical anchor-range projection bound to citation source snapshot d90e1a2e975376af7fa389d4799d24cecbe5d50c1e8d92b1e5b438c088e400a4; claim bytes unchanged; generated by ccr-r10@v1.

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T09:59:20+02:00 — 260928-MIK-L31 curator (staged change set on `ar/260928-mik-l31`, code base `48f680d5b95b8cb6eafff4f1ccd19c8f32e8c48c`; review R3 pass-with-notes): created this card for the new module, recording the carried rulings (L11 the planning marks, L10 the grouping) and PS-1 (the `facts.row` lookup, accepted at 05:36:19). The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
