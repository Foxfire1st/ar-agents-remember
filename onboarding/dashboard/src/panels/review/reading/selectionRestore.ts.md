# dashboard/src/panels/review/reading/selectionRestore.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

Encode/decode admitted subject/family, lane or complete block/hunk identities.

## Code Commentary

### Logic

Encode/decode admitted subject/family, lane or complete block/hunk identities. Wait on unresolved needed reads, reject outside identity with one reason. Hunk comparison/path alone is insufficient: both spans must match a classified hunk.

### Invariants And Boundaries

This file consumes comparison and owner state; it does not author knowledge or decide task acceptance.

## Evidence

- Encode/decode admitted subject/family, lane or complete block/hunk identities. [1]
- Encode/decode admitted subject/family, lane or complete block/hunk identities. [2]
- Encode/decode admitted subject/family, lane or complete block/hunk identities. [3]
