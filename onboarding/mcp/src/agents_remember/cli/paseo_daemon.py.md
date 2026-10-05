# mcp/src/agents_remember/cli/paseo_daemon.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

Reports and stops the configured home daemon through its own CLI boundary.

## Code Commentary

runtime_status reports version, daemon, owned plugin and embed state. stop_runtime inspects the home process record before asking the home-addressed CLI to stop; no AR code selects a process by listen port or signals one directly. A foreign/unreadable record remains a named refusal instead of permission to stop another home.

## Evidence

- Frozen implementation of runtime_status supporting the stated file behavior. [1]
- Frozen implementation of stop_runtime supporting the stated file behavior. [2]
- Frozen implementation of _home_record supporting the stated file behavior. [3]
