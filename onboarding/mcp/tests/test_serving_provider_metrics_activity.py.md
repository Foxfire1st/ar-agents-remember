# mcp/tests/test_serving_provider_metrics_activity.py

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Prevent launch-authority absence from suppressing the serving lifetime's periodic provider safety observation of leftover labelled stacks.

## Code Commentary

The suite calls the actual `_metrics_loop` with controlled sampling, degradation, store and interval boundaries. Empty-authority operation still samples, records, evaluates and compacts. Scenarios cover live admission followed by revocation, admission wholly between ticks and restart with leftovers. Invalid UTF-8 and bad JSON are exercised under empty and enabled boot maps; launch refusal is checked separately from safety. Interval cancellation ends the real loop and remains the public outcome.

## Invariants And Boundaries

The earlier provider-activity gate/helper was withdrawn, not accepted as an empty-fleet optimization. This retained test module guards the original periodic safety loop; it neither launches real containers nor establishes actual fleet retirement, Docker success or native CPU/outbound totals. Safety observation and permission to launch remain separate authorities.

## Evidence

- Real-loop assertions retain periodic safety across empty, live, revoked, between-tick, restarted and malformed authority. [1]
- The unchanged metrics owner samples, records, evaluates, compacts and sleeps without an authority/page gate. [2]
