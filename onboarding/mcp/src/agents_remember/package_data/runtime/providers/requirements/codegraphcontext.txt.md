# codegraphcontext.txt

## Governing Overview

[overview.md](../../../../../../overview.md)

## Purpose

This requirements file pins the CodeGraphContext provider dependencies used by Agents Remember's provider lifecycle tooling.

## Code Commentary

### Logic

The file pins `codegraphcontext==0.4.10` plus the Tree-Sitter parser packages
CGC needs for symbol extraction. CGC 0.4.10 declares the parser dependencies
behind a `python_version != "3.13"` marker; without explicit pins, a Python 3.13
environment can install CGC successfully but build only a file-level graph with
zero functions/classes/modules. Runtime installation copies this package
default into `ar-coordination/providers/requirements/codegraphcontext.txt`; the
managed CGC Docker runner build consumes that installed requirements file.

### Conventions

Provider dependency pins live under
`mcp/src/agents_remember/package_data/runtime/providers/requirements/` in the
source checkout and install into `ar-coordination/providers/requirements/`.
Package-owned provider defaults are source-reproducible scaffolding; CGC
execution is Docker-owned in managed mode, while durable database state belongs
under `ar-coordination/providers/data/`.

### Invariants And Boundaries

Provider versions should stay pinned before patching so version-specific patch checks are meaningful. The parser dependencies are part of the CGC provider contract, not optional local setup. Do not point this file at user-global environments or unpinned package ranges.

## Evidence

### Docs References

No external documentation is needed for the pin itself.

No relevant external documentation found.

### Repo-Internal References

- The provider requirements file pins CodeGraphContext to version 0.4.10 plus Tree-Sitter parser dependencies needed for symbol extraction. [1]
- The MCP runtime installer requires and copies `mcp/src/agents_remember/package_data/runtime/providers` into the coordination root. [2]
- The CGC runner build uses the installed requirements pin when building the Docker runner image. [3]

### Cross-Repo References

No sibling repository evidence is needed for this provider pin.

No meaningful cross-repo references found.
