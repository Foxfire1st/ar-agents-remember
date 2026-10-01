# dashboard/src/data/streamLiveness.ts

## Governing Overview

[data overview](overview.md)

## Purpose

Judge long-lived open EventSource channels after positive sleep evidence or one bounded silent episode,
without reconnect-storming legitimate idle or hidden-tab streams.

## Code Commentary

### Logic

The watchdog samples wall-clock jumps and frame silence only while its channel is open and the page is
visible. It spends at most one quiet backstop cycle, ignores the replacement handshake as proof of life,
and re-arms only when a later independent frame arrives.

### Conventions

All timers, clock, visibility, and listener hooks are injectable for transport-level tests.

### Invariants And Boundaries

Sleep is positive evidence and may cycle again; ordinary silent channels receive at most one quiet cycle
per observed-life episode. The caller owns close/reopen and whether that cycle changes visible state.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory worktree's source registry.

No relevant external documentation is configured.

### Repo-Internal References

- Liveness tuning, one-shot backstop, and visibility handling. [1]
- Conversation and state streams both install this watchdog. [2]

### Cross-Repo References

No meaningful cross-repository references found.

- The watchdog is local browser transport policy. [3]
