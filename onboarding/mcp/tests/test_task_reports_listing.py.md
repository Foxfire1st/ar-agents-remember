# mcp/tests/test_task_reports_listing.py

## Governing Overview

[Route overview](overview.md)

## Purpose

Server tests for the per-task reports listing: recorded starts read newest first with the task filter, the answer caps at twenty with an explorer link beyond, empty starts and null reports degrade honestly, and unreadable or out-of-root records are refused.

## Code Commentary

Four cases pin `list_task_reports`: newest-first ordering with the recorded task reference filter, the twenty-row cap with the explorer folder link, empty starts and null-report rows, and the refusal table including the preserved partial-chain 409. Live and archived receipts both open through the confined report path.

## Evidence

- Starts read newest first with the task filter. [1]
- The answer caps at twenty with an explorer link. [2]
- Empty starts and null reports degrade honestly. [3]
- Unreadable and out-of-root records are refused. [4]
