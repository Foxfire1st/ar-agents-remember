# test_worktree_abandon.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/tests/test_worktree_abandon.py`       |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-01T00:00+02:00                     |
| lastVerifiedCommitHash | `4117c3d98eadb4265af6e55f3dd8f2552e8589a0`                |
| lastVerifiedCommitDate | 2026-06-01T20:31:44+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[overview.md](../../../../../overview.md)

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

### Conventions

Tests that need Git use the `git`/`init_repo` helpers imported from
`test_worktree_support`. Docker tests are purely structural (no containers
started). Temp dirs are cleaned up in `tearDown`.

### Invariants And Boundaries

The tests protect: template container names are expanded per repo root; settings
absence is non-fatal (graceful empty result); unmerged commits are surfaced to
the caller before any destructive action; the force path actually deletes
(`git branch --list` confirms deletion); blockers are only raised for real
blocking conditions (not already-absent).

## Docs References

No external documentation is needed for these standard-library unit tests.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| `teardown_worktree_providers` and Docker resource derivation helpers. | [provider_teardown.py](agents-remember-md/mcp/src/agents_remember/worktrees/modules/provider_teardown.py) |
| `_abandon_branch` and `_abandon_blockers`. | [abandon.py](agents-remember-md/mcp/src/agents_remember/worktrees/modules/abandon.py) |
| `git`/`init_repo` test utilities from the worktree support test module. | [test_worktree_support.py](agents-remember-md/mcp/tests/test_worktree_support.py) |

## Cross-Repo References

No sibling repository evidence is needed for these tests.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-06-01T00:00+02:00 — Created onboarding for the new worktree abandon + provider teardown tests.
