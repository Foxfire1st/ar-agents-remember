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

## Evidence

- Makes per-target send and sent-log outcomes readable. [1]
- Makes per-target send and sent-log outcomes readable. [2]
- Makes per-target send and sent-log outcomes readable. [3]
