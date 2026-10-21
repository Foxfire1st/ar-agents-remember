# dashboard/src/panels/review/reading/codeContextPreference.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

Store Changes only/Full context at browser key, defaulting to changes for missing/unknown/denied storage.

## Code Commentary

### Logic

Store Changes only/Full context at browser key, defaulting to changes for missing/unknown/denied storage. State still works without persistence. Test reload helper rereads storage; this is a display preference, not record state.

### Invariants And Boundaries

This file consumes comparison and owner state; it does not author knowledge or decide task acceptance.

## Evidence

- Store Changes only/Full context at browser key, defaulting to changes for missing/unknown/denied storage. [1]
- Store Changes only/Full context at browser key, defaulting to changes for missing/unknown/denied storage. [2]
- Store Changes only/Full context at browser key, defaulting to changes for missing/unknown/denied storage. [3]
