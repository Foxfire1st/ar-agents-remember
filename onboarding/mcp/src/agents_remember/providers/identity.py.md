# mcp/src/agents_remember/providers/identity.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/identity.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-31T12:50+02:00                     |
| lastVerifiedCommitHash | `c20a3292e667d227a3be0c1fb276f8a701df814f`                         |
| lastVerifiedCommitDate | 2026-05-31T14:17:11+02:00|
| governingOverview      | `../../../overview.md`                     |

## Purpose

`identity.py` owns provider instance naming and Docker ownership labels shared by GrepAI and CodeGraphContext.

## Code Commentary

### Logic

The module normalizes arbitrary workspace, worktree, benchmark, provider, and repository names into Docker-safe components. `stable_slug()` does the base normalization, and `stable_provider_id()` is a thin wrapper over it that slugs a provider/repository name with a `"repo"` fallback. `provider_instance_id()` derives readable default instance ids by scope: workspace providers use the workspace folder slug, worktree providers combine workspace and worktree/task names, and benchmark providers combine workspace and `benchmark`. `scoped_name()` then composes those ids into container, network, and Compose project names. `provider_ownership_labels()` emits the labels lifecycle code stamps onto provider-owned Docker resources.

### Invariants And Boundaries

- Keep generated identifiers Docker-safe and bounded by `MAX_DOCKER_NAME_COMPONENT`.
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

- 2026-05-31T12:50+02:00 — Source added `stable_provider_id()`, a behaviour-preserving wrapper over `stable_slug()` with fallback `"repo"`; noted it in the Logic section (1.0.0 review remediation).
- 2026-05-27T18:10:12+02:00: Created for the provider workflow compatibility slice.
