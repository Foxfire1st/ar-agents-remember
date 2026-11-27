# mcp/src/agents_remember/serving/held_reset_scheduler.py

## Governing Overview

[overview](overview.md)

## Purpose

Owns the deadline-driven wake loop and fixed-size worker pool that deliver provider-limited held messages once their reset time arrives, independently of the ordinary bounded held-message sweep tick.

## Code Commentary

The scheduler pins peak concurrency with `RESET_WORKERS = 16`, head recheck cadence `_HEAD_RECHECK_SECONDS = 3.0`, and retry deferral `_RETRY_DELAY = timedelta(seconds=15)`. `ResetAttempt`, `ResetDeliveryPorts`, and `ResetPassResult` define the typed attempt result, injected CLI ports (`adopt` and `attempt`), and pass summary across the serving-to-CLI boundary.

`deliver_due_pass(index, pool, pool_size, attempt, now)` takes one due snapshot from `index.due_at(now)` and dispatches each `ResetEntry` through `pool.map(run, entries, buffersize=pool_size)` so concurrent attempts across distinct recipients stay bounded by `pool_size` and submission never buffers the full due list unboundedly. Each worker call supplies `datetime.now(UTC) + _RETRY_DELAY` as its retry deadline and aggregates `selected`, `attempted`, and `delivered` into `ResetPassResult`.

`run_held_reset_scheduler(config, ports, ledger)` creates `HeldResetIndex(config.coordination_root)` and two dedicated executors: a single-thread `ar-reset-coordinator` pool and a 16-thread `ar-held-reset` delivery pool. At startup it runs `ports.adopt(index)` once on the coordinator via `offload_on` under `OWNER_HELD_DELIVERY`, logging any exception without crashing startup. It then runs `_run_due_passes`, which queries `index.next_attempt()` on the coordinator; when the head is due (`head <= now`), it runs `deliver_due_pass` on the coordinator (with each worker delivery measured under `OWNER_HELD_DELIVERY`) and immediately loops to recheck the head; otherwise it sleeps for `min(_HEAD_RECHECK_SECONDS, (head - now).total_seconds())` so both an earlier head written by another process and an imminent reset wake promptly.

## Boundaries

`RESET_WORKERS = 16` bounds peak worker threads independently of fleet size; under the D987 Option A host-bridge ceiling, a 16-worker pool clears up to roughly 300 due recipients within thirty seconds of reset and drains larger simultaneous resets at roughly 11 recipients per second. All executor calls run through `background_accounting.offload_on` and `measured`, preserving cancellation drain and `"held-delivery"` accounting without sharing the 4-worker `ar-background` pool.

## Evidence

- `RESET_WORKERS = 16`, `_HEAD_RECHECK_SECONDS = 3.0`, `_RETRY_DELAY = timedelta(seconds=15)`, and the typed port/result dataclasses define the scheduler's fixed bounds and boundary contract. [1]
- `deliver_due_pass` snapshots `index.due_at(now)` and bounds submission and concurrency through `pool.map(run, entries, buffersize=pool_size)`. [2]
- `run_held_reset_scheduler` and `_run_due_passes` run startup adoption and deadline-driven due passes on dedicated `ar-reset-coordinator` and `ar-held-reset` pools accounted under `OWNER_HELD_DELIVERY`. [3]
