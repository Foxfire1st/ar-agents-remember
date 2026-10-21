# dashboard/src/tray/pickKey.ts

## Governing Overview

[Route overview](overview.md)

## Purpose

Defines when two collection picks are the same object.

## Code Commentary

### Logic

Keys references by kind and exact task/tree/side/block/path/revision identity, files by scope/path/range, images by digest and text by passage plus source identity.

### Invariants And Boundaries

Different named snapshots remain distinct. This key is browser deduplication, not backend validation.

## Evidence

- Defines when two collection picks are the same object. [1]
