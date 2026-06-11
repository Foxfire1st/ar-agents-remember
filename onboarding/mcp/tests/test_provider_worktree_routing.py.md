# test_provider_worktree_routing.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_provider_worktree_routing.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-01T00:00+02:00                     |
| lastVerifiedCommitHash | `4117c3d98eadb4265af6e55f3dd8f2552e8589a0`                |
| lastVerifiedCommitDate | 2026-06-01T20:31:44+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[overview.md](../../../../../overview.md)

## Purpose

`test_provider_worktree_routing.py` covers two operational-stability fixes for
worktree-aware provider query routing:

1. CGC/GrepAI tool calls can target a worktree's isolated provider stack via
   hybrid resolution (explicit name wins; single-per-repo is the default;
   multiple/none fall back to workspace scope or raise).
2. A worktree's GrepAI logical `workspace` key must track the workspace
   identity (not the worktree instance id) so the seeded Postgres clone is
   reused instead of re-embedded.

## Code Commentary

### Logic

A `_write_worktree_state` helper writes a synthetic `provider-state.json` and
optionally a `provider-settings.json` under
`coordination_root/worktrees/<repo>/<group>/provider-runtime/`, matching the
layout that `_worktree_provider_targets` scans.

`WorktreeTargetResolutionTests` exercises `_resolve_worktree_target` and
`_worktree_provider_targets`:

- `test_no_worktrees_resolves_to_workspace`: no state files → `None`.
- `test_single_worktree_is_the_default`: one state file for the repo → returned automatically.
- `test_explicit_worktree_matches_by_task_substring`: `worktree="demo"` matches `task="260601_demo"`.
- `test_multiple_worktrees_without_explicit_is_ambiguous`: two stacks for the same repo without an explicit name → `ValueError`.
- `test_explicit_worktree_no_match_raises`: explicit name that matches nothing → `ValueError`.
- `test_other_repo_worktree_does_not_default_for_this_repo`: a worktree for a different repo does not resolve as a default.
- `test_settings_file_missing_is_not_a_candidate`: state without a settings file is filtered out by `_worktree_provider_targets`.

`GrepaiWorkspaceAlignmentTests` calls `_isolated_grepai_base_fields` with a
synthetic `coordination_root` and asserts that the generated `workspace` key
equals the result of scoping `"agents-remember-memory"` by the workspace
instance id (not the worktree instance id), matching `"agents-remember-memory-projects"`.
It also asserts the worktree group name (`"demo-ar"`) does NOT appear in the
workspace key.

### Conventions

Tests use `tempfile.TemporaryDirectory` and write minimal JSON state files; no
provider lifecycle, Docker, or network access required.

### Invariants And Boundaries

The tests protect: the workspace-scoped clone key is reused across worktrees
(fix for the re-embed bug); settings-file absence correctly excludes a stack
from routing candidates; explicit worktree names are matched by substring
against both task name and group name; ambiguous multi-stack scenarios fail
loudly rather than silently picking one.

## Docs References

No external documentation is needed for these standard-library unit tests.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| `_resolve_worktree_target` and `_worktree_provider_targets` live in the provider tools controller. | [provider_tools.py](agents-remember/mcp/src/agents_remember/controllers/provider_tools.py) |
| `_isolated_grepai_base_fields` derives the workspace key under test. | [isolated.py](agents-remember/mcp/src/agents_remember/providers/grepai/isolated.py) |

## Cross-Repo References

No sibling repository evidence is needed for these tests.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-06-01T00:00+02:00 — Created onboarding for the new worktree-provider routing and workspace-alignment tests.
