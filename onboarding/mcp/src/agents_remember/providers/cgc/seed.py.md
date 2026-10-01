# mcp/src/agents_remember/providers/cgc/seed.py

## Governing Overview

[overview.md](overview.md)

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
    GitRunnerOptions(timeout=_CATCH_UP_DIFF_TIMEOUT_SECONDS),
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

## Evidence

### Docs References

No external Domain Documentation source is configured for this memory repo.

### Repo-Internal References

- Provider-level CGC setup calls this module before optional refresh fallback. [1]
- Bundle path rewriting is delegated to the CGC bundle module. [2]
- The GrepAI seed applies the same benchmark-scope hermetic guard. [3]
- Worktree setup constructs CGC seed options through the provider setup request. [4]
- The post-watcher catch-up stage consuming the stashed divergence. [5]

| The canonical selector list identifies inherited Git variables to remove. | `GIT_REPOSITORY_SELECTOR_ENV` | mcp/src/agents_remember/kernel/git_command.py:55-64 |
| The Git environment removes canonical repository selectors before execution. | `git_environment` | mcp/src/agents_remember/kernel/git_command.py:140-146 |
| The shared Git runner applies caller-selected bounds and isolated repository environment; the catch-up diff passes its 60s bound as `GitRunnerOptions(timeout=...)`. | `run_git` | mcp/src/agents_remember/kernel/git_command.py:149-213 |
