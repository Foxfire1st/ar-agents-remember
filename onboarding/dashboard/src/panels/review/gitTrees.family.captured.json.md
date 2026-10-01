# dashboard/src/panels/review/gitTrees.family.captured.json

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**A real `GET /api/review/intent` body over the MIK-L31 worker's converted scratch leaf `260928-MIK-L31` (test
evidence for `ReviewSurface.gitTrees.test.tsx`, `ExpressionCards.test.tsx`, since MIK-L35
`IntentWordDiff.test.tsx` and `ReviewSurface.wordDiff.test.tsx`, and since MIK-L34 `IntentMarkers.test.tsx`, whose card
cases mount `ExpressionCards` over this payload).** The MIK-L35 cases derive a successor guarantee
from its `FAM-2HBJREC2` guarantee, including one revision whose text changes. Its receipt is in `gitTrees.capture-provenance.json` (route, status, sha256 and bytes).

## Code Commentary

### Logic

- The family-selected review of `FAM-2HBJREC2` ("Comparison-bound unchanged realization context"): the source inventory, the family context with its 7-member roster, and the limitations `review:trees:1`, `history:intent:<side>:available` and `knowledge-index:<side>:complete`.
- **MIK-R31 rule 6:** its member sources carry resolved, non-empty ranges (`resolved_ranges`, for example `194–213` for `_not_listed`), and its seven member identities are the ones the cards read names.
- **Re-captured by MIK-L31** from its own scratch leaf `260928-MIK-L31` with this leaf's code (review F7: the bodies are byte-identical to the capture at the L10-synced tree; only the receipt changed). Against L25's capture the deltas are the leaf, the code trees (`8a2d4b47` → the scratch candidate), the curator-authority name and `review:trees:2` → `review:trees:1`. (L25's own recapture history, ruling 02:32:42 (a), is in this card's Update History.)

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

- The tree comparison it was read from (comparison 1 of the MIK-L31 scratch leaf). [1]
- The receipt row for this body, now with its request parameters. [2]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
