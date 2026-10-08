# mcp/test_support/agents_remember_test_support/testing/waits.py

## Governing Overview

[Python test evidence infrastructure](overview.md)

## Purpose

Provides synchronous and asynchronous condition waits under one shared 30-second hang guard.
The deadline prevents an endless test; it is not a performance requirement or a readiness witness.

## Code Commentary

`wait_until` and `async_wait_until` evaluate the supplied condition first, polling only while it is
false. They yield with a short sleep between checks and raise an assertion naming the unreached
condition when the guard expires. A true condition succeeds even when the guard has no remaining time.
Tests requiring causal ordering must supply an actual entry, completion or opportunity signal rather
than treating the poll interval or guard as evidence that a producer ran.

## Evidence

No external domain claim is needed for these repository-owned test helpers.


- Synchronous polling waits for the named condition under the shared hang guard. [1]
- Asynchronous polling yields until the condition or hang guard. [2]
