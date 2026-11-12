# scripts/agent_evals/fixtures.py

## Governing Overview

[governing overview](overview.md)

## Purpose

Admits hashed case inputs and resets each attempt into a fresh UUID-owned fixture.

## Code Commentary

### Invariants And Boundaries

Only declared actor inputs are copied. Undeclared files and exposure of grader-only inputs refuse admission; cleanup checks the unchanged fixture ownership marker.

## Evidence

- The source defines this file's responsibility and the boundaries described here. [1]
