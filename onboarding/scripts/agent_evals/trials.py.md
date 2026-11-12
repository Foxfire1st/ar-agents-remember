# scripts/agent_evals/trials.py

## Governing Overview

[governing overview](overview.md)

## Purpose

Implements the concrete CLI lifecycle from case preflight and slot planning through actor capture, grading and attempt retention.

## Code Commentary

### Invariants And Boundaries

Tooling-only completion is separate from a case verdict. Auth and cleanup failures can override captured results; helper deadlines and semantic unknowns remain distinct.

## Evidence

- The source defines this file's responsibility and the boundaries described here. [1]
