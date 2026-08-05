# mcp/src/agents_remember/providers/cgc/seed.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/providers/cgc/seed.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T00:00+02:00     |
| lastVerifiedCommitHash | `abc7cbcc74921cdcb57a61529445f61641e919e7` |
| lastVerifiedCommitDate | 2026-07-31T21:50:08+02:00|
| governingOverview      | `../../../overview.md`                     |

## Purpose

`seed.py` owns CodeGraphContext seed request options, configured root resolution, source/target validation, export/load lifecycle orchestration, and seed result payloads.

## Code Commentary

### 260731-EFA-L3 Both Git Calls Run On The One Runner

This module's two git calls — `git_head_or_none` (the HEAD it declares the seed fresh against) and
`seed_commit_divergence` (the catch-up diff) — no longer build their own `subprocess.run`. Both call
`run_git` from `agents_remember.kernel.git_command`:

```python
result = run_git(repo_root, ["rev-parse", "HEAD"])
...
result = run_git(
    source_repo_root,
    ["diff", "--name-status", source_head, target_head],
    timeout=_CATCH_UP_DIFF_TIMEOUT_SECONDS,
)
```

What that buys, beyond removing a copy:

- **The seed's freshness claim is anchored to the repository it names.** The removed
  `git_head_or_none` body spelled out `-c safe.directory=… -C <repo_root> rev-parse HEAD` but passed
  no `env=`, so an exported `GIT_DIR` selected the repository regardless: the call would return
  *another* repository's HEAD, and the seed would be declared fresh against a commit this repo never
  had. `run_git` strips the whole `GIT_DIR` family (`GIT_DIR`, `GIT_WORK_TREE`, `GIT_INDEX_FILE`,
  `GIT_OBJECT_DIRECTORY`, `GIT_ALTERNATE_OBJECT_DIRECTORIES`, `GIT_COMMON_DIR`, `GIT_NAMESPACE`,
  `GIT_PREFIX`) before every call. This matters here more than almost anywhere else in the tree,
  because seeding runs during worktree start — exactly when a `GIT_DIR` is likely to be in the
  environment.
- **`git_head_or_none` is bounded at all.** It previously ran with no `timeout`; it now inherits the
  runner's `GIT_LOCAL_TIMEOUT_SECONDS` (300) default.
- The catch-up diff keeps its own tighter bound, now named: `_CATCH_UP_DIFF_TIMEOUT_SECONDS = 60`.
  It runs during provider setup, and a repo whose diff has not answered in a minute is not one a
  per-file touch pass was going to catch up anyway.

Protocol-pipe hygiene is unchanged, just relocated: stdin is `DEVNULL` because that is the runner's
default, not because this module asks for it. `stderr` is now captured rather than discarded (the
runner uses `capture_output=True`), which changes nothing for callers — both call sites branch on
`returncode` only.

### 260731-EFA-L2 Seed Resolution Split

`_resolve_seed_context` is now a sequence of named steps, each of which can return a skip payload:

- `_seed_precondition_skip(args, settings)` — the reasons to skip **before any source settings are
  read**: a benchmark-scoped target (benchmarks are hermetic, so a benchmark target never seeds
  from another stack) and a missing seed-source coordination root. Returns `None` to go ahead.
- `_seed_locations(args, settings, source_settings, source_coordination_root)` — repo root and
  runtime root for both ends, or the first side's skip payload. Every one of the four lookups
  reports failure the same way, so **the first payload wins and the caller never sees a
  half-resolved pair**.
- `_validated_seed_context(args, source, target)` — takes two **`_CgcSeedEnd(coordination_root,
  repo_id, repo_root, runtime_root)`** values. Source and target are symmetric, so naming the end
  makes the seed read as source → target instead of four interleaved pairs whose argument order is
  the only thing keeping them straight. `_seed_validation_failure(args, source, target,
  source_head, target_head)` takes the same two ends.

`run_lifecycle` calls in this module pass a `setup_common.LifecycleCommand`.

### Logic

`_resolve_seed_context` first refuses a **benchmark-scoped** target: when the target `codegraphcontext-code` provider's `instance.scope == "benchmark"`, it returns `_seed_skip` before any source/backend work, so a benchmark never seeds from the live workspace cgc backend (hermetic). Otherwise it defines `CgcSeedOptions` and the internal `CgcSeedContext`, resolves source and target CGC roots from explicit arguments or settings, checks repository HEAD relatability (via `git_head_or_none` + `seed_commit_divergence`, below) unless mismatches are allowed, protects same-coordination-root cross-path seeding unless explicitly allowed or isolated, starts the source backend, exports a bundle, rewrites paths, and loads the rewritten bundle into the target. The CGC provider block is looked up through the shared `setup_common.provider_settings(settings, CGC_PROVIDER_ID)` helper rather than a local wrapper. The export and load commands run under the configurable provider-setup cap (`args.timeout` ← `timeoutCaps.providerSetupSeconds`, default 1800; `0` = unbounded opt-out) — bundle copies run <60s in practice, so only a genuinely wedged docker exec can reach the cap, and a wedge no longer hangs `worktree_start` forever. A stall watchdog (like the GrepAI clone's) is a noted follow-up; the lifecycle-CLI boundary currently blocks a progress callback here.

