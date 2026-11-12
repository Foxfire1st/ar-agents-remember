# dashboard/src/panels/review/reading/LocationGroup.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

Present only nonempty unchanged/not-comparable groups.

## Code Commentary

### Logic

Present only nonempty unchanged/not-comparable groups. Heading names count/reason; open lists first4 full-role/path/range lines then remainder in place, never code cards. Unreadable opposite side gets its own reason. Open state belongs to workspace; “all” list expansion is local component state.

### Invariants And Boundaries

This file consumes comparison and owner state; it does not author knowledge or decide task acceptance.

## Evidence

- Present only nonempty unchanged/not-comparable groups. [1]
- Present only nonempty unchanged/not-comparable groups. [2]
- Present only nonempty unchanged/not-comparable groups. [3]
