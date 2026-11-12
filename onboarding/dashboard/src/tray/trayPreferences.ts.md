# dashboard/src/tray/trayPreferences.ts

## Governing Overview

[Route overview](overview.md)

## Purpose

Owns browser-local copy and positive tray bounds preferences.

## Code Commentary

### Logic

Defaults copy on and bounds to 20 picks, 5 MiB per image and 20 MiB per message; stores only changed settings and resets by removing local keys; keeps a memory value plus warning if storage fails.

### Invariants And Boundaries

No global AR operator settings. Server ceilings remain independently enforced.

## Evidence

- Owns browser-local copy and positive tray bounds preferences. [1]
- Owns browser-local copy and positive tray bounds preferences. [2]
- Owns browser-local copy and positive tray bounds preferences. [3]
