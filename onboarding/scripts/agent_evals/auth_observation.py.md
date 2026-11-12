# scripts/agent_evals/auth_observation.py

## Governing Overview

[governing overview](overview.md)

## Purpose

Captures one private before snapshot, compares it once and discards it.

## Code Commentary

### Invariants And Boundaries

The selected GPT branch compares canonical provider and credential-pool representations. The None branch compares whole-file bytes. Reports receive equality or difference, never the selected credential contents.

## Evidence

- The source defines this file's responsibility and the boundaries described here. [1]
