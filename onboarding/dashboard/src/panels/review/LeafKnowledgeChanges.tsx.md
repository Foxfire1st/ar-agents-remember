# dashboard/src/panels/review/LeafKnowledgeChanges.tsx

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

## Evidence

### Docs References

No domain documentation source is configured; the requirement packets `MIK-R25@v1` and `MIK-R31@v1` and their rulings
live outside the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The module's own statement: what the panel shows, and that history rows answer the unexplained changes while neither the panel nor the lane decides them. [1]
- The lane's focused file renders its gate items through this structure (MIK-L32). [2]
- The panel: status line with the comparison mismatch, degraded sides, diff, currentness, worklist. [3]
- The diff by record, by source path, and history and other files. [4]
- Currentness per side. [5]
- Each item with its planning mark and its history rows. [6]
- The unexplained groups the lane plugs into. [7]
- Knowledge items, planned effects, other kinds, unexplained groups and the gate linkage. [8]
- Where the centre mounts it, only from a tree read. [9]
- On real data: the `planned_untouched` item, and the mismatch sentence for another comparison. [10]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
