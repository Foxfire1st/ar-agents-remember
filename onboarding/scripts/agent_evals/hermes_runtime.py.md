# scripts/agent_evals/hermes_runtime.py

## Governing Overview

[governing overview](overview.md)

## Purpose

Derives and rechecks the prepared Hermes interpreter and ACP command from the published launcher.

## Code Commentary

### Invariants And Boundaries

Unsupported wrappers, missing ownership and changed runtime files refuse binding. This module does not install or repair the developer runtime.

## Evidence

- The source defines this file's responsibility and the boundaries described here. [1]
