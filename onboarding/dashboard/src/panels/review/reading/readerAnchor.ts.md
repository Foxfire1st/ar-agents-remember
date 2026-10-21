# dashboard/src/panels/review/reading/readerAnchor.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

Implement the settled reader-line mechanism separately from allowed selection landing.

## Code Commentary

### Logic

Implement the settled reader-line mechanism separately from allowed selection landing. Skip pending/head/spacer nodes; use document-position identity inside rebuilt editors; settle pending editor measurements up to4 rounds; hold clamp room using last spacer and release below viewport. Replaced/gone line follows surviving content; no anchor at top, while landing due or stacked.

### Invariants And Boundaries

This file consumes comparison and owner state; it does not author knowledge or decide task acceptance.

## Evidence

- Implement the settled reader-line mechanism separately from allowed selection landing. [1]
- Implement the settled reader-line mechanism separately from allowed selection landing. [2]
- Implement the settled reader-line mechanism separately from allowed selection landing. [3]
