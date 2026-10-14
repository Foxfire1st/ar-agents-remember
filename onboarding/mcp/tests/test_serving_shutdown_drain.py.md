# mcp/tests/test_serving_shutdown_drain.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Source-level teardown tests for the retained leaf-archive recovery owner and its off-loop tick worker. The retired terminal-refresh/startup-prime cases are not current test coverage.

## Code Commentary

The current suite parks a real LeafArchiveRecovery.tick worker under the real serving lifetime and observes the cancellation owner directly await that worker before release. Its virtual clock drives archive-recovery cadence, not terminal observation. Fixture/finalizer bounds and patched-surface restoration belong to the test, not production shutdown deadlines. Current assertions concern in-flight recovery drain and the final durable archive result; no current pytest run is claimed by this card.

## Evidence boundary

This is current-source interpretation of the A9 candidate, not a new test result, CODE grade or MEMORY acceptance. The retained supporting references below are reauthored through the ordinary fixer; unsupported removed constructs are withdrawn, not rebound to arbitrary neighboring code.

## Source-bound reference inputs

- [1]
- [2]
- [3]

