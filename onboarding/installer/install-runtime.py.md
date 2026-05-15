# installer/install-runtime.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `installer/install-runtime.py`             |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-15T17:32+02:00                     |
| lastVerifiedCommitHash | `e7c1ee4f983a7309d51c05b97f94e27443c3cf90`         |
| lastVerifiedCommitDate | 2026-05-15T18:10:44+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[overview.md](../overview.md)

## Purpose

`install-runtime.py` is the checkout entrypoint for installing package-owned runtime mechanics into a target `ar-coordination` root. It now also owns the opt-in benchmark package install when callers pass `--include-benchmarks`.

## Code Commentary

### Logic

The installer reconciles package-owned runtime directories by pruning stale files from installed `skills/` and `scripts`, then copying the current runtime skill tree, runtime scripts, and four runtime `AGENTS.md` templates. It skips Python bytecode caches while pruning and copying so local validation artifacts do not become installed package content. It creates missing user-owned coordinator folders but does not run repo onboarding bootstrap, copy settings defaults, or overwrite live memory, task, note, worktree, temp, or settings content. `runtime/system/defaults/` remains checkout template material for initialization skills rather than installed coordinator state.

Benchmark installation is opt-in. When `--include-benchmarks` is present, the installer validates the source `benchmarks/` tree, including the workspace `AGENTS.md` template, reconciles it into `ar-coordination/benchmarks/`, and preserves the `user-runs/` subtree so local benchmark outputs survive reinstall. Benchmark workspaces are generated resettable state rather than committed source package folders, so rerunning the installer can prune stale prepared workspaces while leaving user run outputs intact. Pinned code and memory repositories are not vendored into the source package; the benchmark runner materializes them during `prepare`.

### Conventions

- Regular installs keep the prior runtime-only behavior.
- `--include-benchmarks` installs package-owned benchmark definitions, prompts, workspace templates, author result artifacts, and benchmark docs.
- Only `ar-coordination/benchmarks/user-runs/` is preserved inside the benchmark package.
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
| The benchmark methodology says source packages commit manifests/prompts/results/templates rather than workspaces; `prepare` generates resettable workspaces, clones pinned code and memory repos, and keeps user outputs under `benchmarks/user-runs/`. | L10-L24 | [benchmark methodology](agents-remember-md/docs/benchmarks-methodology.md) |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The installer summary reports copied, unchanged, replaced-link, removed, and created-directory counts. | L25-L40 | [installer](agents-remember-md/installer/install-runtime.py) |
| Runtime installation prunes and copies skills/scripts while ignoring Python bytecode caches, installs four `AGENTS.md` templates, and creates user-owned coordinator folders. | L14-L22; L92-L130; L166-L193 | [installer](agents-remember-md/installer/install-runtime.py) |
| Benchmark installation requires `README.md`, `cases/`, and `templates/workspace-AGENTS.md`, preserves `user-runs/`, and copies package-owned benchmark content into `ar-coordination/benchmarks/` with the same ignored-cache filtering. | L145-L163 | [installer](agents-remember-md/installer/install-runtime.py) |
| The CLI exposes `--include-benchmarks` and prints a benchmark package install line only when that flag is used. | L196-L228 | [installer](agents-remember-md/installer/install-runtime.py) |
| The root README documents normal runtime installation and the optional benchmark install command. | L45-L55 | [README](agents-remember-md/README.md) |

## Cross-Repo References

No sibling repository evidence is needed for the installer.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-15T17:32+02:00: Updated after benchmark install validation switched from committed workspace scaffolds to the generated workspace `AGENTS.md` template and installer copy/prune started ignoring Python bytecode caches. Verification metadata remains pinned to the last committed source state until closeout.
- 2026-05-15T15:50+02:00: Updated after adding opt-in benchmark installation, benchmark tree validation, and `user-runs/` preservation. Verification metadata remains pinned to the last committed source state until closeout.
- 2026-05-15T01:55+02:00: Created with pending verification metadata for the first runtime-layout closeout commit.
- 2026-05-15T03:06+02:00: Corrected installer ownership notes so system defaults remain source-side templates instead of installed runtime files.
