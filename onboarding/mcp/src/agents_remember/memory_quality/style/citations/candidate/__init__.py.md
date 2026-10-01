# mcp/src/agents_remember/memory_quality/style/citations/candidate/__init__.py

## Governing Overview

[overview](../../../overview.md)

## Purpose

Identify the package for exact Git-candidate membership in citation source acquisition.

## Code Commentary

### Logic

The initializer contains only the package docstring. The implementation lives in `git_source.py`; importing this initializer executes no census, hashing, cache acquisition, or publication.

### Conventions

Callers import the implementation from its concrete module. The initializer defines no facade or re-exported API.

### Invariants And Boundaries

- This source is a one-line package declaration with no operational side effects.
- Package navigation uses the existing memory-quality overview; this initializer introduces no additional overview owner.

### Todos

None.

## Evidence

### Repo-Internal References

- The package declaration names its exact Git-candidate acquisition responsibility. [1]
