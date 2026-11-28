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

Starts the configured MCP application with the ordinary registration families, enforces central read-only annotations and per-tool execution wrapping at registration (`AgentsRememberMCP.add_tool`), adds the four explainer tools for a valid explainer launch, enables listing-time `inputSchema` compaction on copied `MCPTool` responses (`_compact_server_tool_schemas`), and narrows the registered tools to the allowlist of a bound role using its own registration ledger (`registered_tool_names`) and public `remove_tool`.

## Code Commentary

A native invocation opens a lazy request memo and clears its shared owner map after all joined work exits. Both registered role-start workers retain that scope through cancellation while their thread drains. The native call then attempts allocator trim in a worker thread. Detached quality has its own computation scope.

### Logic

`create_server(config)` composes the application and server in the following order:

1. Install a supplier through the light kernel service holder; the first dependent worktree operation builds the default services once, including `LeafAgentArchive(config)`. Initialize the boot-time caller-identity tool writer through `server_startup.initialize_mcp_application(config)`. The writer's constructors are light; this is no blanket optional-work deferral claim.
2. Build `extensions = [build_skills_extension()]` and construct `AgentsRememberMCP("Agents Remember", instructions=launched_server_instructions(), version=SERVER_VERSION, extensions=extensions, middleware=[preserve_handshake_extensions(extensions)], subscriptions=False, enforce_read_only_marks=True)`. Passing `version=SERVER_VERSION` advertises the product version from `SERVER_VERSION` (rather than the MCP SDK package version) as `serverInfo.version` on the wire during `initialize`; passing `subscriptions=False` disables MCP resource subscriptions because this server publishes catalog-backed skill resources without a subscribe/unsubscribe notification stream; passing `enforce_read_only_marks=True` enforces central read-only classification inside `add_tool` for every registration (bare unit-test `AgentsRememberMCP` instances default to `False`). A readable launch binding supplies the canonical task-server instruction line; unbound or unreadable binding supplies no instruction line. `create_server` also snapshots `_bound_agent_id` once via `_snapshot_bound_agent_id()` (`read_agent_binding().agent_id`, or `None` when unbound or malformed).
3. Read the required explainer binding. Every launch invokes the ordered `TOOL_REGISTRARS`; a valid explainer launch also registers its four tools and retains its binding for those tools’ per-call validation. An invalid required binding refuses service.
4. During registration, `AgentsRememberMCP.add_tool` merges registration-site `ToolAnnotations` hints through `read_only_annotations(tool_name, annotations)` from `mcp/read_only.py` (central `read_only_hint` always wins; unlisted names raise `UnknownReadOnlyMark` before role narrowing), resolves `effective_structured_output` to `False` when `structured_output is None` and the handler returns a generic `dict[str, Any]` or `dict[str, object]` (via `_returns_generic_dict`, dropping `<name>DictOutput` `outputSchema` and duplicate `structured_content` while keeping `structured_output` for typed `BaseModel` returns), derives `structured_output_spec(fn, structured_output=effective_structured_output)`, wraps the callable with `tool_wrapper.wrap_registered_tool`, delegates to public `MCPServer.add_tool`, and records `tool_name` in `self._registered_tools`.
5. `_compact_server_tool_schemas(server)` enables `_compact_listed_schemas = True` so `AgentsRememberMCP.list_tools()` applies `models.tools.tool_schema_compaction.compact_tool_schema` to copied `MCPTool` instances (`tool.model_copy(...)`) without mutating stored SDK tool definitions, preserving registration order, read-only annotations, and runtime Pydantic argument validation.
6. `_bound_role_tools` reads the agent binding after registration. An unbound process keeps the whole registered roster. A readable role binding keeps that role's `tools_for_role` allowlist, plus the explainer's four tools when an explainer seat is also bound, and `_scope_server_tools` iterates `server.registered_tool_names()` (never calling `list_tools()`, preserving post-discovery start timing) and removes every other registered tool through public `MCPServer.remove_tool`, so the survivors keep their registration order, compacted listed schemas, and read-only annotations. A present but unreadable binding keeps only `server_info`.

