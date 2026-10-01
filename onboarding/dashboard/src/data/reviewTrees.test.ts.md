# dashboard/src/data/reviewTrees.test.ts

## Governing Overview

[dashboard/src/data route overview](overview.md)

## Purpose

**The MIK-R25 adapter cases over the REAL route body of a converted leaf, and since MIK-L31 the wire convention
and the cards address (8 cases).** `reviewTrees.captured.json` is the measured body of `GET /api/review/trees`
served by `create_app(config, collaborators=serving_collaborators(config))` over the MIK-L31 worker's scratch copy
(the real memory repository converted with the worktree's own `knowledge-convert`; a leaf that edits `_not_listed`
in `review_source_admission.py`, re-anchors `RLZ-CXH58B4W` and declares two expected effects; re-captured by
MIK-L31 from L25's). Only `fetch` is stubbed, so the URL and the body travel the way the browser's do.

## Code Commentary

### Logic

- **The tree view of a converted leaf:** the four trees (code base `8a2d4b47`), the pinning refs (under
  `refs/ar/review/260928_maintained-invariant-knowledge/260928-MIK-L31/1`, the directory-name namespace of ruling
  02:32:42 (a)) and both knowledge sides; the currentness read through `code_tree.tree_id`; the memory diff grouped by record and by source path with currentness per
  side; the worklist items, their history rows without a currency mark, and the gate linkage.
- **One wire convention (MIK-L25 review F9, settled by MIK-L31):** no camelCase key anywhere in the real body,
  including the owners' own documents (`stale_members`, `owner_kind` present); `treeComparisonNumber` reads
  `review:trees:<n>` and nothing else, and `reviewTrees` sends `invariants=a,b` with `comparison=7`.
- **The answers that are not a tree view:** an unconverted leaf, a refusal and an unreadable body kept apart; a
  recorded comparison addressed by number and never by path; a side read from a partial index or lost to history
  is named.

### Conventions

- The expectations were updated when the fixture was recaptured under the directory-name refs (L25 worker round 5),
  and again when MIK-L31 re-captured it from its own scratch leaf (leaf, refs, code base and history file names).

### Invariants And Boundaries

- The body is test evidence from scratch copies, not current project knowledge.

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured; the requirement packet `MIK-R25@v1` and its rulings
(`25_reviewer-on-git-trees.json`) live outside the code and memory repositories, so they are named here and not
cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The real captured body. [1]
- The tree view of a converted leaf. [2]
- One wire convention, and the comparison and selection a request names. [3]
- The answers that are not a tree view. [4]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
