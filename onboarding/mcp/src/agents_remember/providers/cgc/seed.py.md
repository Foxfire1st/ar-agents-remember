# mcp/src/agents_remember/providers/cgc/seed.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/cgc/seed.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-31T12:50+02:00|
| lastVerifiedCommitHash | `c20a3292e667d227a3be0c1fb276f8a701df814f` |
| lastVerifiedCommitDate | 2026-05-31T14:17:11+02:00|
| governingOverview      | `../../../overview.md`                     |

## Purpose

`seed.py` owns CodeGraphContext seed request options, configured root resolution, source/target validation, export/load lifecycle orchestration, and seed result payloads.

## Code Commentary

### Logic

It defines `CgcSeedOptions` and the internal `CgcSeedContext`, resolves source and target CGC roots from explicit arguments or settings, checks repository HEAD compatibility (via `git_head_or_none`) unless mismatches are allowed, protects same-coordination-root cross-path seeding unless explicitly allowed or isolated, starts the source backend, exports a bundle, rewrites paths, and loads the rewritten bundle into the target. The CGC provider block is looked up through the shared `setup_common.provider_settings(settings, CGC_PROVIDER_ID)` helper rather than a local wrapper. The export and load commands run with `UNLIMITED_TIMEOUT` so large bundle dump/load operations are never killed by a wall-clock cap.

### Invariants And Boundaries

- Seed source settings must come from explicit provider settings or from the same coordination root's active settings path.
- CGC seed is an optimization; callers decide whether a failed seed can fall back to full refresh.
- Bundle path rewriting is delegated to `bundle.py`.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Provider-level CGC setup calls this module before optional refresh fallback. | [setup.py](setup.py.md) |
| Bundle path rewriting is delegated to the CGC bundle module. | [bundle.py](bundle.py.md) |
| Worktree setup constructs CGC seed options through the provider setup request. | [git_worktree_manager.py](agents-remember-md/mcp/src/agents_remember/worktrees/git_worktree_manager.py) |

## Update History

- 2026-05-31T12:50+02:00 — Renamed `git_head` to `git_head_or_none` (now with a docstring) and removed the local `_cgc_provider` wrapper in favor of `setup_common.provider_settings`; `load_settings`/`settings_path` now take only the settings file path. Corrected Logic prose to name `git_head_or_none` and the shared `provider_settings` lookup (1.0.0 review remediation).
- 2026-05-30T21:33+02:00: Documented that seed export/load now run with `UNLIMITED_TIMEOUT` (never-cap-indexing run). Verified against `825a172`.
- 2026-05-29T18:35+02:00: Narrowed the `CgcSeedContext | dict` union via `isinstance` at the consumption boundary and removed the now-dead `_first_seed_skip`; behavior-preserving (commit `0549b28`).
- 2026-05-25T19:50+02:00: Created when CGC seed orchestration was extracted out of `provider_setup.py`.
