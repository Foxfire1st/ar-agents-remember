# test_provider_worktree_routing.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_provider_worktree_routing.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-02T01:05+02:00                     |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`                |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `../overview.md`                              |

## Governing Overview

[overview.md](../overview.md)

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

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `_resolve_worktree_target` and `_worktree_provider_targets` live in the provider tools application entry point. | `_resolve_worktree_target`, `_worktree_provider_targets` | mcp/src/agents_remember/application/provider_tools.py:161-192; mcp/src/agents_remember/application/provider_tools.py:195-225 |
| `_isolated_grepai_base_fields` derives the workspace key under test. | `_isolated_grepai_base_fields` | mcp/src/agents_remember/providers/grepai/isolated.py:100-143 |

## Cross-Repo References

No sibling repository evidence is needed for these tests.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-03T03:16:00+02:00 — 260731-EFA-L6-W3-B01 curator: curated 1 Repo-Internal table citation with exact worktree-target resolver anchors. Verification metadata remains unchanged for closeout.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-31T16:35+02:00 — No content impact: the only change to
  `mcp/tests/test_provider_worktree_routing.py` since the L2 base commit is the whole-tree `ruff
  format` pass in `00e8379`, which re-wrapped 18 line(s) with no token change whatsoever. Checked
  by parsing both revisions and comparing the abstract syntax trees (identical) and the comment
  tokens (identical), so no symbol, signature, default, decorator, control-flow branch, docstring,
  or assertion this card describes has moved, and every claim this card makes about its own source
  still holds.

- 2026-06-11T14:12+02:00: No content impact: the repository rename sweep replaced `agents-remember-md` with `agents-remember` in the source file; the card already uses the new name and its semantics are unchanged.
- 2026-06-01T00:00+02:00 — Created onboarding for the new worktree-provider routing and workspace-alignment tests.
