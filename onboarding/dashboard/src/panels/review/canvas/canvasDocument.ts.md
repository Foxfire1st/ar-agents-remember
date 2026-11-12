# dashboard/src/panels/review/canvas/canvasDocument.ts

## Governing Overview

[governing route overview](../../overview.md)

## Purpose

Watches the mounted frame for the document-presence messages the host bootstrap announces: entry, departure and challenge answers, so the panel can revoke a channel whose document left.

## Code Commentary

- `useDocumentPresence` binds the window message listener for one session and reports the phase it observed instead of assuming a healthy frame.
- Navigation is reported as departure, which is the signal the panel revokes on.
- The departed document's port is closed at departure, before `onDeparture` runs, rather than later when React runs the effect's cleanup: nothing reads the port once the document has departed.

## Evidence

- The panel observes entry, departure and challenge answers for its session. [1]
