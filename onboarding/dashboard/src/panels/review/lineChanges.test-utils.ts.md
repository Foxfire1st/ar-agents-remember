# dashboard/src/panels/review/lineChanges.test-utils.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

The producer's own line-count measurement for the captures the count tests draw.

## Code Commentary

What must stay true here is the measurement it returns: the producer's line counts for the captured entries, which the captures themselves predate. `ExpressionCards.test.tsx`, `treeCounts.page.test.tsx` and `FamilyTree.triage.test.tsx` are the readers; the assertions are theirs.

## Boundaries

The obligation above is about what this file builds and returns; the assertions belong to the suites that read it.

## Evidence

- Line-count expectations come from the producer's measurement rather than a number typed into the test. [1]
