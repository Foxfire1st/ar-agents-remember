# mcp/tests/test_serving_shutdown_drain.py

## Governing Overview

[overview](overview.md)

## Purpose

Source-level teardown tests for the retained leaf-archive recovery owner and its off-loop tick worker.

## Code Commentary

The current suite parks a real LeafArchiveRecovery.tick worker under the real serving lifetime and observes the cancelling owner wait for that exact worker, including through the current asyncio.wait drain path, before release. Its virtual clock drives archive-recovery cadence, not terminal observation. Fixture/finalizer bounds and patched-surface restoration belong to the test, not production shutdown deadlines. The fixture hands the lifespan a real `McpRuntimeConfig` rooted in the test's temporary root, because the serving lifetime records and removes its running-server record against that configuration. Current assertions concern in-flight recovery drain and the final durable archive result; no current pytest run is claimed by this card.

## Source-bound reference inputs

- [2]
- [3]

- The fixture witnesses the cancelling owner wait for the exact archive-recovery tick worker, following the measured wrapper and the asyncio.wait drain path. [1]
