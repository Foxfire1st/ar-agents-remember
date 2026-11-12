# scripts/agent_evals/runner.py

## Governing Overview

[governing overview](overview.md)

## Purpose

Provides a hook-based single-trial reset, execution and evidence-capture API.

## Code Commentary

### Invariants And Boundaries

This separate API has test callers; it is not the concrete CLI trial path. Native exit success remains captured and ungraded.

## Evidence

- The source defines this file's responsibility and the boundaries described here. [1]
