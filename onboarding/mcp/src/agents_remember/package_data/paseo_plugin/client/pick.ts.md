# mcp/src/agents_remember/package_data/paseo_plugin/client/pick.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

Provides the negotiated iframe tray text-pick and native-composer geometry adapter, which reports the message box's rectangle with its own left and width.

## Code Commentary

### Logic

Offers explicit non-modal add on selected chat text; reads the selected row record time in place and refuses unrecorded rows; reports composer geometry and loss, reserves padded tray height while preserving end scroll, and tears down handlers/observers/style. The composer report carries the box's own left and width beside its vertical edge, taken from one measurement, and is posted again when the layout moves or resizes the box without a window resize: the box and its ancestor chain share one resize observer, and a class/style observer on the same nodes re-measures a move that resizes nothing. The tray-height reservation still pads only the chat's scroll root.

### Invariants And Boundaries

Runs only after a trusted bridge hello says pick is read. Pinned unsupported Paseo 0.11.1/React DOM 19.1.0 row adapter; no timeline paging, selection clearing, focus move or role write. Adapter structural loss produces a named chat-pick notice while dashboard picks continue.

## Evidence

- Provides the negotiated iframe tray text-pick and native-composer geometry adapter. [1]
- Provides the negotiated iframe tray text-pick and native-composer geometry adapter. [2]
- Provides the negotiated iframe tray text-pick and native-composer geometry adapter. [3]

- The composer post carries the box's own left and width from one measurement, and re-measures on a frame resize and on a container or class/style change that moves or resizes it. [4]
