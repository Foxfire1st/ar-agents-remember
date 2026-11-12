# scripts/agent_evals/grade_sources.py

## Governing Overview

[governing overview](overview.md)

## Purpose

Binds each grade producer to its conservative transitive local Python import closure.

## Code Commentary

### Invariants And Boundaries

Missing producer metadata and changed dependency bytes make a retained grade stale. This closure is distinct from the broader runtime source snapshot.

## Evidence

- The source defines this file's responsibility and the boundaries described here. [1]
