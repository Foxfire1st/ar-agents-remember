# dashboard/src/panels/review/worklistGroups.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/worklistGroups.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T09:59:20+02:00 |
| lastVerifiedCommitHash | `b54d1b0331f67454bcf245a7a338b04900181c3c`|
| lastVerifiedCommitDate | 2026-09-30T11:03:56+02:00|
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
  absent), sorted, with a count per file. MIK-R32's lane owns their disposition; this is the structure it plugs into.
- **Rows by `facts.row` (PS-1, accepted at 05:36:19).** `rowSubjects` returns the item's own subject and, when
  different, the subject its `facts.row` names: an unexplained hunk is answered by a `hunk:…` row, so the row is
  found by that subject. The server's `_row_subjects` does the same when it collects the rows.
- **`planningMarks`** maps each invariant or family subject with a planning mark to `<kind> · <planning>` (for
  example `touched invariant · planned`), for the card voices.
- **`hunkLinkage`** counts a changed file's linked hunks and reads its file-level link.

### Conventions

- Snake_case wire keys throughout (`history_rows`, `satisfied_by`, `file_level`).

### Invariants And Boundaries

- Grouping only: no disposition is offered or decided (L32 owns it).
- Card planning marks come from here only through `FamilyReviewCenter.pinnedWorklist`, which passes the worklist of a
  leaf-wide read of the same comparison and nothing otherwise (see the candidate invariant on that card).

### Todos

- **L32:** disposition of the unexplained groups.

## Docs References

No domain documentation source is configured; the requirement packets and rulings live outside the code and memory
repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own statement: grouping only, and the four groups. | "Grouping only"; "(MIK-R32) owns their disposition" | dashboard/src/panels/review/worklistGroups.ts:1-11 |
| The group shapes. | `WorklistEntry`; `UnexplainedGroup`; `WorklistGroups` | dashboard/src/panels/review/worklistGroups.ts:22-38 |
| Rows found by the item's subject and by its `facts.row`. | `rowSubjects`; `entryOf` | dashboard/src/panels/review/worklistGroups.ts:41-44; dashboard/src/panels/review/worklistGroups.ts:46-49 |
| Unexplained items by file, then coverage state. | `coverageState`; `unexplainedGroups` | dashboard/src/panels/review/worklistGroups.ts:51-56; dashboard/src/panels/review/worklistGroups.ts:58-76 |
| The four groups. | `worklistGroups` | dashboard/src/panels/review/worklistGroups.ts:78-99 |
| The cards' planning marks and the hunk linkage. | `planningMarks`; `hunkLinkage` | dashboard/src/panels/review/worklistGroups.ts:102-109; dashboard/src/panels/review/worklistGroups.ts:112-123 |
| The server's matching row lookup. | `_row_subjects` | mcp/src/agents_remember/application/review_tree_knowledge.py:510-516 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T09:59:20+02:00 — 260928-MIK-L31 curator (staged change set on `ar/260928-mik-l31`, code base `48f680d5b95b8cb6eafff4f1ccd19c8f32e8c48c`; review R3 pass-with-notes): created this card for the new module, recording the carried rulings (L11 the planning marks, L10 the grouping) and PS-1 (the `facts.row` lookup, accepted at 05:36:19). The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
