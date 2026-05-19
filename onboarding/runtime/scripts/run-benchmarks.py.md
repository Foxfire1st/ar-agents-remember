# run-benchmarks.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `runtime/scripts/run-benchmarks.py`        |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-18T22:01+02:00                     |
| lastVerifiedCommitHash |                                            `5b26015bb3e9deec8113b1a69a12608bba82cc27`|
| lastVerifiedCommitDate |                                            2026-05-19T03:27:34+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[overview.md](../../overview.md)

## Purpose

`run-benchmarks.py` is the installed benchmark runner and analyzer for the optional Agents Remember benchmark package. It discovers manifest-defined cases, renders generated benchmark workspace instructions from templates, prepares resettable benchmark workspaces, runs paired `codex exec --json` variants, stores JSONL/stderr/final-message/metadata outputs under `benchmarks/user-runs/`, and generates Markdown summaries from JSONL plus sidecar metadata.

## Code Commentary

### Logic

The script locates the benchmark root from either an installed coordinator or the source checkout, loads every `cases/*/case.json` manifest with schema version `1`, validates all manifest-controlled paths before using them, and lets callers select all cases or one case by id. Preparation creates one source-only environment and one memory-enabled environment under `workspaces/<case-id>/`. Both environments receive a `.benchmark-root` marker for Codex project-root detection. The source-only environment receives a rendered `source-only/AGENTS.md` from `templates/source-only-AGENTS.md` plus a pinned repository checkout under `source-only/repos/`. The memory-enabled environment receives the same pinned repository checkout under `with-memory/repos/`, a rendered `with-memory/AGENTS.md` from `templates/workspace-AGENTS.md`, synced runtime assets under `with-memory/ar-coordination/`, benchmark skill exposure under `with-memory/.agents/skills/agents-remember-md`, and the manifest-pinned memory repository under `with-memory/ar-coordination/memory-repos/`.

Repository preparation wraps git calls with `core.longpaths=true`. Existing generated checkouts are treated as reusable caches: if the manifest-pinned commit is already present locally, preparation skips clone and fetch, then still checks out, resets, and cleans the worktree to keep fixtures deterministic. If the pinned commit is missing, preparation fetches before checkout. Callers can pass `--force-clone` on `prepare` or `run` to discard existing code and memory repository checkouts before cloning. Generated tree replacement and legacy workspace pruning use an extended-path and read-only retry strategy, while preserving symlink paths rather than resolving through them before deletion. Windows directory symlinks and junctions are removed with directory-link semantics so repeated `prepare` runs can clean stale `.agents/skills/agents-remember-md` links without touching the linked runtime skill tree.

Skill exposure defaults to `auto`: it tries the existing shell-backed symlink installer when available, then falls back to a Python-native directory copy if Bash, the shell script, or symlink creation is unavailable. Callers can force `link`, `copy`, or `none` with `--skill-exposure-mode` on `prepare` and `run`.

Running a case optionally prepares the workspace, creates one unique `user-runs/<case>/<run-id>/` output root, and builds selected prompt/variant/repetition tasks by repetition so paired variants for the same prompt run land under the same dated entry. Dry-run mode prints the planned files and commands sequentially for auditability. Real runs submit the tasks to a `ThreadPoolExecutor`; default concurrency is the number of selected variants, and `--jobs` can override it. On Windows, the runner resolves the default `codex` command to an executable shim such as `codex.cmd` or `codex.exe` before launching it with `subprocess.run`. The command always uses `--ephemeral`, `--skip-git-repo-check`, `--sandbox danger-full-access`, `--output-last-message`, project-root marker configuration, and `approval_policy="never"` because benchmark prompts must run headlessly and stay isolated to generated fixture roots. Each run writes JSONL, stderr, final-message, and metadata sidecars.

Analysis scans JSONL recursively under a run root, loads sidecar metadata when present, extracts event counts, detected command/tool events, token counters, errors, duration, exit code, and JSONL size, then emits grouped range summaries by prompt and variant.

### Conventions

- Benchmark manifests own code repository URL, memory repository URL, pinned commits, workspace fixture path, source-only root, memory-enabled root, repo path within each environment, coordination root path, prompt paths, and variant CWDs.
- Manifest path fields must be string relative paths contained within the benchmark root. Non-string values, empty paths, absolute POSIX paths, drive-qualified Windows paths, and parent-directory escapes are rejected before workspace writes.
- Source benchmark packages own manifests, prompts, author results, docs, and templates. They do not commit generated workspace folders.
- `benchmarks/workspaces/` is a generated resettable fixture area. It is not where user run outputs belong.
- `benchmarks/user-runs/` is the preserved output area for local JSONL, stderr, final-message text, metadata, and generated summaries.
- `--skill-exposure-mode copy` is the most portable preparation mode for Windows hosts without Bash or symlink privileges; `auto` is the default compatibility mode for normal use. Repeated prepares must remove stale directory symlinks as links, not as their resolved target directories.
- `--force-clone` is the explicit opt-in for throwing away cached benchmark repository checkouts; normal preparation reuses existing checkouts when the pinned commit is already available locally.
- Variants are execution modes and result groups. They select a prepared environment root, but the runner keeps the environment set fixed to source-only and memory-enabled roots instead of creating one workspace per prompt variant.
- `run` creates one dated output root per case invocation; paired `no-onboarding` and `with-onboarding` variants should appear under that same root for each repetition.
- `--jobs` controls the maximum concurrent Codex runs. If omitted, concurrency defaults to the number of selected variants so the paired benchmark variants run together.
- Runtime asset sync excludes `__pycache__`, `.pyc`, and `.pyo` files so local validation artifacts do not become benchmark fixture content.
- The script uses only Python standard-library modules so the installed runtime does not need additional dependencies.

