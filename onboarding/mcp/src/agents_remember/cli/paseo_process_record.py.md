# mcp/src/agents_remember/cli/paseo_process_record.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

Proves that the home process record names that home native supervisor.

## Code Commentary

inspect_record combines recorded PID with live process command/cwd facts. Stale records may be removed only under their classified state; foreign or unreadable process identity is refused. This protects home-addressed native stop/start, whose upstream PID check alone does not prove home ownership.

## Evidence

- Frozen implementation of inspect_record supporting the stated file behavior. [1]
- Frozen implementation of read_process supporting the stated file behavior. [2]
- Frozen implementation of remove_stale_record supporting the stated file behavior. [3]
