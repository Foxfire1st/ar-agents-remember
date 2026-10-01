# mcp/src/agents_remember/providers/grepai/ - GrepAI Provider Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| sourceRoute            | `mcp/src/agents_remember/providers/grepai/` |

## Governing Overview

[mcp/overview.md](../../../../overview.md)

## Purpose

`grepai/` is the provider-owned home for Docker-only GrepAI setup, context
layout, workspace generation, and lifecycle operations. It replaces the former
top-level `grepai_setup.py` plus mixed `context_modules/grepai` and
`lifecycle_modules/grepai` routes.

## Hot Path Summary

Use `setup.py` for setup-time refresh/install wiring, `seed.py` for worktree
PostgreSQL database clone/reuse, and `isolated.py` for worktree-scoped provider
settings that keep the multi-root provider shape while swapping only the active
project root to the task memory worktree. Use `context/` for Docker runtime layout, workspace YAML, live memory
roots, and per-root `.gitignore` of grepai's `.grepai/` working dir. Use
`lifecycle/` for Postgres, Ollama, runner image/container, and high-level
GrepAI actions. The lifecycle package owns the current preferred auto host
ports (`61432` for Postgres, `61434` for Ollama); Docker container service
ports stay `5432` and `11434`.

## Route Model

- `setup.py` wires enabled GrepAI setup through lifecycle commands and
  announces its phases (`grepai install`, `grepai clone-db`) through the
  provider setup progress sink so background worktree setup is observable
  (GitHub #53).
- `seed.py` clones the source GrepAI database into an isolated worktree backend
  so embeddings can be reused instead of rebuilt. The clone runs under a stall
  watchdog (killed after `GREPAI_CLONE_STALL_SECONDS` of zero progress in dump
  growth / target database size) and is never capped by total duration — a
  wedge's signature is silence, not size (2.5.1). A benchmark-scoped target is
  refused up front (`_clone_skip`) so a benchmark never clones from another
  stack (hermetic; task 260619).
- `isolated.py` rewrites provider settings for worktree-specific containers,
  roots, logs, and runtime paths while preserving the logical workspace key and
  leaving unrelated repository roots on their configured paths.
- `context/` owns GrepAI runtime layout, workspace config, and live-root indexing.
- `lifecycle/` owns Docker backend, embedder, runner, and top-level actions.

## Invariants And Boundaries

- GrepAI is Docker-or-bust; there is no host binary or host Ollama fallback.
- GrepAI can be one aggregate provider instance with multiple addressable
  project roots; worktree isolation rewrites only the active project root.
- GrepAI-specific behavior belongs under this package, not in CGC modules or
  shared lifecycle helpers.
- Shared helpers must stay provider-agnostic.

## Evidence

### Repo-Internal References

- GrepAI setup delegates to provider lifecycle commands. [1]
- GrepAI context behavior is grouped under the provider-owned context package. [2]
- GrepAI lifecycle behavior is grouped under the provider-owned lifecycle package. [3]

## 260731-EFA-L2 — The Clone Reads As Source → Target

Everything recorded above about the clone still holds: the stall watchdog, the deliberate absence of
a total-duration cap, the up-front benchmark-scoped refusal. What changed is that `seed.py` now
states the *direction*.

**`_GrepaiCloneEnd` (frozen: `coordination_root`, `settings_path`, `provider`) names one end of the
clone.** Source and target are symmetric — each is a coordination root, the settings file that
describes it, and the enabled `grepai-memory` provider entry found there — and they previously
travelled as six interleaved keyword arguments whose pairing was held together by name prefixes
alone. `_clone_context_from_providers(source, target, *, project_id)` now takes the two ends.

`_CloneInputs` (a `NamedTuple` of `source_coordination_root`, `target_settings_path`, `project_id`)
is the caller-supplied coordinate triple **once each is known to be present**; `_clone_inputs`
returns either it or the skip payload naming the *first* missing coordinate. The refusal ordering is
therefore explicit: missing coordinates are reported before any source settings file is read, and
each of the four subsequent provider-presence checks reports its own reason.

`setup.py` dispatches through `LifecycleCommand(provider=, action=, extra_args=, native_args=)`
from `providers/setup_common.py` instead of positional provider/action strings — the type records
that the provider CLI splits its arguments either side of the action. The progress-sink phase
announcements (`grepai install`, `grepai clone-db`) are unchanged.

Layout construction moved to `GrepaiWorkspace` / `GrepaiInstance` / `GrepaiBackend`
(see the [context route](context/overview.md)); the resolved-invocation types the lifecycle package
now uses are listed in the [lifecycle route](lifecycle/overview.md). **The multi-root invariant is
untouched** — `GrepaiWorkspace.roots` is exactly the multi-root shape `isolated.py` rewrites one
entry of.

## 260731-EFA-L9 Route Impact — Caller Re-Points

GrepAI provider modules now import the shared kernel primitives directly (`kernel/primitives/runtime_config.py`, `kernel/primitives/identity.py`, `kernel/primitives/provider_degradation_settings.py`) after the L9 layering cleanup. Seed/setup behavior is unchanged.