`run_server(config)` records this process in the running-server registry as an `"mcp"` server (`register_server`), then writes this server's per-PID binding and process-ancestry record under `<coordination-root>/runtime/server-bindings/<pid>.json` through `_register_process_binding(config)` → `serving/server_bindings.register_server_binding` (distinguishing `bound` with `BoundIdentityPayload`, `unbound`, and `unreadable` with `unreadable_reason`) before calling `create_server(config).run()`. In `finally`, it runs both idempotent cleanups (removing the binding record first, then the server registry record), and both cleanups are also registered with `atexit` for normal process exit.

### Dispatch at the public transport boundary

`AgentsRememberMCP` subclasses `MCPServer` and overrides the public `add_tool`, `remove_tool`, `list_tools()`, and 3-argument `call_tool(name, arguments, context)` methods without provisional call middleware. `AgentsRememberMCP.list_tools` awaits `super().list_tools()`, applies `compact_tool_schema` to copied `MCPTool` instances when `_compact_listed_schemas` is enabled, schedules `start_after_discovery(config)` with the running loop’s `call_soon`, and returns that answer. The shared latch starts outside-scratch reconciliation once, including on a bare no-config server, and dashboard autostart only with config/settings. `call_tool` reaches that same latch as the fallback for a client that never lists, before entering `tool_call_context`. Calls to an explainer tool still present in `self._registered_tools` validate their launched seat before dispatch (returning a compact single-line UTF-8 JSON early refusal with `structured_content=None` via `tool_results.build_early_refusal_result`); a call to an explainer tool that role narrowing removed reaches `super().call_tool` and fails there as an unknown tool. `_dispatch_tool` delegates to `super().call_tool(name, arguments, context)` and maps `UnexpectedToolError` back to `ToolError` carrying the cause message so wire error texts stay intact. Tool argument admission belongs to each retained registered schema; the registration-time wrapper in `mcp/tool_wrapper.py` receives SDK-validated kwargs, checks stale-build refusals, offloads sync handlers under the write lock, and converts normal tool results through `tool_results.build_call_tool_result`.

### Stale installed builds refuse publication writes at dispatch

Inside the tool-call context, a server with config reads its build currentness off the event loop (`build_currentness`) and carries that reading through the call with `tool_build_currentness`, so both the per-tool wrapper and the answer boundary can observe a stale installed build. Immediately before entering `tool_build_currentness`, `_execute_tool_call` awaits `_maybe_suppress_provider_limits(config)`, which offloads `suppress_provider_limits_for_live_tool_call(config, agent_id)` via `asyncio.to_thread` when both `config` and `_bound_agent_id` are present and catches any exception so suppression never breaks or delays an unbound call. A checkout build yields no reading unless inspection is asked for, and a bare no-config server reads nothing. When the reading is an installed build in state `stale`, `MCPServer.call_tool` validates arguments and invokes the registration-time wrapper (`tool_wrapper.wrap_registered_tool`), which normalizes validated `BaseModel` kwargs via `admitted_arguments` and, if `is_stale_build_write` names a publication write, builds `stale_build_refusal` (code `server-build-stale`, naming loaded/installed digests and restart remedy) in a detached worker thread and returns `build_early_refusal_result` without running the handler. Reads, previews, unnamed tools, and current or unknown readings proceed to the wrapped handler.

- `_execute_tool_call` reads `build_currentness`, runs `_maybe_suppress_provider_limits` off-loop inside `suppress(Exception)`, and dispatches under `tool_build_currentness`; `wrap_registered_tool` refuses stale installed publication writes before calling the handler. [13]

- `_maybe_suppress_provider_limits` skips when `config` or `_bound_agent_id` is absent and runs `suppress_provider_limits_for_live_tool_call` via `asyncio.to_thread` inside `suppress(Exception)`. [21]
- `_snapshot_bound_agent_id` reads `read_agent_binding()` once at server creation and returns `None` when unbound or malformed (`ValueError`). [22]

