# scripts/agent_evals/graders/ladder.py

## Governing Overview

[governing overview](../overview.md)

## Purpose

Checks disclosed same-tool/input-class recovery against native event identities, ordering and bound artifacts.

## Code Commentary

### Invariants And Boundaries

Wrong class or order fails; incomplete evidence stays unknown. Observable boundary checks still leave semantic judgment to the rubric.

## Evidence

- The source defines this file's responsibility and the boundaries described here. [1]
