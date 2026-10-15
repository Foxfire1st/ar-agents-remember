# mcp/src/agents_remember/serving/_app_lifespan.py

## Governing Overview

[Serving overview](overview.md)

## Purpose

Own the serving lifetime, its retained background loops and drained shutdown. Terminal catalog observation, notifier sweeps and their health payload readers are absent; one leaf-archive recovery cadence remains.

## Code Commentary

Startup compacts the workspace river before projector prime, then starts projection, provider metrics, leaf-archive recovery, held-message delivery and river-compaction tasks. Heap tracing and malloc trimming are separately opt-in. The archive loop awaits one tick through the drained thread boundary, sleeps after each completed attempt and closes its archive owner in finally; it introduces no second recovery timer. Shutdown first invokes the review-tree child shutdown hook, then cancels and awaits every background task. A cancelled shielded worker is awaited before cancellation is re-raised, so serving cannot return while that worker still writes. Provider sampling/recording/degradation/compaction use the same drained boundary. Source inspection does not supply new teardown execution.

The serving lifetime retains the L81 shared background ledger and server-side host-start loading watch. Archive recovery, provider metrics, held-message work and each native resume are attributed to their executing worker units. The loading driver uses shared OS lease/progress, records completion or cancellation, and drains before its claim closes. Removed terminal observation and notifier sweeps are not reintroduced by that loading watch.

## Evidence boundary

This is current-source interpretation of the A9 candidate, not a new test result, CODE grade or MEMORY acceptance. The retained supporting references below are reauthored through the ordinary fixer; unsupported removed constructs are withdrawn, not rebound to arbitrary neighboring code.

## Source-bound reference inputs

- [11]
- [16]
- [20]
- [22]
- [24]
- [25]
- [26]

