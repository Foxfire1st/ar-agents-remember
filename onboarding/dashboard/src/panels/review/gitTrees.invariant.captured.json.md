# dashboard/src/panels/review/gitTrees.invariant.captured.json

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/gitTrees.invariant.captured.json` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T03:46:54+02:00 |
| lastVerifiedCommitHash | `8a2d4b478971bf40cca0f24d5e5d24a0844bd563`|
| lastVerifiedCommitDate | 2026-09-30T04:16:14+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**A real `GET /api/review/intent` body over the worker's converted scratch leaf `260928-MIK-L25` (test evidence for
`ReviewSurface.gitTrees.test.tsx`).** Its receipt is in `gitTrees.capture-provenance.json` (route, status, sha256 and bytes).

## Code Commentary

### Logic

- The invariant-selected review of the touched member (`INV-2TQGXFAX`, realized by the re-anchored `RLZ-CXH58B4W`), with both statements and the same tree limitations.
- The fixtures were recaptured under the directory-name refs (ruling 02:32:42 (a)); against round 1 the deltas are the ref rename, comparison `1` → `2`, `review:trees:1` → `review:trees:2`, `code_sides: []` and L11's `planning` marks, all explained by the reviewer's R6 check.

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
| The tree comparison it was read from. | "review:trees:2" | dashboard/src/panels/review/gitTrees.invariant.captured.json:1354-1354 |
| The receipt row for this body. | "gitTrees.invariant.captured.json" | dashboard/src/panels/review/gitTrees.capture-provenance.json:22-22 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T03:46:54+02:00 — 260928-MIK-L25 curator (uncommitted change set on `ar/260928-mik-l25`, code base `3eb034a6ab0493a51da5dcd6d013aa6f27f39496` plus the staged delta): created this card for the new captured fixture. The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
