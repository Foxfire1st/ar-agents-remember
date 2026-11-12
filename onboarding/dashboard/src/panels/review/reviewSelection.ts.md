# dashboard/src/panels/review/reviewSelection.ts

## Governing Overview

[Route overview](overview.md)

## Purpose

Declare the review's subject, exact-block and lane selections, deterministic sorts and explainer-category sort keys.

## Code Commentary

### Logic

ReviewSelection distinguishes a subject with optional family occurrence, a ReviewBlockIdentity, and a lane with optional file path. The page may hold null separately for no selection.

REVIEW_SORTS and SORT_LABELS list Priority, Authored, Memory currentness and four memory-dependent sorts. MEMORY_SORTS identifies the four options whose values come from the card read.

### Invariants And Boundaries

This is shared vocabulary, not selection state, persistence or ranking implementation. changeSetOrder owns ordering/availability, and blockIdentity owns URL encoding.

## Evidence

- Selection forms and sort domain [1]

Declare subject, exact block and lane selections, plus deterministic and explainer-category sort vocabulary. DeterministicSort contains the seven existing sorts; JudgmentSort is a nonempty judgment:<category> key. isJudgmentSort, judgmentCategoryOf and judgmentSortFor convert that vocabulary. REVIEW_SORTS keeps the deterministic array for enumeration but its includes handler accepts valid judgment keys; SORT_LABELS derives their ✦ category label. MEMORY_SORTS still identifies only the four entry-memory-dependent deterministic sorts. This file owns vocabulary, not ranking, persisted preference or judgment authoring.

- Declare subject, exact block and lane selections, plus deterministic and explainer-category sort vocabulary. DeterministicSort contains the seven existing sorts; JudgmentSort is a nonempty judgment:<category> key. isJudgmentSort, judgmentCategoryOf and judgmentSortFor convert that vocabulary. REVIEW_SORTS keeps the deterministic array for enumeration but its includes handler accepts valid judgment keys; SORT_LABELS derives their ✦ category label. MEMORY_SORTS still identifies only the four entry-memory-dependent deterministic sorts. This file owns vocabulary, not ranking, persisted preference or judgment authoring. [3]

- The sort vocabulary retains seven deterministic values and four memory-dependent sorts, accepts nonempty judgment:<category> keys through REVIEW_SORTS.includes and derives their ✦ labels through SORT_LABELS. [2]
