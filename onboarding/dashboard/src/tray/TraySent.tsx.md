# dashboard/src/tray/TraySent.tsx

## Governing Overview

[Route overview](overview.md)

## Purpose

Makes per-target send and sent-log outcomes readable.

## Code Commentary

### Logic

Shows delivered, held and refusal results; refreshes selected targets after sends; disclosure rows expose exact pick IDs and message file/hash. Named unavailable states avoid silently treating a failed log fetch as empty.

### Invariants And Boundaries

Held is not delivered. The UI never resends from a log or infers a terminal result without server evidence.


**L184 — INV-4DQMNE.** This module writes both the summary line and each target's full answer, so both obligations are realized here. The obligation this leaf records for this place is stated in the invariant named here; the card's earlier account of this file stands, and this paragraph adds what the change made true.

## Evidence

- Makes per-target send and sent-log outcomes readable. [1]
- Makes per-target send and sent-log outcomes readable. [2]
- Makes per-target send and sent-log outcomes readable. [3]
