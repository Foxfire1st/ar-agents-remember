# mcp/src/agents_remember/providers/grepai/context/layout.py

## Governing Overview

[overview.md](overview.md)

## Purpose

`grepai/layout.py` owns GrepAI memory-root models, provider-owned runtime layout expansion, requirements pin writing, and per-root `.gitignore` management for grepai's `.grepai/` working dir.

## Code Commentary

### 260731-EFA-L2 Layout Parameter Objects

`grepai_runtime_layout(workspace, *, instance=DEFAULT_GREPAI_INSTANCE,
backend=DEFAULT_GREPAI_BACKEND)` replaces the previous ten keywords, mirroring the CGC layout
builder:

- **`GrepaiWorkspace(coordination_root, name="agents-remember-memory", roots=())`** — the memory
  workspace GrepAI indexes and the root that owns the instance. The only required argument.
- **`GrepaiInstance(runtime_root, logs_root, requirements_file, state_file)`** — where the instance
  lives on disk and what it is pinned to.
- **`GrepaiBackend(root, data_root, state_file)`** — the managed PostgreSQL backend.

**Every field of the last two is an override, so the empty instance IS the convention** — hence the
`DEFAULT_GREPAI_INSTANCE` / `DEFAULT_GREPAI_BACKEND` frozen module singletons used as defaults.
Omitting a bundle means conventional placement under `providers/runners/grepai`.

### Logic

It defines `GrepaiMemoryRoot` and `GrepaiRuntimeLayout`, builds the provider
runtime/data/config/log/home/cache paths from settings, validates configured
memory roots, creates runtime directories, and ensures each indexed root's
`.gitignore` ignores grepai's `.grepai/` working dir (`ensure_grepai_root_gitignore`,
idempotent). When settings omit a watch log directory, the default is the central
coordination log tree at `logs/providers/grepai`.

### Invariants And Boundaries

- Runtime state stays under coordinator provider roots such as `providers/runners/grepai` and `providers/data/grepai/postgres`; operator logs stay under `logs/providers/grepai`.
- Indexed roots are watched live in place (read-write bind-mounted into the watcher); grepai's `.grepai/` working dir is kept out of git via each root's `.gitignore` rather than by mirroring to a throwaway copy.
- Root paths with unresolved placeholders or missing directories raise `ContextProviderError`.

## Evidence

### Repo-Internal References

- Workspace YAML rendering consumes `GrepaiRuntimeLayout` and its normalized roots. [1]
- Lifecycle GrepAI backend and runner code use this layout through the public context facade. [2]
