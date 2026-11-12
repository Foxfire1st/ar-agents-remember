# scripts/agent_evals/adapters/discovery.py

## Governing Overview

[governing overview](../overview.md)

## Purpose

Selects a fresh native session matching the supplied project, time boundary and optional session identity.

## Code Commentary

### Invariants And Boundaries

Missing and ambiguous matches remain unknown; host UUIDs do not stand in for native provider session identities.

## Evidence

- The source defines this file's responsibility and the boundaries described here. [1]
