# dashboard/src/panels/review/reading/useScrollOnce.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

Arm one subject/block/group/lane target; spend after read settles.

## Code Commentary

### Logic

Arm one subject/block/group/lane target; spend after read settles. Column scroll/wheel/touch/key/scrollbar interaction disarms. Product scroll changes only column scrollTop above40rem; stacked uses scrollIntoView. Reader anchoring owns other content movement.

### Invariants And Boundaries

This file consumes comparison and owner state; it does not author knowledge or decide task acceptance.

## Evidence

- Arm one subject/block/group/lane target; spend after read settles. [1]
- Arm one subject/block/group/lane target; spend after read settles. [2]
- Arm one subject/block/group/lane target; spend after read settles. [3]
