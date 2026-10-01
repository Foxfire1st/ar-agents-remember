# mcp/src/agents_remember/kernel/primitives/identity.py

## Governing Overview

[kernel primitives overview](overview.md)

## Purpose

`kernel/primitives/identity.py` (moved from `providers/identity.py` by 260731-EFA-L9) owns provider instance naming and Docker ownership labels shared by GrepAI and CodeGraphContext.

## Code Commentary

### Logic

The module normalizes arbitrary workspace, worktree, benchmark, provider, and repository names into Docker-safe components. `stable_slug()` lowercases and replaces any character outside `[a-z0-9_-]` with `-`, so dotted release/worktree names such as `release-mcp-2.3.3-ar` become Compose-safe `release-mcp-2-3-3-ar` instead of leaking dots into Docker Compose project names. `stable_provider_id()` is a thin wrapper over it that slugs a provider/repository name with a `"repo"` fallback. `provider_instance_id()` derives readable default instance ids by scope: workspace providers use the workspace folder slug, worktree providers combine workspace and worktree/task names, and benchmark providers combine workspace and `benchmark`. `scoped_name()` then composes those ids into container, network, and Compose project names, and bounds the joined result to `MAX_SCOPED_NAME` (63) with a deterministic `short_hash` suffix so it stays a valid DNS label — per-component `MAX_DOCKER_NAME_COMPONENT` caps alone are insufficient once several components are joined (a long worktree-scoped FalkorDB host otherwise overflowed 63 chars and failed resolution with `label too long`). `provider_ownership_labels()` emits the labels lifecycle code stamps onto provider-owned Docker resources.

### Invariants And Boundaries

- Keep generated identifiers Docker-safe, Compose-project-safe, and bounded by `MAX_DOCKER_NAME_COMPONENT`.
- Keep `scoped_name()` output within `MAX_SCOPED_NAME` (63) — it becomes a container/network hostname and must stay a valid DNS label; bound it deterministically and collision-safely, not by lossy truncation.
- Prefer readable workflow names over opaque hash-first ids; callers can still pass explicit instance ids for duplicate workspace names.
- Do not let provider-specific modules duplicate ownership label keys or Docker name formatting.
- The helper derives names only; lifecycle modules still own Docker inspection and mutation.

## Evidence

### Repo-Internal References

- MCP config uses `provider_instance_id()` when provider settings omit an explicit `instanceId`. [1]
- Generated lifecycle settings derive GrepAI and CGC runtime names and ownership labels through the settings builders. [2]
- Worktree CGC isolated settings derive workflow-local instance ids through this helper. [3]
- Worktree GrepAI isolated settings derive workflow-local instance ids through this helper. [4]
