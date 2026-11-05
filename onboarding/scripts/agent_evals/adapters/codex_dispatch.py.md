# scripts/agent_evals/adapters/codex_dispatch.py

## Governing Overview

[governing overview](../overview.md)

## Purpose

Recovers supported Codex exec dispatches from completed native items or source-bound returned values.

## Code Commentary

### Invariants And Boundaries

It parses syntax without executing JavaScript. Unsupported forms remain unknown.

## Evidence

- The source defines this file's responsibility and the boundaries described here. [1]
