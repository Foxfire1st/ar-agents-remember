# mcp/test_support/agents_remember_test_support/testing/database_retirement_guard.py

## Governing Overview

[mcp/test_support/agents_remember_test_support/testing/overview.md](overview.md)

## Purpose

The pytest guard that fails a test which opens or writes a retired knowledge database.

## Code Commentary

The guard attributes every APSW connection and database-file operation to the module that made it, charges the ones outside the named exemptions (`ALLOWED_MODULES`, which includes `controlplane/held_reset_index.py` for the non-knowledge held-reset schedule store), restores any hook a test removed, and states its own limits.

## Evidence

No separate reference list: the file's sidecar carries the realization entries this leaf re-anchored.
