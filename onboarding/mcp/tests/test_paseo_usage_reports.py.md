# mcp/tests/test_paseo_usage_reports.py

## Governing Overview

[mcp overview](../overview.md)

## Purpose

The bridge reads the pinned host's usage reports as the SDK answers them.

## Code Commentary

The real client answers with a request-and-reports envelope and refuses a call that selects both by agent and by report ids. The finding this file guards was a bridge that read the answer as a bare array and refreshed with both selectors, so the envelope read as no entries and the refresh could never run. The fake client keeps the pinned shape and the SDK's own refusal.

**L184 — INV-4T6KSE.** The report reader is held by these cases, which is where a shape change would surface. The obligation this leaf records for this place is stated in the invariant named here; the card's earlier account of this file stands, and this paragraph adds what the change made true.
