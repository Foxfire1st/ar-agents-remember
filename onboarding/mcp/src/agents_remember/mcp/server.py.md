# mcp/src/agents_remember/mcp/server.py

## Governing Overview

[MCP package overview](../../../overview.md)

## Purpose

`server.py` is the stdio MCP **process and transport-boundary wiring** for Agents Remember. It holds
`AgentsRememberMCP`, `create_server`, `run_server`, and `main`; tool ownership remains in the
registration families.

The tool surface it used to carry — every `@server.tool()` declaration and its model-visible
docstring — now lives in `agents_remember.mcp.registration`, one module per family. If you are
looking for what a tool advertises, what it refuses, or which payload builder it forwards to, that
is the [registration route overview](registration/overview.md), not this file.

Starts the one configured MCP application and registrar loop.

## Code Commentary

### Logic

`create_server(config) -> FastMCP` does four things in order:

1. `install_compact_content()` — idempotent; makes the JSON text mirror of every tool result emit
   without FastMCP's hardcoded indentation. It affects text-mirror serialization only, never
   `structuredContent` or tool behaviour.
2. `install_ambient(AmbientLifecycle(EventStore(observer_root(config))))` — one ambient lifecycle
   per server process, with the store root resolved through the shared `observer.observer_root`.
   The `lifecycle_*` tools and the `_tool_payload` choke point read that singleton, so it must be
   installed before any tool runs.
3. `AgentsRememberMCP("Agents Remember", instructions=launched_server_instructions())`. A readable
   launch binding supplies the canonical task-server instruction line; unbound or unreadable binding
   supplies no instruction line.
4. `for register_tools in TOOL_REGISTRARS: register_tools(server, config)` — the loop is the only
   place that decides which families a server advertises.

`run_server(config)` is `create_server(config).run()`.

### Closed dispatch input at the public transport boundary

FastMCP 1.x generates argument models that ignore undeclared keys by default. For
`dispatch_agent`, that would silently discard a caller-supplied `model`, `thinking`, or other spend
override even though the public contract says settings own those choices. `AgentsRememberMCP`
therefore uses FastMCP's public `list_tools` and `call_tool` hooks to publish
`additionalProperties: false` and reject undeclared dispatch inputs before the registered handler
runs. This is one closed-schema enforcement seam, not a second registrar or handler. Other tool
registration, descriptions, and argument ownership remain in `mcp/registration/`.

`main(argv)` parses a required `--config` (an absolute path to trusted MCP settings JSON), calls
`declare_mcp_process()` **before** `load_config`, turns a `ConfigError` into an argparse error, then
calls `prepare_mcp_process(config)` between config loading and `run_server`. The early declaration
is load-bearing for worktree-hosted MCP development: without it the checkout policy would classify
the process as an undeclared CLI and ignore the supplied authority in favor of the leaf-local dummy
coordinator. `prepare_mcp_process` idempotently reasserts the same declaration and invokes the
dashboard-autostart hook. That hook is a no-op
unless the trusted settings set `dashboard.autoStart`; otherwise a daemon thread adopts a healthy
dashboard daemon, spawns an absent one, or restarts one on version mismatch. It is total and
threaded so it can never delay or break the stdio handshake this process exists for, and its only
output goes to stderr — stdout is the MCP protocol.

### Durable-store process-role startup is owned by the application boundary

`main` calls the application-layer `declare_mcp_process` before authority loading, then the
`prepare_mcp_process` wrapper before optional dashboard supervision.
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
  second tool registry. ARSPAWN-L4's dispatch-only undeclared-input refusal is the current instance.
- Keep `install_compact_content()` and `install_ambient(...)` at the top of `create_server()`,
  before tools can be exercised.
- **`declare_mcp_process()` stays before `load_config`, `prepare_mcp_process(config)` stays before
  `run_server`, and neither declaration may move into `create_server`.**
  `create_server` is called in-process by the test suite and `_declared` has no reset, so declaring
  there marks the whole interpreter `"mcp"` — after which `is_compaction_owner()` answers `True` for
  every MCP-owned log in a test that is exercising the dashboard, and `check_declared_writer()`
  answers for a process that is not the MCP server. The mirrored dashboard obligations are
  `cli/dashboard.py::_dev_app` and `cli/dashboard.py::run`.
- The dashboard-autostart hook must stay total and threaded; anything that can raise or block here
  breaks the handshake.
- Do not add a raw shell or arbitrary-command tool to this server.

### Role Runtime and Scope

Readable launch binding supplies one canonical launched-server instruction line. Unbound or unreadable binding supplies no instructions; malformed binding still refuses at its actual server_info/bound-tool boundary rather than changing startup authority. create_server retains existing worktree services and application trust composition.

## Leaf agent archive binding (MIK-R76)

`create_server` builds the default worktree services with `leaf_agent_archive=LeafAgentArchive(config)`,
so the MCP process's finalize and abandon transactions reach the archive service. The binding is
composition only; the archive behavior lives in `cli/role_launch_archive.py` and the admitted
terminal transactions.

## Evidence

### Repo-Internal References

- `create_server` builds the FastMCP instance and invokes the registered tool families. [1]
- The registration package imports each family registrar, collects them in `TOOL_REGISTRARS`, and exports that collection for server wiring. [2]
- The stable tools package declares the public import surface for payload builders. [3]
- The package imports worktree payload builders from the owning module. [4]
- The package explicitly exports its builder vocabulary. [5]

### Cross-Repo References

No sibling repository defines this process wiring.

No meaningful cross-repo references found.

### Runtime Source References

- Frozen implementation of launched_server_instructions supporting the stated file behavior. [6]
- Frozen implementation of create_server supporting the stated file behavior. [7]

## L23 Runtime Package Review

The transport server now imports its composition boundary as
`application.runtime.startup as server_startup`. Startup trust, configuration, registration, and
durable-store ownership remain application concerns; only their package location changed.