A HEAD difference between source and target is a state to CATCH UP from, not
a teardown (260707-HFX-L2): the old exact-equality refusal fed the
refresh-all fallback — a full reindex on every normal worktree start, the OOM
amplifier. `seed_commit_divergence(source_repo_root, source_head,
target_head)` runs `git diff --name-status` in the SOURCE repo (a target that
is a worktree of the source shares its object database, so both commits
resolve there) and returns CLASSIFIED `entries` — `[{status, path, from?}]`,
a rename `R` carrying the new path as `path` and the old path as `from` —
plus their count and both heads. The classification exists because the
catch-up must be HONEST about deliverability (review L2/B2):
additions/modifications on disk are touchable, while deletions and
rename-sources leave phantom graph nodes no touch can fix — those are
reported as residual staleness, never blessed as caught up. `None` means git
cannot relate the heads — unrelated repositories, the one case where refusing
is still right. `_seed_commit_mismatch` now PROCEEDS on a
relatable divergence, stashing the delta on `args._cgc_seed_divergence` for
`provider_setup`'s post-watcher catch-up stage, and refuses only unrelatable
heads with the reworded reason ("source and target repository heads are
unrelated (divergence not computable); refusing to seed a foreign graph") —
the foreign-graph protection. `CgcSeedOptions.delta_max_files` (`0` = the
built-in `DEFAULT_SEED_DELTA_MAX_FILES`, 200) is the catch-up bound that
stage applies: at or below it the seeded near-perfect graph catches up
through the watcher's own per-file indexing; above it the clone still serves
— stale, surfaced — and a from-zero rebuild stays an explicit `cgc refresh`
only.

`_cgc_settings_path(args)` is the single source of truth for which settings file cgc actually runs against. It walks the priority chain `cgc_from_settings > provider_from_settings > from_settings` and returns the first truthy value. Both `cgc_extra_args` (which builds the `--from-settings` CLI flag) and `_seed_target_runtime_root` call this helper so both always agree on the settings file.

The argv after `--` in `_seed_export`/`_seed_load` executes inside the Linux runner container, so the bundle paths and the export `--repo` root are rendered through `to_container_path` (canonical home: `providers/context_common.py`; drive letter stripped on Windows, identity on POSIX). Host-form `C:/` paths made every Windows seed export die on a nonexistent path — CGC even joined the drive-lettered `--repo` value onto its cwd as a relative path — silently forcing the full reindex fallback on every Windows worktree start (GitHub #58). The host-side bundle rewrite (`bundle.py`) keeps host paths.

`_seed_target_runtime_root(args, settings, repo_id)` resolves the host path under which the rewritten target bundle is written. In an isolated worktree seed (`cgc_isolated_runtime_root` is set), the `bundle import` runs inside the worktree's cgc runner, which bind-mounts only the worktree instance runtime root and receives the bundle path in container form. Using the caller's `settings` (which resolve against the workspace coordination root) would land the bundle under the workspace runner root that the worktree runner cannot see, causing "Bundle file not found" and a silent fallback to a full re-index (OQ5). The fix: resolve from the isolated `--from-settings` path (via `_cgc_settings_path` + `_seed_runtime_root`) so the bundle lands under `<worktreeRuntimeRoot>/<repoId>` — the path the worktree runner's mount covers. Falls back to the workspace `_seed_runtime_root` when not isolated or when the isolated settings file is unreadable. `_seed_bundle_paths` consumes `context.target_runtime_root` returned by this function.

### Invariants And Boundaries

- A benchmark-scoped target is never seeded (hermetic): `_resolve_seed_context` returns `_seed_skip` before resolving any source or starting a backend, mirroring the GrepAI clone guard so a benchmark cannot reach the live workspace cgc backend (task 260619).
- Seed source settings must come from explicit provider settings or from the same coordination root's active settings path.
- CGC seed is an optimization; callers decide whether a failed seed can fall back to full refresh.
- A relatable HEAD divergence never refuses the seed (260707-HFX-L2): the
  graph clones and the recorded delta drives the watcher-event catch-up; only
  unrelatable heads refuse, protecting against cloning a different
  repository's graph.
- Bundle path rewriting is delegated to `bundle.py`.
- Every git call in this module goes through `kernel.git_command.run_git`, never `subprocess`
  directly: the seed's freshness decision is only as trustworthy as the guarantee that the HEAD it
  read came from the repository it named, and an inherited `GIT_DIR` breaks exactly that.
- `_cgc_settings_path` is the canonical priority chain for the cgc settings file; it must match the chain in `cgc_extra_args`.
- Argv after `--` runs inside the Linux container and must be container-form (`to_container_path`); `--from-settings` and other pre-`--` arguments are consumed host-side and stay host paths (GitHub #58).

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Provider-level CGC setup calls this module before optional refresh fallback. | "def prepare_enabled_provider(" | mcp/src/agents_remember/providers/cgc/setup.py:241-241 |
| Bundle path rewriting is delegated to the CGC bundle module. | "def rewrite_cgc_bundle_paths(" | mcp/src/agents_remember/providers/cgc/bundle.py:79-79 |
| The GrepAI seed applies the same benchmark-scope hermetic guard. | "benchmark grepai-memory is hermetic; seeding/cloning is disabled" | mcp/src/agents_remember/providers/grepai/seed.py:153-153 |
| Worktree setup constructs CGC seed options through the provider setup request. | "cgc_seed=provider_setup.CgcSeedOptions(" | mcp/src/agents_remember/worktrees/modules/start.py:851-851 |
| The post-watcher catch-up stage consuming the stashed divergence. | "def _seed_catchup_results(" | mcp/src/agents_remember/providers/provider_setup.py:250-250 |
| Index-lifecycle tests pin relatable/unrelatable divergence and the proceed/stash/refuse mismatch paths. | "def test_relatable_heads_report_the_changed_files(self) -> None:"; "def test_unrelatable_heads_return_none(self) -> None:"; "def test_relatable_divergence_proceeds_and_stashes_the_delta(self) -> None:"; "def test_unrelatable_heads_still_refuse(self) -> None:" | mcp/tests/test_provider_index_lifecycle.py:62-62; mcp/tests/test_provider_index_lifecycle.py:75-75; mcp/tests/test_provider_index_lifecycle.py:92-92; mcp/tests/test_provider_index_lifecycle.py:121-121 |
| `run_git`, the one runner both git calls here use: `GIT_REPOSITORY_SELECTOR_ENV` + `git_environment` strip the selectors, and `GIT_LOCAL_TIMEOUT_SECONDS` is the default bound `git_head_or_none` inherits. | "GIT_REPOSITORY_SELECTOR_ENV = ("; "GIT_LOCAL_TIMEOUT_SECONDS = 300"; "def git_environment() -> dict[str, str]:" | mcp/src/agents_remember/kernel/git_command.py:33-33; mcp/src/agents_remember/kernel/git_command.py:70-70; mcp/src/agents_remember/kernel/git_command.py:76-76 |
| `DecoyRepositoryTests` proves a set `GIT_DIR` cannot make a runner call answer from another repository, and `SingleRunnerTests.test_only_the_kernel_module_defines_a_git_runner` stops a private copy from reappearing here. | "class DecoyRepositoryTests(unittest.TestCase):"; "class SingleRunnerTests(unittest.TestCase):"; "def test_only_the_kernel_module_defines_a_git_runner(self) -> None:" | mcp/tests/test_git_command.py:155-155; mcp/tests/test_git_command.py:393-393; mcp/tests/test_git_command.py:448-448 |

## Update History

- 2026-08-02T17:00+02:00 — 260731-EFA-L6 curator W1-B03: repaired 8 citation rows with exact anchors and current source paths; scoped citation recheck recorded separately. Verification metadata remains pinned until closeout.

- 2026-07-31T20:55+02:00 — 260731-EFA-L3 curator: this module lost both of its local
  `subprocess.run` calls. `git_head_or_none` and `seed_commit_divergence` now call
  `kernel.git_command.run_git`, so the seed's HEAD comparison runs with the `GIT_DIR`-family
  selectors stripped — the removed body passed `-C <repo_root>` but no `env=`, so an exported
  `GIT_DIR` (likely during worktree start, which is when seeding runs) would have returned another
  repository's HEAD and the seed would have been declared fresh against a commit this repo never
  had. `git_head_or_none` also gains a bound it never had (the runner's 300 s local default), and
  the catch-up diff's 60 s is now the named `_CATCH_UP_DIFF_TIMEOUT_SECONDS`. Recorded this as a
  new Code Commentary section plus an invariant, and superseded the "detaches stdin" detail from
  the 2026-06-10 entry: stdin is still `DEVNULL`, now as the runner's default rather than this
  module's own argument. Skip reasons, divergence classification and the produced `CgcSeedContext`
  are unchanged. Verification metadata pinned until closeout stamps the L3 commit.
- 2026-07-31T00:00+02:00 — 260731-EFA-L2 (gate honesty, `C901`/`PLR0911`/`PLR0913` armed with no
  exemptions): extracted `_seed_precondition_skip` and `_seed_locations` from
  `_resolve_seed_context`, and re-signed `_validated_seed_context` / `_seed_validation_failure`
  onto the new frozen `_CgcSeedEnd` (source and target as named ends). Skip reasons, validation
  failures and the produced `CgcSeedContext` are unchanged. Verification metadata pinned until
  closeout stamps the L2 commit.
- 2026-07-07T20:45+02:00 — 260707-HFX-L2 review fix (L2/B2): `seed_commit_divergence` switched to
  `git diff --name-status` and returns classified `entries` (`[{status, path, from?}]`; a rename
  carries its old path as `from`) so the catch-up stage can be honest about deliverability —
  deletions and rename-sources are phantom residuals no touch can fix. Verification metadata
  pinned until closeout stamps the HFX-L2 commit.
- 2026-07-07T19:30+02:00 — 260707-HFX-L2 (index lifecycle): a HEAD difference is a state to catch
  up from, not a teardown — added `seed_commit_divergence` (git diff in the source repo, shared
  object database; `None` = unrelatable) and `CgcSeedOptions.delta_max_files`
  (`0` = `DEFAULT_SEED_DELTA_MAX_FILES` = 200); `_seed_commit_mismatch` now proceeds on relatable
  divergence and stashes the delta on `args._cgc_seed_divergence` for the catch-up stage,
  refusing only unrelatable heads (foreign-graph protection, new reason text). Verification
  metadata pinned until closeout stamps the HFX-L2 commit.
- 2026-06-19T13:42: `_resolve_seed_context` now refuses a benchmark-scoped target (`instance.scope == "benchmark"`) with a `_seed_skip` before any source/backend work — mirrors the GrepAI hermetic guard so a benchmark never seeds from the live workspace cgc backend (task 260619).
- 2026-06-10T07:05+02:00 — Export/load in-container argv (bundle paths, export `--repo`) now rendered via `to_container_path` (GitHub #58): raw host paths made every Windows seed export fail and silently forced the full reindex fallback. `to_container_path`'s canonical home moved to `providers/context_common.py` (provider-agnostic; also avoids the facade star-import diamond a `cgc/seed.py → cgc.context.core` import would trip).
- 2026-06-10T05:30+02:00 — `git_head_or_none` detaches stdin (protocol-pipe hygiene), and `_seed_export`/`_seed_load` are bounded by the configurable provider-setup cap (`timeoutCaps.providerSetupSeconds`) instead of UNLIMITED — only a wedge can reach the cap since bundle copies run <60s in practice.
- 2026-06-01T23:40+02:00 — Added `_cgc_settings_path(args)` as the single-source settings-path resolver (priority: `cgc_from_settings > provider_from_settings > from_settings`) used by both `cgc_extra_args` and the new `_seed_target_runtime_root`. Added `_seed_target_runtime_root(args, settings, repo_id)`: in an isolated worktree seed resolves the bundle's host path from the isolated worktree settings (via `_cgc_settings_path` + `_seed_runtime_root`) so the bundle lands under the worktree runner's instance mount, not the workspace runner root where the worktree runner can't find it. Fixes OQ5 ("Bundle file not found" / silent full re-index fallback). Falls back to workspace `_seed_runtime_root` when not isolated or isolated settings are unreadable. Updated Logic and Invariants accordingly.
- 2026-05-31T12:50+02:00 — Renamed `git_head` to `git_head_or_none` (now with a docstring) and removed the local `_cgc_provider` wrapper in favor of `setup_common.provider_settings`; `load_settings`/`settings_path` now take only the settings file path. Corrected Logic prose to name `git_head_or_none` and the shared `provider_settings` lookup (1.0.0 review remediation).
- 2026-05-30T21:33+02:00: Documented that seed export/load now run with `UNLIMITED_TIMEOUT` (never-cap-indexing run). Verified against `825a172`.
- 2026-05-29T18:35+02:00: Narrowed the `CgcSeedContext | dict` union via `isinstance` at the consumption boundary and removed the now-dead `_first_seed_skip`; behavior-preserving (commit `0549b28`).
- 2026-05-25T19:50+02:00: Created when CGC seed orchestration was extracted out of `provider_setup.py`.
