# mcp/src/agents_remember/mcp/server.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/mcp/server.py`    |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T15:31+02:00                     |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d` |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
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
`maybe_autostart_dashboard(config)` **between** `load_config` and `run_server`. That hook is a no-op
unless the trusted settings set `dashboard.autoStart`; otherwise a daemon thread adopts a healthy
dashboard daemon, spawns an absent one, or restarts one on version mismatch. It is total and
threaded so it can never delay or break the stdio handshake this process exists for, and its only
output goes to stderr — stdout is the MCP protocol.

### Invariants And Boundaries

- **No tool declarations here.** A new tool means editing one family module under `registration/`;
  a new family means a new module plus one entry in `TOOL_REGISTRARS`. `create_server` must not grow
  per-tool special cases.
- Keep `install_compact_content()` and `install_ambient(...)` at the top of `create_server()`,
  before tools can be exercised.
- The dashboard-autostart hook must stay total and threaded; anything that can raise or block here
  breaks the handshake.
- Do not add a raw shell or arbitrary-command tool to this server.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| `TOOL_REGISTRARS` and the twelve family modules that hold every `@server.tool()`. | [registration overview](registration/overview.md) |
| The payload builders the declarations forward to. | [tools overview](tools/overview.md) |
| The config loader, which rejects coordinator `system/settings.json` as MCP authority. | [config.py](agents-remember/mcp/src/agents_remember/mcp/config.py) |
| The shared observer store-root resolver used to install the ambient. | [observer/paths.py](agents-remember/mcp/src/agents_remember/observer/paths.py) |
| The compact-content shim installed at server creation. | [compact_content.py](agents-remember/mcp/src/agents_remember/mcp/compact_content.py) |
| The boot-time dashboard supervision hook `main()` calls. | [serving/daemon.py](agents-remember/mcp/src/agents_remember/serving/daemon.py) |
| Tests build a live server from this module to check the advertised tool list and each declaration's wiring. | [test_tools.py](agents-remember/mcp/tests/test_tools.py) |

## Cross-Repo References

No sibling repository defines this process wiring.

| Finding                                      | Citations | Source Path |
| -------------------------------------------- | --------- | ----------- |
| No meaningful cross-repo references found. | n/a       | n/a         |

## Update History

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
