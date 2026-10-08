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

## Evidence

### Repo-Internal References


- Exact memory input movement and staleness fold. [5]


- Unreadable/forged rebinding is unavailable. [7]


- Movement model rejects false bindings/states. [9]


- Current projection table. [11]


- Actual unavailable reason and tree-bound statement. [14]


- Current shared enclosure and sibling measurement. [30]


### Cross-Repo References

No cross-repository contract is established by this file.
