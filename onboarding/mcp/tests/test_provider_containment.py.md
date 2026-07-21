# test_provider_containment.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_provider_containment.py`   |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-21T11:30+02:00                     |
| lastVerifiedCommitHash | `38c3fd81bdf851dce96e9b2b14e2bff741e7b383` |
| lastVerifiedCommitDate | 2026-07-21T11:31:07+02:00|
| governingOverview      | `../overview.md`                              |

## Governing Overview

[overview.md](../overview.md)

## Purpose

`test_provider_containment.py` pins the provider containment layer of task
260707-HFX-L1: unconfigured on disk means no launch, ever. The 2026-07-07 WSL
OOM proved two bypasses of the settings gate — the boot snapshot (running
servers never re-read the authority file) and benchmark self-arming (the case
manifest synthesized and persisted its own providers map). The suite covers
the authority reload's fail-closed semantics, the worktree-start veto and
armed-path live-map launch, the per-provider query funnel gate, the runtime
rebind derivation, the benchmark manifest filter (including the fail-closed
`None` default, the env escape, and the stale-registration sweep), the
host-scoped fleet setup lock (containment R2), and the metrics feed
(containment R4).

## Code Commentary

### Logic

The `_armed_boot_config(tmp, disk_providers=...)` helper builds a real
`McpRuntimeConfig` whose BOOT SNAPSHOT is armed (a `grepai-memory`
`ProviderScope`) while a real `authority.json` written into the temp root says
`disk_providers` — the snapshot/disk divergence every R1 test exercises.

- `ReloadProviderAuthorityTests` — a disk-disabled file yields an empty map
  WITHOUT an error (a deliberate kill-switch is not a failure); a disk-armed
  file yields the live map; a missing file and invalid JSON both fail closed
  (empty map plus a populated `error`); `require_provider_launch_authority`
  refuses a disk-disabled config with a `ConfigError` naming containment R1
  and the stale boot-snapshot ids, and returns the live-map config when armed.
- `WorktreeStartVetoTests` — with `git_worktree_manager.start_result` mocked
  (the gate under test is the controller's, not the git layer's): a stale
  armed snapshot vetoed by the disk produces NO settings file and no
  `provider_setup_config` (the launch side-channel never materializes) and the
  result's `providersAuthority` block names the `bootSnapshotProviders`; a
  disk-armed run hands the worktree manager a setup config whose written
  settings have `contextProviders.enabled: true` (read inside the mock, while
  the temp file still exists) and carries no `providersAuthority` block.
- `QueryFunnelGateTests` — `_provider_operation_result` with
  `launch_capable_provider="codegraphcontext-code"` refuses under a
  grepai-only-armed authority: `ConfigError` naming the missing provider and
  the runner mock never called — an armed grepai must not authorize a cgc
  one-shot.
- `RuntimeRebindDerivationTests` — the runtime-install rebind derivation
  (`lifecycle_settings_from_config(reload_provider_authority(config).apply(config))`)
  yields `contextProviders.enabled: false` when the disk disables providers.
- `BenchmarkProviderFilterTests` — `filter_benchmark_provider_ids` drops
  manifest ids outside the authority set and an empty authority filters
  everything; `None` (no authority context) is FAIL-CLOSED (review B4) while
  the `AR_BENCHMARK_ALLOW_UNFILTERED_PROVIDERS=1` env escape restores
  unfiltered direct script use; and `disarm_stale_benchmark_registrations`
  narrows a persisted two-provider workspace registration to the authority
  set, reports the rewritten path, is idempotent on a second pass, and leaves
  files untouched under `None` (review B3).
- `FleetSetupLockTests` — a holder thread takes `_fleet_setup_lock` on an
  explicit lock path, a second entry waits and then raises the loud
  `RuntimeError` naming containment R2 after its 1s timeout, the released
  lock is re-acquirable, the uncontended path is a plain no-op, and
  `fleet_setup_lock_path()` is pinned host-scoped — parented at the system
  temp dir with the `agents-remember-provider-setup` name, outside every
  prunable coordination root and per-workspace tree (review B1/B2).
