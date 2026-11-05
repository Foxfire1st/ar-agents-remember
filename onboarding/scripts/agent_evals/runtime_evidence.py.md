# scripts/agent_evals/runtime_evidence.py

## Governing Overview

[governing overview](overview.md)

## Purpose

Derives runtime observations from retained native events and frozen trial receipts.

## Code Commentary

### Invariants And Boundaries

Explicit executable paths, frozen-PATH resolution and unresolved shell dispatch remain distinct. A lookup observation is not transferred to later commands or resolved from today's environment.

## Evidence

- The source defines this file's responsibility and the boundaries described here. [1]
