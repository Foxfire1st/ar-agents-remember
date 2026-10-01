# mcp/src/agents_remember/providers/grepai/context/__init__.py

## Governing Overview

[overview.md](overview.md)

## Purpose

`grepai/__init__.py` is the Docker-owned GrepAI context provider subpackage facade.

## Code Commentary

### Logic

It re-exports GrepAI constants, layout, and workspace-config helpers from the focused GrepAI context modules for the public `providers.context` facade.

### Invariants And Boundaries

- This file is part of the direct `providers.context` facade implementation; there is no `context_providers.py` compatibility fallback.
- Provider runtime paths stay under configured provider roots unless a helper explicitly validates another source path.

## Evidence

### Repo-Internal References
