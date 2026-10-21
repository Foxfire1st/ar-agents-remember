# dashboard/src/tray/trayModel.ts

## Governing Overview

[Route overview](overview.md)

## Purpose

Provides collection byte accounting, limit checks, target default and readable pick summaries.

## Code Commentary

### Logic

Checks positive supported-image/count/message admission and Send bounds, chooses a source-chat or shown-chat default, and formats provenance/previews.

### Invariants And Boundaries

Browser byte estimate includes encoded images/reference representations and is not the same counting formula as server decoded-byte enforcement. Defaults apply only under the store first-pick decision.

## Evidence

- Provides collection byte accounting, limit checks, target default and readable pick summaries. [1]
- Provides collection byte accounting, limit checks, target default and readable pick summaries. [2]
- Provides collection byte accounting, limit checks, target default and readable pick summaries. [3]
