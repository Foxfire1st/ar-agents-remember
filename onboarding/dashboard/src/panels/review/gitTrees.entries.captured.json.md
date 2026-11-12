# dashboard/src/panels/review/gitTrees.entries.captured.json

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**A real `GET /api/review/intent/entries` body over the MIK-L31 worker's converted scratch leaf `260928-MIK-L31`
(test evidence for `ReviewSurface.gitTrees.test.tsx`, and since MIK-L35 `ReviewSurface.wordDiff.test.tsx`).** Its receipt is in `gitTrees.capture-provenance.json` (route, status, sha256 and bytes).

## Code Commentary

### Logic

- The entry list of the converted leaf: 108 subjects (94 invariants and 14 families) with their presence, as the review navigation reads it.
- **Re-captured by MIK-L31** from its own scratch leaf: against L25's capture only `leaf_id` changed (`260928-MIK-L25` → `260928-MIK-L31`). (L25's own recapture history is in this card's Update History.)

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

- The subject total: 94 invariants and 14 families. [1]
- The receipt row for this body, now with its request parameters. [2]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
