# dashboard/src/tray/trayImages.ts

## Governing Overview

[Route overview](overview.md)

## Purpose

Retains pasted image bytes by digest across reload while keeping a live memory copy.

## Code Commentary

### Logic

Uses IndexedDB ar-tray/images plus an in-memory map; reads memory first, falls back to the database, removes unused data defensively and supplies SHA/base64 helpers.

### Invariants And Boundaries

Storage refusal does not discard the live image; callers display the non-persistence warning. No screen capture or raster rendering.

## Evidence

- Retains pasted image bytes by digest across reload while keeping a live memory copy. [1]
- Retains pasted image bytes by digest across reload while keeping a live memory copy. [2]
