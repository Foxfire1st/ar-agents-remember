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

## 260928-MIK-L177 Background Units Run On Their Own Pool

`offload` no longer schedules on the loop's default executor, which every `asyncio.to_thread` call in
the process shares; a long background unit could therefore hold a thread another awaited read needed.
(Starlette's own synchronous endpoints are not on that executor: `run_in_threadpool` hands them to
AnyIO's worker threads, so the queueing this change removes is the loop's, not Starlette's.)
Background units now run on a process-wide `ThreadPoolExecutor` named `ar-background` with
`BACKGROUND_WORKERS = 4` threads, created once and never resized, and each unit carries a copy of the
loop's context so it observes the same context variables a read does. The accounting labels, the
bounded detail and the cancellation drain are unchanged; the change is where the work runs.

## 260928-MIK-L177 A9 — The Unit Is A Task, Not A Bare Future

`offload` now runs a unit through `_background_thread`, which copies the loop's context and awaits
`loop.run_in_executor(_background_pool(), context.run, func)`, and it wraps that in an explicit
`asyncio.create_task`. The task boundary is the point: the shutdown drain shields and awaits that task
even when its owner is cancelled repeatedly, which a bare executor future did not give. The executor
stays the background-only pool with `BACKGROUND_WORKERS = 4`; accounting labels, bounded detail and
cancellation handling are unchanged.
