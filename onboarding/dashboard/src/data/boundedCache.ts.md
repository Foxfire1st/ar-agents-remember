# dashboard/src/data/boundedCache.ts

## Purpose

Caller-budgeted retained-history LRU.

## Code Commentary

get promotes access; set replaces prior accounting, skips oversized values and evicts oldest entries until entry/byte budgets hold. delete updates bytes; retained reports both totals. Not an active-render cap.

## Governing Overview

[Area overview](overview.md)

## Evidence

- Implementation [1]
