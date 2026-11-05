# scripts/agent_evals/codex_access.py

## Governing Overview

[governing overview](overview.md)

## Purpose

Installs and revalidates an explicitly admitted access-only Codex credential pool row.

## Code Commentary

### Invariants And Boundaries

Admission checks private ownership, permissions, required identity and expiry. Refresh-token fields are rejected recursively; this is not JWT signature verification.

## Evidence

- The source defines this file's responsibility and the boundaries described here. [1]
