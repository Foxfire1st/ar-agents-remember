# mcp/src/agents_remember/cli/__init__.py

## Governing Overview

[overview.md](../../../overview.md)

## Purpose

Package marker for the `agents-remember` command-line adapter surface; the module docstring names its role as the command-line adapters for the application layer. The real adapters live in the sibling modules under `mcp/src/agents_remember/cli/`.

## Code Commentary

- The module carries only the package docstring `Command-line adapters for the application layer.`; no symbols are defined here.
- Sibling `__main__.py` defines `build_parser()` and `main` as the umbrella `agents-remember` console entrypoint.
- Sibling `dashboard.py` defines `add_arguments`, `run`, and the daemon/settings helpers for the dashboard subcommand.
- Sibling `context_packet.py` defines `main` for the context-packet CLI adapter.

## Evidence

### Repo-Internal References

This package marker is documented by the nearest mcp route overview and the real CLI adapters in sibling modules.

- The package docstring names the CLI adapter role. [1]
The nearest route overview documents the umbrella CLI under `cli/`.
- The umbrella entrypoint dispatches subcommands for this package. [2]
- The dashboard subcommand adapter registered by the umbrella parser. [3]
- The context-packet CLI adapter peer. [4]
