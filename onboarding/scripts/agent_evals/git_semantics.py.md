# scripts/agent_evals/git_semantics.py

## Governing Overview

[governing overview](overview.md)

## Purpose

Compares semantic Git endpoints through sanitized scratch copies of retained repositories.

## Code Commentary

### Invariants And Boundaries

Selected metadata churn is benign only when the measured semantic endpoints agree. Endpoint equality does not prove that no Git operation occurred during the attempt.

## Evidence

- The source defines this file's responsibility and the boundaries described here. [1]
