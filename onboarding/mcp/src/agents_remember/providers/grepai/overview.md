# mcp/src/agents_remember/providers/grepai/ - GrepAI Provider Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| sourceRoute            | `mcp/src/agents_remember/providers/grepai/` |

## Governing Overview

[mcp/overview.md](../../../../overview.md)

## Purpose

`grepai/` contains the retained provider-owned implementation of Docker GrepAI setup, memory-root layout, workspace configuration, database cloning, worktree isolation, and lifecycle actions. These responsibilities live under the provider package rather than the former top-level setup and mixed context/lifecycle routes.

GrepAI is retired from enabled product setup: `provider_enabled` returns false for `grepai-memory` even when retained settings say `enabled: true`. The setup and lifecycle implementations described here remain in source; their presence and settings vocabulary do not establish an available public provisioning command.

## Hot Path Summary

For understanding the retained implementation, start with `setup.py` for setup orchestration, `seed.py` for PostgreSQL clone/reuse, and `isolated.py` for worktree-scoped settings. Follow [context/overview.md](context/overview.md) for runtime layout, workspace YAML, live memory roots, and `.grepai/` exclusions; follow [lifecycle/overview.md](lifecycle/overview.md) for PostgreSQL, embedder, runner, and high-level action implementations.

For current product behavior, read the shared enablement gate before following those implementation routes: setup install/prepare and watcher selection consult it, so retained GrepAI configuration does not enable those operations.

## How It Is Built

`setup.py` retains install, prepare, and refresh entry points, all guarded by `selected_provider_enabled`. Behind that gate, install and refresh construct `LifecycleCommand` values for lifecycle dispatch; prepare invokes the database clone directly. The retained progress announcements identify `grepai install` and `grepai clone-db` phases. `LifecycleCommand` groups provider, action, provider-level arguments preceding the action, and native arguments following it. The product preparation caller invokes install and prepare, rather than the retained refresh entry point.

`seed.py` implements a source-to-target PostgreSQL clone intended to reuse embeddings. Frozen `_GrepaiCloneEnd` values pair each coordination root with its settings path and enabled provider entry. `_clone_context_from_providers(source, target, *, project_id)` resolves their layouts and backend identities. `_CloneInputs` contains the source coordination root, target settings path, and project ID only after validation succeeds.

Clone validation first refuses a benchmark-scoped target, then reports the first missing coordinate before reading source settings. It subsequently distinguishes missing source settings, an absent or disabled source provider, an absent or disabled target provider, and identical source/target backend containers. These intentional skips return successful skip payloads with reasons. Valid inputs lead to source and target backend-start requests followed by dump and restore.

The clone has no total-duration cap. Its stall watchdog samples dump-file size during dump and target-database size during restore, killing a command after the configured interval without a sampled change. The default interval is `GREPAI_CLONE_STALL_SECONDS` (300 seconds), with a caller override retained in the implementation. A stall returns a structured result identifying the phase.

`isolated.py` constructs worktree-scoped container, network, runtime, backend, embedder, and log settings. Its logical workspace key follows workspace identity so cloned data remains addressable; Docker resources and runtime paths follow worktree identity. It rewrites the active project's normalized root to the task memory root, preserves other valid normalized roots, and appends the active project when absent.

`context/` represents layout inputs as `GrepaiWorkspace`, `GrepaiInstance`, and `GrepaiBackend`. `GrepaiWorkspace.roots` supplies the multi-root shape used by layout construction. Workspace rendering writes PostgreSQL store configuration, embedder configuration, and addressable project entries. The retained watcher layout uses live memory roots; the root helper adds `.grepai/` to each existing root's `.gitignore` to exclude its working directory.

`lifecycle/` separates PostgreSQL backend, embedder, runner image/container, compose, settings, and high-level actions. The retained Docker start implementation starts the backend and embedder before the watcher; refresh combines stop and start. Preferred automatic host ports are `61432` for PostgreSQL and `61434` for Ollama, with existing mappings reused and allocation handled by shared helpers. Default container service ports are `5432` and `11434`; settings may override them.

`isolated.py` imports identity primitives directly from `kernel/primitives/identity.py`. Setup and context common helpers also obtain stable provider identity from that kernel module. The lifecycle settings module imports provider context and common leaf helpers directly to avoid the context aggregator's circular import.

## Invariants And Boundaries

- Retained `grepai-memory` settings cannot enable product install, prepare/seed, or watcher selection: the shared enablement gate returns false for this retired provider.
- The retained GrepAI install and ordinary lifecycle-action implementations require Docker settings and reject host GrepAI operation. Their old recovery-message strings are not public provisioning authority.
- One retained workspace can describe multiple addressable project roots. Worktree isolation changes the active project mapping while preserving other valid normalized mappings and the logical workspace identity needed by cloned data.
- Benchmark-scoped clone targets are hermetic: clone validation skips them before source settings or backend startup.
- Database clone duration scales with data size; lack of sampled progress, rather than total elapsed time, triggers its watchdog.
- GrepAI-specific responsibilities belong in this provider package. Shared helpers remain provider-agnostic; CGC behavior belongs in its own provider package.

## Evidence

- GrepAI setup retains lifecycle delegation for install and refresh and direct clone orchestration for prepare, but all three entry points are disabled by the shared retired-provider enablement gate. [1]
- GrepAI context behavior is grouped under the provider-owned context package: typed layout inputs preserve workspace roots, workspace rendering describes projects, and root exclusions keep `.grepai/` artifacts out of Git. Isolation preserves other valid normalized roots while replacing or adding the active project. [2]
- GrepAI lifecycle behavior remains grouped under the provider-owned lifecycle package; retained Docker start/refresh/install implementations do not establish a public provisioning route. Default port vocabulary remains in source. Clone validation explicitly pairs source and target, skips benchmark targets, and applies a no-progress watchdog without a total-duration cap. Identity imports are direct in isolation and shared common helpers, not uniformly direct across GrepAI modules. [3]
