# dashboard/src/panels/review/reading/readGate.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

Bound deferred file work to8 concurrent tasks.

## Code Commentary

### Logic

Bound deferred file work to8 concurrent tasks. A lane file can start after opening signal without gesture; card marks after first page gesture. Observe near viewport600px margin; once seen remains seen; absent observer treats seen true but still respects gate start.

### Invariants And Boundaries

Eight concurrent file tasks; a lane file has two requests. Initial in-view lane reads need no gesture after opening; card marks still need engagement.

## Evidence

- Bound deferred file work to8 concurrent tasks. [1]
- Bound deferred file work to8 concurrent tasks. [2]
- Bound deferred file work to8 concurrent tasks. [3]
