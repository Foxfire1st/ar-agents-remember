# dashboard/src/tray/TrayLayer.tsx

## Governing Overview

[Route overview](overview.md)

## Purpose

Mounts dashboard-wide tray selection and frame-pick integration once.

## Code Commentary

### Logic

Synchronizes copy preference, registers the incoming chat-pick listener and renders the selection offer plus corner-dock route.

### Invariants And Boundaries

It is a runtime mount, not a second store, message route or frame owner.

## Evidence

- Mounts dashboard-wide tray selection and frame-pick integration once. [1]
- Mounts dashboard-wide tray selection and frame-pick integration once. [2]
