# dashboard/src/panels/review/reviewSelection.ts

## Governing Overview

[Route overview](overview.md)

## Purpose

Declare the review’s subject, exact block and code-without-invariant lane selections plus its deterministic sort vocabulary.

## Code Commentary

### Logic

ReviewSelection distinguishes a subject with optional family occurrence, a ReviewBlockIdentity, and a lane with optional file path. The page may hold null separately for no selection.

REVIEW_SORTS and SORT_LABELS list Priority, Authored, Memory currentness and four memory-dependent sorts. MEMORY_SORTS identifies the four options whose values come from the card read.

### Invariants And Boundaries

This is shared vocabulary, not selection state, persistence or ranking implementation. changeSetOrder owns ordering/availability, and blockIdentity owns URL encoding.

## Evidence

- Selection forms and sort domain [1]
- Complete labels and memory-dependent subset [2]
