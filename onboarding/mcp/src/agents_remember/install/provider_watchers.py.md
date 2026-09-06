# mcp/src/agents_remember/install/provider_watchers.py

| Field                  | Value                                              |
| ---------------------- | -------------------------------------------------- |
| repository             | agents-remember                                 |
| path                   | `mcp/src/agents_remember/install/provider_watchers.py` |
| doc_type               | `file-level-onboarding`                            |
| lastUpdated            | 2026-07-31T00:00+02:00                             |
| lastVerifiedCommitHash |                                                    `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d`|
| lastVerifiedCommitDate |                                                    2026-07-31T19:28:50+02:00|
| governingOverview      | `../../../overview.md`                             |

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Purpose

`install/provider_watchers.py` owns provider watcher rebind orchestration for
`runtime_install(install_provider_deps=true)`. It keeps watcher stop/start/status
sequencing out of `install/runtime.py` while preserving the runtime install
summary contract and recovery guidance.

## Code Commentary

### 260731-EFA-L2 The Rebind As One Object

**`ProviderWatcherRebind(coordination_root, settings, dry_run, timeout,
report=ProviderWatcherRebindReport())`** is the runtime install's stop → refresh → start cycle
around the provider tree: the coordination root it acts on, the live provider settings its
lifecycle actions are derived from, its execution mode and budget, and the report every phase
accumulates into. **Every phase needs all of it**, so the cycle travels as one object and the
report can no longer be threaded separately from the settings that produced it.

Current signatures: `run_provider_watcher_lifecycle(rebind, action)`,
`stop_provider_watchers_before_refresh(rebind)`, `complete_provider_watcher_rebind(rebind)`.
`provider_watcher_lifecycle_args(coordination_root, settings_path, *, dry_run, timeout)` is
unchanged — it builds the lifecycle argv from the temp settings file, and the temp file is still
written and unlinked per action. Stop/start ordering, the degraded retry, the unrecovered-failure
guidance and everything reported are unchanged.

### Logic

`ProviderWatcherRebindReport` records lifecycle runs, final readiness, recovery
actions, and operator-facing messages. The helper writes temporary lifecycle
settings from the trusted provider settings, calls `lifecycle.watchers_run()` for
`stop`, `start`, and `status`, and records each result with an install phase.

`stop_provider_watchers_before_refresh()` performs the pre-refresh stop and
raises if the stop result is not fully ok, preventing provider runner pruning
while a watcher could still be mounted to the old runtime tree.
`complete_provider_watcher_rebind()` starts watchers, checks status, and if the
status is degraded or partial, performs one additional non-destructive
stop/start/status restart before marking the report ok or adding recovery
actions.

### Conventions

- Use generated lifecycle settings rather than coordinator-local settings files.
- Record dry-run watcher operations the same way as real runs so
  `runtime_install(dry_run=true)` can report the plan.
- Recovery actions use shared provider recovery wording from
  `providers/recovery.py`.

### Invariants And Boundaries

- This helper never invalidates provider indexes and never calls the destructive
  `invalidate-indexes` action.
- Provider data under `providers/data/**` is outside this module's scope; the
  runtime installer owns filesystem preservation while this helper owns watcher
  lifecycle calls.
- A degraded post-install status gets exactly one automatic non-destructive
  restart/rebind attempt before reporting the remaining issue.

### Todos

None.

## Docs References

No external documentation is configured for this repository slice.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant documentation found after checking configured sources. | n/a | n/a |

## Repo-Internal References

The helper is called from runtime installation and is covered by the installer
regression suite.

| Finding | Anchor | Source |
| --- | --- | --- |
| The rebind report stores lifecycle runs, readiness, recovery actions, messages, and the MCP payload shape. | `payload` | mcp/src/agents_remember/install/provider_watchers.py:25-31 |
| Watcher lifecycle calls use temporary provider settings, `lifecycle.watchers_run`, and per-phase result recording. | "watchers_run" | mcp/src/agents_remember/install/provider_watchers.py:83-83 |
| The pre-refresh stop aborts on non-ok/partial watcher stop before runtime provider refresh proceeds. | `stop_provider_watchers_before_refresh` | mcp/src/agents_remember/install/provider_watchers.py:128-141 |
| The post-install path starts watchers, checks status, and attempts one non-destructive restart/rebind before adding recovery guidance. | `complete_provider_watcher_rebind` | mcp/src/agents_remember/install/provider_watchers.py:144-166 |
| Runtime install creates and attaches the report, stops watchers before provider refresh, and completes rebind/recovery before returning. | `install_runtime` | mcp/src/agents_remember/install/runtime.py:462-553 |

## Cross-Repo References

No sibling repository evidence is needed for this helper.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History
- 2026-08-02T21:18:27+02:00 — 260731-EFA-L6 curator W2-B06: repaired 6 citation claims; scoped result 0 findings.

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 3 cross-file line citations that moved when
  the rebind helper was re-signed onto `ProviderWatcherRebind`. `complete_provider_watcher_rebind` is
  now L144-L166 (was L154-L214, past the 166-line file); the `install_runtime` create/attach/stop plus
  complete-rebind-before-return span is now L486-L553 in `runtime.py` (was L437-L527); the five focused
  watcher-rebind tests now span L166-L463 in `test_install_runtime.py` (was L162-L452). All three ranges
  read back against the current files.
- 2026-07-31T00:00+02:00 — 260731-EFA-L2 (gate honesty, `PLR0913` armed with no exemptions):
  added the frozen `ProviderWatcherRebind` and re-signed `run_provider_watcher_lifecycle`,
  `stop_provider_watchers_before_refresh` and `complete_provider_watcher_rebind` onto it; the
  `ProviderWatcherRebindReport` now rides on the rebind rather than being passed alongside it.
  Ordering, retry and reported detail are unchanged. Verification metadata pinned until closeout
  stamps the L2 commit.
- 2026-06-04T22:15+02:00 — Created for the extracted runtime-install provider watcher rebind helper.