### Invariants And Boundaries

The runner can execute networked `git clone`/`fetch` and expensive Codex runs, so verification should prefer `list`, `prepare --dry-run`, `run --dry-run`, and `analyze` with fixture JSONL unless the developer explicitly wants to spend benchmark tokens.

Manifest validation is a security and portability boundary. A case manifest must not be able to redirect preparation into an absolute host path or escape the benchmark workspace with `..`.

The analyzer is schema-tolerant rather than schema-authoritative. It keeps the largest observed token counter for known token keys because Codex JSONL streams may contain cumulative usage updates.

The runner renders environment-specific `AGENTS.md` files into both generated environments. The source-only template blocks parent workspace instructions and treats the checked-out repository's `AGENTS.md` as source content only. The memory-enabled template reads the benchmark-local coordination root, syncs runtime assets there, exposes the installed benchmark skills for nested benchmark agents, and materializes the pinned memory repo at `with-memory/ar-coordination/memory-repos/ar-<repo>/`.

Run failures are aggregated after all submitted tasks finish. A subprocess launch or execution exception in one variant must not prevent the other submitted variant runs from completing and being included in the summary.

### Todos

- Refresh verification metadata after the benchmark checkout cache change is committed.
- Extend JSONL parsing if future Codex versions expose richer stable metrics.

### Docs References

No external documentation is needed for the runner itself. The benchmark methodology is documented in-repository.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The benchmark methodology defines paired source-only and onboarding-enabled variants, records raw JSONL/stderr/final-message/metadata/summaries, and treats token parsing defensively because JSONL schemas can evolve. | L3-L8; L37-L64 | [benchmark methodology](agents-remember-md/benchmarks/docs/benchmarks-methodology.md) |
| The methodology says source packages commit manifests/prompts/results/templates rather than workspaces; `prepare` generates resettable source-only and memory-enabled environments with benchmark root markers, harness `AGENTS.md` files, and portable skill exposure, while keeping user outputs separately under `benchmarks/user-runs/`. | L10-L24 | [benchmark methodology](agents-remember-md/benchmarks/docs/benchmarks-methodology.md) |

## Repo-Internal References

