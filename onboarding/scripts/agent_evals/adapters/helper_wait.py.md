# scripts/agent_evals/adapters/helper_wait.py

## Governing Overview

[governing overview](../overview.md)

## Purpose

Reduces finite native helper observations into a pure snapshot.

## Code Commentary

### Invariants And Boundaries

No I/O occurs. A dispatch receipt or host event is not a process-local live roster, and unresolved capture state remains unresolved.

## Evidence

- The source defines this file's responsibility and the boundaries described here. [1]
