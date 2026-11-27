# mcp/tests/test_reader_task_context_protocol.py

## Governing Overview

[Route overview](overview.md)

## Current source contract evidence

- Current source declarations support the qualified naming or fixture account; no executed test or acceptance is inferred. [5]

## Purpose

An in-memory registered MCP session verifies the optional exact task_context pair on context_packet/read_ar_files. Slim packets name distinct base/leaf code and memory roots. A memory root is normalized against its absolute answered code anchor only when it is code-relative; an absolute root stays absolute. The added os import supports that assertion, not a new protocol deadline or admission policy. Only a leaf marker is created: repeated and concurrent naming calls assert base exists=false and leaf exists=true, and that the naming answers carry no body field — `source`, `content`, `text` or `body` — at any depth of the response or of a file row, while a source root or path name such as `sourceRoot` is allowed, which is what distinguishes a source root from file content. The removed object-form entry refuses argument-removed with the required sentence; wrong repository/contract or an incomplete context pair raises the named protocol error. Marker cleanup restores both Git statuses in the assertions. It launches no host runtime or stdio server.

## Code Commentary

### Logic

`RegisteredTaskReaderContextProtocolTests.setUp` builds its server through the product factory `create_server`, not a bare `MCPServer` with selected registrars, so the test exercises the full product wiring (including the SEP-2133 `SkillsExtension` registered per server at construction). `tearDown` resets the worktree services and cleans the temporary fixture; no ambient observer or process-wide session patch is installed or reset.

`test_registered_readers_use_call_local_admitted_leaf_context` drives the protocol exchange through `_run_protocol`, which runs the whole exercise under `_await_protocol`'s default 60-second limit; a passed limit raises the ordinary assertion failure "MCP reader protocol responses did not arrive". `_git_status` gives the test's two Git observations the same limit.

`test_late_tool_list_response_times_out_and_closes_the_handler` starts a three-second response deadline only after the session is initialized, patches public `self.server.list_tools` via `mock.patch.object` to hold the response until it is cancelled, requires the named failure, and then re-runs the primary case so the server is proven usable afterwards. The shared limit of the driver and of `git status` stays at 60 seconds, so neither a slow `git status` nor a slow session start fails the case for reasons it does not test.

### Invariants And Boundaries

- The server under test is composed through `create_server` the way the product composes one; under `mcp` 2.x, `SkillsExtension` registers per server at construction with no process-wide session patch. Teardown resets worktree services and removes the disposable fixture.
- The protocol exchange ends in a named failure at its limit and the module's own `git status` observations end at a subprocess limit; the `git`/`init_repo` helpers in `test_worktree_support` carry no timeout of their own and are outside the bounded protocol operations.

## Evidence

- The scoped current source carries the module/document behavior described above. [1]

- The bounded driver and the 60-second Git observation limit. [3]

- The late-response case that patches public `self.server.list_tools` to hold its handler and starts its deadline after session initialization. [4]
- The product factory `create_server` composes `AgentsRememberMCP` with `SkillsExtension` and invokes `TOOL_REGISTRARS`. [2]
