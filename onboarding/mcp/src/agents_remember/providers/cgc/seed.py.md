# mcp/src/agents_remember/providers/cgc/seed.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/providers/cgc/seed.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-07T20:45+02:00     |
| lastVerifiedCommitHash | `915e841a45cec40283902b69fe98e761672904af` |
| lastVerifiedCommitDate | 2026-07-07T18:43:43+02:00|
| governingOverview      | `../../../overview.md`                     |

## Purpose

`seed.py` owns CodeGraphContext seed request options, configured root resolution, source/target validation, export/load lifecycle orchestration, and seed result payloads.

## Code Commentary

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
- `_cgc_settings_path` is the canonical priority chain for the cgc settings file; it must match the chain in `cgc_extra_args`.
- Argv after `--` runs inside the Linux container and must be container-form (`to_container_path`); `--from-settings` and other pre-`--` arguments are consumed host-side and stay host paths (GitHub #58).

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Provider-level CGC setup calls this module before optional refresh fallback. | [setup.py](setup.py.md) |
| Bundle path rewriting is delegated to the CGC bundle module. | [bundle.py](bundle.py.md) |
| The GrepAI seed applies the same benchmark-scope hermetic guard. | [../grepai/seed.py](agents-remember/mcp/src/agents_remember/providers/grepai/seed.py) |
| Worktree setup constructs CGC seed options through the provider setup request. | [git_worktree_manager.py](agents-remember/mcp/src/agents_remember/worktrees/git_worktree_manager.py) |
| The post-watcher catch-up stage consuming the stashed divergence. | [provider_setup.py](agents-remember/mcp/src/agents_remember/providers/provider_setup.py) |
| Index-lifecycle tests pin relatable/unrelatable divergence and the proceed/stash/refuse mismatch paths. | [test_provider_index_lifecycle.py](agents-remember/mcp/tests/test_provider_index_lifecycle.py) |

## Update History

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
