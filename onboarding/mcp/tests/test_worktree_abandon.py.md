# test_worktree_abandon.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_worktree_abandon.py`       |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-21T04:10+02:00                     |
| lastVerifiedCommitHash | `eb7ea60ab9919f009fef58f81afe5861aa1709da`                |
| lastVerifiedCommitDate | 2026-08-22T11:44:33+02:00|
| governingOverview      | `../overview.md`                              |

## Governing Overview

[overview.md](../overview.md)

## Purpose

`test_worktree_abandon.py` covers worktree provider teardown and abandon in
isolation: Docker-resource derivation from provider settings, dry-run teardown
behaviour, Docker ownership-reclaim helpers, branch safety (unmerged refusal
without force, force discard), blocker reporting, and enclosure-report cleanup.

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

- `setUp` creates canonical local default-ref authority and derives a real
  `worktree_abandon` terminal capability from the exact leaf contract.
- `test_no_force_refuses_unmerged_and_reports_commits`: `_abandon_branch` without
  force receives the exact branch target and capability, refuses a branch with one unmerged
  commit, and reports it in
  `unmergedCommits`; branch is still present.
- `test_force_discards_unmerged_branch`: `_abandon_branch` with `force=True`
  uses the same contract-derived capability and deletes the branch regardless of unmerged
  commits.

`AbandonBlockerTests` calls `_abandon_blockers` with synthetic result dicts and
asserts two blockers (dirty worktree + unmerged branch), or zero blockers for a
clean removal.

`AbandonReportCleanupTests` creates an enclosure-local
`reports/curator-memory-quality.md`, calls `_abandon_directories` without force,
and proves both the reports tree and then-empty worktree group are removed.

`AbandonLifecyclePhaseTests` (slice 05l P1, Gap A) covers the abandon-phase
projection in isolation: `test_abandoned_cleanup_projects_abandoned_phase` calls
`lifecycle_guidance(SimpleNamespace(cleanup="abandoned"))` and asserts the result's
`phase` is `"abandoned"` and `nextOperation` is `"done"`. It pins the new
`cleanup == "abandoned"` guidance branch so an abandoned worktree no longer falls
through to the `worktree-started` phantom and the teardown can render (05k). The test
imports `lifecycle_guidance` from `worktrees.modules.guidance`.

### Conventions

Tests that need Git use the `git`/`init_repo` helpers imported from
`test_worktree_support`; destructive branch helpers also receive a real contract-derived
terminal authority. Docker tests are purely structural (no containers
started). Temp dirs are cleaned up in `tearDown` or by their context manager.
The report-cleanup and `lifecycle_guidance` tests use `SimpleNamespace` contract
stubs, so neither needs a real coordinator, Git worktree, or Docker runtime.

### Invariants And Boundaries

The tests protect: template container names are expanded per repo root; settings
absence is non-fatal (graceful empty result); unmerged commits are surfaced to
the caller before any destructive action; direct abandon helpers cannot bypass the
contract-derived terminal capability; the force path actually deletes
(`git branch --list` confirms deletion); blockers are only raised for real
blocking conditions (not already-absent); and non-force abandon removes the
enclosure report before reclaiming the now-empty worktree group.

## Docs References

No external documentation is needed for these standard-library unit tests.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `teardown_worktree_providers` loads worktree provider settings, removes the derived resources, and reclaims the provider-runtime tree. | `teardown_worktree_providers` | mcp/src/agents_remember/application/provider_runtime.py:161-180 |
| `_worktree_provider_docker_resources` derives the provider container/network resources used by teardown. | `_worktree_provider_docker_resources` | mcp/src/agents_remember/application/provider_runtime.py:194-208 |
| `_abandon_branch` and `_abandon_blockers`. | `_abandon_branch`; `_abandon_blockers` | mcp/src/agents_remember/worktrees/modules/abandon.py:429-469; mcp/src/agents_remember/worktrees/modules/abandon.py:558-572 |
| `_abandon_directories` removes the enclosure reports tree before attempting to reclaim the enclosing worktree group. | `_abandon_directories` | mcp/src/agents_remember/worktrees/modules/abandon.py:493-534 |
| `lifecycle_guidance` delegates terminal cleanup states to `_reclaimed_phase`, including the `cleanup == "abandoned"` branch pinned by the 05l-P1 phase test. | `lifecycle_guidance`; `_reclaimed_phase` | mcp/src/agents_remember/worktrees/modules/guidance.py:225-235; mcp/src/agents_remember/worktrees/modules/guidance.py:238-252 |
| `git`/`init_repo` test utilities from the worktree support test module. | "def git"; "def init_repo" | mcp/tests/test_worktree_support.py:71-71; mcp/tests/test_worktree_support.py:85-85 |

## Cross-Repo References

No sibling repository evidence is needed for these tests.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-08-17T12:30+02:00 — No content impact: L5 coverage-pragma alignment only; the documented abandon behavior is unchanged.

- 2026-08-16T00:10+02:00 — 260815-DAG-L4 targeted-gate repair: migrated both real
  `_abandon_branch` paths to exact `_AbandonBranchTarget` inputs and the production
  contract-derived abandon authority. Verification metadata remains closeout-owned.

- 2026-08-11T17:26+02:00 — L19 report-folder delta: added direct non-force abandon proof that the enclosure reports tree is removed before the empty worktree group; verification metadata remains pinned for governed closeout.

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

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
