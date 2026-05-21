# installer/install-runtime.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `installer/install-runtime.py`             |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-21T04:53+02:00                     |
| lastVerifiedCommitHash |                                            `0462de46a1da1bf1997e3979f4cc5bc53d1132f6`|
| lastVerifiedCommitDate |                                            2026-05-21T08:30:44+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[overview.md](../overview.md)

## Purpose

`install-runtime.py` is the checkout entrypoint for installing package-owned runtime mechanics into a target `ar-coordination` root. It installs runtime skills, scripts, provider package defaults, provider dependencies for enabled providers, coordinator `AGENTS.md` templates, and opt-in benchmark package content when callers pass `--include-benchmarks`.

## Code Commentary

### Logic

The installer reconciles package-owned runtime directories by pruning stale files from installed `skills/` and `scripts`, then copying the current runtime skill tree, runtime scripts, provider defaults, and four runtime `AGENTS.md` templates. It skips Python bytecode caches while pruning and copying so local validation artifacts do not become installed package content. Provider scaffolding is intentionally disposable: reinstall removes `ar-coordination/providers/` wholesale and recreates it from `runtime/providers/`, so pinned requirements and patch assets are source-reproducible instead of preserved by fragile exception lists. Durable provider databases live outside that tree under `ar-coordination/provider-data/`.

The provider defaults include both `codegraphcontext.txt` and `grepai.txt`; provider lifecycle tooling reads those installed requirement files when installing CGC or GrepAI. After recreating package assets and user-owned directories, regular reinstall checks the live `system/settings.json`. If no providers are enabled there, dependency install is skipped. If providers are enabled, reinstall calls the installed `scripts/provider-setup.py install` entrypoint, which delegates lower-level mechanics to `provider-lifecycle.py`. `--skip-provider-deps` is the explicit scaffolding-only escape hatch. `provider-lifecycle.py cgc apply-settings` or `install-all` can still reconcile configured CGC runtime shape while the runtime is active, but the reinstall contract is now complete: `providers/` is rebuilt from source, enabled provider dependencies are reinstalled from copied pins through the shared setup script, and `provider-data/` is preserved. Pruning uses a Windows long-path removal adapter and a read-only retry path so generated benchmark workspaces with deeply nested Git repositories can still be deleted. The installer creates missing user-owned coordinator folders, including `provider-data/`, but does not run repo onboarding bootstrap, copy settings defaults, or overwrite live memory, task, note, worktree, temp, provider-data, or settings content. `runtime/system/defaults/` remains checkout template material for initialization skills rather than installed coordinator state.

Benchmark installation is opt-in. When `--include-benchmarks` is present, the installer validates the source `benchmarks/` tree, including the workspace `AGENTS.md` template, ensures the target coordinator root `.gitignore` contains `benchmarks/`, reconciles package content into `ar-coordination/benchmarks/`, and preserves the installed `user-runs/` subtree so local benchmark outputs survive reinstall. Source-side `benchmarks/workspaces/` and `benchmarks/user-runs/` are ignored while copying package content, and installed `benchmarks/workspaces/` is pruned as resettable state. Pinned code and memory repositories are not vendored into the source package; the benchmark runner materializes them during `prepare`.

### Conventions

- Regular installs reconcile runtime skills, scripts, provider defaults, enabled provider dependencies, and coordinator `AGENTS.md` templates.
- Provider scaffold install requires `runtime/providers/` in the source checkout, deletes the installed `providers/` tree, and copies source defaults back into it before dependency installation runs.
- Provider dependency install is settings-driven through `scripts/provider-setup.py install`, and is skipped when live settings do not enable any providers.
- `--skip-provider-deps` deliberately disables provider dependency installation for file-only repair.
- Durable provider database state belongs under `ar-coordination/provider-data/`, which is created if missing and is not deleted by reinstall.
- `runtime/providers/requirements/codegraphcontext.txt` and `runtime/providers/requirements/grepai.txt` are required package assets copied into `ar-coordination/providers/requirements/`.
- `--include-benchmarks` installs package-owned benchmark definitions, prompts, workspace templates, author result artifacts, and benchmark docs.
- Benchmark installs append `benchmarks/` to the target coordinator root `.gitignore` when the entry is missing, without replacing existing ignore rules.
- Only `ar-coordination/benchmarks/user-runs/` is preserved inside the benchmark package.
- Source checkout `benchmarks/workspaces/` and `benchmarks/user-runs/` are ignored while copying benchmark package content, even when local verification created those generated folders in the source checkout.
- Generated benchmark workspaces may contain long nested repository and memory paths plus read-only Git pack files; pruning converts removal targets to extended Windows paths and retries read-only deletes as writable before deleting them.
- Normal user memory under `ar-coordination/memory-repos/` is never touched by benchmark installation.
- Benchmark-local memory under `ar-coordination/benchmarks/workspaces/<case-id>/ar-coordination/memory-repos/` is resettable runner state, not normal user memory.
- `__pycache__`, `.pyc`, and `.pyo` paths are ignored package artifacts and should be pruned from installed runtime and benchmark trees.

### Invariants And Boundaries

