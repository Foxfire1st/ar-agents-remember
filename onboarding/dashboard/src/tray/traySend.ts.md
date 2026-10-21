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

## Evidence

- Sends one immutable collection snapshot separately to each chosen target. [1]
- Sends one immutable collection snapshot separately to each chosen target. [2]
- Sends one immutable collection snapshot separately to each chosen target. [3]
