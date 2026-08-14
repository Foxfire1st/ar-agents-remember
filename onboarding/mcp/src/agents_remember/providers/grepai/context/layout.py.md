# mcp/src/agents_remember/providers/grepai/context/layout.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/providers/grepai/context/layout.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T00:00+02:00     |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `overview.md`                              |

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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Workspace YAML rendering consumes `GrepaiRuntimeLayout` and its normalized roots. | `grepai_workspace_config_text`; `write_grepai_workspace_config` | mcp/src/agents_remember/providers/grepai/context/workspace.py:23-42; mcp/src/agents_remember/providers/grepai/context/workspace.py:112-128 |
| Lifecycle GrepAI backend and runner code use this layout through the public context facade. | `grepai_backend_state`; `grepai_watcher_workspace_status` | mcp/src/agents_remember/providers/grepai/lifecycle/backend.py:178-213; mcp/src/agents_remember/providers/grepai/lifecycle/runner.py:155-175 |

## Update History

- 2026-08-04T00:22:04+02:00 — 260731-EFA-L6 S18-B05 curator: repaired and normalised mechanical citation findings with current source anchors and fixer-generated ranges; no semantic claim changes. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-31T00:00+02:00 — 260731-EFA-L2 (gate honesty, `PLR0913` armed with no exemptions):
  `grepai_runtime_layout` was re-signed onto `GrepaiWorkspace` + the optional `GrepaiInstance` /
  `GrepaiBackend` bundles (with `DEFAULT_GREPAI_*` frozen singletons as defaults). The resolved
  `GrepaiRuntimeLayout` is unchanged. Verification metadata pinned until closeout stamps the L2
  commit.
- 2026-06-10T07:30+02:00 — No content impact: import path updated to `providers/context_common.py` (shared helpers moved out of the facade package, GitHub #58); documented behavior unchanged.
- 2026-06-02T01:15+02:00: Dropped the mirror redirect and `sync_grepai_index_roots`/`_sync_grepai_index_root`; roots are now indexed live in place. Added `ensure_grepai_root_gitignore` (called from `prepare_grepai_workspace`) and removed `GrepaiMemoryRoot.source_path`.
- 2026-05-28T12:32+02:00: Updated after GrepAI watch log defaults moved under `logs/providers/grepai`.
- 2026-05-25T19:33+02:00: Created when GrepAI runtime layout and mirror syncing were split out of `grepai/core.py`.
