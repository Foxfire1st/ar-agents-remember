# dashboard/src/tray/AddToTray.tsx

## Governing Overview

[Route overview](overview.md)

## Purpose

Provides one quiet accessible object add control.

## Code Commentary

### Logic

The host class reveals its own control on hover/focus; the control prevents selection-changing mousedown, reflects existing membership and delegates one click to the store.

### Invariants And Boundaries

The store/key owns deduplication and limits. An inactive nested host keeps its own idle control quiet while an outer host is hovered or focused.

## Evidence

- Provides one quiet accessible object add control. [1]
- Provides one quiet accessible object add control. [2]
