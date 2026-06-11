# mcp/src/agents_remember/providers/identity.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/providers/identity.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-04T23:15+02:00                     |
| lastVerifiedCommitHash | `83b147e9ccc481749f7a3b40a27acf23cfe4296b`                         |
| lastVerifiedCommitDate | 2026-06-04T23:30:06+02:00|
| governingOverview      | `../../../overview.md`                     |

## Purpose

`identity.py` owns provider instance naming and Docker ownership labels shared by GrepAI and CodeGraphContext.

## Code Commentary

### Logic

The module normalizes arbitrary workspace, worktree, benchmark, provider, and repository names into Docker-safe components. `stable_slug()` lowercases and replaces any character outside `[a-z0-9_-]` with `-`, so dotted release/worktree names such as `release-mcp-2.3.3-ar` become Compose-safe `release-mcp-2-3-3-ar` instead of leaking dots into Docker Compose project names. `stable_provider_id()` is a thin wrapper over it that slugs a provider/repository name with a `"repo"` fallback. `provider_instance_id()` derives readable default instance ids by scope: workspace providers use the workspace folder slug, worktree providers combine workspace and worktree/task names, and benchmark providers combine workspace and `benchmark`. `scoped_name()` then composes those ids into container, network, and Compose project names, and bounds the joined result to `MAX_SCOPED_NAME` (63) with a deterministic `short_hash` suffix so it stays a valid DNS label — per-component `MAX_DOCKER_NAME_COMPONENT` caps alone are insufficient once several components are joined (a long worktree-scoped FalkorDB host otherwise overflowed 63 chars and failed resolution with `label too long`). `provider_ownership_labels()` emits the labels lifecycle code stamps onto provider-owned Docker resources.

### Invariants And Boundaries

- Keep generated identifiers Docker-safe, Compose-project-safe, and bounded by `MAX_DOCKER_NAME_COMPONENT`.
- Keep `scoped_name()` output within `MAX_SCOPED_NAME` (63) — it becomes a container/network hostname and must stay a valid DNS label; bound it deterministically and collision-safely, not by lossy truncation.
- Prefer readable workflow names over opaque hash-first ids; callers can still pass explicit instance ids for duplicate workspace names.
- Do not let provider-specific modules duplicate ownership label keys or Docker name formatting.
- The helper derives names only; lifecycle modules still own Docker inspection and mutation.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| MCP config uses `provider_instance_id()` when provider settings omit an explicit `instanceId`. | [config.py](../../../mcp/config.py.md) |
| Generated lifecycle settings use `scoped_name()` and `provider_ownership_labels()` for GrepAI and CGC runtime names. | [settings.py](settings.py.md) |
| Worktree CGC isolated settings derive workflow-local instance ids through this helper. | [cgc/setup.py](cgc/setup.py.md) |
| Worktree GrepAI isolated settings derive workflow-local instance ids through this helper. | [grepai/isolated.py](grepai/isolated.py.md) |

## Update History

- 2026-06-04T23:15+02:00: `stable_slug()` now normalizes dots to hyphens so dotted worktree names produce Docker Compose-safe provider instance IDs (for example `release-mcp-2.3.3-ar` -> `release-mcp-2-3-3-ar`). Verification metadata pinned until closeout.
- 2026-06-01T13:30+02:00: `scoped_name()` now bounds its joined output to `MAX_SCOPED_NAME` (63) via deterministic truncation + `short_hash`, so container/host/network names stay valid DNS labels (fixes worktree cgc FalkorDB `label too long`; mcp 1.0.1). Verification metadata pinned until closeout.
- 2026-05-31T12:50+02:00 — Source added `stable_provider_id()`, a behaviour-preserving wrapper over `stable_slug()` with fallback `"repo"`; noted it in the Logic section (1.0.0 review remediation).
- 2026-05-27T18:10:12+02:00: Created for the provider workflow compatibility slice.
