# dashboard/src/data/reviewTrees.captured.json

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/reviewTrees.captured.json` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T03:46:54+02:00 |
| lastVerifiedCommitHash | `8a2d4b478971bf40cca0f24d5e5d24a0844bd563`|
| lastVerifiedCommitDate | 2026-09-30T04:16:14+02:00|
| governingOverview | `dashboard/src/data/overview.md` |

## Governing Overview

[dashboard/src/data route overview](overview.md)

## Purpose

**The real `GET /api/review/trees` body of the worker's converted scratch leaf `260928-MIK-L25` (test evidence
for `reviewTrees.test.ts`).** Its receipt is the fourth entry of
`panels/review/gitTrees.capture-provenance.json` (route, status, sha256 and bytes).

## Code Commentary

### Logic

- `state: "trees"` with comparison number `2`, code base and memory base committed, and both candidates pinned by
  `refs/ar/review/260928_maintained-invariant-knowledge/260928-MIK-L25/2` (the directory-name namespace; comparison
  2 because the recapture after ruling 02:32:42 (a) wrote a new record rather than reusing one named by the old id).
- `code_sides: []` (a live comparison; review F4 fills it on reopen), per-side `currentness`, the
  `knowledge_diff`, both `knowledge_sides`, and a `worklist` with `bound: true`.
- The worklist items carry `"planning": "unplanned"` (L11's planned marks after the sync), which the reviewer's R6
  check found expected.

### Conventions

Keep the captured bytes and their receipt intact; only the test reads this file.

### Invariants And Boundaries

The body describes scratch copies under `/tmp/mik-l25-real`, not current project knowledge.

### Todos

No additional work is asserted by this card.

## Docs References

No domain documentation source is configured; the requirement packet `MIK-R25@v1` and its rulings
(`25_reviewer-on-git-trees.json`) live outside the code and memory repositories, so they are named here and not
cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The pinned code candidate under the directory-name namespace. | "refs/ar/review/260928_maintained-invariant-knowledge/260928-MIK-L25/2" | dashboard/src/data/reviewTrees.captured.json:10-10 |
| The per-side currentness. | "currentness" | dashboard/src/data/reviewTrees.captured.json:30-30 |
| The memory diff, the knowledge sides, the state and the bound worklist. | "knowledge_diff"; "knowledge_sides"; "worklist" | dashboard/src/data/reviewTrees.captured.json:1482-1547 |
| The receipt row for this body. | "dashboard/src/data/reviewTrees.captured.json" | dashboard/src/panels/review/gitTrees.capture-provenance.json:29-29 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T03:46:54+02:00 — 260928-MIK-L25 curator (uncommitted change set on `ar/260928-mik-l25`, code base `3eb034a6ab0493a51da5dcd6d013aa6f27f39496` plus the staged delta): created this card for the new captured fixture, recording ruling 02:32:42 (a) and review F4 as the body shows them. The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
