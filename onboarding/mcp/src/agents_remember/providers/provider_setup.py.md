# mcp/src/agents_remember/providers/provider_setup.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/providers/provider_setup.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T00:00+02:00     |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb` |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
| governingOverview      | `../../../overview.md`                     |

## Purpose

`provider_setup.py` is the provider setup facade. It keeps the typed
`ProviderSetupRequest`, CLI parser, action payload assembly, watcher dispatch,
and public compatibility exports while implementation lives in focused setup
modules.

## Code Commentary

### 260731-EFA-L2 Seed-Catchup Split

`_seed_catchup_results` was split into three named steps that make the honesty rule explicit:

- `_seed_touch_plan(entries, root)` → `(touch_paths, residuals)` — splits the diff into paths a
  touch can re-index and **residual staleness it cannot**: deletions, the vanished source half of a
  rename, and paths absent from the checkout have no file left to touch, so they stay in the index
  as phantoms until an explicit refresh.
- `_stale_index_skip(args, settings, payload, stale_index)` — records and reports a delta this run
  did not deliver: the index serves, knowingly stale. Both skip paths (over the delta-file limit,
  and watcher-not-ready) go through it, so they report identically by construction.
- `_deliver_seed_touches(args, settings, payload, touch_paths, residuals)` — touches the
  deliverable files; **`caughtUp` is claimed only with zero residuals**.

`run_lifecycle` calls pass a `LifecycleCommand` (re-exported here as
`provider_setup.LifecycleCommand`).

### Logic

The facade imports shared setup helpers from `setup_common.py`, CGC seed and
bundle helpers from `cgc/seed.py` and `cgc/bundle.py`, CGC provider-level setup
from `cgc/setup.py`, and GrepAI provider-level setup from `grepai/setup.py`.
It re-exports only the narrow set of symbols callers and tests still use,
including `run_provider_setup`, `ProviderSetupRequest`, `rewrite_cgc_bundle_paths`,
`isolated_cgc_settings`, and the `subprocess` handle. Unused compatibility
re-exports (e.g. `command_display`, `expand_template`, `load_json`,
`parse_json_stdout`, `stable_provider_id`, `subprocess_env`,
`cgc_seed_source_extra_args`, `configured_cgc_repo_root`, `git_head`,
`write_isolated_cgc_settings`, `path_replacements`, `rewrite_json_value`,
`rewrite_string`) are no longer aliased here; import them from their owning
module. `load_settings` and `settings_path` are called with only the settings
path argument (`args.from_settings`); the `coordination_root` parameter was
dropped from both helpers.

During `prepare`, the facade runs install steps, GrepAI refresh, CGC seed or
explicit refresh fallback, watcher start/status, and finally the seed
catch-up stage in sequence. `cgc_refresh_fallback` defaults to FALSE
(260707-HFX-L2): a refused seed must never cost a from-zero reindex on its
own — the implicit refresh-all fallback turned every seed refusal into a full
re-index. Opting in is the positive `--cgc-refresh-fallback` flag (the
`--no-cgc-refresh-fallback` negative is kept), and only under that explicit
opt-in does a REFUSED seed (unrelatable heads, carrying
`sourceHead`/`targetHead`) stop failing the prepare.
`result_ok_for_prepare` additionally forgives benign skips regardless of the
flag: a seed that was never intended or possible (hermetic benchmark, no
source configured — `skipped` without a `sourceHead`) never fails a prepare,
because the watcher building the index from scratch is that path's designed
behavior. Setup payload finalization now delegates
to `setup_reporting.py`, which keeps strict phase `ok`, records separate
readiness from final watcher status, stores failed phases and result counts, and
writes compact summaries under `logs/providers/setup/`.
Workflow-local isolated provider settings are reported through the canonical
`isolatedProviderSettings` payload only; the setup payload no longer emits
per-provider duplicate isolated-settings keys.

