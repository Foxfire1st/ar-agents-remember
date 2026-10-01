# grepai.txt

## Governing Overview

[overview.md](../../../../../../overview.md)

## Purpose

`grepai.txt` is the package-owned provider requirement pin for the managed
GrepAI Docker runner image.

## Code Commentary

### Logic

The file pins GrepAI to `grepai==0.35.0`. The runtime installer requires this file as part of `mcp/src/agents_remember/package_data/runtime/providers/`, rebuilds `ar-coordination/providers/` from source defaults during reinstall, and copies it to `ar-coordination/providers/requirements/grepai.txt`. Provider lifecycle tooling reads the installed pin and uses it to build the Docker-owned GrepAI runner image; no managed host `_bin/grepai` binary is installed.

### Conventions

- Keep one exact GrepAI requirement line in this file.
- Update Docker runner image release handling when changing the pin format.
- Reinstall may recreate this requirement file and other `providers/` scaffolding, but it must not delete durable provider data such as GrepAI indexes or CGC backend data.

### Invariants And Boundaries

This file is package metadata, not runtime state. It should not contain machine-local paths, generated status, or search indexes.

### Todos

None.

## Evidence

### Docs References

No external documentation is needed for this pin file.

No relevant external documentation found.

### Repo-Internal References

- The requirement file pins GrepAI to `grepai==0.35.0`. [1]
- The MCP runtime installer requires both CGC and GrepAI provider requirement files before copying provider defaults into the coordination root. [2]
- The provider helper exposes the GrepAI pin and writes the managed requirements file through the package provider helper. [3]
- The lifecycle installer reads the GrepAI pin and builds the Docker-owned runner image through the lifecycle facade. [4]

### Cross-Repo References

No sibling repository evidence is needed.

No meaningful cross-repo references found.
