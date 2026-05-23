# installer/install-runtime.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `installer/install-runtime.py`             |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-23T05:32+02:00                     |
| lastVerifiedCommitHash |                                            `00aae9dad3d8740e10a41ab285f87ecab8608745`|
| lastVerifiedCommitDate |                                            2026-05-21T23:53:08+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[overview.md](../overview.md)

## Purpose

`install-runtime.py` is the checkout entrypoint for installing package-owned runtime mechanics into a target `ar-coordination` root. It installs runtime skills, the runtime `install-skills.sh` script, provider package defaults, coordinator `AGENTS.md` templates, and opt-in benchmark package content when callers pass `--include-benchmarks`. Provider dependency installation and provider runner reinstall are MCP-owned operations, not source-installer side effects.

## Code Commentary

### Logic

The installer reconciles package-owned runtime directories by pruning stale files from installed `skills/` and `scripts`, then copying the current runtime skill tree, `runtime/scripts/install-skills.sh`, provider defaults, and four runtime `AGENTS.md` templates. It skips Python bytecode caches while pruning and copying so local validation artifacts do not become installed package content. Provider scaffolding is now split by ownership: regular source installs reconcile package-owned provider requirement and patch assets from `runtime/providers/`, while preserving provider dependency state under `_bin`, `_venvs`, and `runners` plus durable provider data/log roots. Python provider lifecycle, setup, and benchmark helpers live in the source/package layer under top-level `scripts/`; they are not installed into coordinator runtimes.

The provider defaults include both `codegraphcontext.txt` and `grepai.txt`; MCP/package-local lifecycle tooling reads those installed requirement files when installing CGC or GrepAI. Source installs no longer read coordinator `system/settings.json`, no longer expose `--skip-provider-deps`, and no longer run provider dependency commands. Provider runtime install/reinstall is exposed through the MCP `runtime_install` tool, which derives settings from MCP authority and can run package-local lifecycle code. The source installer still creates missing user-owned coordinator folders, including provider data/log/runner roots, but does not run repo onboarding bootstrap, copy settings defaults, or overwrite live memory, task, note, worktree, temp, provider dependency, provider data/log, or settings content. `runtime/system/defaults/` remains checkout template material for initialization skills rather than installed coordinator state.

Benchmark installation is opt-in. When `--include-benchmarks` is present, the installer validates the source `benchmarks/` tree, including the workspace `AGENTS.md` template, ensures the target coordinator root `.gitignore` contains `benchmarks/`, reconciles package content into `ar-coordination/benchmarks/`, and preserves the installed `user-runs/` subtree so local benchmark outputs survive reinstall. Source-side `benchmarks/workspaces/` and `benchmarks/user-runs/` are ignored while copying package content, and installed `benchmarks/workspaces/` is pruned as resettable state. Pinned code and memory repositories are not vendored into the source package; the benchmark runner materializes them during `prepare`.

### Conventions

- Regular installs reconcile runtime skills, `scripts/install-skills.sh`, provider defaults, and coordinator `AGENTS.md` templates.
- Provider scaffold install requires `runtime/providers/` in the source checkout, reconciles package-owned installed provider defaults, and preserves provider dependency/runtime/data/log directories.
- Provider dependency install is not a source-installer responsibility; use the MCP `runtime_install` tool for package-local provider lifecycle install/reinstall.
- Durable provider database state belongs under `ar-coordination/providers/data/`, logs under `ar-coordination/providers/logs/`, and runner instances under `ar-coordination/providers/runners/<provider>/`.
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

The installer owns package assets and provider defaults for the source-checkout CLI path. It does not initialize or refresh target repository onboarding, create normal memory repos, install provider dependencies, reinstall provider runners, prepare benchmark/worktree provider indexes, run benchmark Codex jobs, mutate user-generated benchmark outputs, or delete `providers/data` or `providers/logs`. Destructive provider actions such as deleting a FalkorDB graph or purging backend data must remain explicit lifecycle operations.

### Todos

- Refresh verification metadata after the runtime install/provider layout changes are committed.

### Docs References

No external documentation is needed for this installer. Benchmark behavior is documented in-repository.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The benchmark methodology says source packages commit manifests/prompts/results/templates rather than workspaces; `prepare` generates resettable source-only and memory-enabled environments, and keeps user outputs under `benchmarks/user-runs/`. | L10-L24 | [benchmark methodology](agents-remember-md/benchmarks/docs/benchmarks-methodology.md) |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The installer summary reports copied, unchanged, replaced-link, removed, created-directory, and dependency command counts; source-installer dependency counts remain zero because provider install is MCP-owned. | L33-L50 | [installer](agents-remember-md/installer/install-runtime.py) |
| Runtime installation now requires `runtime/providers`, the CGC and GrepAI requirement pins, runtime skills, and `runtime/scripts/install-skills.sh` before installing package content. | L197-L207 | [installer](agents-remember-md/installer/install-runtime.py) |
| Runtime installation prunes/copies skills and the runtime `install-skills.sh` script while ignoring Python bytecode caches, preserves provider data/log/dependency/runtime roots, installs four `AGENTS.md` templates, and creates user-owned coordinator provider folders without running provider dependency commands. | L254-L310 | [installer](agents-remember-md/installer/install-runtime.py) |
| Removal of stale installed package paths uses an extended Windows path adapter before unlinking files or recursively deleting directories, and read-only files are made writable before retrying removal. | L91-L144 | [installer](agents-remember-md/installer/install-runtime.py) |
| Benchmark installation requires `README.md`, `cases/`, and `templates/workspace-AGENTS.md`, appends `benchmarks/` to the target coordinator root `.gitignore` when needed, preserves installed `user-runs/`, prunes installed `workspaces/`, and copies package-owned benchmark content while ignoring source-side generated `workspaces/` and `user-runs/`. | L234-L261 | [installer](agents-remember-md/installer/install-runtime.py) |
| `.gitignore` updates reject a directory at the target ignore-file path, preserve existing rules, count an existing `benchmarks/` entry as unchanged, and append the entry only when missing. | L202-L216 | [installer](agents-remember-md/installer/install-runtime.py) |
| The CLI exposes `--source-root`, `--dry-run`, and `--include-benchmarks`, then calls `install_runtime` without provider dependency options. | L313-L345 | [installer](agents-remember-md/installer/install-runtime.py) |
| The runtime layout reference states that coordinator runtimes install only `scripts/install-skills.sh`; Python provider and benchmark helpers remain source/package-owned. | n/a | [runtime layout reference](agents-remember-md/docs/reference/runtime-layout.md) |

## Cross-Repo References

No sibling repository evidence is needed for the installer.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-23T05:32+02:00: Updated after coordinator runtimes stopped installing Python provider/benchmark scripts and the source installer stopped reading coordinator settings or running provider dependency commands.
- 2026-05-23T04:29+02:00: Updated after provider layout moved to `providers/runners`, `providers/data`, and `providers/logs`, with MCP-owned runtime install becoming the preferred authority path.
- 2026-05-21T23:55+02:00: Updated after `--skip-provider-deps` was fixed to preserve installed provider binaries, venvs, and runtime roots while updating package-owned provider defaults.
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
