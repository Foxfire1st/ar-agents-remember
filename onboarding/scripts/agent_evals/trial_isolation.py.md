# scripts/agent_evals/trial_isolation.py

## Governing Overview

[governing overview](overview.md)

## Purpose

Builds private trial actor state, independent serving-build copies and frozen executable observations.

## Code Commentary

### Invariants And Boundaries

Selected dotenv seeds are visible within the private trial home. Cleanup is descriptor-confined; the empty private Codex home applies to the Hermes GPT arm.

## Evidence

- The source defines this file's responsibility and the boundaries described here. [1]
