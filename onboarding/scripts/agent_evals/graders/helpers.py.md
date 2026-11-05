# scripts/agent_evals/graders/helpers.py

## Governing Overview

[governing overview](../overview.md)

## Purpose

Grades helper liveness, scoped turn ends and actual wait-check receipt from supported evidence.

## Code Commentary

### Invariants And Boundaries

Incomplete windows, unsupported carriers and unmatched assertions remain unknown rather than proving a silent ending.

## Evidence

- The source defines this file's responsibility and the boundaries described here. [1]
