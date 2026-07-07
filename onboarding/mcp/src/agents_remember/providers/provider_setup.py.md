# mcp/src/agents_remember/providers/provider_setup.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/providers/provider_setup.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-07T17:40+02:00     |
| lastVerifiedCommitHash | `946ecca65e02faf864ea024ae1056600cd0c8021` |
| lastVerifiedCommitDate | 2026-07-07T17:26:18+02:00|
| governingOverview      | `../../../overview.md`                     |

## Purpose

`provider_setup.py` is the provider setup facade. It keeps the typed
`ProviderSetupRequest`, CLI parser, action payload assembly, watcher dispatch,
and public compatibility exports while implementation lives in focused setup
modules.

## Code Commentary

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
refresh fallback, and watcher start/status in sequence. CGC seed failure still
does not fail the whole prepare operation when `cgc_refresh_fallback` is enabled
and the fallback refresh path succeeds. Setup payload finalization now delegates
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
- A failed CGC seed must not fail the whole prepare operation when the existing
  refresh fallback is enabled and then runs.
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

| Finding | Source Path |
| --- | --- |
| Worktree start calls provider setup with MCP-derived provider settings. | [git_worktree_manager.py](agents-remember/mcp/src/agents_remember/worktrees/git_worktree_manager.py) |
| Benchmark preparation calls package-local provider setup instead of a source script. | [runner.py](agents-remember/mcp/src/agents_remember/benchmarks/runner.py) |
| Provider lifecycle calls are captured through package-local command capture. | [command_capture.py](agents-remember/mcp/src/agents_remember/mcp/command_capture.py) |
| CGC seed orchestration and bundle rewriting now live outside the facade. | [seed.py](cgc/seed.py.md); [bundle.py](cgc/bundle.py.md) |
| Provider-specific setup branches live in provider-owned setup modules. | [CGC setup](cgc/setup.py.md); [GrepAI setup](grepai/setup.py.md) |
| Shared settings and command helpers live in the setup common module. | [setup_common.py](setup_common.py.md) |
| Setup payload summaries and failed-phase compaction live in the setup reporting module. | [setup_reporting.py](setup_reporting.py.md) |
| Containment tests pin the fleet setup lock's contention timeout and uncontended no-op. | [test_provider_containment.py](agents-remember/mcp/tests/test_provider_containment.py) |

## Update History

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
