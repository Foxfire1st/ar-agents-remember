# mcp/src/agents_remember/application/review_frame_inventory.py

## Governing Overview

[Governing overview](overview.md)

## Purpose

The module owns the advisory inventory sidecar for an explanation revision.

## Code Commentary

Before promotion, it chooses the encoded inventory or the storage-limit omission marker according to the room left for the optional file. The guarded persistence path applies the same capacity constraint under the task lock. Readers return the inventory or omission for the addressed revision.

## Relationships

The frame store promotes the revision and owns the ready pointer. Serving projects the stored inventory or omission beside the frame.

## Evidence

- Staging writes the selected inventory or omission marker before revision promotion. [1]
