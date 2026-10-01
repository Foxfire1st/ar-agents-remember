# mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_location_errors.py

## Governing Overview

[Worktree-integration overview](../overview.md)

## Purpose

Centralizes typed lifecycle-location failures and exact regular-file reads for locator, manifest,
contract, journal, archive, and receipt authority.

## Code Commentary

The reader distinguishes genuine absence from present-but-invalid state. An unreadable,
non-regular, or symlinked authority file is a conflict and is never silently treated as missing.

## Invariants And Boundaries

- Present-invalid authority fails closed.
- All location callers share one failure vocabulary instead of reimplementing lower-level catches.
- No scan, guessed path, compatibility reader, or raw-Git fallback is introduced.
