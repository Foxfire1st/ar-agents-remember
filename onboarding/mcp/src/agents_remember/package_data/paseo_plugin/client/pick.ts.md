# mcp/src/agents_remember/package_data/paseo_plugin/client/pick.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

Provides the negotiated iframe tray text-pick and native-composer geometry adapter.

## Code Commentary

### Logic

Offers explicit non-modal add on selected chat text; reads the selected row record time in place and refuses unrecorded rows; reports composer geometry and loss, reserves padded tray height while preserving end scroll, and tears down handlers/observers/style.

### Invariants And Boundaries

Runs only after a trusted bridge hello says pick is read. Pinned unsupported Paseo 0.11.1/React DOM 19.1.0 row adapter; no timeline paging, selection clearing, focus move or role write. Adapter structural loss produces a named chat-pick notice while dashboard picks continue.

## Evidence

- Provides the negotiated iframe tray text-pick and native-composer geometry adapter. [1]
- Provides the negotiated iframe tray text-pick and native-composer geometry adapter. [2]
- Provides the negotiated iframe tray text-pick and native-composer geometry adapter. [3]
