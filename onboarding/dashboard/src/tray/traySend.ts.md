# dashboard/src/tray/traySend.ts

## Governing Overview

[Route overview](overview.md)

## Purpose

Sends one immutable collection snapshot separately to each chosen target.

## Code Commentary

### Logic

Builds structured wire picks, reads image bytes, chooses a repository from page/reference/target context and posts one message per target; parses named delivered/held/refused results and settles only the snapshot IDs/text.

### Invariants And Boundaries

Held counts as sent and is never resent. One target refusal does not stop others. Missing image, invalid answer and network errors are explicit per-target refusals.


**L184 — INV-4DQMNE.** This parser is where a delivery's fields arrive from the server, so the reset has to survive here. The obligation this leaf records for this place is stated in the invariant named here; the card's earlier account of this file stands, and this paragraph adds what the change made true.

## Evidence

- Sends one immutable collection snapshot separately to each chosen target. [1]
- Sends one immutable collection snapshot separately to each chosen target. [2]
- Sends one immutable collection snapshot separately to each chosen target. [3]
