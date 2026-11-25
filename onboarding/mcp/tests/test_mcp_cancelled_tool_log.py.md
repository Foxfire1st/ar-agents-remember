# mcp/tests/test_mcp_cancelled_tool_log.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Tests that an MCP request cancelled before its call ends leaves exactly one tool-log row that says how the call ended.

## Code Commentary

`logging_server` is a bare `AgentsRememberMCP` from the dispatch-concurrency test module, with the startup latch and the build-currentness read stubbed out and a config whose transcript root is `tool-log` under the test's temporary folder. `role_server` adds the role-agent tools to it. `_logged_call` requires exactly one row in the day's tool log with the expected tool and arguments, and `_logged_detail` reads that row's detail file.

- `test_cancelled_running_writer_logs_once` cancels a running synchronous tool. The request ends only after its thread is released. A late error gives one `raised` row whose detail keeps the error text and `requestCancelled: true`; a late result gives one ordinary row.
- `test_cancelled_before_dispatch_logs_wait` cancels a request while it waits for the held write lock or for a slow build-currentness read. The tool never runs, and the row has code `cancelled`, a `waitingFor` field naming the wait and an error saying the tool never ran.
- The role cases use a waiting `role_message`. A cancellation ends the request promptly, before the worker has finished. `test_detached_role_worker_logs_the_error_after_cancellation` and `test_detached_role_worker_logs_during_runner_shutdown` check that the worker's later error is logged as `raised` with `requestCancelled`, also when the worker finishes only while the event loop runner shuts down. `test_waiting_role_message_cancels_before_its_worker_returns` checks that a later result is logged once as an ordinary row.
- `test_cancelled_queued_role_work_never_starts` keeps a one-thread executor busy, so the role message is still queued when it is cancelled: its work never runs, and the row has code `cancelled` with `waitingFor: worker-thread`.
- `test_both_registered_role_tools_use_the_detached_thread_helper` checks that `user_settings_init` and `role_message` pass their work through `run_in_detached_request_thread`.

## Relationships

The module is declared in the `integration` lane. It proves the server's cancellation logging and the detached worker helper; see the cards of `mcp/src/agents_remember/mcp/server.py` and `mcp/src/agents_remember/mcp/thread_workers.py`.

## Evidence

- The logging server and the one-row log readers. [1]
- A cancelled running tool logs its late error once, or its late result. [2]
- A request cancelled while it waits is logged as cancelled with its wait. [3]
- A detached role worker logs its late error, also at runner shutdown. [4]
- Both role tools use the detached helper. [5]
- Cancellation ends a waiting role message before its late result is logged. [6]
- Cancelled queued role work never starts and is logged with the worker-thread wait. [7]
