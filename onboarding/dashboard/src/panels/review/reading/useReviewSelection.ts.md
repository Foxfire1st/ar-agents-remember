# dashboard/src/panels/review/reading/useReviewSelection.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

Route one selection to subject read/context/workspace/scroll.

## Code Commentary

### Logic

Route one selection to subject read/context/workspace/scroll. Block reads its invariant from existing card set; older comparison reads no subject. URL restore waits on required reads, cancels on a new user selection and writes `sel`/older comparison through replace-state owner.

### Invariants And Boundaries

This file consumes comparison and owner state; it does not author knowledge or decide task acceptance.

## Evidence

- Route one selection to subject read/context/workspace/scroll. [1]
- Route one selection to subject read/context/workspace/scroll. [2]
- Route one selection to subject read/context/workspace/scroll. [3]
