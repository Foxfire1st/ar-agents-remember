# scripts/agent_evals/adapters/paseo_session.py

## Governing Overview

[governing overview](../overview.md)

## Purpose

Resolves the created fixture actor's persisted provider session and checks runtime agreement.

## Code Commentary

### Invariants And Boundaries

The read opens only the exact actor record. It uses the pinned host's stored-agent path and checks its provider session identity against runtime information when that information is present.

## Evidence

- The adapter resolves the bound stored-agent record and checks its persisted identity and any runtime identity. [1]
