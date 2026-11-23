# mcp/src/agents_remember/cli/role_launch_options_receipts.py

## Governing Overview

[MCP runtime](../../../overview.md)

## Purpose

Reads the launcher’s saved role selections and applies host liveness observations.

## Code Commentary

The coordinator reads the host outside the dispatch lock. It acquires the lock to compare the current receipt with the snapshot and applies the observation only to matching contents. Taskless options lists saved records and preserves the Investigator omission count. Taskless Result requires the exact request ID and checks the recorded selection. Legacy migration finds candidates outside the lock and compares current contents inside it.

## Evidence

- Options lists saved taskless records. Result resolves the exact saved request and validates its address. [1]
- The liveness observation is applied only after the locked receipt comparison. [2]
