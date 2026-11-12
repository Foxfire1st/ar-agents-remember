# dashboard/src/tray/chatPicks.ts

## Governing Overview

[Route overview](overview.md)

## Purpose

Converts a trusted frame chat-text message to a tray text pick.

## Code Commentary

### Logic

Trims empty text, builds the passage title, preserves source agent/message ID/recorded time and delegates admission to the store.

### Invariants And Boundaries

Trust and parser validation belong to the frame control/model. This function does not fabricate provenance.

## Evidence

- Converts a trusted frame chat-text message to a tray text pick. [1]
- Converts a trusted frame chat-text message to a tray text pick. [2]
