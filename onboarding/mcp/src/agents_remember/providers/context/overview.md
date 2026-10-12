# mcp/src/agents_remember/providers/context/ - Provider Context Facade Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| sourceRoute            | `mcp/src/agents_remember/providers/context/` |

## Governing Overview

[mcp/overview.md](../../../../overview.md)

## Purpose

`context/` contains the public provider-context facade. It re-exports shared context helpers from `providers/context_common.py` and provider-specific implementations from `providers/cgc/context/` and `providers/grepai/context/`.

## Hot Path Summary

Start with `__init__.py` for the public context facade. Shared error, pin, template, state, hash, removal, and host→container path helpers live in `../context_common.py`, deliberately outside this package to avoid re-entering the facade during provider-package initialization. `to_container_path` normalizes path separators and strips a leading drive letter for container paths; ordinary POSIX paths remain unchanged. CGC behavior lives under `../cgc/context/`; GrepAI behavior lives under `../grepai/context/`.

## How It Is Built

- Shared helper primitives live in `../context_common.py` outside this package.
- `../cgc/context/` owns CodeGraphContext provider context layout, materialization, cleanup, constants, and patch helpers.
- `../grepai/context/` owns Docker-oriented GrepAI provider context constants, layout, and workspace configuration rendering.
- `providers.context` collects these exports through star imports without an explicit `__all__`.

## Invariants And Boundaries

There is no `context_providers.py` compatibility module in the current provider source tree. CGC runtime layout remains CGC-specific and lives under `cgc/`. Shared helpers remain provider-agnostic: `context_common.py` imports only errors and identity from the project, alongside standard-library modules, and low-level provider context modules import those helpers directly.

The shared helpers must remain outside `providers.context`. The facade imports both provider context facades; importing it while one of those packages is initializing can collect an incomplete set of exports. The facade's source documents the import-order failure and the placement that prevents it (GitHub #58).

The retained GrepAI runner implementation builds a Docker watcher image, whose Dockerfile installs the GrepAI binary and selects it as the entrypoint. These source-level construction boundaries do not establish that a provider is installed, running, or publicly provisionable.

## Evidence

- Public context exports are collected by the package facade. [1]

- CGC context behavior is grouped under the CGC provider package. [2]

- GrepAI context behavior is grouped under the GrepAI provider package. [3]
