# mcp/src/agents_remember/serving/paseo/paseo_process_record.py

## Governing Overview

[overview](../overview.md)

## Purpose

Proves that the home process record names that home's Paseo supervisor.

## Code Commentary

inspect_record combines recorded PID with live process command/cwd facts. Stale records may be removed only under their classified state; foreign or unreadable process identity is refused. This protects home-addressed native stop/start, whose upstream PID check alone does not prove home ownership.

L96: the module moved from `cli/paseo_process_record.py` into `serving/paseo/`. `read_process` now also records the process executable (`/proc/<pid>/exe`) and the carried session-variable names through the product's `carried_session_variables`, which the start/status outcomes report without values.

## Evidence

- The home record trust rule. [1]
- The process facts including executable and session names. [2]
