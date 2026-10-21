# dashboard/src/tray/types.ts

## Governing Overview

[Route overview](overview.md)

## Purpose

Defines tray object identity, collection entries, developer-send payloads and truthful server results.

## Code Commentary

### Logic

Keeps references structured; distinguishes panel/chat provenance, partial seat listings, delivered/held/refused outcomes and filed-message identity.

### Invariants And Boundaries

Types do not validate channel trust or resolve referenced records. Optional wire revision fields are checked or derived by the backend.

## Evidence

- Defines tray object identity, collection entries, developer-send payloads and truthful server results. [1]
- Defines tray object identity, collection entries, developer-send payloads and truthful server results. [2]
- Defines tray object identity, collection entries, developer-send payloads and truthful server results. [3]
