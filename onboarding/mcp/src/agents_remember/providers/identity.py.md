# mcp/src/agents_remember/providers/identity.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/identity.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-27T18:10:12+02:00                  |
| lastVerifiedCommitHash | `f20f75e3e3c6da0c56a6ccfdedfa9d859d7329b7`                         |
| lastVerifiedCommitDate | 2026-05-27T18:11:35+02:00|
| governingOverview      | `../../../overview.md`                     |

## Purpose

`identity.py` owns provider instance naming and Docker ownership labels shared by GrepAI and CodeGraphContext.

## Code Commentary

### Logic

The module normalizes arbitrary workspace, worktree, benchmark, provider, and repository names into Docker-safe components. `provider_instance_id()` derives readable default instance ids by scope: workspace providers use the workspace folder slug, worktree providers combine workspace and worktree/task names, and benchmark providers combine workspace and `benchmark`. `scoped_name()` then composes those ids into container, network, and Compose project names. `provider_ownership_labels()` emits the labels lifecycle code stamps onto provider-owned Docker resources.

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

- 2026-05-27T18:10:12+02:00: Created for the provider workflow compatibility slice.
