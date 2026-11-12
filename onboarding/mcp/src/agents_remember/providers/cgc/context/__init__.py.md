# mcp/src/agents_remember/providers/cgc/context/__init__.py

## Governing Overview

[overview.md](overview.md)

## Purpose

`cgc/__init__.py` is the CGC context provider subpackage facade.

## Code Commentary

### Logic

It re-exports CGC constants, runtime-layout helpers, cleanup helpers, module discovery helpers, and patch applicators so `providers.context` can keep the old public symbol surface without a monolithic implementation file.

### Invariants And Boundaries

- This file is part of the direct `providers.context` facade implementation; there is no `context_providers.py` compatibility fallback.
- Provider runtime paths stay under configured provider roots unless a helper explicitly validates another source path.

## Evidence

### Repo-Internal References

- The public context facade imports CGC exports through this subpackage facade. [1]
