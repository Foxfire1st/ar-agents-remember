# mcp/src/agents_remember/install/__init__.py

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Purpose

This package initializer marks `agents_remember.install` as the runtime and
skill installation service package.

## Code Commentary

### Logic

The file intentionally carries only the package docstring. Concrete install
behavior lives in sibling modules such as `runtime.py` and `skills.py`.

### Conventions

Keep initializer files lightweight. Do not hide service exports or compatibility
aliases here without a specific approved reason.

### Invariants And Boundaries

- Package initialization should not perform filesystem work.
- Runtime and skill installation behavior belongs in dedicated modules.

### Todos

None.

## Evidence

### Docs References

No external documentation is needed for this local package marker.

No relevant external documentation is needed for the package marker.

### Repo-Internal References

The source file itself is the direct evidence.

- The initializer identifies the package as runtime installation services and contains no executable behavior. [1]

### Cross-Repo References

No meaningful cross-repo boundary is documented here.

No sibling repository boundary is needed to explain this file.
