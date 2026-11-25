# mcp/src/agents_remember/mcp/server.py

## Governing Overview

[overview](../../../overview.md)

## Current source contract evidence






## Purpose

`server.py` is the stdio MCP **process and transport-boundary wiring** for Agents Remember. It holds
`AgentsRememberMCP`, `create_server`, `run_server`, and `main`; tool ownership remains in the
registration families.

Every `@server.tool()` declaration and its model-visible docstring lives in
`agents_remember.mcp.registration`, one module per family. If you are
looking for what a tool advertises, what it refuses, or which payload builder it forwards to, that
is the [registration route overview](registration/overview.md), not this file.

Starts the configured MCP application with the ordinary registration families and adds the four explainer tools for a valid explainer launch.

## Code Commentary

A native invocation opens a lazy request memo and clears its shared owner map after all joined work exits. Both registered role-start workers retain that scope through cancellation while their thread drains. The native call then attempts allocator trim in a worker thread. Detached quality has its own computation scope.

### Logic

`create_server(config)` composes the application and server in the following order:

1. `install_compact_content()` — idempotent; makes the JSON text mirror of every tool result emit
   without FastMCP's hardcoded indentation. It affects text-mirror serialization only, never
   `structuredContent` or tool behaviour.
2. Install a supplier through the light kernel service holder; the first dependent worktree operation builds the default services once, including `LeafAgentArchive(config)`. Initialize the boot-time caller-identity tool writer through `server_startup.initialize_mcp_application(config)` and complete FastMCP settings before constructing the server. The writer's constructors are light; this is no blanket optional-work deferral claim.
3. `AgentsRememberMCP("Agents Remember", instructions=launched_server_instructions())`. A readable
   launch binding supplies the canonical task-server instruction line; unbound or unreadable binding
   supplies no instruction line.
4. Read the required explainer binding. Every launch invokes the ordered `TOOL_REGISTRARS`; a valid explainer launch also registers its four tools and retains its binding for those tools’ per-call validation. An invalid required binding refuses service.
5. `apply_read_only_marks(server)` applies the single `mcp/read_only.py` inventory to every registered
   tool. An unlisted name raises `UnknownReadOnlyMark`; server creation fails rather than advertising
   an unmarked tool. This step changes annotations, not registration order or handler ownership.

`run_server(config)` records this process in the running-server registry as an `"mcp"` server (`register_server`), runs `create_server(config).run()`, and calls the returned cleanup when serving ends; the cleanup removes the record and is also registered to run at normal process exit.

### Dispatch at the public transport boundary

AgentsRememberMCP.list_tools first awaits the FastMCP answer, then schedules start_after_discovery(config) with the running loop’s call_soon and returns that already-produced answer. The shared latch starts outside-scratch reconciliation once, including on a bare no-config server, and dashboard autostart only with config/settings. call_tool reaches that same latch as the fallback for a client that never lists, before entering tool_call_context. Calls to the four explainer tools validate their launched seat before the registered handler; ordinary tools keep their own argument admission. The retained delegation and raised-call logging use the shared boundary. Tool argument admission belongs to each retained registered schema. The synchronous dispatch wrapper described below keeps that validation path while moving the handler body off the event loop.

### Stale installed builds refuse publication writes at dispatch

Inside the tool-call context, a server with config reads its build currentness off the event loop (`build_currentness`) and carries that reading through the call with `tool_build_currentness`, so the answer boundary can annotate answers from a stale installed build. A checkout build yields no reading unless inspection is asked for, and a bare no-config server reads nothing. When the reading is an installed build in state `stale`, the call's arguments are validated against the registered tool's argument model, and a call that `is_stale_build_write` names a publication write is answered by `stale_build_refusal` (code `server-build-stale`, naming the loaded and installed digests and the restart remedy) without running the handler. The refusal is built in a detached worker thread, so cancelling the request does not wait for it. Reads, previews, unnamed tools and current or unknown readings go on to `_dispatch_tool`.

- A stale installed build's publication writes are refused before dispatch; other calls dispatch under the carried currentness reading. [13]

- `run_server` registers the process as an `"mcp"` server and runs the cleanup when serving ends. [14]

### Tool-call logging at the transport boundary (MIK-R108 rule 3)