The installer owns package assets, disposable provider scaffolding, and enabled provider dependency installation through the shared provider setup entrypoint. It does not initialize or refresh target repository onboarding, create normal memory repos, prepare benchmark/worktree provider indexes, run benchmark Codex jobs, mutate user-generated benchmark outputs, or delete `provider-data/`. Destructive provider actions such as deleting a FalkorDB graph or purging backend data must remain explicit lifecycle operations.

### Todos

- Refresh verification metadata after the benchmark installer changes are committed.

### Docs References

No external documentation is needed for this installer. Benchmark behavior is documented in-repository.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The benchmark methodology says source packages commit manifests/prompts/results/templates rather than workspaces; `prepare` generates resettable source-only and memory-enabled environments, and keeps user outputs under `benchmarks/user-runs/`. | L10-L24 | [benchmark methodology](agents-remember-md/benchmarks/docs/benchmarks-methodology.md) |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The installer summary reports copied, unchanged, replaced-link, removed, created-directory, and provider dependency command counts. | L33-L50 | [installer](agents-remember-md/installer/install-runtime.py) |
| Runtime installation now requires `runtime/providers`, including the CGC and GrepAI requirement pins, before installing package content. | L219-L227 | [installer](agents-remember-md/installer/install-runtime.py) |
| Provider dependency installation loads live coordinator settings, detects enabled providers, and runs GrepAI and CGC lifecycle install commands from the installed runtime script. | L264-L385 | [installer](agents-remember-md/installer/install-runtime.py) |
| Runtime installation prunes/copies skills and scripts while ignoring Python bytecode caches, deletes and recreates installed provider scaffolding from source defaults, installs four `AGENTS.md` templates, creates user-owned coordinator folders including `provider-data`, and then installs enabled provider dependencies unless skipped. | L400-L423 | [installer](agents-remember-md/installer/install-runtime.py) |
| Removal of stale installed package paths uses an extended Windows path adapter before unlinking files or recursively deleting directories, and read-only files are made writable before retrying removal. | L91-L144 | [installer](agents-remember-md/installer/install-runtime.py) |
| Benchmark installation requires `README.md`, `cases/`, and `templates/workspace-AGENTS.md`, appends `benchmarks/` to the target coordinator root `.gitignore` when needed, preserves installed `user-runs/`, prunes installed `workspaces/`, and copies package-owned benchmark content while ignoring source-side generated `workspaces/` and `user-runs/`. | L234-L261 | [installer](agents-remember-md/installer/install-runtime.py) |
| `.gitignore` updates reject a directory at the target ignore-file path, preserve existing rules, count an existing `benchmarks/` entry as unchanged, and append the entry only when missing. | L202-L216 | [installer](agents-remember-md/installer/install-runtime.py) |
| The CLI exposes `--include-benchmarks`, `--skip-provider-deps`, and `--provider-deps-timeout`, and passes those options into `install_runtime`. | L428-L464 | [installer](agents-remember-md/installer/install-runtime.py) |
| The root README documents normal runtime installation, default provider dependency installation, the `--skip-provider-deps` escape hatch, and the optional benchmark install command. | L45-L59 | [README](agents-remember-md/README.md) |

## Cross-Repo References

No sibling repository evidence is needed for the installer.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-21T04:53+02:00: Updated after the installer switched provider dependency installation to the shared `scripts/provider-setup.py install` entrypoint.
- 2026-05-21T02:14+02:00: Updated after reinstall began running enabled provider dependency installers by default, with `--skip-provider-deps` as the explicit scaffolding-only mode.
- 2026-05-21T02:10+02:00: Updated for the new idempotence contract: reinstall deletes and recreates `ar-coordination/providers/` while preserving durable provider databases under `ar-coordination/provider-data/`.
- 2026-05-21T01:47+02:00: Clarified that the installer ships CGC and GrepAI provider defaults but does not own live CGC runtime cleanup; stale generated CGC folders and legacy Kuzu artifacts are reconciled by provider lifecycle commands.
- 2026-05-20T19:11+02:00: Documented that regular runtime installation now ships package provider defaults from `runtime/providers/` while preserving live provider runtime state under `ar-coordination/providers/`.
- 2026-05-16T12:13+02:00: Documented that benchmark installation ignores source-side generated `workspaces/` and `user-runs/`, prunes installed `workspaces/`, and still preserves installed `user-runs/` across reinstalls.
- 2026-05-16T11:32+02:00: Documented the benchmark installer `.gitignore` guard that adds `benchmarks/` to target coordinator roots when benchmark fixtures are installed plus the Windows long-path/read-only removal adapters used while pruning generated benchmark workspaces.
- 2026-05-15T17:32+02:00: Updated after benchmark install validation switched from committed workspace scaffolds to the generated workspace `AGENTS.md` template and installer copy/prune started ignoring Python bytecode caches. Verification metadata remains pinned to the last committed source state until closeout.
- 2026-05-15T15:50+02:00: Updated after adding opt-in benchmark installation, benchmark tree validation, and `user-runs/` preservation. Verification metadata remains pinned to the last committed source state until closeout.
- 2026-05-15T01:55+02:00: Created with pending verification metadata for the first runtime-layout closeout commit.
- 2026-05-15T03:06+02:00: Corrected installer ownership notes so system defaults remain source-side templates instead of installed runtime files.
