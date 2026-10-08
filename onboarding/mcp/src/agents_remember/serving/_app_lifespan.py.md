# mcp/src/agents_remember/serving/_app_lifespan.py

## Governing Overview

[Serving overview](overview.md)

## Purpose

The lifespan of the dashboard app and the background loops it owns: terminal catalog observation, the
agent notifier, provider metrics, workspace event compaction, and two optional memory diagnostics. It also
builds the two volatile payloads that ride on a state response, the notifier heartbeat and the terminal
observer health.

## Code Commentary

### Startup and shutdown (`_serving_lifespan`)

Startup, in order: migrate the control-plane identity logs; compact the workspace event river once; start
the observer-health lifetime; observe the terminal catalog once (`_prime_terminal_observation`); prime the
projection; then create the tasks for the projector, the metrics loop, the terminal observation loop, the
agent notifier loop, the relay death watch and the river compaction loop. A heap diagnostic task and a
memory trim task are added only when their environment switches are set.

Shutdown, in order:

1. When the runtime has a `review_trees_shutdown` callable, it is called on a worker thread
   (`asyncio.to_thread`) and awaited. This stops and reaps the reviewer's worklist children before
   anything else is torn down, and it does not block the event loop while it waits for them.
2. Every background task is cancelled and awaited.
3. The terminal host is shut down.

### Loops

- `_terminal_observation_loop` refreshes the terminal catalog for the whole serving lifetime, independent
  of HTTP requests. It sleeps after each attempt returns, so attempts never overlap.
  `_observe_terminal_catalog` publishes the outcome and duration of each completed observation to the
  observer-health record; a cancelled observation records nothing.
- `_prime_terminal_observation` runs the same observation once before the projection is primed and
  contains a failure, so a degraded observation does not prevent serving.
- `_agent_notifier_loop` loads the agentic settings inside its `try` on every sweep. A failed load keeps
  the last good settings for that sweep; with none, the sweep is skipped.
- `_to_thread_drained_on_cancel` runs a function on a thread and, when the awaiting task is cancelled,
  waits for the thread to finish before the cancellation propagates.

### Payloads

- `_agent_notifier_heartbeat_payload` computes the age of the last notifier tick at response time and
  marks it stale at the configured cutoff.
- `_terminal_observer_health_payload` returns the observer's persisted health record at response time, or
  `None`, in which case the key is omitted. It reads only and never repairs the record.

## Leaf archive recovery in the terminal observation loop (MIK-R76)

`_terminal_observation_loop` constructs one `LeafArchiveRecovery` and calls `archives.tick()` through
the existing `_to_thread_drained_on_cancel` helper after each terminal catalog observation, closing
the recovery cursor in a `finally`. The loop remains the only recurring owner; no second timer,
queue or scheduler is added, and an archive-recovery failure is logged and retried on the next
interval.

## Evidence

- Startup order, the background tasks, and the shutdown order with the tree route's shutdown first. [11]
- The observation loop sleeps after each attempt. [12]
- One completed observation is published to the health record. [13]
- The pre-serve observation and its contained failure. [14]
- The notifier loop keeps the last good settings. [15]
- A cancelled wait drains its worker thread first. [16]
- The observer-health payload at response time. [17]
- Every lifespan of the fixture calls the worklist shutdown exactly once, off the main thread. [18]
- A shutdown during a running leaf-wide read stops the child and its Git process. [19]
