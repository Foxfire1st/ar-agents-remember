# dashboard/src/tray/trayPreferences.test.ts

## Governing Overview

[Route overview](overview.md)

## Purpose

Checks browser-local positive bound edits, reset and memory-only operation.

## Code Commentary

### Logic

Accepts positive whole bounds, rejects zero/negative/fraction/NaN, stores changed bounds only, rereads on a new instance, removes the key on reset and preserves page-lifetime values despite quota refusal.

In-memory Storage implementation optionally throws on both set/remove.

### Invariants And Boundaries

No AR operator setting is edited; this does not prove IndexedDB image persistence.

## Evidence

- Checks browser-local positive bound edits, reset and memory-only operation. [1]
- Checks browser-local positive bound edits, reset and memory-only operation. [2]
