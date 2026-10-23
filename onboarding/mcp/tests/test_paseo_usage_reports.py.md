# mcp/tests/test_paseo_usage_reports.py

## Governing Overview

[tests overview](overview.md)

## Purpose

The bridge reads the pinned host's usage reports as the SDK answers them.

## Code Commentary

The real client answers with a request-and-reports envelope and refuses a call that selects both by agent and by report ids. The finding this file guards was a bridge that read the answer as a bare array and refreshed with both selectors, so the envelope read as no entries and the refresh could never run. The fake client keeps the pinned shape and the SDK's own refusal.

**L184 — INV-4T6KSE.** The report reader is held by these cases, which is where a shape change would surface. The obligation this leaf records for this place is stated in the invariant named here; the card's earlier account of this file stands, and this paragraph adds what the change made true.


Scenario timestamps are sampled when the case builds its inputs. `_fresh()` uses the current UTC time, `_stale()` subtracts five minutes, and `_reset()` adds two hours. `_entry()` resolves its default stale stamp when called. Import-to-execution delay therefore does not consume a case's intended freshness window. The bridge's 60-second threshold and the fresh/no-refresh versus stale/refresh assertions stay unchanged.

Cases that compare timestamp identity capture one stamp and reuse it: the refresh case compares its returned `fetchedAt` with that stamp, and an empty refresh preserves the exact cached stale stamp.

## Evidence

- Scenario timestamps are sampled at call time [1]
