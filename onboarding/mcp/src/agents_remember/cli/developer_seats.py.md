# mcp/src/agents_remember/cli/developer_seats.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

Lists existing live AR role seats for cross-chat developer recipients.

## Code Commentary

### Logic

Walks bounded current role/taskless launch records, joins host live unarchived agents, keeps newest record per agent, resolves canonical task labels and pages rows with completeness evidence.

### Invariants And Boundaries

Historical receipts alone do not create selectable live seats. Budget/unread gaps report incomplete; missing then means unknown.

## Evidence

- Lists existing live AR role seats for cross-chat developer recipients. [1]
- Lists existing live AR role seats for cross-chat developer recipients. [2]
- Lists existing live AR role seats for cross-chat developer recipients. [3]
