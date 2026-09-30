# dashboard/src/panels/review/LeafKnowledgeChanges.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/LeafKnowledgeChanges.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T13:23:08+02:00 |
| lastVerifiedCommitHash | `07d6584afba8a9504e4a3cf2e80eac41f68b28a9`|
| lastVerifiedCommitDate | 2026-09-30T13:46:40+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**The panel that renders MIK-R25 rules 2 and 3 for a tree comparison, carried to MIK-L31 by ruling 2026-09-29T22:22:37
Q2: the leaf's knowledge changes, each side's currentness, and the worklist.** It is a closed `<details>` ("Knowledge
changes in this leaf") placed after the evidence in the centre (open in the unselected centre), fed by the one
leaf-wide `/api/review/trees` read the workspace makes. It shows:

- the Git diff of the two memory trees **by record** (with the entries a sidecar change touched) and **by source
  path**, plus history and other knowledge files, each with its patch;
- **currentness per side** at that side's own code tree, with the counts and every invariant that is not current;
- **the worklist**: knowledge items with MIK-R11's `planned`/`unplanned` mark, the `planned_untouched` items (the
  declared effects no row delivered; ruling 2026-09-29T21:56:18, carried from L11), the other kinds by kind, the
  unexplained items grouped by file and coverage state, and the gate linkage of each changed file (linked hunks of
  all hunks, and the file-level link).

## Code Commentary

### Logic

- **Status line.** `n knowledge file(s) changed · worklist <state> · <k> item(s) · <source>`, "not bound to this
  comparison" when the worklist's pairing is not these four trees, and **"this view reads comparison X, the review
  shows comparison Y"** when the leaf-wide read answered for another comparison (review F11 and R2-3).
- `degradedKnowledgeSides` lines name a knowledge side that is not available or was read from a partial index.
- **Rows.** Each item lists the history rows about its subject (owner, disposition and ID) or "no history row
  about it"; rows about an item are found by its subject and by the subject its `facts.row` names
  (`worklistGroups.rowSubjects`, the PS-1 lookup). Item facts are in a nested disclosure.
- **`UnexplainedGroups`** (exported) is the structure MIK-R32's lane plugs into: one disclosure per file, split by
  coverage state, each item listed with its rows. It offers and decides no disposition (ruling 2026-09-30T01:56:39,
  carried from L10).

### Conventions

- Grouping comes from `worklistGroups.ts`; this file only renders. Every key it reads is snake_case (MIK-L25
  review F9, settled here).

### Invariants And Boundaries

- It never writes a current or stale mark on a history row (MIK-R09 owns that rule).
- A dataset review has no tree read, so this panel is never mounted for one.

### Todos

- **L32:** the unexplained-changes lane's disposition controls plug into `UnexplainedGroups`.

## Docs References

No domain documentation source is configured; the requirement packets `MIK-R25@v1` and `MIK-R31@v1` and their rulings
live outside the code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The panel: status line with the comparison mismatch, degraded sides, diff, currentness, worklist. | `LeafKnowledgeChanges`; `worklistStatus` | dashboard/src/panels/review/LeafKnowledgeChanges.tsx:49-82; dashboard/src/panels/review/LeafKnowledgeChanges.tsx:84-89 |
| The diff by record, by source path, and history and other files. | `FileChange`; `KnowledgeDiff` | dashboard/src/panels/review/LeafKnowledgeChanges.tsx:91-103; dashboard/src/panels/review/LeafKnowledgeChanges.tsx:105-155 |
| Currentness per side. | `sideCounts`; `Currentness` | dashboard/src/panels/review/LeafKnowledgeChanges.tsx:157-164; dashboard/src/panels/review/LeafKnowledgeChanges.tsx:166-201 |
| Each item with its planning mark and its history rows. | `Rows`; `ItemLine` | dashboard/src/panels/review/LeafKnowledgeChanges.tsx:203-211; dashboard/src/panels/review/LeafKnowledgeChanges.tsx:213-232 |
| The unexplained groups the lane plugs into. | `UnexplainedGroups` | dashboard/src/panels/review/LeafKnowledgeChanges.tsx:236-263 |
| Knowledge items, planned effects, other kinds, unexplained groups and the gate linkage. | `Worklist` | dashboard/src/panels/review/LeafKnowledgeChanges.tsx:265-321 |
| Where the centre mounts it, only from a tree read. | `knowledgePanel` | dashboard/src/panels/review/FamilyReviewCenter.tsx:975-988 |
| On real data: the `planned_untouched` item, and the mismatch sentence for another comparison. | "planned_untouched"; "this view reads comparison 2, the review shows comparison 1" | dashboard/src/panels/review/ReviewSurface.gitTrees.test.tsx:188-194; dashboard/src/panels/review/ReviewSurface.gitTrees.test.tsx:250-252 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History
- 2026-09-30T13:23:08+02:00 — 260928-MIK-L35 curator (staged change set on `ar/260928-mik-l35`, code base `ce4594231eac0b18950d22d6aee0d3b9f3eba3db`; review R1 changes-required, R2 pass-with-notes, R2-1 fixed): No content impact: the mount row into `FamilyReviewCenter.tsx`, which this leaf changed, was re-pointed by the installed fixer (its bullet below), and one row into the unchanged `ReviewSurface.gitTrees.test.tsx` was normalised (`249-251` → `250-252`). Claim wording unchanged. No stamp advanced.
- 2026-09-30T11:14:43+00:00: Generated citation repair: `knowledgePanel` repointed to dashboard/src/panels/review/FamilyReviewCenter.tsx:975-988. No content impact: mechanical anchor-range projection bound to citation source snapshot 2597c838ec1e64a918943e8db9f63ef52ddf51fa320d55ca6abc370de5fa8b59; claim bytes unchanged; generated by ccr-r10@v1.

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T09:59:20+02:00 — 260928-MIK-L31 curator (staged change set on `ar/260928-mik-l31`, code base `48f680d5b95b8cb6eafff4f1ccd19c8f32e8c48c`; review R3 pass-with-notes): created this card for the new panel, recording the carried rulings (L25 Q2 the panel, L11 the planning marks, L10 the grouping, PS-1 the `facts.row` lookup) and review F11/R2-3 (the comparison mismatch stated). The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
