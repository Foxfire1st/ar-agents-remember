# test_provider_async.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_provider_async.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-10T07:30+02:00                     |
| lastVerifiedCommitHash | `ab7e21b4ab4b8526adcdad8ea2243657b8aea7a0` |
| lastVerifiedCommitDate | 2026-06-10T08:21:41+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

Behavior coverage for the GitHub #53 async worktree provider setup: the
launcher thread, status projections, start ordering, retry path, controller
settings ownership, and the teardown guards.

## Code Commentary

### Logic

`make_contract` builds a disabled-memory `default_contract` under a temp root;
`CapturedThreads` is a `thread_factory` seam that records spawned threads so
tests can join them deterministically. Launcher tests inject a fake `runner`:
success writes the state file, records `providerStateFile` in the finish
summary, and unlinks the temp settings file from the thread; a failed payload
finishes `failed` without a state file; a raising runner finishes `failed`
with the typed error and still unlinks settings. Projection tests cover
None (no progress, no state file), legacy `prepared`, and the failed-state
`retryArgs` (worktree_name from `code_worktree.name`).

`StartOrderingTests` pins the GitHub #53 core: with start internals mocked,
the contract file must exist on disk at the moment `run_or_launch_provider_setup`
is invoked, and the started payload carries providers `starting` plus the
background summary. Dry-run stays synchronous (`planned`, launcher never
called), and the settings path transfers to the launcher only when
`unlink_settings_after_setup` is set. Retry tests: refusal (exit 2, poll hint)
while `provider_setup_running` is True; relaunch returning
`provider-setup-retried` otherwise. `_settings_owned_by_background` is pinned
for starting/planned/non-dict/None results. Guard tests: cleanup blocks (exit
2) while setup runs; abandon blocks without `force` with the force hint.

### Invariants And Boundaries

- No real provider setup runs: the launcher's `runner`/`thread_factory` seams
  and `mock.patch.object` on module attributes keep everything side-effect
  free.
- Thread joins are bounded (10s) and assert completion — no sleeps, no flaky
  timing.

## Docs References

No external documentation is needed for these standard-library unit tests.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Launcher and projections under test. | [provider_async.py](agents-remember/mcp/src/agents_remember/worktrees/modules/provider_async.py) |
| Start ordering and retry path under test. | [start.py](agents-remember/mcp/src/agents_remember/worktrees/modules/start.py) |
| Controller ownership helper under test. | [worktree_tools.py](agents-remember/mcp/src/agents_remember/controllers/worktree_tools.py) |

## Update History

- 2026-06-10T07:30+02:00 — Created with the GitHub #53 async provider setup.
