# mcp/src/agents_remember/cli/role_registry_recovery.py

## Governing Overview

[MCP overview](../../../overview.md)

## Purpose

Restore missing receipt-backed role agent records before the dashboard establishes current host activity.

## Code Commentary

Recovery reads unarchived history with background agents and records which registry rows existed before inventory. Exact reclamation requires complete, usable observations. A positive exact archive can reclaim an unchanged row when it follows the recorded registration, or when the row has no usable registration timestamp. Exact absence can reclaim an unchanged row when its receipt is absent or settled. A starting or replayable receipt preserves the row on exact absence. The writer rechecks the recorded row under its lock.

When history identifies a labeled role that lacks a row, recovery enumerates receipts before exact lookup and restores usable receipt-backed identities. With a complete inventory, that enumeration also finds eligible unfinished receipt IDs absent from the inventory and registry. A complete inventory permits exact reads for registered IDs missed by history. If exact lookup returns a usable null and receipts have not been read, recovery reads them once to judge absence, without adding unfinished receipt gaps. An incomplete inventory can restore positively observed receipt-backed roles. Boot qualification requires a complete, usable pass. Recovery starts no host session and uses the existing bridge.

## Relationships

The dashboard's activity input invokes the reader on startup and on a new plug-in boot. An incomplete or unqualified registry pass returns before the snapshot RPC. A later native publication or restart supplies a new input. Preview reads the snapshot without registry reconciliation. A qualified attempt reads the snapshot and checks its daemon and plug-in boot against the expected pair. A mismatch clears the attempt's binding and withholds its publication.

## Evidence

- Inventory admits receipt-backed recovery and requires usable exact evidence for reclamation. [1]
- A failed inventory qualification returns before a snapshot can publish the attempt's next input. [2]
- The writer rechecks the observed rows under its own registry lock. [3]
