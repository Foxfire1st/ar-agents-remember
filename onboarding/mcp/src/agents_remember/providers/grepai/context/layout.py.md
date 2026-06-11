# mcp/src/agents_remember/providers/grepai/context/layout.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/providers/grepai/context/layout.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-10T07:30+02:00     |
| lastVerifiedCommitHash | `ab7e21b4ab4b8526adcdad8ea2243657b8aea7a0` |
| lastVerifiedCommitDate | 2026-06-10T08:21:41+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[overview.md](overview.md)

## Purpose

`grepai/layout.py` owns GrepAI memory-root models, provider-owned runtime layout expansion, requirements pin writing, and per-root `.gitignore` management for grepai's `.grepai/` working dir.

## Code Commentary

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

| Finding | Source Path |
| --- | --- |
| Workspace YAML rendering consumes `GrepaiRuntimeLayout` and its normalized roots. | [workspace.py](workspace.py.md) |
| Lifecycle GrepAI backend and runner code use this layout through the public context facade. | [backend.py](../lifecycle/backend.py.md); [runner.py](../lifecycle/runner.py.md) |

## Update History

- 2026-06-10T07:30+02:00 — No content impact: import path updated to `providers/context_common.py` (shared helpers moved out of the facade package, GitHub #58); documented behavior unchanged.
- 2026-06-02T01:15+02:00: Dropped the mirror redirect and `sync_grepai_index_roots`/`_sync_grepai_index_root`; roots are now indexed live in place. Added `ensure_grepai_root_gitignore` (called from `prepare_grepai_workspace`) and removed `GrepaiMemoryRoot.source_path`.
- 2026-05-28T12:32+02:00: Updated after GrepAI watch log defaults moved under `logs/providers/grepai`.
- 2026-05-25T19:33+02:00: Created when GrepAI runtime layout and mirror syncing were split out of `grepai/core.py`.
