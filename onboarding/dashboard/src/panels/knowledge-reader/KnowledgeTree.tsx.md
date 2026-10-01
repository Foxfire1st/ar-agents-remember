# dashboard/src/panels/knowledge-reader/KnowledgeTree.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**The knowledge reader's explorer (MIK-R29 rule 1): the repository's directories and files at the selected
memory tree, one level per read, each child with its knowledge entry count.** A path known only to the
onboarding mirror (a card whose code is gone) is listed and marked "(onboarding only)"; a code tree that cannot
be listed is named, and the onboarding mirror is still shown.

## Code Commentary

### Logic

- **Lazy levels.** `useTreeLevels` asks one `tree` read per opened directory (the root `''` and the ancestors of
  the current path are open from the start) and keeps each level's answer, loading state or failure.
- **Stale answers dropped (ruling 2026-09-30T09:42:58, F13).** Each read remembers the (repository, memory
  tree) it was asked for; an answer that lands after either changed is another tree's listing and is dropped,
  and the levels are reset on a switch.
- **Rows.** `TreeNode` shows the toggle for a directory, the name (the current path highlighted), the entry
  count, and "(onboarding only)" when `inCode` is false. It only descends into a child that lies below its
  directory, so a listing that says otherwise is never followed.
- **Failures named.** `TreeLevel` shows a failed level's detail (`tree-unavailable`) and, above a listed level,
  the code side's state when it is not `listed` (`tree-code-unavailable`), for example a commit with no
  `Code-Commit` trailer.
- **Navigation.** Clicking a name calls `onOpen`, which the panel turns into a path address (a URL change); the
  repository row opens the root summary.

### Conventions

- Panda CSS owns the looks; the tree is a `nav` labelled "Repository paths".

### Invariants And Boundaries

- An unlisted code tree is named, never shown as an empty directory.
- Proved by the dashboard's navigation case (explorer counts, clicks change the hash) and the stale-answer case
  (the pinned commit's listings held, the selector switched back, then released: nothing lands); removing the
  guard fails it.

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured for this repository. The design authority is the requirement
packet `MIK-R29@v1` with its rulings in `29_path-based-knowledge-reader.json`; they live outside the code and
memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The component's own statement of the explorer. [1]
- One read per opened level; an answer after a switch is dropped (F13). [2]
- A row: toggle, name, count, "(onboarding only)"; descends only below its directory. [3]
- A level, with a failed read and an unlisted code tree named. [4]
- The explorer, with the current path's ancestors open. [5]
- The stale-answer case. [6]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
