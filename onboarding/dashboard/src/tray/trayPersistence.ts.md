# dashboard/src/tray/trayPersistence.ts

## Governing Overview

[Route overview](overview.md)

## Purpose

Persists reloadable tray metadata in browser-origin storage.

## Code Commentary

### Logic

Validates kept rows, recomputes keys and deduplicates on restore; preserves picks/text/target choices and default-decision flags, reporting write failure to the caller.

### Invariants And Boundaries

Does not persist open/minimized UI state or image bytes; IndexedDB is separate. Malformed old rows are not treated as valid provenance.

## Evidence

- Persists reloadable tray metadata in browser-origin storage. [1]
- Persists reloadable tray metadata in browser-origin storage. [2]
- Persists reloadable tray metadata in browser-origin storage. [3]