- `MetricsTests` — the byte/mem-usage/percent/label parsers; the sampler's
  `docker ps` failure and dockerless-host (`ContextProviderError`) paths both
  yield error-annotated empty snapshots; a labeled container is collected with
  stats (provider/instance labels, mem/limit bytes, cpu percent, restarts 0,
  and a non-JSON `ps` line skipped); a stats failure is tolerated while a
  `Restarting` status flags `restarts=1` and `running=False`; the store
  round-trips `record`/`read_current` (with `runningCount`) and `read_recent`
  skips a torn append line. 260718-CHATS-L5F (R6) adds
  `test_sampler_bounds_docker_ps_timeout_into_error_sample`: a `docker ps` that
  times out now returns an error-annotated snapshot (via `allow_timeout=True`)
  instead of letting `subprocess.TimeoutExpired` escape and dump a full
  traceback every sampling interval into the daemon log.

### Conventions

Standard suite conventions: `unittest`, tempfile roots per test. Real
authority files (and, for the sweep test, real workspace registration files)
are written because the re-read/rewrite file I/O is the unit under test; the
docker seams (`metrics.docker_command`, `metrics.run_command`),
`git_worktree_manager.start_result`, and the filter's env escape
(`mock.patch.dict` on `os.environ`) are patched. No docker or network access
is required anywhere.

### Invariants And Boundaries

- No test touches the real coordination root or creates a real worktree; the
  worktree tests pin the controller's gate, not the git layer.
- The launch-authority tests assert fail-closed semantics: an unreadable or
  invalid authority file must behave like "no launch authority", never fall
  back to the boot snapshot.
- The lock tests must prove both directions: contention fails loudly at the
  timeout AND an uncontended/released lock never blocks.

## Docs References

No external documentation is needed for these standard-library unit tests.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| `ProviderAuthority` / `reload_provider_authority` / `require_provider_launch_authority` under test. | [config.py](agents-remember/mcp/src/agents_remember/mcp/config.py) |
| The worktree-start authority reload, live-map settings write, and `providersAuthority` veto block. | [worktree_tools.py](agents-remember/mcp/src/agents_remember/controllers/worktree_tools.py) |
| The benchmark manifest filter under test. | [workspace.py](agents-remember/mcp/src/agents_remember/benchmarks/runner_modules/workspace.py) |
| The stale-registration sweep under test (review B3). | [mcp_registration.py](agents-remember/mcp/src/agents_remember/benchmarks/runner_modules/mcp_registration.py) |
| The per-provider query funnel gate under test. | [provider_tools.py](agents-remember/mcp/src/agents_remember/controllers/provider_tools.py) |
| The fleet setup lock under test (containment R2). | [provider_setup.py](agents-remember/mcp/src/agents_remember/providers/provider_setup.py) |
| The metrics sampler, parsers, and store under test (containment R4). | [metrics.py](agents-remember/mcp/src/agents_remember/providers/metrics.py) |
| The rebind derivation these tests replicate lives in the runtime installer. | [install/runtime.py](agents-remember/mcp/src/agents_remember/install/runtime.py) |
| The lifecycle settings generator used by the rebind-derivation test. | [settings.py](agents-remember/mcp/src/agents_remember/providers/settings.py) |

## Cross-Repo References

No sibling repository evidence is needed for these tests.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-07-21T11:30+02:00 — 260718-CHATS-L5F curator: recorded the R6 docker-ps timeout bound in
  `MetricsTests` (`test_sampler_bounds_docker_ps_timeout_into_error_sample`) — a timed-out `docker ps`
  now yields an error-annotated snapshot via `allow_timeout=True` instead of an escaping
  `TimeoutExpired` traceback each sampling interval. Verification metadata stays pinned (uncommitted);
  closeout re-stamps the candidate commit.
- 2026-07-07T17:40+02:00 — 260707-HFX-L1 review fixes: the suite grew `QueryFunnelGateTests`
  (per-provider funnel refusal — armed grepai does not authorize a cgc one-shot), the lock
  host-path pin (`fleet_setup_lock_path()` under the system temp dir) with the explicit
  `lock_path` signature in the lock tests, the benchmark sweep tests
  (narrow/idempotent/None-untouched, review B3), and the fail-closed-`None` + env-escape filter
  tests (review B4). Verification metadata pinned until closeout stamps the HFX-L1 commit.
- 2026-07-07T16:30+02:00 — Created for 260707-HFX-L1 (provider containment): pins the authority
  reload fail-closed semantics, the launch-authority refusal/armed paths, the worktree_start
  veto + armed live-map launch, the runtime rebind derivation, the benchmark manifest filter,
  the fleet setup lock contention/timeout/no-op, and the metrics parsers/sampler/store
  (incl. dockerless and torn-line tolerance). Verification metadata pinned to the branch base
  until closeout stamps the HFX-L1 commit.
