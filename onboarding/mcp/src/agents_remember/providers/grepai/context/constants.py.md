# mcp/src/agents_remember/providers/grepai/context/constants.py

## Governing Overview

[overview.md](overview.md)

## Purpose

`grepai/constants.py` centralizes Docker-owned GrepAI provider identifiers, pins, image/container names, and preferred loopback host ports.

## Code Commentary

### Logic

The module is constant-only: it declares the GrepAI package pin, Docker network, runner/Postgres/Ollama container names, preferred host ports, and image references used by the context and lifecycle GrepAI modules. The managed provider prefers host `61432` for Postgres and host `61434` for Ollama when a host port is configured as `auto`; the Docker container ports remain owned by the lifecycle settings (`5432` and `11434` respectively).

### Invariants And Boundaries

- GrepAI is Docker-owned; these constants do not point to a host `_bin` or `_venv` install path.
- Preferred host ports intentionally avoid common neighboring service ports `5432` and `11434`.
- `.grepai` is grepai's per-root working dir; it lives inside each live indexed root and is kept out of git via the root's `.gitignore` (see `layout.py`).
- This file is imported through `providers.context`; there is no `context_providers.py` compatibility fallback.

## Evidence

### Repo-Internal References

- GrepAI layout consumes these constants for provider-owned runtime paths through `grepai_runtime_layout`. [1]
- GrepAI lifecycle modules consume Docker container/image constants through `grepai_network_name`, `grepai_runner_settings`, and `grepai_backend_settings` in `providers.context`. [2]
