# mcp/src/agents_remember/providers/grepai/context/core.py

## Governing Overview

[overview.md](overview.md)

## Purpose

`grepai/core.py` is a compatibility-free package-local facade for the focused Docker-owned GrepAI context modules.

## Code Commentary

### Logic

It imports public names from `constants.py`, `layout.py`, and `workspace.py`. It keeps `grepai.core` as a local organization point inside the new subpackage, while the public API remains `providers.context`.

### Invariants And Boundaries

- This file is part of the direct `providers.context` facade implementation; there is no `context_providers.py` compatibility fallback.
- Provider runtime paths stay under configured provider roots unless a helper explicitly validates another source path.

## Evidence

### Repo-Internal References

- GrepAI lifecycle modules consume these exports through the context package. [1]
