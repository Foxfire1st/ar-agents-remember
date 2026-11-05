# scripts/agent_evals/trial_setup.py

## Governing Overview

[governing overview](overview.md)

## Purpose

Provisions the batch host and a fresh native trial fixture without starting its actor.

## Code Commentary

### Invariants And Boundaries

Provisioning binds private serving bytes, repositories, configuration and the concrete task server. Uncertain actor creation can defer release until supported host stop; cleanup does not acquire foreign-fixture authority.

## Evidence

- The source defines this file's responsibility and the boundaries described here. [1]
