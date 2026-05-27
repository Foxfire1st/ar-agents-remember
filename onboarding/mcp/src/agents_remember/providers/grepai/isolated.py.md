# mcp/src/agents_remember/providers/grepai/isolated.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/grepai/isolated.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-27T18:10:12+02:00                  |
| lastVerifiedCommitHash | `f20f75e3e3c6da0c56a6ccfdedfa9d859d7329b7`                         |
| lastVerifiedCommitDate | 2026-05-27T18:11:35+02:00|
| governingOverview      | `../../../overview.md`                     |

## Purpose

`isolated.py` builds worktree-local GrepAI provider settings that preserve the normal multi-memory provider shape while swapping only the active repository memory root.

## Code Commentary

### Logic

`isolated_grepai_settings()` reads the configured `grepai-memory` provider, requires an active project id plus target memory root, and deep-copies the source provider settings into a workflow-local target. The generated target settings namespace the GrepAI workspace, runner, Postgres backend, Ollama embedder, network, runtime roots, data roots, logs, and ownership labels by a worktree provider instance id. `_isolated_grepai_roots()` preserves unrelated memory roots and replaces only the active project root with the worktree-local memory path.

### Invariants And Boundaries

- Worktree GrepAI remains an all-memory provider instance; it must not collapse to a single-repo-only provider unless that architecture changes.
- Only the active project memory root is rewritten for worktree mode; unrelated memory roots must remain pointed at their configured roots.
- Indexed chunk contents are not rewritten here. File-content changes flow through the target memory files and watcher reconciliation.
- This file creates settings only. Database clone/restore behavior lives in `seed.py`; lifecycle start/refresh remains in the GrepAI lifecycle modules.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Provider setup combines isolated GrepAI and CGC settings before running workflow-local provider lifecycle operations. | [../provider_setup.py](../provider_setup.py.md) |
| GrepAI database warm-start is handled by the seed module after isolated target settings exist. | [seed.py](seed.py.md) |
| Provider identity helpers derive the worktree instance id and ownership labels. | [../identity.py](../identity.py.md) |
| Unit tests verify active-root swapping and preservation of unrelated memory roots. | [../../../../../tests/test_provider_setup.py](../../../../../tests/test_provider_setup.py.md) |

## Update History

- 2026-05-27T18:10:12+02:00: Created for the GrepAI worktree warm-start settings slice.
