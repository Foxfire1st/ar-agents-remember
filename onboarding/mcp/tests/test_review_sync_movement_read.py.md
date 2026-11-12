# mcp/tests/test_review_sync_movement_read.py

## Governing Overview

[mcp tests route overview](overview.md)

## Purpose

Live review renders exact managed-sync tree movement and separates unavailable evidence.

## Code Commentary

### Logic

A real recorded rebinding after a memory-only edit produces stale movement naming the reviewed memory tree and resolved capture. Its fold retains previous comparison identity; a historical comparison receives no live movement. [5]

Unreadable and forged records render unavailable. Validator forgeries reject contradictory states, missing complete source comparison, another source digest/tree and retired generation/dataset keys. [7] [9]

The projection maps current/moved/unmeasured to current/stale/not-measured and carries resolved identities only for moved channels. [11] [14]

### Invariants And Boundaries

- A memory-only movement matters when code still matches.
- Unavailable and unmeasured are not agreement.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository — the memory layer's `system/sources.md`
records no entries at all. The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References


- Exact memory input movement and staleness fold. [5]


- Unreadable/forged rebinding is unavailable. [7]


- Movement model rejects false bindings/states. [9]


- Current projection table. [11]


- Actual unavailable reason and tree-bound statement. [14]


- Current shared enclosure and sibling measurement. [30]


- The `unavailable` value: an absence reported with its reason and without an agreement clause. [31]
- One accepted record projected, with resolved identities carried exactly on the channel that moved. [32]
- The record model and its self-consistency validator the projected movement reads. [33]

- The production sync tool whose payload the read-side block is attached to. [34]

### Cross-Repo References

No cross-repository contract is established by this file.
