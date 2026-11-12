# dashboard/src/explainer/testSupport.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

The explainer tests' shared support: a scripted dashboard server that answers each path from a queue and records every call, the tray reset, and the fixtures for one leaf's address.

## Code Commentary

- Each path answers its queued answers in order, the last one standing, so a test can script state that changes between reads.
- Every call is recorded with its method, path and parsed body, so a test can say what was and was not posted.
- The frame descriptor always answers as unreachable, so no case depends on a live host.
- The exported address, routes and plain state belong to one leaf, and the tray reset empties picks, text and targets without touching anything else.

## Evidence

- Each path answers its queue in order and every call is recorded [1]
- A plain state has no seat, no build and no stale parts unless a case patches one [2]
- The tray is emptied of picks, text and targets [3]
- A pick names an invariant reference in the test's repository [4]