`_execute_tool_call` brackets every call in `tool_call_context` carrying the exact arguments, start time and
this server's config (`_agents_remember_config`, set once by `create_server`) to the answer boundary,
which logs the completed call; a call that raises is logged here by `_log_raised_tool_call` and
re-raised, with the log write itself never raising. Refusals raised by registered tools happen inside the
context and are logged like other raised calls.

A cancelled request also leaves one row. The call opens `track_worker_cancellation` with two writers bound to its name, arguments and config. When the request is cancelled while it reads the build currentness, while it waits for the write lock, or while a detached worker is still queued, `_log_cancelled_wait` writes a row with code `cancelled`, a `waitingFor` field naming the wait (`build-currentness`, `write-lock` or `worker-thread`), and an error saying the tool never ran. When a worker raises after the request was cancelled, `_log_raised_tool_call` writes the ordinary `raised` row with `requestCancelled: true`: from `_log_interrupted_dispatch` for a drained worker, and from the worker thread itself for a detached one. Both kinds go through `_log_failed_tool_call`, which writes a detail file for every such row. A worker that returns a result after the cancellation is logged once at the answer boundary, as usual.

- The request's cancelled-wait and late-error writers are bound before dispatch, and a cancellation hands the interrupted state to the dispatch logger. [16]
- An interrupted dispatch logs either the wait it was cancelled in or the drained worker's error with the cancellation marker. [17]
- A cancelled wait is logged with code `cancelled`, the `waitingFor` field and a never-ran error. [18]
- A late error keeps the raised row and adds `requestCancelled`. [19]

`main(argv)` parses a required `--config` (an absolute path to trusted MCP settings JSON), calls
`declare_mcp_process()` **before** `load_config`, turns a `ConfigError` into an argparse error, then
calls `prepare_mcp_process()` between config loading and `run_server`. The early declaration remains necessary for trusted worktree-hosted MCP authority. Preparation only reasserts the declaration. Process entry and initialization start neither the sweep nor dashboard supervision; list_tools computes its answer before scheduling the shared latch on the next loop callback. The first call_tool on an ordinary or explainer-bound server invokes that same latch as the fallback before its explainer-tool binding check and dispatch. The first attempt starts the sweep even without config; with config and trusted `dashboard.autoStart` enabled, the existing total launcher also starts its daemon thread. Later calls start neither again. The sweep thread runs its heavy worktree owner in a one-shot child with stdin=DEVNULL, so it cannot consume the serving process’s MCP stdin. Launcher/sweep failures are contained and stdout remains the MCP protocol.

### Durable-store process-role startup is owned by the application boundary

`main` calls the application-layer `declare_mcp_process` before authority loading, then the
`prepare_mcp_process` wrapper before serving; the joint sweep/conditional-dashboard start is scheduled after the tools/list answer is produced, with first-tool-call fallback through the same latch.
`controlplane/durable_store.py` obtains shared-store writer roles from the kernel execution-mode owner, and the declaration identifies this process for ownership checks. `StoreOwnership.is_compaction_owner()` answers `role is None or
compaction_owner is None or role == compaction_owner`, so a process that declares nothing counts as
the owner of every log.

**The wrapper belongs on the process-entry path, not in `create_server`, and that is a correctness
requirement rather than a style choice.** `create_server` is a *factory* the test suite calls
in-process; `_declared` is a plain module-level dict with no reset, so a declaration made inside the
factory would stamp `"mcp"` onto the interpreter and every later test in it — including tests that
exercise the dashboard's own write paths. `main` runs once, in a process that exists only to be the
MCP server, so the wrapper declares a fact about the process rather than about whoever last built a
server object. The dashboard declares its durable-store role in `_dev_app` for the reload worker and in `run` for the foreground or daemon command.

What the declaration does **not** buy is durability. Every append and every rewrite of all six logs
takes that log's `flock` unconditionally, in every process, declared or not; the role only decides
who runs a reclaim pass and makes an undeclared new writer visible inside the two daemons. A process
that skips this line loses no records — it just stops being distinguishable from the dashboard.

### Invariants And Boundaries

- **No tool declarations here.** A new tool means editing one family module under `registration/`;
  a new family means a new module plus one entry in `TOOL_REGISTRARS`.
- The transport subclass may enforce a closed public boundary only when the framework-generated
  boundary is demonstrably weaker. It must not duplicate handlers, invent fallbacks, or become a
  second tool registry.
- Initialize compact-content serialization and application services before registering tools;
  no ambient lifecycle installer remains.
