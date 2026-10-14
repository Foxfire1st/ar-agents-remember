# mcp/src/agents_remember/cli/removed_stores.py

## Governing Overview

[Area overview](../../../overview.md)

## Purpose

The explicit user-commanded removed-stores CLI owns deletion of stores belonging to removed parts. Installation only reports their presence; this command does not recreate a gate-deciding or agent-session plane.

## Code Commentary

### Logic

run resolves trusted configuration, collects stores plus unreadable places, reports paths/sizes and gate recovery text, and either lists in dry-run or removes individual files followed by emptied store folders. _contained_target resolves parent aliases but removes a symlink as the link itself. File or folder errors are accumulated with their path/reason; independent targets continue. Unreadable stores are not declared absent and their folders are left alone.

### Invariants And Boundaries

A target outside the resolved coordination root is refused. Link destinations and stores belonging to retained parts stay untouched. Dry-run makes no deletion. Exit1 covers discovery/removal failures; successful absence or complete removal exits0. Store enumeration lives in install.runtime, not a second CLI inventory.

## Evidence

No Domain Documentation source is configured for this repository-specific boundary.

- Explicit removed-store cleanup: implementation/assertion boundary described above. [1]