The runner is tied to the benchmark package layout and manifest shape.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The benchmark README defines `cases/`, `templates/`, generated resettable `workspaces/`, preserved `user-runs/`, the install command, the current draft case, and the paired `source-only/` plus `with-memory/` generated workspace layout including root markers, rendered templates, final-message output files, and portable skill exposure. | L1-L30; L32-L81 | [benchmark README](agents-remember-md/benchmarks/README.md) |
| The benchmark methodology says `prepare` generates source-only and memory-enabled environments, keeps user outputs under `benchmarks/user-runs/`, and treats generated workspaces as excluded benchmark state. | L3-L8; L22-L24 | [benchmark methodology](agents-remember-md/benchmarks/docs/benchmarks-methodology.md) |
| The draft case manifest pins the code repository URL/commit, memory repository URL/commit, file-count scope, workspace fixture path, source-only root, memory-enabled root, shared repo-relative path inside each environment, coordination root, prompt variant CWDs, and author result location. | L1-L55 | [case manifest](agents-remember-md/benchmarks/cases/agents-remember-md-drift-workflow/case.json) |
| The source-only instruction template marks the source-only fixture root as isolated, fills in case/repo placeholders, tells the agent to use source evidence only, and prevents following the checked-out repository's `AGENTS.md` as active instructions. | L3-L22 | [source-only AGENTS template](agents-remember-md/benchmarks/templates/source-only-AGENTS.md) |
| The memory-enabled instruction template marks the fixture root as isolated, reads the benchmark-local coordination root, fills in case/repo/memory placeholders, and repeats non-interactive execution discipline. | L3-L24 | [workspace AGENTS template](agents-remember-md/benchmarks/templates/workspace-AGENTS.md) |
| The runner rejects non-string, absolute, drive-qualified, empty, and parent-escaping manifest paths before loading a case for later workspace writes. | L55-L95; L157 | [benchmark runner](agents-remember-md/runtime/scripts/run-benchmarks.py) |
| Repository preparation uses long-path-aware git commands, reuses existing checkouts when the pinned commit is present, fetches only when that commit is absent, and lets callers opt into deleting cached checkouts with `force_clone`. | L482-L518; L639-L675 | [benchmark runner](agents-remember-md/runtime/scripts/run-benchmarks.py) |
| Workspace preparation renders both source-only and memory-enabled templates, writes benchmark root markers, and uses Windows-safe removal helpers for generated tree replacement, read-only files, stale directory symlinks, and legacy generated workspace pruning. | L224-L278; L583-L618; L628-L675 | [benchmark runner](agents-remember-md/runtime/scripts/run-benchmarks.py) |
| The memory-enabled workspace exposes benchmark skills through `auto`, `link`, `copy`, or `none`; `auto` falls back to Python-native copying when the shell-backed symlink path is unavailable, and stale skill links are cleaned without resolving into their targets. | L405-L470; L674 | [benchmark runner](agents-remember-md/runtime/scripts/run-benchmarks.py) |
| Manifest-owned workspace roots, repository-relative paths, coordination roots, prompt paths, and variant CWDs all pass through the path validator before being joined to local roots. | L525-L562; L774-L780 | [benchmark runner](agents-remember-md/runtime/scripts/run-benchmarks.py) |
| Run execution resolves Windows command shims before building the `codex exec --json` command with ephemeral mode, benchmark root marker configuration, stdin prompt delivery, and final-message capture, then writes JSONL/stderr/final-message/metadata artifacts under `user-runs`. | L727-L834 | [benchmark runner](agents-remember-md/runtime/scripts/run-benchmarks.py) |
| Case execution creates one output root, queues prompt/variant/repetition tasks by repetition, dry-runs planned runs sequentially, executes real runs through a bounded `ThreadPoolExecutor`, writes a summary, and raises an aggregated error if submitted runs failed. | L841-L925 | [benchmark runner](agents-remember-md/runtime/scripts/run-benchmarks.py) |
| The CLI exposes `list`, `prepare`, `run`, and `analyze` commands with dry-run and selection options, including `--jobs` for run concurrency, `--skill-exposure-mode` for preparation portability, and `--force-clone` when a fresh clone is required. | L1087-L1196 | [benchmark runner](agents-remember-md/runtime/scripts/run-benchmarks.py) |
| The draft case prompts explicitly mark benchmark runs as non-interactive, put completion criteria before the primary task, and tell the agent to complete the same drift-workflow explanation from source-only or source-plus-memory evidence. | L5-L22; L5-L23 | [no-onboarding prompt](agents-remember-md/benchmarks/cases/agents-remember-md-drift-workflow/prompts/explain-drift-workflow.no-onboarding.md); [with-onboarding prompt](agents-remember-md/benchmarks/cases/agents-remember-md-drift-workflow/prompts/explain-drift-workflow.with-onboarding.md) |

## Cross-Repo References

The draft case points at a GitHub repository URL for cloning, but this onboarding file does not rely on a sibling repository checkout.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No sibling-repository boundary evidence is required for the runner implementation. | n/a | n/a |

## Update History

- 2026-05-18T22:01+02:00: Updated after benchmark repository preparation started reusing cached checkouts for unchanged pinned commits and added `--force-clone` as the explicit fresh-clone override.
- 2026-05-16T20:14+02:00: Updated after fixing Windows benchmark rerun failures by deleting stale directory symlinks without following them and resolving the default `codex` command to `codex.cmd`/`codex.exe` before subprocess launch.
- 2026-05-16T20:07+02:00: Refreshed closeout documentation after benchmark docs and prompts were aligned with source-only `AGENTS.md`, benchmark root markers, final-message capture, and auto/copy skill exposure behavior.
- 2026-05-16T19:52+02:00: Updated after benchmark runner portability work added manifest path validation, Windows-safe generated tree removal, Python-native benchmark skill exposure copying, and `--skill-exposure-mode` on `prepare` and `run`.
- 2026-05-16T18:39+02:00: Updated after benchmark runs switched to one dated output root with paired variants scheduled by repetition, bounded parallel execution, `--jobs` concurrency control, aggregate run-failure reporting, and non-interactive prompt discipline for the drift workflow case.
- 2026-05-16T12:09+02:00: Updated after benchmark preparation moved to paired `source-only/` and `with-memory/` environment roots, and after git preparation became long-path-aware and recovery-safe for interrupted generated checkouts. Verification metadata should be refreshed after the source change is committed.
- 2026-05-15T17:32+02:00: Updated after workspace `AGENTS.md` generation moved to `templates/workspace-AGENTS.md`, source-side empty workspaces were removed, and runtime asset sync started ignoring Python bytecode caches. Verification metadata remains blank until the new source file is committed.
- 2026-05-15T15:50+02:00: Created onboarding for the new benchmark runner and analyzer. Verification metadata is intentionally blank until the new source file is committed.
