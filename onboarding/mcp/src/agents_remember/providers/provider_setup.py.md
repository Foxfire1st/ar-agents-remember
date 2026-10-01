# mcp/src/agents_remember/providers/provider_setup.py

## Governing Overview

[overview.md](../../../overview.md)

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

## Evidence

### Repo-Internal References

- Worktree start calls provider setup with MCP-derived provider settings. [1]
- Benchmark preparation calls package-local provider setup instead of a source script. [2]
- Provider lifecycle calls are captured through package-local command capture. [3]
- CGC seed orchestration and bundle rewriting now live outside the facade. [4]
- Shared settings and command helpers live in the setup common module. [5]
- Setup payload summaries and failed-phase compaction live in the setup reporting module. [6]

| The index-state metrics rows the catch-up stage records best-effort. | `record_index_state` | mcp/src/agents_remember/providers/metrics.py:269-283 |
