# mcp/src/agents_remember/serving/background_accounting.py

## Governing Overview

[governing overview](overview.md)

## Purpose

Attribute actual executing-thread CPU and wall intervals to every wired serving owner, record projector wake reasons/domains/paths, and expose cumulative plus trailing diagnostics. Bounded detail and monotonic aggregate buckets report incomplete cutoff windows honestly; process share is context, not owner CPU. Offloaded cancellation drains the worker and synchronous publication is separately measured.

## Code Commentary

Attribute actual executing-thread CPU and wall intervals to every wired serving owner, record projector wake reasons/domains/paths, and expose cumulative plus trailing diagnostics. Bounded detail and monotonic aggregate buckets report incomplete cutoff windows honestly; process share is context, not owner CPU. Offloaded cancellation drains the worker and synchronous publication is separately measured.

The retained catalog has nine labels: projection, landing-refresh, terminal-observation, metrics, held-delivery, river-compaction, warmup, event-tail and startup. The terminal-observation label now accounts for the retained leaf archive recovery loop; it does not revive terminal refresh. L113 removed the agent-notifier, relay-death-watch and conversation-ingestion record sites, so their unused constants and catalog entries are absent. Surviving accounting and budgets remain governed by the existing owners.

## Boundaries

Local implementation and executable evidence do not replace requirement authority or the owning transaction. Retained source semantics and explicit unavailable/failure states remain binding.

## Evidence


- Nine retained labels account for wired serving work after three retired record owners were removed; actual executing-thread CPU, bounded detail, honest incomplete windows and worker drain remain the existing accounting contract. [1]



## Background Pool And Dedicated Executors

`offload` schedules background units on a process-wide `ThreadPoolExecutor` named `ar-background` with `BACKGROUND_WORKERS = 4` threads (created once and never resized) rather than on the event loop's default executor, so long background work cannot starve awaited default-executor reads. (Starlette's synchronous endpoints use AnyIO's worker threads via `run_in_threadpool`, so this isolates the event loop's default executor rather than Starlette's.) Each unit runs through `_background_thread`, copying the loop's context so context variables remain visible, and is wrapped in an explicit `asyncio.create_task` awaited through `_drain_worker`. On cancellation, `_drain_worker` shields and awaits the running worker task across repeated cancellations before re-raising, preserving worker-drain guarantees that a bare executor future does not provide.

`offload_on(executor, owner, ledger, func, *args, **kwargs)` runs a measured unit on a caller-supplied dedicated `Executor` (such as the held-reset scheduler's coordinator pool) through the same context-copying `_background_thread` and `_drain_worker` cancellation-drain boundary, keeping owner attribution and shutdown drain consistent without sharing the 4-thread `ar-background` pool.
