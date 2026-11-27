# dashboard/src/tray/traySend.test.ts

## Governing Overview

[Route overview](overview.md)

## Purpose

Checks one per-target snapshot POST and truthful browser settlement.

## Code Commentary

### Logic

Asserts ordered reference/text/image payloads and notes, distinct per-target message IDs, full-success emptying, held never resent, refusal-only retry, network retention, repository omission for taskless Projects Architect delivery, parsed 422/413/500 detail and bound/no-target refusal without POST.

Fake fetch captures typed bodies; in-memory image bytes and deterministic IDs/clock.

### Invariants And Boundaries

Does not prove native host send/file order. Held is only accepted-for-later here, not delivery.

## Evidence

- Checks one per-target snapshot POST and truthful browser settlement. [1]
- Checks one per-target snapshot POST and truthful browser settlement. [2]

- Checks keeping the tray unchanged when the server cannot be reached. [3]
- Checks sending without a repository to a taskless Projects Architect and settling cleanly. [4]

- Checks one per-target snapshot POST and truthful browser settlement. [5]
- Checks one per-target snapshot POST and truthful browser settlement. [6]
