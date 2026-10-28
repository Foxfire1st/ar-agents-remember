# mcp/src/agents_remember/mcp/server.py

## Governing Overview

[MCP package overview](../../../overview.md)

## Current source contract evidence






## Purpose

`server.py` is the stdio MCP **process and transport-boundary wiring** for Agents Remember. It holds
`AgentsRememberMCP`, `create_server`, `run_server`, and `main`; tool ownership remains in the
registration families.

The tool surface it used to carry — every `@server.tool()` declaration and its model-visible
docstring — now lives in `agents_remember.mcp.registration`, one module per family. If you are
looking for what a tool advertises, what it refuses, or which payload builder it forwards to, that
is the [registration route overview](registration/overview.md), not this file.

Starts the configured MCP application with either the ordinary registration families or the launch-bound explainer surface.

## Code Commentary

### Logic

`create_server(config)` composes the application and server in the following order:

1. `install_compact_content()` — idempotent; makes the JSON text mirror of every tool result emit
   without FastMCP's hardcoded indentation. It affects text-mirror serialization only, never
   `structuredContent` or tool behaviour.
2. Install a supplier through the light kernel service holder; the first dependent worktree operation builds the default services once, including `LeafAgentArchive(config)`. Initialize the boot-time caller-identity tool writer through `server_startup.initialize_mcp_application(config)` and complete FastMCP settings before constructing the server. The writer's constructors are light; this is no blanket optional-work deferral claim.
3. `AgentsRememberMCP("Agents Remember", instructions=launched_server_instructions())`. A readable
   launch binding supplies the canonical task-server instruction line; unbound or unreadable binding
   supplies no instruction line.
4. Read the required explainer binding before choosing the surface. An ordinary launch invokes the ordered `TOOL_REGISTRARS`; a valid bound launch registers only the 22-tool explainer surface and saves its seat binding for per-call validation. An invalid required binding refuses instead of selecting the ordinary roster.
5. `apply_read_only_marks(server)` applies the single `mcp/read_only.py` inventory to every registered
   tool. An unlisted name raises `UnknownReadOnlyMark`; server creation fails rather than advertising
   an unmarked tool. This step changes annotations, not registration order or handler ownership.

`run_server(config)` is `create_server(config).run()`.

### Closed dispatch input at the public transport boundary

AgentsRememberMCP.list_tools first awaits the FastMCP answer, then schedules start_after_discovery(config) with the running loop’s call_soon and returns that already-produced answer. The shared latch starts outside-scratch reconciliation once, including on a bare no-config server, and dashboard autostart only with config/settings. call_tool reaches that same latch as the fallback for a client that never lists, before checking the bound surface and entering tool_call_context. Bound explainer calls also validate their launched seat before the registered handler. The retained delegation and raised-call logging use the shared boundary. Tool argument admission belongs to each retained registered schema. The synchronous dispatch wrapper described below keeps that validation path while moving the handler body off the event loop.

### Tool-call logging at the transport boundary (MIK-R108 rule 3)

`call_tool` brackets every call in `tool_call_context` carrying the exact arguments, start time and
this server's config (`_agents_remember_config`, set once by `create_server`) to the answer boundary,
which logs the completed call; a call that raises is logged here by `_log_raised_tool_call` and
re-raised, with the log write itself never raising. Refusals raised by registered tools happen inside the
context and are logged like other raised calls.

`main(argv)` parses a required `--config` (an absolute path to trusted MCP settings JSON), calls
`declare_mcp_process()` **before** `load_config`, turns a `ConfigError` into an argparse error, then
calls `prepare_mcp_process()` between config loading and `run_server`. The early declaration remains necessary for trusted worktree-hosted MCP authority. Preparation only reasserts the declaration. Process entry and initialization start neither the sweep nor dashboard supervision; list_tools computes its answer before scheduling the shared latch on the next loop callback. The first call_tool on either surface invokes that same latch as the fallback before its surface check and dispatch. The first attempt starts the sweep even without config; with config and trusted `dashboard.autoStart` enabled, the existing total launcher also starts its daemon thread. Later calls start neither again. The sweep thread runs its heavy worktree owner in a one-shot child with stdin=DEVNULL, so it cannot consume the serving process’s MCP stdin. Launcher/sweep failures are contained and stdout remains the MCP protocol.

### Durable-store process-role startup is owned by the application boundary

`main` calls the application-layer `declare_mcp_process` before authority loading, then the
`prepare_mcp_process` wrapper before serving; the joint sweep/conditional-dashboard start is scheduled after the tools/list answer is produced, with first-tool-call fallback through the same latch.
`controlplane/durable_store.py` names two concurrent writers of the six
control-plane JSONL logs, `"mcp"` and `"dashboard"`, and the declaration is what lets shared code
ask which one it is running in. `StoreOwnership.is_compaction_owner()` answers `role is None or
compaction_owner is None or role == compaction_owner`, so a process that declares nothing counts as
the owner of every log.

