# mcp/src/agents_remember/mcp/thread_workers.py

## Governing Overview

[MCP overview](../../../overview.md)

## Purpose

Runs blocking native tool work in a thread while preserving its request context, and records how a cancelled request's worker ended.

## Code Commentary

`run_in_request_thread` starts the worker as its own task and waits for it, so cancelling the caller does not cancel the worker. When the caller is cancelled, the helper waits for the worker inside a shielded cancel scope, also through repeated cancellation, records an exception the worker raised on the request's `WorkerCancellation`, and re-raises the cancellation. Without a cancellation it returns the worker's result or raises its error. The caller retains its scope and any write lock while the worker drains.

`track_worker_cancellation` binds a `WorkerCancellation` to the request through a context variable. It carries the request's two log writers, one for an error that arrives after the cancellation and one for work cancelled before it started, and it clears the stored error on exit.

`run_in_detached_request_thread` lets a cancellation through at once instead of draining. Work still queued in the thread pool never starts, and the request's wait writer runs. Work already running goes on; an error it raises later is written from the worker thread itself, so the log line does not depend on the event loop that the cancellation may already have closed.

## Relationships

Native dispatch uses this helper for blocking calls. The registered role start and role start set operations use it directly. `server.py` opens `track_worker_cancellation` for every tool call with its raised-error and cancelled-wait writers, and runs the stale-build refusal through `run_in_detached_request_thread`. The registered `role_message` and `user_settings_init` tools also use the detached helper.

## Evidence

- The worker drains under a shielded scope before the caller's cancellation propagates, and its error is kept for the request's log. [1]

- The tracker binds the request's two log writers and clears the stored error on exit. [2]
- The detached helper passes cancellation on at once, logs a still-queued wait, and lets the worker write its own late error. [3]
