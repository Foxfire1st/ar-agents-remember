# mcp/src/agents_remember/providers/grepai/isolated.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/providers/grepai/isolated.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-23T22:31+02:00     |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`                         |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `overview.md`                              |

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

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Provider setup combines isolated GrepAI and CGC settings before running workflow-local provider lifecycle operations. | [../provider_setup.py](../provider_setup.py.md) |
| GrepAI database warm-start is handled by the seed module after isolated target settings exist. | [seed.py](seed.py.md) |
| Provider identity helpers derive the worktree instance id and ownership labels. | [../identity.py](../identity.py.md) |
| Unit tests verify active-root swapping and preservation of unrelated memory roots. | [../../../../../tests/test_provider_setup.py](../../../../../tests/test_provider_setup.py.md) |

## Update History

- 2026-06-23T22:31+02:00 — Clarified the topology-relevant isolated-GrepAI invariant: worktree mode
  keeps one all-memory provider config, rewrites only the active project root to the task memory
  worktree, and leaves unrelated roots on their configured paths. Verification metadata will be stamped
  at closeout.
- 2026-06-10T05:30+02:00 — Leaf import replaces the `providers.context` aggregator import (circular-import fix; see grepai/lifecycle/core.py 2026-06-10 entry).
- 2026-06-01T00:00+02:00 — `_isolated_grepai_base_fields` now derives `workspace` from the workspace-scope `provider_instance_id` (not the worktree instance id) so the seeded Postgres clone is reused; `_isolated_grepai_embedder` now sets `seedFromContainer` to the workspace Ollama container name. Updated Code Commentary Logic.
- 2026-05-31T12:50+02:00 — Source dropped the file-local `_grepai_provider()` helper and now resolves the GrepAI block through the shared `setup_common.provider_settings()` (import switched from `context_providers` to `provider_settings`); behaviour-preserving, Logic prose updated to name the shared helper (1.0.0 review remediation).
- 2026-05-28T12:32+02:00: Updated after isolated GrepAI settings moved watch logs under `logs/providers/`.
- 2026-05-27T18:10:12+02:00: Created for the GrepAI worktree warm-start settings slice.
