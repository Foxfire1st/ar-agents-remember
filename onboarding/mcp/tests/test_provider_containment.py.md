# test_provider_containment.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_provider_containment.py`   |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-02T01:05+02:00                     |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb` |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
| governingOverview      | `../overview.md`                              |

## Governing Overview

[overview.md](../overview.md)

## Purpose

`test_provider_containment.py` exercises provider-authority reload and
fail-closed launch checks, the worktree-start veto and armed path, the
provider-specific query gate, runtime rebind derivation, benchmark filtering
and stale-registration narrowing, the host-scoped setup lock, and the metrics
parser/sampler/store behavior.

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
  (the gate under test is the application entry point's, not the git layer's): a stale
  armed snapshot vetoed by the disk produces no `provider_setup_config` and the
  result's `providersAuthority` block names `bootSnapshotProviders`; a
  disk-armed run hands the worktree manager a setup config whose written
  settings have `contextProviders.enabled: true` (read inside the mock, while
  the temp file still exists) and carries no `providersAuthority` block.
  (Since 260731-EFA-L2 both calls read
  `worktree_start_tool(config, TaskIdentity(repo_id="repo", task_name="t", worktree_name="w"))`:
  the task's identity travels as one `TaskIdentity` parameter object in the second positional
  slot, in place of the three loose keywords. The bases and execution knobs stay keyword-only
  at their defaults, so what these two tests drive is unchanged.)
- `QueryFunnelGateTests` — `_provider_operation_result` with
  `ProviderOperation(operation="cgc_symbol_search", required_provider="codegraphcontext-code",
  run=run)` refuses under a grepai-only-armed authority: `ConfigError` naming the missing
  provider and the runner mock never called — an armed grepai must not authorize a cgc
  one-shot. (Since 260731-EFA-L2 the operation, its required provider and its runner travel
  as one `ProviderOperation` parameter object; the former `launch_capable_provider=` keyword
  is now `ProviderOperation.required_provider`.)
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
  worktree tests pin the application entry point's gate, not the git layer.
- The launch-authority tests assert fail-closed semantics: an unreadable or
  invalid authority file must behave like "no launch authority", never fall
  back to the boot snapshot.
- The lock tests must prove both directions: contention fails loudly at the
  timeout AND an uncontended/released lock never blocks.

## Docs References

No external documentation is needed for these standard-library unit tests.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Authority reload and launch-authority refusal/acceptance. | `test_disk_disabled_yields_empty_map_without_error`; `test_disk_armed_yields_live_map`; `test_missing_file_fails_closed`; `test_invalid_json_fails_closed`; `test_require_launch_authority_refuses_disk_disabled`; `test_require_launch_authority_returns_live_config_when_armed` | mcp/tests/test_provider_containment.py:79-84; mcp/tests/test_provider_containment.py:86-91; mcp/tests/test_provider_containment.py:93-99; mcp/tests/test_provider_containment.py:101-107; mcp/tests/test_provider_containment.py:109-115; mcp/tests/test_provider_containment.py:117-121 |
| Worktree-start veto and live-map launch. | `test_stale_armed_snapshot_is_vetoed_by_disk`; `test_disk_armed_snapshot_launches_with_live_map` | mcp/tests/test_provider_containment.py:125-146; mcp/tests/test_provider_containment.py:148-177 |
| Provider-specific query gate and runtime rebind. | `test_query_funnel_requires_its_specific_provider`; `test_live_disabled_disables_rebind_settings` | mcp/tests/test_provider_containment.py:181-196; mcp/tests/test_provider_containment.py:200-206 |
| Benchmark filtering and stale-registration narrowing. | `test_manifest_cannot_arm_outside_authority`; `test_empty_authority_filters_everything`; `test_none_authority_context_is_fail_closed`; `test_env_escape_allows_unfiltered_direct_script_use`; `test_stale_registration_sweep_narrows_to_authority` | mcp/tests/test_provider_containment.py:210-216; mcp/tests/test_provider_containment.py:218-222; mcp/tests/test_provider_containment.py:224-228; mcp/tests/test_provider_containment.py:230-233; mcp/tests/test_provider_containment.py:235-273 |
| Host-scoped setup-lock contention and no-op paths. | `test_second_setup_waits_and_times_out_loudly`; `test_lock_is_noop_when_uncontended`; `test_lock_path_is_host_scoped_outside_prunable_roots` | mcp/tests/test_provider_containment.py:277-300; mcp/tests/test_provider_containment.py:302-307; mcp/tests/test_provider_containment.py:309-315 |
| Metrics parsers, sampler errors, collection, and store tolerance. | `test_parsers`; `test_sampler_reports_docker_ps_failure`; `test_sampler_bounds_docker_ps_timeout_into_error_sample`; `test_sampler_dockerless_host_yields_error_sample`; `test_sampler_collects_labeled_containers_with_stats`; `test_sampler_tolerates_stats_failure_and_flags_restarting`; `test_store_roundtrip_and_torn_line_tolerance` | mcp/tests/test_provider_containment.py:319-327; mcp/tests/test_provider_containment.py:329-340; mcp/tests/test_provider_containment.py:342-357; mcp/tests/test_provider_containment.py:359-367; mcp/tests/test_provider_containment.py:369-405; mcp/tests/test_provider_containment.py:407-433; mcp/tests/test_provider_containment.py:435-450 |

## Cross-Repo References

No sibling repository evidence is needed for these tests.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History
- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-04T08:03:35+02:00 — 260731-EFA-L6 S18-B07 curator: repaired the bounded citation findings from the recovered Avicenna and Kuhn ledgers, splitting or narrowing claims to the frozen source and normalizing scoped citation ranges.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-31T16:50+02:00 — 260731-EFA-L2 curator: the `PLR0913` pass rewrote two call shapes this
  card describes, and this entry records both. `QueryFunnelGateTests` now drives
  `_provider_operation_result(config, ProviderOperation(operation=…, required_provider=…, run=…))`
  — that half of the body was already corrected; completing it here, note the old `launch_capable=`
  boolean has no successor keyword at all, because a `None` `required_provider` is now what marks
  an operation needing no launch authority. The second change had not been recorded: both
  `WorktreeStartVetoTests` cases call
  `worktree_start_tool(config, TaskIdentity(repo_id=…, task_name=…, worktree_name=…))` instead of
  passing those three as keywords, so the card now names `TaskIdentity` where it describes the veto
  and armed-launch paths. Everything else in the diff is `ruff format` reflow — rejoined call
  arguments, the redundant parentheses on the docker `Labels` literal, and the uncontended-lock test
  moving to a parenthesized `with (...)` block, which is the same two context managers in the same
  order. Re-read every remaining claim against the current file: the refusal still raises
  `ConfigError` naming `codegraphcontext-code` with the runner never called, the vetoed run still
  produces no settings file and no `provider_setup_config`, and the fail-closed, lock and metrics
  invariants are untouched. This card's references table carries no line citations, so nothing
  needed re-anchoring. Verification metadata stays pinned until closeout stamps the code commit.

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
