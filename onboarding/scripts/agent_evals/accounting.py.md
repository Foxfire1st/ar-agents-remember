# scripts/agent_evals/accounting.py

## Governing Overview

[governing overview](overview.md)

## Purpose

Validates attempt chronology and builds case, model, text and batch accounting.

## Code Commentary

### Invariants And Boundaries

Tooling checks stay outside measurement results. Unknown causes remain distinct; three graded trials are required before two-of-three case passage is calculated.

## Evidence

- The source defines this file's responsibility and the boundaries described here. [1]
