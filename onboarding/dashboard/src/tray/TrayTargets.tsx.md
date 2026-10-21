# dashboard/src/tray/TrayTargets.tsx

## Governing Overview

[Route overview](overview.md)

## Purpose

Chooses one or several existing AR chat recipients in an unclipped popup.

## Code Commentary

### Logic

Positions a fixed menu inside the viewport above/below its trigger, follows geometry changes, reloads first page on open and exposes More; keeps chosen recipients even if not in the loaded page and shows incomplete-list uncertainty.

### Invariants And Boundaries

Choosing a recipient does not navigate a chat or create a role. Portal-like fixed placement remains keyboard navigable.

## Evidence

- Chooses one or several existing AR chat recipients in an unclipped popup. [1]
- Chooses one or several existing AR chat recipients in an unclipped popup. [2]
- Chooses one or several existing AR chat recipients in an unclipped popup. [3]
