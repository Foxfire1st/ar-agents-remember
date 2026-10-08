# mcp/src/agents_remember/worktrees/reopen_row_guard.py

## Governing Overview

[worktrees overview](overview.md)

## Purpose

What a master's row must satisfy before reopening a leaf resets it to planning. The guard refuses a row that carries a retirement proof through the shared retired-row refusal, so reopening never changes a retirement record.

## Code Commentary

`require_reopenable_row` checks the master's row for the reopened leaf and calls `refuse_retired_row` when the row records a retirement; the caller supplies the read and refusal seams so the guard stays testable.

## Evidence

- Reopening a leaf refuses a master row that carries a retirement proof, through the shared retired-row refusal. [1]
