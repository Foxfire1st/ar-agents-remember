# test_worktree_abandon.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_worktree_abandon.py`       |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-21T04:10+02:00                     |
| lastVerifiedCommitHash | `b252c42cca200933d5c9c36e26de47a526a569ce`                |
| lastVerifiedCommitDate | 2026-08-07T23:58:52+02:00|
| governingOverview      | `../overview.md`                              |

## Governing Overview

[overview.md](../overview.md)

## Purpose

`test_worktree_abandon.py` covers worktree provider teardown and abandon in
isolation: Docker-resource derivation from provider settings, dry-run teardown
behaviour, Docker ownership-reclaim helpers, branch safety (unmerged refusal
without force, force discard), and blocker reporting.

## Code Commentary

### Logic

A `_settings()` helper returns a realistic synthetic provider-settings dict
with CGC (FalkorDB backend, watcher container-name template, network) and
GrepAI (Postgres backend, Ollama embedder backend, watcher runner, network)
providers.

`DockerResourceDerivationTests` calls `_worktree_provider_docker_resources`:

- `test_derives_every_container_and_network`: asserts all five container names
  (including the template expanded per `repoId`) and both network names are present.
- `test_empty_settings_yield_no_resources`: empty settings → empty lists.

`ReclaimImageTests` calls `_reclaim_image`:

- `test_picks_a_backend_image_for_ownership_reclaim`: first backend/embedder image found is returned.
- `test_none_when_no_images`: no images in settings → `None`; `None` settings → `None`.

`ReclaimOwnershipTests` covers the no-image and platform-unavailable paths plus
`_reclaim_result` returncode mapping without calling Docker.

`TeardownDryRunTests` writes real settings files to a temp dir and calls
`teardown_worktree_providers(contract, dry_run=True)`:

- `test_dry_run_lists_resources_without_touching_docker_or_disk`: asserts 5
  containers and 2 networks with `would_remove=True`, `providerRuntime` with
  `would_remove=True`, and that the settings file still exists afterwards.
- `test_missing_settings_reports_not_found`: missing settings → `settingsFound=False`,
  empty `containers` list.

`AbandonBranchSafetyTests` uses real Git repos (via `test_worktree_support`
helpers):

- `test_no_force_refuses_unmerged_and_reports_commits`: `_abandon_branch` without
  force refuses a branch with one unmerged commit and reports it in
  `unmergedCommits`; branch is still present.
- `test_force_discards_unmerged_branch`: `_abandon_branch` with `force=True`
  deletes the branch regardless of unmerged commits.

`AbandonBlockerTests` calls `_abandon_blockers` with synthetic result dicts and
asserts two blockers (dirty worktree + unmerged branch), or zero blockers for a
clean removal.

`AbandonLifecyclePhaseTests` (slice 05l P1, Gap A) covers the abandon-phase
projection in isolation: `test_abandoned_cleanup_projects_abandoned_phase` calls
`lifecycle_guidance(SimpleNamespace(cleanup="abandoned"))` and asserts the result's
`phase` is `"abandoned"` and `nextOperation` is `"done"`. It pins the new
`cleanup == "abandoned"` guidance branch so an abandoned worktree no longer falls
through to the `worktree-started` phantom and the teardown can render (05k). The test
imports `lifecycle_guidance` from `worktrees.modules.guidance`.

### Conventions

Tests that need Git use the `git`/`init_repo` helpers imported from
`test_worktree_support`. Docker tests are purely structural (no containers
started). Temp dirs are cleaned up in `tearDown`. `lifecycle_guidance` (slice 05l)
is exercised against a `SimpleNamespace` contract stub — no real Git or Docker.

### Invariants And Boundaries

The tests protect: template container names are expanded per repo root; settings
absence is non-fatal (graceful empty result); unmerged commits are surfaced to
the caller before any destructive action; the force path actually deletes
(`git branch --list` confirms deletion); blockers are only raised for real
blocking conditions (not already-absent).

## Docs References

No external documentation is needed for these standard-library unit tests.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `teardown_worktree_providers` loads worktree provider settings, removes the derived resources, and reclaims the provider-runtime tree. | `teardown_worktree_providers` | mcp/src/agents_remember/worktrees/modules/provider_teardown.py:27-46 |
| `_worktree_provider_docker_resources` derives the provider container/network resources used by teardown. | `_worktree_provider_docker_resources` | mcp/src/agents_remember/worktrees/modules/provider_teardown.py:60-74 |
| `_abandon_branch` and `_abandon_blockers`. | `_abandon_branch`; `_abandon_blockers` | mcp/src/agents_remember/worktrees/modules/abandon.py:339-372; mcp/src/agents_remember/worktrees/modules/abandon.py:431-445 |
| `lifecycle_guidance` delegates terminal cleanup states to `_reclaimed_phase`, including the `cleanup == "abandoned"` branch pinned by the 05l-P1 phase test. | `lifecycle_guidance`; `_reclaimed_phase` | mcp/src/agents_remember/worktrees/modules/guidance.py:230-240; mcp/src/agents_remember/worktrees/modules/guidance.py:243-257 |
| `git`/`init_repo` test utilities from the worktree support test module. | "def git"; "def init_repo" | mcp/tests/test_worktree_support.py:54-54; mcp/tests/test_worktree_support.py:68-68 |

## Cross-Repo References

No sibling repository evidence is needed for these tests.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-08-04T13:42:02+02:00 — 260731-EFA-L6 S18-B08 curator: regenerated teardown/resource-derivation and reclaimed-phase extents so cleanup predicates retain their operative branches.

- 2026-08-02T21:13:21+02:00 — W2-B07 curator: repaired 2 repository-reference citations after bounded source reads; the scoped citation check is clean.
- 2026-07-31T16:35+02:00 — No content impact: the only change to
  `mcp/tests/test_worktree_abandon.py` since the L2 base commit is the whole-tree `ruff format`
  pass in `00e8379`, which re-wrapped 6 line(s) with no token change whatsoever. Checked by
  parsing both revisions and comparing the abstract syntax trees (identical) and the comment
  tokens (identical), so no symbol, signature, default, decorator, control-flow branch, docstring,
  or assertion this card describes has moved, and every claim this card makes about its own source
  still holds.

- 2026-06-21T04:10+02:00 — slice 05l P1 (backend teardown visibility, Gap A): added `AbandonLifecyclePhaseTests.test_abandoned_cleanup_projects_abandoned_phase` (a unit test that `lifecycle_guidance(SimpleNamespace(cleanup="abandoned"))` returns phase `"abandoned"` / `nextOperation` `"done"`) plus the `lifecycle_guidance` import from `worktrees.modules.guidance`; documented the new suite + reference row. Verification metadata pinned until closeout stamps the 05l-P1 code commit.
- 2026-06-11T14:12+02:00: No content impact: the repository rename sweep replaced `agents-remember-md` with `agents-remember` in the source file; the card already uses the new name and its semantics are unchanged.
- 2026-06-01T00:00+02:00 — Created onboarding for the new worktree abandon + provider teardown tests.
