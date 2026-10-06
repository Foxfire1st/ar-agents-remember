# mcp/tests/test_reader_task_context_protocol.py

## Governing Overview

[Route overview](overview.md)

## Purpose

An in-memory registered MCP session verifies the optional exact task_context pair on context_packet/read_ar_files. Alternating and concurrent base/leaf reads return their own source and memory roots, wrong repository/contract or incomplete pair refuses, and the temporary marker cleanup restores both Git statuses. It launches no host runtime or stdio server.

## Code Commentary

### Logic

`RegisteredTaskReaderContextProtocolTests.setUp` builds its server through the product factory `create_server`, not a bare `FastMCP` with selected registrars. The factory installs the skills extension's process-wide request union together with its per-server dispatcher; a server composed without the dispatcher silently drops `tools/list` once another test in the same process has installed the union, which is the hang this fixture met in a combined run. `tearDown` resets the ambient observer and the worktree services.

`test_registered_readers_use_call_local_admitted_leaf_context` drives the protocol exchange through `_run_protocol`, which runs the whole exercise under `_await_protocol`'s default 60-second limit; a passed limit raises the ordinary assertion failure "MCP reader protocol responses did not arrive". `_git_status` gives the test's two Git observations the same limit.

`test_late_tool_list_response_times_out_and_closes_the_handler` starts a three-second response deadline only after the session is initialized, holds its `tools/list` handler until it is cancelled, requires the named failure, and then re-runs the primary case so the server with its patched handler is proven usable afterwards. The shared limit of the driver and of `git status` stays at 60 seconds, so neither a slow `git status` nor a slow session start fails the case for reasons it does not test.

### Invariants And Boundaries

- The server under test is composed the way the product composes one; the fixture does not reset the skills extension's process-wide request union. Its teardown clears only what its own factory call installed: the ambient lifecycle and the worktree services.
- The protocol exchange ends in a named failure at its limit and the module's own `git status` observations end at a subprocess limit; the `git`/`init_repo` helpers in `test_worktree_support` carry no timeout of their own and are outside the bounded protocol operations.

## Evidence

- The scoped current source carries the module/document behavior described above. [1]
- The factory that pairs the process-wide request union with its per-server dispatcher. [2]
- The bounded driver and the 60-second Git observation limit. [3]
- The late-response case that holds its handler and starts its deadline after session initialization. [4]
