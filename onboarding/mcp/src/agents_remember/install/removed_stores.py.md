# mcp/src/agents_remember/install/removed_stores.py

## Governing Overview

[Area overview](../../../overview.md)

## Purpose

Inventory retired stores for install reporting and the separately commanded removal path.

## Code Commentary

The shared inventory names removed-part files/folders, lifecycle event/heartbeat/served stores and retained stored-gate logs. Install reporting deletes none of them. Discovery uses lstat, never follows a store symlink, includes plain-file lock/backup siblings and records unreadable traversal instead of calling it absence. A gate log is listed without the lock the landing chain still uses. Optional lone terminal gate-lock stores require complete readable canonical-contract evidence, including archived contracts, and terminal cleanup with no unknown cells; notes copies are not contracts. Reported sizes are best-effort summaries, not a locked filesystem snapshot. This module inventories; the explicit CLI command owns deletion.

## Evidence

- Retired path inventory and no-install-deletion notice. [1]
- Discovery does not follow stores through symbolic links. [2]
- Terminal-lock eligibility fails closed on incomplete contracts. [3]
- Inventory and reporting keep gate logs distinct. [4]
