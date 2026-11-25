# mcp/src/agents_remember/package_data/paseo_plugin/server/provider_limit_check.ts

## Governing Overview

[plugin overview](../overview.md)

## Purpose

Run the one pending-only early-clear check that lets a deferred provider-limit resume or a held parent line act on a written clear instead of waiting for the old deadline.

## Code Commentary

The module keeps one timer while at least one resume or flush is pending, and stops it when none is. The first pending action's `observedAt` sets the due time; the timer then reads one limit-file snapshot every fifteen seconds through the tracker's generation-cached reader. A seat with a `clearedSeats` entry and no live limit in the same snapshot is cleared: its resume fires with the marker's `clearedAt`, and the cleared parents are claimed and flushed through one `flushClearedParents` call. The check re-arms from the moment it checked, so a clear published later is still seen; a snapshot that still shows a live limit acts on nothing.

## Evidence

- One shared fifteen-second snapshot serves the pending resumes and flushes, and stops with them. [1]