- `run_server` registers both the `"mcp"` running-server record and the per-PID binding/ancestry record (`bound`, `unbound`, or `unreadable`) via `_register_process_binding` before serving and runs both cleanups when serving ends. [14]


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
- Initialize application services and build `SkillsExtension` before constructing `AgentsRememberMCP`; compact JSON `CallToolResult` construction lives directly in `mcp/tool_results.py` with no SDK monkeypatch or ambient lifecycle installer.
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

Readable launch binding supplies one canonical launched-server instruction line. Unbound or unreadable binding supplies no instructions. An unreadable binding narrows the server to `server_info`, whose answer names what is wrong with the binding; every other tool is unknown to that process. create_server retains existing worktree services and application trust composition.

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

After the applicable explainer-tool seat checks, `_dispatch_tool` calls public `super().call_tool(name, arguments, context)` and maps `UnexpectedToolError` to `ToolError` carrying the cause message. Each tool callable was wrapped at registration time in `AgentsRememberMCP.add_tool` via `tool_wrapper.wrap_registered_tool`, so `MCPServer` validates arguments and injects `Context` while the wrapper checks stale-build refusals, offloads synchronous handlers via `thread_workers.run_in_request_thread` (`_run_sync_call`), and converts normal return values into a compact `CallToolResult` via `tool_results.build_call_tool_result`. The worker receives the call's context. Each async handler owns any worker it starts.

Potentially mutating synchronous calls hold one per-server lock (`_write_lock_for_call`) until their worker stops. Cancellation does not release it while the thread is alive, including repeated cancellation. A request cancelled while it still waits for the lock invokes `_log_write_lock_cancellation`, leaving a `cancelled` tool-log row that names the write lock. Centrally declared read-only calls and explicitly nonwriting modes (`tool_wrapper.nonwriting_call`) bypass the lock; the bypass is a dispatch policy, not host-wide purity or permission. A string-coercible false value does not satisfy the strict boolean checks.

- `_dispatch_tool` delegates to public `super().call_tool` and maps `UnexpectedToolError` to `ToolError`, while registration-time `wrap_registered_tool` runs synchronous offload and compact `CallToolResult` conversion. [10]
- Declared reads and explicit nonwriting modes bypass the synchronous write lock. [11]
- Cancellation drains the worker before releasing its caller. [12]

- `launched_server_instructions` returns the launched-server line for a readable binding and none for an absent or unreadable one. [6]

- Current transport wiring retains boot-time caller identity and lazy worktree service construction. It schedules a shared post-discovery sweep/conditional-dashboard latch after producing the list answer, with first-call fallback; application initialization installs no ambient lifecycle.

- `create_server` builds `AgentsRememberMCP` with `version=SERVER_VERSION`, `extensions=[build_skills_extension()]`, `middleware=[preserve_handshake_extensions(extensions)]`, `subscriptions=False`, and `enforce_read_only_marks=True`, snapshots `_bound_agent_id`, invokes the tool registrars, enables listing-time schema compaction (`_compact_server_tool_schemas`), and narrows to a bound role's allowlist. [1]
- `create_server` wires registration-time read-only annotations (`enforce_read_only_marks=True`), listing-time schema compaction (`_compact_server_tool_schemas`), and role narrowing without mutating stored SDK tools. [7]
- `_bound_role_tools` resolves the binding precedence, and `_scope_server_tools` iterates `registered_tool_names()` to remove tools outside the allowlist via public `remove_tool`, keeping survivors' order. [20]

## Retirements

- Initialization installs the worktree supplier and tool registrars, adds explainer tools for a bound launch, and narrows by role binding; `list_tools` schedules `start_after_discovery` after producing its answer, and `call_tool` uses the same latch as fallback. [9]


- The dashboard declares its durable-store role on the reload-worker and foreground or daemon entry paths. [15]