- **`declare_mcp_process()` stays before `load_config`, `prepare_mcp_process()` stays before
  `run_server`, and neither declaration may move into `create_server`.**
  `create_server` is called in-process by the test suite and `_declared` has no reset, so declaring
  there marks the whole interpreter `"mcp"` — after which `is_compaction_owner()` answers `True` for
  every MCP-owned log in a test that is exercising the dashboard, and `check_declared_writer()`
  answers for a process that is not the MCP server. The mirrored dashboard obligations are
  `cli/dashboard.py::_dev_app` and `cli/dashboard.py::run`.
- The shared post-discovery latch starts the sweep once even without config, and invokes dashboard autostart only with config/settings. The tools/list path schedules it after its answer exists; the first-call path is the fallback. The first attempt consumes the latch, with no second sweep or dashboard launch on later lists or calls.
- Do not add a raw shell or arbitrary-command tool to this server.

### Role Runtime and Scope

Readable launch binding supplies one canonical launched-server instruction line. Unbound or unreadable binding supplies no instructions; malformed binding still refuses at its actual server_info/bound-tool boundary rather than changing startup authority. create_server retains existing worktree services and application trust composition.

## Leaf agent archive binding (MIK-R76)

`create_server` installs the supplier whose first dependent worktree operation builds default services with `leaf_agent_archive=LeafAgentArchive(config)`, so finalize and abandon still reach the same archive owner. Supplier installation itself does not construct those services. Archive behavior remains in `cli/role_launch_archive.py` and the admitted terminal transactions.

## Evidence

### Repo-Internal References





- The registration package imports each family registrar, collects them in `TOOL_REGISTRARS`, and exports that collection for server wiring. [2]

- The stable tools package declares the public import surface for payload builders. [3]
- The package imports worktree payload builders from the owning module. [4]
- The package explicitly exports its builder vocabulary. [5]

### Cross-Repo References

No sibling repository defines this process wiring.

No meaningful cross-repo references found.

### Runtime Source References






## Startup composition boundary

The transport server imports its composition boundary as
`application.runtime.startup as server_startup`. Startup trust, configuration, registration, and
durable-store ownership remain application concerns.




## Call-owned definitions

Every tool call owns one definition scope around its complete dispatch. Synchronous handlers receive that scope through copied ContextVars; separate calls retain no definitions from each other.

## Synchronous dispatch and write ordering

After the applicable explainer-tool seat checks, `_dispatch_tool` wraps a synchronous registered function on a per-call Tool copy and runs it through the shared request-thread helper. FastMCP validates the original arguments, injects context and converts the result. The worker receives the call's context. Each async handler owns any worker it starts.

Potentially mutating synchronous calls hold one per-server lock until their worker stops. Cancellation does not release it while the thread is alive, including repeated cancellation. A request cancelled while it still waits for the lock leaves a `cancelled` tool-log row that names the write lock. Centrally declared read-only calls and explicitly nonwriting modes bypass the lock; the bypass is a dispatch policy, not host-wide purity or permission. A string-coercible false value does not satisfy the strict boolean checks.


- Threaded synchronous dispatch retains the registered validation and conversion path. [10]


- Declared reads and explicit nonwriting modes bypass the synchronous write lock. [11]



- Cancellation drains the worker before releasing its caller. [12]




- `create_server` builds the FastMCP instance and invokes the registered tool families.  Anchor: `create_server` 



- Frozen implementation of launched_server_instructions supporting the stated file behavior. [6]



- Frozen implementation of create_server supporting the stated file behavior.  Anchor: `create_server` 



- Current transport wiring retains boot-time caller identity and lazy worktree service construction. It schedules a shared post-discovery sweep/conditional-dashboard latch after producing the list answer, with first-call fallback; application initialization installs no ambient lifecycle.






- `create_server` builds the FastMCP instance and invokes the registered tool families. [1]

- `create_server` installs compact content, initializes the application services, registers every tool family, adds a bound explainer surface and applies the read-only marks. [7]


## Retirements

- Initialization installs the worktree supplier and every ordinary tool family, adding the four explainer tools for a bound launch. list_tools schedules start_after_discovery after its answer exists; call_tool invokes the same latch before applicable explainer-seat checks. The latch starts the sweep even without config and dashboard supervision only with config/settings. [9]

- The dashboard declares its durable-store role on the reload-worker and foreground or daemon entry paths. \[15] [15]
