# scripts/agent_evals/evidence_selection.py

## Governing Overview

[governing overview](overview.md)

## Purpose

Selects criterion-specific evidence from explicit case policies, native references, reports and history deltas.

## Code Commentary

### Invariants And Boundaries

Citations must be hash-bound. An absent citation does not select every input; malformed retained data is distinct from an absent report.

## Evidence

- The source defines this file's responsibility and the boundaries described here. [1]
