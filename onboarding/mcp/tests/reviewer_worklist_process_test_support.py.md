# mcp/tests/reviewer_worklist_process_test_support.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Controlled real-child replies, owner-local clocks and executor contention for the reviewer worklist process tests. These fixtures make sharing, deadline and resource ownership observable without elapsed-speed assertions.

## Code Commentary

`held_child_script` parks a real process on a private release path; the caller observes admission or contention before releasing it. `controlled_worklist_clock` patches only the process owner's monotonic clock, leaving harness hang guards on real time. `busy_default_executor` holds both workers of a two-thread default executor plus one queued job until the route has answered, then releases and drains all work.

The process-tree helpers read Linux `/proc`, and the lifetime-child script waits for its parent to observe the Git descendant before arming the tested alarm. `joined_requesters` bounds completion with the shared guard while measuring the number of live children. This file supplies fixtures and observations; the importing test module owns the product assertions.

## Evidence

No Domain Documentation source is configured; the references below establish repository-owned fixture and assertion behavior.

- A child stays held until the test releases its private gate. [1]
- Only the process owner's request clock advances under test control. [2]
- Both executor workers and a queued job remain held until the route answers. [3]
- The lifetime script arms its alarm after the Git-descendant handshake. [4]
