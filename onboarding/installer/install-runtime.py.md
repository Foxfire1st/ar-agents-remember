# installer/install-runtime.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `installer/install-runtime.py`             |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-16T12:13+02:00                     |
| lastVerifiedCommitHash | `032a5b839c5c7a0f8e487fe65f5b060e11a9b8a2`         |
| lastVerifiedCommitDate | 2026-05-16T18:07:23+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[overview.md](../overview.md)

## Purpose

`install-runtime.py` is the checkout entrypoint for installing package-owned runtime mechanics into a target `ar-coordination` root. It now also owns the opt-in benchmark package install when callers pass `--include-benchmarks`.

## Code Commentary

### Logic

The installer reconciles package-owned runtime directories by pruning stale files from installed `skills/` and `scripts`, then copying the current runtime skill tree, runtime scripts, and four runtime `AGENTS.md` templates. It skips Python bytecode caches while pruning and copying so local validation artifacts do not become installed package content. Pruning uses a Windows long-path removal adapter and a read-only retry path so generated benchmark workspaces with deeply nested Git repositories can still be deleted. The installer creates missing user-owned coordinator folders but does not run repo onboarding bootstrap, copy settings defaults, or overwrite live memory, task, note, worktree, temp, or settings content. `runtime/system/defaults/` remains checkout template material for initialization skills rather than installed coordinator state.

Benchmark installation is opt-in. When `--include-benchmarks` is present, the installer validates the source `benchmarks/` tree, including the workspace `AGENTS.md` template, ensures the target coordinator root `.gitignore` contains `benchmarks/`, reconciles package content into `ar-coordination/benchmarks/`, and preserves the installed `user-runs/` subtree so local benchmark outputs survive reinstall. Source-side `benchmarks/workspaces/` and `benchmarks/user-runs/` are ignored while copying package content, and installed `benchmarks/workspaces/` is pruned as resettable state. Pinned code and memory repositories are not vendored into the source package; the benchmark runner materializes them during `prepare`.

### Conventions

- Regular installs keep the prior runtime-only behavior.
- `--include-benchmarks` installs package-owned benchmark definitions, prompts, workspace templates, author result artifacts, and benchmark docs.
- Benchmark installs append `benchmarks/` to the target coordinator root `.gitignore` when the entry is missing, without replacing existing ignore rules.
- Only `ar-coordination/benchmarks/user-runs/` is preserved inside the benchmark package.
- Source checkout `benchmarks/workspaces/` and `benchmarks/user-runs/` are ignored while copying benchmark package content, even when local verification created those generated folders in the source checkout.
- Generated benchmark workspaces may contain long nested repository and memory paths plus read-only Git pack files; pruning converts removal targets to extended Windows paths and retries read-only deletes as writable before deleting them.
- Normal user memory under `ar-coordination/memory-repos/` is never touched by benchmark installation.
- Benchmark-local memory under `ar-coordination/benchmarks/workspaces/<case-id>/ar-coordination/memory-repos/` is resettable runner state, not normal user memory.
- `__pycache__`, `.pyc`, and `.pyo` paths are ignored package artifacts and should be pruned from installed runtime and benchmark trees.

### Invariants And Boundaries

The installer owns package assets only. It does not initialize or refresh target repository onboarding, create normal memory repos, run benchmark Codex jobs, or mutate user-generated benchmark outputs.

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
| The installer summary reports copied, unchanged, replaced-link, removed, and created-directory counts. | L25-L40 | [installer](agents-remember-md/installer/install-runtime.py) |
| Runtime installation prunes and copies skills/scripts while ignoring Python bytecode caches, installs four `AGENTS.md` templates, and creates user-owned coordinator folders. | L16-L26; L126-L178; L240-L265 | [installer](agents-remember-md/installer/install-runtime.py) |
| Removal of stale installed package paths uses an extended Windows path adapter before unlinking files or recursively deleting directories, and read-only files are made writable before retrying removal. | L84-L122 | [installer](agents-remember-md/installer/install-runtime.py) |
| Benchmark installation requires `README.md`, `cases/`, and `templates/workspace-AGENTS.md`, appends `benchmarks/` to the target coordinator root `.gitignore` when needed, preserves installed `user-runs/`, prunes installed `workspaces/`, and copies package-owned benchmark content while ignoring source-side generated `workspaces/` and `user-runs/`. | L210-L237 | [installer](agents-remember-md/installer/install-runtime.py) |
| `.gitignore` updates reject a directory at the target ignore-file path, preserve existing rules, count an existing `benchmarks/` entry as unchanged, and append the entry only when missing. | L181-L195 | [installer](agents-remember-md/installer/install-runtime.py) |
| The CLI exposes `--include-benchmarks` and prints a benchmark package install line only when that flag is used. | L270-L301 | [installer](agents-remember-md/installer/install-runtime.py) |
| The root README documents normal runtime installation and the optional benchmark install command. | L45-L55 | [README](agents-remember-md/README.md) |

## Cross-Repo References

No sibling repository evidence is needed for the installer.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-16T12:13+02:00: Documented that benchmark installation ignores source-side generated `workspaces/` and `user-runs/`, prunes installed `workspaces/`, and still preserves installed `user-runs/` across reinstalls.
- 2026-05-16T11:32+02:00: Documented the benchmark installer `.gitignore` guard that adds `benchmarks/` to target coordinator roots when benchmark fixtures are installed plus the Windows long-path/read-only removal adapters used while pruning generated benchmark workspaces.
- 2026-05-15T17:32+02:00: Updated after benchmark install validation switched from committed workspace scaffolds to the generated workspace `AGENTS.md` template and installer copy/prune started ignoring Python bytecode caches. Verification metadata remains pinned to the last committed source state until closeout.
- 2026-05-15T15:50+02:00: Updated after adding opt-in benchmark installation, benchmark tree validation, and `user-runs/` preservation. Verification metadata remains pinned to the last committed source state until closeout.
- 2026-05-15T01:55+02:00: Created with pending verification metadata for the first runtime-layout closeout commit.
- 2026-05-15T03:06+02:00: Corrected installer ownership notes so system defaults remain source-side templates instead of installed runtime files.
