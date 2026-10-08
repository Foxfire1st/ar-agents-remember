# mcp/tests/test_serving_shutdown_drain.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Cancellation and shutdown ownership checks over the real serving lifespan: a running observation worker drains before the terminal host closes, startup-prime cancellation drains its worker, and the final durable commit remains relayable after the next startup.

## Code Commentary

The suite reuses the observation-loop virtual clock and recorders while parking a real refresh worker in its thread. A scoped task factory identifies that exact `to_thread` task and observes its direct await by the cancelling product coroutine. The monitor releases the still-held worker only after this drain boundary, so cancellation ordering is causal.

The host callback captures the durable state it closes over. Subsequent absence checks require every recorded producer task to be done and the virtual cadence to have no waiter, then compare the captured calls and bytes. Startup absence is checked after the same actual drain await. Finalizer waits and bounded cleanup rounds use the shared hang guard, independently of production's drain ownership. The fixture reports unfinished tasks and restores shared patch surfaces rather than letting a stuck drain strand the test runner. These local proofs do not constitute full-suite certification.

## Evidence

No Domain Documentation source is configured; the references below establish repository-owned fixture and assertion behavior.

- The cancelled product owner's direct await witnesses the exact worker drain. [1]
- The running worker drains before host close and post-close state stays unchanged. [2]
- Startup cancellation waits for its worker and finalizer bounds use the shared guard. [3]
- The last in-flight durable commit remains available to the next startup. [4]
