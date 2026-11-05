# scripts/agent_evals/validation.py

## Governing Overview

[governing overview](overview.md)

## Purpose

Compares real whole-tree writer validation across captured memory snapshots.

## Code Commentary

### Invariants And Boundaries

New findings and remaining findings on written paths block. Unchanged inherited findings retain before/after hashes; this comparison does not create a missing layout marker or weaken product publication guards.

## Evidence

- The source defines this file's responsibility and the boundaries described here. [1]
