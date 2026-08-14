# mcp/src/agents_remember/cli/__init__.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/cli/__init__.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[overview.md](../../../overview.md)

## Purpose

Package marker for the `agents-remember` command-line adapter surface; the module docstring names its role as the command-line adapters for the application layer. The real adapters live in the sibling modules under `mcp/src/agents_remember/cli/`.

## Code Commentary

- The module carries only the package docstring `Command-line adapters for the application layer.`; no symbols are defined here.
- Sibling `__main__.py` defines `build_parser()` and `main` as the umbrella `agents-remember` console entrypoint.
- Sibling `dashboard.py` defines `add_arguments`, `run`, and the daemon/settings helpers for the dashboard subcommand.
- Sibling `context_packet.py` defines `main` for the context-packet CLI adapter.

## Repo-Internal References

This package marker is documented by the nearest mcp route overview and the real CLI adapters in sibling modules.

| Finding | Anchor | Source |
| --- | --- | --- |
| The package docstring names the CLI adapter role. | "Command-line adapters for the application layer" | mcp/src/agents_remember/cli/__init__.py:1-1 |
| The nearest route overview documents the umbrella CLI under `cli/`. | — | — |
| The umbrella entrypoint dispatches subcommands for this package. | `main` | mcp/src/agents_remember/cli/__main__.py:31-33 |
| The dashboard subcommand adapter registered by the umbrella parser. | `run` | mcp/src/agents_remember/cli/dashboard.py:161-196 |
| The context-packet CLI adapter peer. | `main` | mcp/src/agents_remember/cli/context_packet.py:17-60 |

## Update History

- 2026-08-05T13:06:07+02:00 — 260731-EFA-L6 residual curator: fixed two Repo-Internal Reference rows: the package-docstring anchor is now the double-quoted literal "Command-line adapters for the application layer" (the backticked span was not anchor-shaped), and the route-overview row was repointed from the vanished mcp/overview.md:803-803 to the memory-tree onboarding/mcp/overview.md:803-803 with the quoted literal "`agents-remember` CLI under `cli/`" as anchor.

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors derived from current worktree source. Verification metadata pinned until closeout stamps the code commit.
