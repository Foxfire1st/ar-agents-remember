# dashboard/src/tray/TrayDock.tsx

## Governing Overview

[Route overview](overview.md)

## Purpose

Places the same tray outside an active chat frame or at the page corner.

## Code Commentary

### Logic

Registers visible column docks so one owns the tray; derives placement from frame and native composer rectangles, caps height to available room and reserves measured tray space through the frame channel. When the composer edge carries the message box's own left and width, the column dock's horizontal placement is exactly that left translated by the frame's origin into the anchor's coordinates, at the box's own width, with no minimum and no clamp; a report without the pair keeps the frame-wide placement, and the corner dock's own width is unchanged. In Operations, where the frame is the column, that is a measured inset: the retained case puts the tray that spanned the 300 px column at the box's left 16 and width 268, 16 px in from each side and 32 px narrower, at both 1920 and 1440. Falls below an unreadable composer with a notice.

### Invariants And Boundaries

No iframe reparent/key/reload or page spacer. Bottom-right is used only without a visible column dock. A minimized line, full panel and closed pill remain distinct.

## Evidence

- Places the same tray outside an active chat frame or at the page corner. [1]
- Places the same tray outside an active chat frame or at the page corner. [2]
- Places the same tray outside an active chat frame or at the page corner. [3]
