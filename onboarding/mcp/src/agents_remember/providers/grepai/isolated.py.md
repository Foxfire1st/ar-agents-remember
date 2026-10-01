# mcp/src/agents_remember/providers/grepai/isolated.py

## Governing Overview

[overview.md](overview.md)

## Purpose

`isolated.py` builds worktree-local GrepAI provider settings that preserve the normal multi-memory provider shape while swapping only the active repository memory root.

## Code Commentary

### Logic

`isolated_grepai_settings()` reads the configured `grepai-memory` provider via the shared `setup_common.provider_settings()` helper (which returns the provider block only when it is a dict), requires an active project id plus target memory root, and deep-copies the source provider settings into a workflow-local target. The generated target settings namespace the GrepAI workspace, runner, Postgres backend, Ollama embedder, network, runtime roots, data roots, logs, and ownership labels by a worktree provider instance id. `_isolated_grepai_roots()` preserves unrelated memory roots and replaces only the active project root with the worktree-local memory path. The isolated log root follows the central workflow-local `logs/providers/grepai/<instance>` layout rather than the provider runtime tree.

This is the worktree-provider reason for keeping GrepAI as an all-memory
provider shape: a worktree instance can leave unrelated repository memory roots
as configured while making the active repo's project target point at the task
memory worktree. Query results for the active repo then resolve against the
worktree memory branch without moving unrelated repo targets.

`_isolated_grepai_base_fields` sets the GrepAI logical `workspace` key to a
scope derived from the **workspace** identity (not the worktree instance id).
The worktree's Postgres is seeded as a clone of the workspace Postgres; the
clone is keyed by the workspace `workspace` value. If the worktree instance id
scoped the `workspace` key instead, the seeded clone would be invisible to the
worktree watcher (different key), forcing a full re-embed. The fix: derive a
`workspace_instance_id` for the `"workspace"` provider scope and use it as the
scoping argument for `scoped_name("agents-remember-memory", ...)`, matching the
workspace's own `workspace` value exactly.

`_isolated_grepai_embedder` sets `seedFromContainer` in the embedder backend to
the workspace Ollama container name (derived by the same `workspace_instance_id`
approach). The worktree Ollama starts empty; this key tells the embedder
lifecycle to copy the model from the workspace Ollama via a local tar pipe
instead of re-pulling it over the network.

### Invariants And Boundaries

- Worktree GrepAI remains an all-memory provider instance; it must not collapse to a single-repo-only provider unless that architecture changes.
- Only the active project memory root is rewritten for worktree mode; unrelated memory roots must remain pointed at their configured roots.
- Per-repo topology dots are allowed to reflect these addressable project targets,
  but this file still creates one aggregate worktree GrepAI provider config.
- Worktree-local GrepAI logs should use `logs/providers/...` so cleanup can
  remove provider logs without confusing them with runtime/data roots.
- Indexed chunk contents are not rewritten here. File-content changes flow through the target memory files and watcher reconciliation.
- This file creates settings only. Database clone/restore behavior lives in `seed.py`; lifecycle start/refresh remains in the GrepAI lifecycle modules.

## Evidence

### Repo-Internal References

- Provider setup combines isolated GrepAI and CGC settings before running workflow-local provider lifecycle operations. [1]
- GrepAI database warm-start is handled by the seed module after isolated target settings exist. [2]
- Provider identity helpers derive the worktree instance id and ownership labels. [3]
