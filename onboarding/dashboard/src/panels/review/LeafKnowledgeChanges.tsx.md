# dashboard/src/panels/review/LeafKnowledgeChanges.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/LeafKnowledgeChanges.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T22:35:02+02:00 |
| lastVerifiedCommitHash | `3dc2ab0cf59cdc87ec478f6563d4ac6696871076`|
| lastVerifiedCommitDate | 2026-09-30T23:11:04+02:00|
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
- **`UnexplainedGroups`** (exported): one disclosure per file, split by coverage state, each item listed with its
  rows. It offers and decides no disposition (ruling 2026-09-30T01:56:39, carried from L10); the module header says
  history rows (MIK-R10) answer the unexplained changes and neither this panel nor the lane decides them. Since MIK-L32 the
  unexplained-changes lane reuses it, not a copy: `LaneFileFocus.GateItems` renders an opened file's gate items (the
  `worklistGroups(...).unexplained` groups for that path) through it, beside the lane's own classification.

### Conventions

- Grouping comes from `worklistGroups.ts`; this file only renders. Every key it reads is snake_case (MIK-L25
  review F9, settled here).

### Invariants And Boundaries

- It never writes a current or stale mark on a history row (MIK-R09 owns that rule).
- A dataset review has no tree read, so this panel is never mounted for one.

### Todos

- **Resolved by MIK-L32:** the lane plugs into `UnexplainedGroups` for display only. MIK-R32 adds no disposition
  control: its adopted Exclusions forbid any assessment, approval or waiver of unexplained changes, so the gate's
  items are shown with the history rows that answer them and nothing more.
