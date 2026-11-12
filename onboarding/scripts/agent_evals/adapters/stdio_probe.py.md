# scripts/agent_evals/adapters/stdio_probe.py

## Governing Overview

[governing overview](../overview.md)

## Purpose

Initializes the exact supplied stdio definition, collects its paginated tool inventory and reads server_info in that session.

## Code Commentary

### Invariants And Boundaries

Repeated cursors or tool names refuse. Each awaited boundary has its own timeout.

## Evidence

- The source defines this file's responsibility and the boundaries described here. [1]
