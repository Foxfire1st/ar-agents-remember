# mcp/src/agents_remember/mcp/server.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/mcp/server.py`    |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-01T13:20+02:00                     |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview      | `../../../overview.md`                     |

## Governing Overview

[MCP package overview](../../../overview.md)

## Purpose

`server.py` is the stdio MCP **process wiring** for Agents Remember, and since 260731-EFA-L2 that is
all it is: about fifty lines holding `create_server`, `run_server` and `main`.

The tool surface it used to carry — every `@server.tool()` declaration and its model-visible
docstring — now lives in `agents_remember.mcp.registration`, one module per family. If you are
looking for what a tool advertises, what it refuses, or which payload builder it forwards to, that
is the [registration route overview](registration/overview.md), not this file.

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
3. `FastMCP("Agents Remember")`.
4. `for register_tools in TOOL_REGISTRARS: register_tools(server, config)` — the loop is the only
   place that decides which families a server advertises.

`run_server(config)` is `create_server(config).run()`.

`main(argv)` parses a required `--config` (an absolute path to trusted MCP settings JSON), loads it
through `load_config` and turns a `ConfigError` into an argparse error, then calls
`prepare_mcp_process(config)` between `load_config` and `run_server`. The application-layer wrapper
declares the MCP durable-store role and then invokes the dashboard-autostart hook. That hook is a no-op
unless the trusted settings set `dashboard.autoStart`; otherwise a daemon thread adopts a healthy
dashboard daemon, spawns an absent one, or restarts one on version mismatch. It is total and
threaded so it can never delay or break the stdio handshake this process exists for, and its only
output goes to stderr — stdout is the MCP protocol.

### Durable-store process-role startup is owned by the application boundary

`main` calls the application-layer `prepare_mcp_process` wrapper, which declares the MCP role before
optional dashboard supervision cit:([`main`], mcp/src/agents_remember/mcp/server.py:35-57) cit:([`prepare_mcp_process`], mcp/src/agents_remember/application/server_startup.py:20-23).
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
worker and `run` for the foreground/daemon command path cit:([`_dev_app`, `run`], mcp/src/agents_remember/cli/dashboard.py:52-81; mcp/src/agents_remember/cli/dashboard.py:161-196).

What the declaration does **not** buy is durability. Every append and every rewrite of all six logs
takes that log's `flock` unconditionally, in every process, declared or not; the role only decides
who runs a reclaim pass and makes an undeclared new writer visible inside the two daemons. A process
that skips this line loses no records — it just stops being distinguishable from the dashboard.

### Invariants And Boundaries

- **No tool declarations here.** A new tool means editing one family module under `registration/`;
  a new family means a new module plus one entry in `TOOL_REGISTRARS`. `create_server` must not grow
  per-tool special cases.
- Keep `install_compact_content()` and `install_ambient(...)` at the top of `create_server()`,
  before tools can be exercised.
- **`prepare_mcp_process(config)` stays in `main` and process-role declaration must never move into `create_server`.**
  `create_server` is called in-process by the test suite and `_declared` has no reset, so declaring
  there marks the whole interpreter `"mcp"` — after which `is_compaction_owner()` answers `True` for
  every MCP-owned log in a test that is exercising the dashboard, and `check_declared_writer()`
  answers for a process that is not the MCP server. The mirrored dashboard obligations are
  `cli/dashboard.py::_dev_app` and `cli/dashboard.py::run`.
- The dashboard-autostart hook must stay total and threaded; anything that can raise or block here
  breaks the handshake.
- Do not add a raw shell or arbitrary-command tool to this server.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `create_server` builds the FastMCP instance and invokes the registered tool families. | `create_server` | mcp/src/agents_remember/mcp/server.py:18-28 |
| The registration package imports each family registrar, collects them in `TOOL_REGISTRARS`, and exports that collection for server wiring. | `register_core_tools`; `TOOL_REGISTRARS`; `__all__` | mcp/src/agents_remember/mcp/registration/__init__.py:20-48; mcp/src/agents_remember/mcp/registration/__init__.py:50-50 |
| The stable `mcp.tools` package imports the payload builders and exports that builder surface for the registered tool families. | "Pure payload builders"; `worktree_sync_payload`; `__all__` | mcp/src/agents_remember/mcp/tools/__init__.py:1-87; mcp/src/agents_remember/mcp/tools/__init__.py:93-159 |

## Cross-Repo References

No sibling repository defines this process wiring.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History
- 2026-08-04T15:29:35+02:00 — 260731-EFA-L6 S18-B11 same-reviewer residual correction: rebound registrar imports/collection and tools builder imports/exports to packet-specified source spans. Verification metadata unchanged.

- 2026-08-03T23:26:43+02:00 — 260731-EFA-L6 S18-T3: moved the live account to the current
  application-layer startup boundary: `main` calls `prepare_mcp_process`, which declares the MCP
  role before optional dashboard supervision; dashboard role declaration is present on both
  `_dev_app` and `run`. New self/cross-file ranges are explicit scoped fixer output.

- 2026-08-03T02:43:00+02:00 — W3-B01 curator: curated 9 Repo-Internal table citations with exact overview headings, current module identifiers, and live test anchor. The earlier call-site commentary was superseded by the current application-layer startup boundary recorded in the S18-T3 entry above. Verification metadata remains unchanged for closeout.
- 2026-08-01T13:20+02:00 — 260731-EFA-L5 curator: recorded the process-entry declaration boundary and why it stays outside the in-process `create_server` factory cit:([`main`, `declare_process_role`], mcp/src/agents_remember/controlplane/durable_store.py:76-84; mcp/src/agents_remember/mcp/server.py:35-57). The dashboard owns its mirrored entry paths cit:([`_dev_app`, `run`], mcp/src/agents_remember/cli/dashboard.py:52-81; mcp/src/agents_remember/cli/dashboard.py:161-196). Verification metadata pinned until closeout stamps the L5 code commit.
- 2026-07-31T15:31+02:00 — 260731-EFA-L2 curator: **rewritten**. The whole tool-registration surface
  left this file for the new `mcp/registration/` package, and `create_server` became wiring plus a
  loop over `TOOL_REGISTRARS`. The previous body — a per-tool catalogue of signatures, refusal
  vocabularies and docstring contracts accumulated over ~30 entries — described functions that are
  no longer in this file at all; that content now belongs to the registration route overview and its
  thirteen file sidecars, which were written from the current source. Verification metadata pinned
  to the pre-change commit until closeout stamps the L2 code commit.
- 2026-07-24T14:31Z — 260718-CHATS-L5I incremental curator: reconciled the public
  `worktree_closeout_preview` / `worktree_closeout_apply` descriptions with approval-before-apply and
  mandatory quality-before-mutation ordering. (Those descriptions now live in
  `registration/closeout.py`.)

> **Earlier history (not a dated entry).** This file's Update History was a long per-tool
> registration log (2026-05-23 through 2026-07-24) recording which tool gained which argument or
> docstring clause. Every one of those entries is about text that moved to `mcp/registration/`; the
> log was not carried forward here because it would document a surface this file no longer has. The
> landed history remains in git and in the registration sidecars' own records.
