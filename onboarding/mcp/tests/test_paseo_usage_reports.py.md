# mcp/tests/test_paseo_usage_reports.py

## Governing Overview

[overview](overview.md)

## Purpose

The bridge reads the pinned host's usage reports as the SDK answers them.

## Code Commentary

The real client answers with a request-and-reports envelope and refuses a call that selects both by agent and by report ids. The cases guard against a bridge that reads the answer as a bare array or refreshes with both selectors, which would read the envelope as no entries and never refresh. The fake client keeps the pinned shape and the SDK's own refusal.

**INV-4T6KSE.** The report reader is held by these cases, which is where a shape change would surface; the obligation for this place is stated in that invariant.


Scenario timestamps are sampled when the case builds its inputs. `_fresh()` uses the current UTC time, `_stale()` subtracts five minutes, and `_reset()` adds two hours. `_entry()` resolves its default stale stamp when called. Import-to-execution delay therefore does not consume a case's intended freshness window. The bridge's 60-second threshold and the fresh/no-refresh versus stale/refresh assertions stay unchanged.

Cases that compare timestamp identity capture one stamp and reuse it: the refresh case compares its returned `fetchedAt` with that stamp, and an empty refresh preserves the exact cached stale stamp.

## Evidence

- Scenario timestamps are sampled at call time [1]
