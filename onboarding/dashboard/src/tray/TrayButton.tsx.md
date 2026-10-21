# dashboard/src/tray/TrayButton.tsx

## Governing Overview

[Route overview](overview.md)

## Purpose

Owns the persistent bottom-bar tray button and closed-tray edge pill.

## Code Commentary

### Logic

Shows count and accessible state, opens a full empty or populated tray, and keeps the tray control outside the four-view group; the edge pill opens retained picks.

### Invariants And Boundaries

This control owns presentation only. It must preserve selection and not become a fifth view tab.

## Evidence

- Owns the persistent bottom-bar tray button and closed-tray edge pill. [1]
- Owns the persistent bottom-bar tray button and closed-tray edge pill. [2]
- Owns the persistent bottom-bar tray button and closed-tray edge pill. [3]
