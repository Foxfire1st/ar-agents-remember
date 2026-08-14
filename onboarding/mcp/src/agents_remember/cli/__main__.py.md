# mcp/src/agents_remember/cli/__main__.py

| Field                  | Value                                         |
| ---------------------- | --------------------------------------------- |
| repository             | agents-remember                               |
| path                   | `mcp/src/agents_remember/cli/__main__.py`     |
| doc_type               | `file-level-onboarding`                       |
| lastUpdated            | 2026-06-14T11:30+02:00                        |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`    |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `../../../../overview.md`                      |

## Governing Overview

[overview.md](../../../../overview.md)

## Purpose

`cli/__main__.py` is the umbrella `agents-remember` console entrypoint: a single front door
that dispatches subcommands (today `dashboard`; future CLI adapters slot in as subparsers).
Backed by the `agents-remember = agents_remember.cli.__main__:main` console script.

## Code Commentary

`build_parser()` builds an `argparse` parser with a required subcommand group and registers
the `dashboard` subparser via `dashboard.add_arguments`, setting `func=dashboard.run`.
`main(argv=None)` parses and dispatches to `args.func(args)`, returning its int exit code.

The MCP server keeps its own separate `agents-remember-mcp` console script — harness MCP
configs launch the server by that exact name, so it is never folded into this umbrella.

## Invariants And Boundaries

- `agents-remember-mcp` is **not** a subcommand here; renaming or absorbing it would break
  harness MCP registrations.
- Subcommand wiring stays declarative (`add_arguments` + `set_defaults(func=...)`) so each
  adapter owns its own flags.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The `dashboard` subcommand adapter this dispatches to. | `run` | mcp/src/agents_remember/cli/dashboard.py:161-196 |
| The peer CLI adapter pattern. | `main` | mcp/src/agents_remember/cli/context_packet.py:17-60 |
| The separate MCP server console entry that stays standalone. | `main` | mcp/src/agents_remember/mcp/__main__.py:8-8 |

## Update History

- 2026-08-03T04:00:52+02:00 — 260731-EFA-L6 W3-B06 curator: curated 6 citation findings for the dashboard, context-packet, and MCP console entry points.

- 2026-06-14T11:30+02:00 — Created for slice 04 commit 4a: the umbrella `agents-remember`
  dispatcher with the `dashboard` subcommand. Verification metadata pinned until closeout
  stamps the 4a code commit.
