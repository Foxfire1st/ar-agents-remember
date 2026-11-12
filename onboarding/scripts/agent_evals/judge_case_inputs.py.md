# scripts/agent_evals/judge_case_inputs.py

## Governing Overview

[governing overview](overview.md)

## Purpose

Materializes explicitly declared, hash-bound judge-only case inputs.

## Code Commentary

### Invariants And Boundaries

Judge inputs remain separate from actor inputs and effect inventories. Existing destination bytes must agree with the declared input.

## Evidence

- The source defines this file's responsibility and the boundaries described here. [1]