`run_provider_setup(request, progress=None)` accepts a `SetupProgress` sink
and rides it on the args namespace (the established state-carrier pattern);
`_watcher_results` announces the `watchers start`/`watchers status` phases.
Without a sink every announcement is a no-op, so CLI behavior is unchanged
(GitHub #53).

`_seed_catchup_results(args, settings)` (260707-HFX-L2) runs after
`_watcher_results`: when the cgc seed recorded a relatable HEAD divergence
(`args._cgc_seed_divergence`), it first classifies the delta — touchable
paths (additions/modifications/rename-targets that exist on disk) versus
RESIDUALS a touch cannot deliver (`deleted-phantom`,
`rename-source-phantom`, `missing-on-disk`) — and then WAITS for the cgc
watcher's post-subscribe log marker before touching anything (review L2/B1):
`_wait_for_cgc_watcher_ready` polls `docker logs --since 15m --tail 200` on
the container resolved by `_cgc_watcher_container_name` (the provider's
`runtime.runner.containerNameTemplate` expanded with the stable repo id) for
the SINGLE `_CGC_WATCH_READY_MARKERS` entry — `"monitoring"`, the one
post-subscribe line verified against the pinned codegraphcontext wheel;
speculative extra markers risked a false-positive on some future
pre-subscribe line, silently re-opening the attach race, so the marker is
re-verified on every cgc version bump — on a 2s cadence up to
`CGC_WATCHER_READY_TIMEOUT_SECONDS` (90). `--since` bounds the window to THIS
boot's output, so a marker left by a previous boot cannot satisfy a fresh
one; inotify has no replay and seeded graphs skip the initial scan, so a
touch before subscription is silently lost. No marker within the bound (or an
unresolved container name, or a dockerless host) means NO touch and an honest
`staleIndex` ("watcher not ready before the touch window; delta not
delivered"). With a ready watcher it `os.utime`-touches exactly the touchable
files — the watcher is event-driven, so it re-indexes just the delta; a small
diff becomes an index UPDATE, never a teardown — and claims `caughtUp: true`
ONLY for a clean delta (zero residuals) delivered to a ready watcher;
residuals keep `caughtUp: false` with the `staleIndex.residuals` list. Above
the bound
(`--cgc-seed-delta-max-files`; `0` = `DEFAULT_SEED_DELTA_MAX_FILES`, 200;
threaded through `normalized`/`request_from_args`/`args_from_request` into
`CgcSeedOptions.delta_max_files`) nothing is touched: the clone still serves
and the payload carries a `staleIndex` block (`served: true`, `behindFiles`,
`deltaMaxFiles`, and `reindex: "explicit 'cgc refresh' only"`) so the
staleness is surfaced, never silent — a from-zero rebuild stays an explicit
`cgc refresh`. Dry runs and no-divergence are no-ops. Every outcome is
recorded through `_record_index_state`, a best-effort
(`contextlib.suppress(Exception)`) `ProviderMetricsStore.record_index_state`
row carrying the repoId and provider instance id beside
divergence/touched/caughtUp/watcherReady/staleIndex — observability must
never break a setup.

`_fleet_setup_lock(lock_path, timeout)` (containment R2, 260707-HFX-L1)
serializes provider setup host-wide: `_action_payload_from_args` wraps
`_action_results` in the lock for `action="prepare"` non-dry runs, passing
`fleet_setup_lock_path()` — a HOST-scoped path,
`<tempdir>/agents-remember-provider-setup-<uid>.lock` (`tempfile.gettempdir()`;
uid from `os.getuid()`, `shared` where the platform has none). The lock
deliberately lives outside every coordination root: `runtime_install` prunes
`providers/`, so a coordination-root lock file was deleted mid-hold (review
B1), and benchmark prepares run against workspace-local coordination roots
that must still serialize with fleet setups because the guarded resource is
the HOST's memory/docker daemon, not any one root (review B2). The lock is an
`fcntl` exclusive flock; the holder writes its pid and UTC timestamp into the
file, and a waiter polls non-blocking every 2s up to the setup timeout, then
raises a loud `RuntimeError` naming the lock path instead of piling on. The
2026-07-07 OOM was an aggregate storm — several sessions launched provider
stacks concurrently, each inside its per-container caps (L12) but summing
past the host — so one setup at a time bounds the aggregate. On non-POSIX
hosts (`fcntl` unavailable) the lock is a guarded no-op; the docker-backed
provider stack is POSIX-hosted anyway.

### Invariants And Boundaries

- MCP worktree provider setup must pass `--from-settings`; it must not depend on
  coordinator `system/settings.json`.
- `run_provider_setup(ProviderSetupRequest)` is the package service entry point;
  worktree and benchmark callers should not rebuild provider setup CLI `argv`.
- CGC worktree seed uses the original MCP-derived source settings when the seed
  source and target share a coordination root, and isolated target settings for
  the worktree runtime.
- Child subprocess helpers use `stdin=subprocess.DEVNULL` so provider children
  cannot consume the MCP stdio transport.
- This module is a typed provider setup facade; CGC seed, CGC bundle rewrite,
  GrepAI setup, setup reporting, and shared command helpers belong in their own
  modules.
- The refresh-all fallback is explicit opt-in (`cgc_refresh_fallback=False`
  default, 260707-HFX-L2): a refused seed alone must never trigger a
  from-zero reindex. Benign seed skips (`skipped` without `sourceHead`) never
  fail a prepare; a refused seed is forgiven only under the explicit opt-in.
- The seed catch-up stage touches only diff files at or below the delta
  bound AND only after the watcher's post-subscribe marker (inotify has no
  replay — an early touch is a silent lie); `caughtUp` is claimed only for a
  clean, fully-deliverable delta to a ready watcher. Deletions,
  rename-sources, missing-on-disk paths, a not-ready watcher, and
  above-bound deltas are all surfaced (`staleIndex`), never torn down —
  rebuilds stay explicit.
- Setup summaries record historical setup attempts; current provider truth is
  reported through provider status/current-state files.
- Isolated workflow settings should have one canonical payload shape:
  `isolatedProviderSettings`.
- Non-dry-run `prepare` actions are serialized host-wide through the
  `fleet_setup_lock_path()` flock (containment R2); the lock must never live
  under a coordination root or benchmark workspace — those trees are prunable
  or per-workspace while the guarded resource is the host — and a waiter that
  exhausts the setup timeout must fail loudly, never queue silently past it.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Worktree start calls provider setup with MCP-derived provider settings. | `run_or_launch_provider_setup`, `_provider_setup_request` | mcp/src/agents_remember/worktrees/modules/start.py:628-665; mcp/src/agents_remember/worktrees/modules/start.py:841-873 |
| Benchmark preparation calls package-local provider setup instead of a source script. | `run_provider_setup` | mcp/src/agents_remember/providers/provider_setup.py:547-555 |
| Provider lifecycle calls are captured through package-local command capture. | `run_package_main` | mcp/src/agents_remember/kernel/primitives/command_capture.py:12-39 |
| CGC seed orchestration and bundle rewriting now live outside the facade. | `cgc_seed_bundle`, `rewrite_cgc_bundle_paths` | mcp/src/agents_remember/providers/cgc/seed.py:211-230; mcp/src/agents_remember/providers/cgc/bundle.py:79-99 |
| Shared settings and command helpers live in the setup common module. | `run_command`, `LifecycleCommand`, `run_lifecycle` | mcp/src/agents_remember/providers/setup_common.py:109-146; mcp/src/agents_remember/providers/setup_common.py:159-172; mcp/src/agents_remember/providers/setup_common.py:175-218 |
| Setup payload summaries and failed-phase compaction live in the setup reporting module. | `finalize_setup_payload` | mcp/src/agents_remember/providers/setup_reporting.py:45-66 |
| Containment tests pin the fleet setup lock's contention timeout and uncontended no-op. | `FleetSetupLockTests` | mcp/tests/test_provider_containment.py:276-315 |
| The index-state metrics rows the catch-up stage records best-effort. | `record_index_state` | mcp/src/agents_remember/providers/metrics.py:269-283 |
| Index-lifecycle tests pin the catch-up touch/stale/no-op paths and the metrics row. | `test_clean_delta_to_ready_watcher_is_caught_up`, `test_watcher_not_ready_means_no_touch_and_honest_staleness`, `test_no_divergence_or_dry_run_is_a_noop` | mcp/tests/test_provider_index_lifecycle.py:192-207; mcp/tests/test_provider_index_lifecycle.py:209-233; mcp/tests/test_provider_index_lifecycle.py:277-289 |

## Update History

- 2026-08-03T04:32:19+02:00 — W3-B08 curator: curated 22 citations (citation_anchor_missing=10, citation_prose_not_in_cit_form=0, citation_source_malformed=12); final scoped citation check clean.
- 2026-07-31T00:00+02:00 — 260731-EFA-L2 (gate honesty, `C901`/`PLR0912`/`PLR0915` armed with no
  exemptions): extracted `_seed_touch_plan`, `_stale_index_skip` and `_deliver_seed_touches` from
  `_seed_catchup_results`, and updated the watcher `run_lifecycle` call for the new
  `LifecycleCommand` signature (also re-exported here). Every emitted payload — `skipped`,
  `staleIndex`, `touched`, `residuals`, `caughtUp` — is unchanged. Verification metadata pinned
  until closeout stamps the L2 commit.
- 2026-07-07T20:45+02:00 — 260707-HFX-L2 review fixes (L2/B1+B2 + round-2 verdict): the catch-up
  stage now WAITS for the cgc watcher's post-subscribe log marker before touching
  (`_wait_for_cgc_watcher_ready` + `_cgc_watcher_container_name`,
  `CGC_WATCHER_READY_TIMEOUT_SECONDS` = 90; the marker set was NARROWED to the single
  wheel-verified `"monitoring"` line — speculative markers risked false-positives re-opening the
  race — and the poll is bounded `docker logs --since 15m` so a previous boot's marker cannot
  satisfy a fresh one; no marker ⇒ no touch + an honest "watcher not ready" `staleIndex`),
  classifies touchable vs residual (deleted-phantom / rename-source-phantom / missing-on-disk)
  and claims `caughtUp` only for a clean delta to a ready watcher; the `_record_index_state`
  rows carry repoId + instance identity; `result_ok_for_prepare`'s benign-skip rule is unchanged
  and now test-pinned. Verification metadata pinned until closeout stamps the HFX-L2 commit.
- 2026-07-07T19:30+02:00 — 260707-HFX-L2 (index lifecycle): `cgc_refresh_fallback` default flipped
  FALSE (a refused seed must never cost a from-zero reindex on its own) with the positive
  `--cgc-refresh-fallback` opt-in flag; new `--cgc-seed-delta-max-files` plumbed through
  `normalized`/`request_from_args`/`args_from_request`; new `_seed_catchup_results` stage after
  `_watcher_results` (touch exactly the diff files ≤ bound — watcher-event catch-up; above it
  `staleIndex` served + explicit `cgc refresh` only) with best-effort `_record_index_state`
  metrics rows; `result_ok_for_prepare` forgives benign skips (no `sourceHead`) and forgives
  refusals only under the explicit fallback. Verification metadata pinned until closeout stamps
  the HFX-L2 commit.
- 2026-07-07T17:40+02:00 — 260707-HFX-L1 review fixes B1/B2: the setup lock moved HOST-scoped —
  new `fleet_setup_lock_path()` at `<tempdir>/agents-remember-provider-setup-<uid>.lock` and
  `_fleet_setup_lock` now takes the explicit `lock_path` (B1: `runtime_install` prunes
  `providers/`, so the coordination-root lock died mid-hold; B2: benchmark prepares run against
  workspace-local coordination roots and must serialize on the same host lock — the guarded
  resource is the host). Verification metadata pinned until closeout stamps the HFX-L1 commit.
- 2026-07-07T16:30+02:00 — 260707-HFX-L1 (provider containment R2): added the `_fleet_setup_lock`
  context manager (fcntl flock at `<coordinationRoot>/providers/.setup.lock`, holder pid+timestamp
  written, waiter deadline = the setup timeout then a loud `RuntimeError`, POSIX-guarded no-op
  elsewhere) and wrapped `_action_results` in it for non-dry-run `prepare` actions, so provider
  setup is serialized fleet-wide. Verification metadata pinned until closeout stamps the HFX-L1
  commit.
- 2026-06-10T07:30+02:00 — `run_provider_setup(request, progress=None)` accepts a `SetupProgress` sink and rides it on the args namespace (the established state-carrier pattern); `_watcher_results` announces `watchers start`/`watchers status` phases. With no sink everything is a no-op, so CLI behavior is unchanged (GitHub #53).
- 2026-06-01T20:45+02:00 — Provider setup no longer starts the grepai watcher early; it starts once at `_watcher_results` after the DB clone, cgc seed, and index-root copy, so the watcher never sees files mid-copy (OQ7 copy-first / watch-last ordering).
- 2026-05-31T12:50+02:00 — Pruned unused compatibility re-exports (`command_display`, `expand_template`, `load_json`, `parse_json_stdout`, `stable_provider_id`, `subprocess_env`, `cgc_seed_source_extra_args`, `cgc_seed_source_settings_path`, `configured_cgc_repo_root`, `git_head`, `write_isolated_cgc_settings`, `path_replacements`, `rewrite_json_value`, `rewrite_string`) and dropped the `coordination_root` argument from `load_settings`/`settings_path` calls; corrected the Logic prose's "preserves the public symbols ... subprocess helper exports" claim to the narrowed export set (1.0.0 review remediation).
- 2026-05-28T14:21:08+02:00: Updated after duplicate per-provider isolated
  settings payload keys were removed in favor of canonical
  `isolatedProviderSettings`.
- 2026-05-28T12:32+02:00: Updated after provider setup delegated payload finalization and summary persistence to `setup_reporting.py`.
- 2026-05-25T21:14+02:00: Updated imports after CGC and GrepAI setup modules moved into provider-owned packages.
- 2026-05-25T19:50+02:00: Refactored into a setup facade backed by `setup_common.py`, `cgc_setup.py`, `cgc_seed.py`, `cgc_bundle.py`, and `grepai_setup.py`; targeted Radon CC/MI no longer reports B-or-worse output for the setup slice.
- 2026-05-24T05:48+02:00: Updated after CGC seed failure stopped failing provider prepare payloads when the existing refresh fallback is enabled.
- 2026-05-23T23:46+02:00: Updated after Phase 05 F-05 made provider setup require explicit settings and added the typed `ProviderSetupRequest` service front door.
- 2026-05-23T13:46+02:00: Added when provider setup moved from the deleted source `scripts/` route into the MCP package.