- **Resolved in MIK-L32 (the coordinator's comment-only fix):** the module header (line 5) now says of the
  unexplained changes that "history rows (MIK-R10) answer them, and neither this panel nor the lane decides them",
  which matches MIK-R32's Exclusions. (The comment above `UnexplainedGroups`, "The structure the unexplained-changes
  lane (MIK-R32) plugs into", was already accurate: the lane renders through it.)

## Docs References

No domain documentation source is configured; the requirement packets `MIK-R25@v1` and `MIK-R31@v1` and their rulings
live outside the code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own statement: what the panel shows, and that history rows answer the unexplained changes while neither the panel nor the lane decides them. | "history rows (MIK-R10) answer them, and neither this panel nor the lane decides them." | dashboard/src/panels/review/LeafKnowledgeChanges.tsx:1-5 |
| The lane's focused file renders its gate items through this structure (MIK-L32). | "return <UnexplainedGroups groups={groups} />;" | dashboard/src/panels/review/LaneFileFocus.tsx:480-480 |
| The panel: status line with the comparison mismatch, degraded sides, diff, currentness, worklist. | `LeafKnowledgeChanges`; `worklistStatus` | dashboard/src/panels/review/LeafKnowledgeChanges.tsx:49-82; dashboard/src/panels/review/LeafKnowledgeChanges.tsx:84-89 |
| The diff by record, by source path, and history and other files. | `FileChange`; `KnowledgeDiff` | dashboard/src/panels/review/LeafKnowledgeChanges.tsx:91-103; dashboard/src/panels/review/LeafKnowledgeChanges.tsx:105-155 |
| Currentness per side. | `sideCounts`; `Currentness` | dashboard/src/panels/review/LeafKnowledgeChanges.tsx:157-164; dashboard/src/panels/review/LeafKnowledgeChanges.tsx:166-201 |
| Each item with its planning mark and its history rows. | `Rows`; `ItemLine` | dashboard/src/panels/review/LeafKnowledgeChanges.tsx:203-211; dashboard/src/panels/review/LeafKnowledgeChanges.tsx:213-232 |
| The unexplained groups the lane plugs into. | `UnexplainedGroups` | dashboard/src/panels/review/LeafKnowledgeChanges.tsx:236-263 |
| Knowledge items, planned effects, other kinds, unexplained groups and the gate linkage. | `Worklist` | dashboard/src/panels/review/LeafKnowledgeChanges.tsx:265-321 |
| Where the centre mounts it, only from a tree read. | `knowledgePanel` | dashboard/src/panels/review/FamilyReviewCenter.tsx:986-999 |
| On real data: the `planned_untouched` item, and the mismatch sentence for another comparison. | "planned_untouched"; "this view reads comparison 2, the review shows comparison 1" | dashboard/src/panels/review/ReviewSurface.gitTrees.test.tsx:201-226; dashboard/src/panels/review/ReviewSurface.gitTrees.test.tsx:306-308 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History
- 2026-09-30T22:35:02+02:00 — 260928-MIK-L33 curator (staged change set on `ar/260928-mik-l33`, code base `c052b2593b85d9baf425cc1d5c46f384b13fc9ea`; review R1 changes-required, R2 and R3 pass-with-notes, each followed by a fix round, with the merge round after MIK-L34): No content impact: citation repair only; this document's own source is unchanged by MIK-L33. Rows citing MIK-L33's changed sources (`FamilyReviewCenter.tsx`) moved with the leaf's inserted lines: 1 passing row(s) normalised by the fixer. No claim wording changed, and no verification stamp was advanced.
- 2026-09-30T20:14:26+02:00 — 260928-MIK-L34 curator (staged change set on `ar/260928-mik-l34`, code base `904e804b07a598d5d6c66f06b7e67ddab64d9b8e`; reviews R1 to R3 changes-required, each followed by a fix round): No content impact: MIK-R34 inserted lines above `GateItems` in `LaneFileFocus.tsx` and one import line in `FamilyReviewCenter.tsx`. The generated repair above re-points the `UnexplainedGroups` call row (`374-391` → `480-480`), and the fixer normalised the `knowledgePanel` row (`975-988` → `976-989`). Claims unchanged. No stamp advanced.
- 2026-09-30T18:06:06+00:00: Generated citation repair: "return <UnexplainedGroups groups={groups} />;" repointed to dashboard/src/panels/review/LaneFileFocus.tsx:480-480. No content impact: mechanical anchor-range projection bound to citation source snapshot dd511ab0f1e150e6e017fdffb93a370d587225cb8c691b071ace179d457746ab; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T14:52:40+02:00 — 260928-MIK-L32 curator (staged change set on `ar/260928-mik-l32`, now 35 files over code base `07d6584afba8a9504e4a3cf2e80eac41f68b28a9`): **body update; this card's source is now a change of this leaf.** The coordinator corrected the stale module header (line 5, comment text only, line count unchanged): the unexplained changes are answered by "history rows (MIK-R10) ... and neither this panel nor the lane decides them." The stale-comment Todo is resolved, Logic records the header's statement, and one row is added for the header. No cited row moved: the line count is unchanged, and no row quoted the old header text. No verification stamp was advanced.
- 2026-09-30T14:18:54+02:00 — 260928-MIK-L32 curator (staged change set on `ar/260928-mik-l32`, code base `07d6584afba8a9504e4a3cf2e80eac41f68b28a9`; review R1 pass-with-notes, fixes, R2 pass): this card's source is unchanged. **Body update: the L32 Todo is resolved.** `UnexplainedGroups` is now reused by the lane's `LaneFileFocus.GateItems` for display only; MIK-R32's adopted Exclusions forbid assessment, approval or waiver, so no disposition control was added; the module-header comment that still assigns disposition to MIK-R32 is recorded as a stale-comment Todo. One row added (the lane's use). The real-data row was re-pointed by the exact base-to-staged shift (`ReviewSurface.gitTrees.test.tsx`). No verification stamp was advanced.
- 2026-09-30T13:23:08+02:00 — 260928-MIK-L35 curator (staged change set on `ar/260928-mik-l35`, code base `ce4594231eac0b18950d22d6aee0d3b9f3eba3db`; review R1 changes-required, R2 pass-with-notes, R2-1 fixed): No content impact: the mount row into `FamilyReviewCenter.tsx`, which this leaf changed, was re-pointed by the installed fixer (its bullet below), and one row into the unchanged `ReviewSurface.gitTrees.test.tsx` was normalised (`249-251` → `250-252`). Claim wording unchanged. No stamp advanced.
- 2026-09-30T11:14:43+00:00: Generated citation repair: `knowledgePanel` repointed to dashboard/src/panels/review/FamilyReviewCenter.tsx:975-988. No content impact: mechanical anchor-range projection bound to citation source snapshot 2597c838ec1e64a918943e8db9f63ef52ddf51fa320d55ca6abc370de5fa8b59; claim bytes unchanged; generated by ccr-r10@v1.

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T09:59:20+02:00 — 260928-MIK-L31 curator (staged change set on `ar/260928-mik-l31`, code base `48f680d5b95b8cb6eafff4f1ccd19c8f32e8c48c`; review R3 pass-with-notes): created this card for the new panel, recording the carried rulings (L25 Q2 the panel, L11 the planning marks, L10 the grouping, PS-1 the `facts.row` lookup) and review F11/R2-3 (the comparison mismatch stated). The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
