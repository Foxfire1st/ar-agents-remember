# dashboard/src/data/reviewTrees.captured.json

## Governing Overview

[dashboard/src/data route overview](overview.md)

## Purpose

**The real leaf-wide `GET /api/review/trees` body of the MIK-L31 worker's converted scratch leaf `260928-MIK-L31`
(test evidence for `reviewTrees.test.ts`, `worklistGroups.test.ts`, `ReviewSurface.gitTrees.test.tsx`, and since MIK-L35
`panels/review/ReviewSurface.wordDiff.test.tsx`, whose stub answers every leaf-wide `/trees` read with it).**
Re-captured by MIK-L31 from L25's capture with this leaf's code (51,212 bytes); its receipt is the fourth entry of
`panels/review/gitTrees.capture-provenance.json` (route, parameters, status, seconds, sha256 and bytes).

## Code Commentary

### Logic

- `state: "trees"` with comparison number `1`, the code base committed at `8a2d4b47`, and both candidates pinned by
  `refs/ar/review/260928_maintained-invariant-knowledge/260928-MIK-L31/1` (the directory-name namespace).
- `code_sides: []` (a live comparison; review F4 fills it on reopen), per-side `currentness`, the
  `knowledge_diff` (3 knowledge files changed, including `knowledge/history/260928-MIK-L31.json`), both
  `knowledge_sides`, and a `worklist` with `source: "computed"`, `bound: true`, state `complete` and 7 items.
- **Every key is snake_case** (MIK-L25 review F9, settled by MIK-L31): the currentness documents carry `code_tree`
  and `stale_members`, and the history row carries `owner_kind`; the test asserts no camelCase key anywhere.
- **MIK-R11's marks and the planned effects (ruling 2026-09-29T21:56:18, carried from L11):** the scratch leaf
  declares two expected effects, so INV-2TQGXFAX is `planned` and FAM-2HBJREC2 `unplanned`, and two
  `planned_untouched` items name the effects no row delivered.
- The body carries no `entries`: the leaf-wide view never does (the cards read is `gitTrees.cards.captured.json`).

### Conventions

Keep the captured bytes and their receipt intact; only the tests read this file.

### Invariants And Boundaries

The body describes scratch copies under `/tmp/mik-l31-real`, not current project knowledge.

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured; the requirement packet `MIK-R25@v1` and its rulings
(`25_reviewer-on-git-trees.json`) live outside the code and memory repositories, so they are named here and not
cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- Comparison 1, both candidates pinned under `refs/ar/review/260928_maintained-invariant-knowledge/260928-MIK-L31/1`. [1]
- No camelCase key anywhere in this body, including the owners' own documents (the test asserts it). [2]
- The two planned effects no row delivered, and the unplanned and planned marks. [3]
- The per-side currentness. [4]
- The memory diff, the knowledge sides, the state and the bound worklist. [5]
- The receipt row for this body, now a path relative to the dashboard. [6]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
