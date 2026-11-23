# mcp/test_support/agents_remember_test_support/testing/event_loop.py

## Governing Overview

[Python testing boundary](overview.md)

## Purpose

Create asyncio loops for test processes whose sandbox can deny the socket send that wakes the selector.

## Operating boundary

The selector caps each idle wait at 50 milliseconds and preserves any shorter timeout. When a cross-thread callback is queued but the socket send is refused, the selector returns control to asyncio so the next iteration can process the queue. The factory returns a normal selector event loop, including its normal executor shutdown path.

Pytest installs this factory for Runner and the public asyncio loop constructor for the session. Test-authored dashboard and historical-review children supply it explicitly. The factory belongs to test support.

## Evidence

- The selector limits idle waits and the factory installs it on an asyncio selector loop. [1]
- Pytest installs both factory aliases and registers their restoration during cleanup. [2]
