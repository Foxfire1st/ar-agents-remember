# scripts/agent_evals/regrade.py

## Governing Overview

[governing overview](overview.md)

## Purpose

Plans and executes actor-free regrading from frozen retained attempts and package identities.

## Code Commentary

### Invariants And Boundaries

Census and dry-run make no judge call. Execution rechecks original inputs, source currency and package bindings; semantic unknowns require clarification rather than another judge.

For retained Hermes attempts, preparation first reparses the frozen native rows and then replays retained fixture-server placements over those rebuilt events before preparing the case grade. This path reopens neither the original SQLite database nor server logs, preserves raw records and their export digest, and keeps unrelated recording failures. It does not rerun the actor or make a census/dry-run a judged result.

## Evidence

- The source defines this file's responsibility and the boundaries described here. [1]
