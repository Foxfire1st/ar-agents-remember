# dashboard/src/tray/TrayDock.tsx

## Governing Overview

[Route overview](overview.md)

## Purpose

Places the same tray outside an active chat frame or at the page corner.

## Code Commentary

### Logic

Registers visible column docks so one owns the tray; derives placement from frame and native composer rectangles, caps height to available room and reserves measured tray space through the frame channel. Falls below an unreadable composer with a notice.

### Invariants And Boundaries

No iframe reparent/key/reload or page spacer. Bottom-right is used only without a visible column dock. A minimized line, full panel and closed pill remain distinct.

## Evidence

- Places the same tray outside an active chat frame or at the page corner. [1]
- Places the same tray outside an active chat frame or at the page corner. [2]
- Places the same tray outside an active chat frame or at the page corner. [3]
