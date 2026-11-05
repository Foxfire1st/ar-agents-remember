# scripts/agent_evals/adapters/execution.py

## Governing Overview

[governing overview](../overview.md)

## Purpose

Runs an explicitly configured native command after checking its project, build and profile binding.

## Code Commentary

### Invariants And Boundaries

The adapter captures bounded output and reclaims the process group. It writes no harness configuration; judge bindings admit no MCP servers.

## Evidence

- The source defines this file's responsibility and the boundaries described here. [1]