**The wrapper belongs on the process-entry path, not in `create_server`, and that is a correctness
requirement rather than a style choice.** `create_server` is a *factory* the test suite calls
in-process; `_declared` is a plain module-level dict with no reset, so a declaration made inside the
factory would stamp `"mcp"` onto the interpreter and every later test in it — including tests that
exercise the dashboard's own write paths. `main` runs once, in a process that exists only to be the
MCP server, so the wrapper declares a fact about the process rather than about whoever last built a
server object. The dashboard declares its role on both real entry paths: `_dev_app` for the reload
worker and `run` for the foreground/daemon command path cit:([`_dev_app`, `run`], mcp/src/agents_remember/cli/dashboard.py:133-169; mcp/src/agents_remember/cli/dashboard.py:249-284).
worker and `run` for the foreground/daemon command path cit:([`_dev_app`, `run`], mcp/src/agents_remember/cli/dashboard.py:166-196; mcp/src/agents_remember/cli/dashboard.py:276-311).

What the declaration does **not** buy is durability. Every append and every rewrite of all six logs
takes that log's `flock` unconditionally, in every process, declared or not; the role only decides
who runs a reclaim pass and makes an undeclared new writer visible inside the two daemons. A process
that skips this line loses no records — it just stops being distinguishable from the dashboard.

### Invariants And Boundaries

- **No tool declarations here.** A new tool means editing one family module under `registration/`;
  a new family means a new module plus one entry in `TOOL_REGISTRARS`.
- The transport subclass may enforce a closed public boundary only when the framework-generated
  boundary is demonstrably weaker. It must not duplicate handlers, invent fallbacks, or become a
  second tool registry. The earlier dispatch-only undeclared-input refusal is historical, not a
  current special case.
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






## L23 Runtime Package Review

The transport server now imports its composition boundary as
`application.runtime.startup as server_startup`. Startup trust, configuration, registration, and
durable-store ownership remain application concerns; only their package location changed.




## Synchronous dispatch and write ordering

After the existing launch-surface and seat checks, `_dispatch_tool` runs a synchronous registered function through `asyncio.to_thread` on a per-call Tool copy. FastMCP still validates the original arguments, injects context and converts the result. The worker receives the call's ContextVars; async handlers retain their existing event-loop path.

Potentially mutating synchronous calls hold one per-server lock until their worker stops. Cancellation does not release it while the thread is alive, including repeated cancellation. Centrally declared read-only calls and explicitly nonwriting modes bypass the lock; the bypass is a dispatch policy, not host-wide purity or permission. A string-coercible false value does not satisfy the strict boolean checks.


- Threaded synchronous dispatch retains the registered validation and conversion path. [10]


- Declared reads and explicit nonwriting modes bypass the synchronous write lock. [11]


- Cancellation drains the shielded worker before releasing its caller. [12]



- `create_server` builds the FastMCP instance and invokes the registered tool families.  Anchor: `create_server` 



- Frozen implementation of launched_server_instructions supporting the stated file behavior. [6]



- Frozen implementation of create_server supporting the stated file behavior.  Anchor: `create_server` 



- Current transport wiring retains boot-time caller identity and lazy worktree service construction. It schedules a shared post-discovery sweep/conditional-dashboard latch after producing the list answer, with first-call fallback; application initialization installs no ambient lifecycle.

Retired at the fifth freeze d59c3493: mcp/src/agents_remember/mcp/server.py:281-314 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit d445e83e7d28e3c34b15d8299d279d65ab9183b9; mcp/src/agents_remember/mcp/server.py:93-127 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit dc03c64a91947cee470622c560c516854eec86b5. Retired means the anchor no longer stands, not that the cited subject was deleted [8]



- Initialization names the worktree supplier and selects the ordinary or bound surface. list_tools produces its answer before scheduling start_after_discovery; call_tool invokes the same latch before bound-name/exact-seat checks. The latch starts the sweep even without config and starts dashboard supervision only with config/settings; bound checks and raised-call logging retain their owners. [9]


- `create_server` builds the FastMCP instance and invokes the registered tool families.  Anchor: `create_server` [1]

- Frozen implementation of create_server supporting the stated file behavior.  Anchor: `create_server` [7]

- Retired at the fifth freeze d59c3493: mcp/src/agents_remember/mcp/server.py::create_server - the bytes it recorded now occur 3 times in the file, so no single home can be named and it is not given to the likelier one. Retired means the anchor no longer stands, not that the cited subject was deleted.

## Retirements

- Retired at the fifth freeze d59c3493: mcp/src/agents_remember/mcp/server.py:281-314 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit d445e83e7d28e3c34b15d8299d279d65ab9183b9; mcp/src/agents_remember/mcp/server.py:93-127 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit dc03c64a91947cee470622c560c516854eec86b5. Retired means the anchor no longer stands, not that the cited subject was deleted.
