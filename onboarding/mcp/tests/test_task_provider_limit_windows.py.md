# mcp/tests/test_task_provider_limit_windows.py

## Governing Overview

[mcp overview](../overview.md)

## Purpose

A limited task's hover names the window that actually holds the seat.

## Code Commentary

The producer stores a report's resumption as the latest reset among the exhausted windows, so that is the seat's own window. The served detail used to name whichever window the runtime listed first, telling a reader a session reset in hours while the same account's weekly window held the seat for days.

**L184 — NEW-LIMIT-FROM-REPORT-ONLY.** The task's own windows are computed here, so the earliest-reset rule is held by this case. The obligation this leaf records for this place is stated in the invariant named here; the card's earlier account of this file stands, and this paragraph adds what the change made true.
