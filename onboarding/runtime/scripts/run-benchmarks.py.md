# run-benchmarks.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `runtime/scripts/run-benchmarks.py`        |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-16T12:09+02:00                     |
| lastVerifiedCommitHash |                                            `032a5b839c5c7a0f8e487fe65f5b060e11a9b8a2`|
| lastVerifiedCommitDate |                                            2026-05-16T18:07:23+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[overview.md](../../overview.md)

## Purpose

`run-benchmarks.py` is the installed benchmark runner and analyzer for the optional Agents Remember benchmark package. It discovers manifest-defined cases, renders generated benchmark workspace instructions from templates, prepares resettable benchmark workspaces, runs paired `codex exec --json` variants, stores user outputs under `benchmarks/user-runs/`, and generates Markdown summaries from JSONL plus sidecar metadata.

## Code Commentary

### Logic

The script locates the benchmark root from either an installed coordinator or the source checkout, loads every `cases/*/case.json` manifest with schema version `1`, and lets callers select all cases or one case by id. Preparation creates one source-only environment and one memory-enabled environment under `workspaces/<case-id>/`. The source-only environment receives only a pinned repository checkout under `source-only/repos/`. The memory-enabled environment receives the same pinned repository checkout under `with-memory/repos/`, a rendered `with-memory/AGENTS.md` from `templates/workspace-AGENTS.md`, synced runtime assets under `with-memory/ar-coordination/`, and the manifest-pinned memory repository under `with-memory/ar-coordination/memory-repos/`.

Repository preparation wraps git calls with `core.longpaths=true` and cleans existing generated checkouts before checkout, which keeps Windows benchmark paths usable and lets a later prepare recover from an interrupted or partially failed clone.

Running a case optionally prepares the workspace, creates a unique `user-runs/<case>/<run-id>/` output root, and runs each selected prompt/variant/repetition through `codex exec --json`. The command always uses `--skip-git-repo-check`, `--sandbox danger-full-access`, and `approval_policy="never"` because benchmark prompts must run headlessly. Each run writes JSONL, stderr, and metadata sidecars.

Analysis scans JSONL recursively under a run root, loads sidecar metadata when present, extracts event counts, detected command/tool events, token counters, errors, duration, exit code, and JSONL size, then emits grouped range summaries by prompt and variant.

### Conventions

- Benchmark manifests own code repository URL, memory repository URL, pinned commits, workspace fixture path, source-only root, memory-enabled root, repo path within each environment, coordination root path, prompt paths, and variant CWDs.
- Source benchmark packages own manifests, prompts, author results, docs, and templates. They do not commit generated workspace folders.
- `benchmarks/workspaces/` is a generated resettable fixture area. It is not where user run outputs belong.
- `benchmarks/user-runs/` is the preserved output area for local JSONL, stderr, metadata, and generated summaries.
- Variants are execution modes and result groups. They select a prepared environment root, but the runner keeps the environment set fixed to source-only and memory-enabled roots instead of creating one workspace per prompt variant.
- Runtime asset sync excludes `__pycache__`, `.pyc`, and `.pyo` files so local validation artifacts do not become benchmark fixture content.
- The script uses only Python standard-library modules so the installed runtime does not need additional dependencies.

### Invariants And Boundaries

The runner can execute networked `git clone`/`fetch` and expensive Codex runs, so verification should prefer `list`, `prepare --dry-run`, `run --dry-run`, and `analyze` with fixture JSONL unless the developer explicitly wants to spend benchmark tokens.

The analyzer is schema-tolerant rather than schema-authoritative. It keeps the largest observed token counter for known token keys because Codex JSONL streams may contain cumulative usage updates.

The runner renders `AGENTS.md` only inside the memory-enabled environment before syncing runtime assets into that environment's benchmark-local coordination root and materializing the pinned memory repo at `with-memory/ar-coordination/memory-repos/ar-<repo>/`. The source-only environment intentionally has no generated benchmark `AGENTS.md` or `ar-coordination/` root.

### Todos

- Refresh verification metadata after this new runner is committed.
- Extend JSONL parsing if future Codex versions expose richer stable metrics.

### Docs References

No external documentation is needed for the runner itself. The benchmark methodology is documented in-repository.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The benchmark methodology defines paired source-only and onboarding-enabled variants, records raw JSONL/stderr/metadata/summaries, and treats token parsing defensively because JSONL schemas can evolve. | L3-L8; L37-L64 | [benchmark methodology](agents-remember-md/benchmarks/docs/benchmarks-methodology.md) |
| The methodology says source packages commit manifests/prompts/results/templates rather than workspaces; `prepare` generates resettable source-only and memory-enabled environments, and keeps user outputs separately under `benchmarks/user-runs/`. | L10-L24 | [benchmark methodology](agents-remember-md/benchmarks/docs/benchmarks-methodology.md) |

## Repo-Internal References

The runner is tied to the benchmark package layout and manifest shape.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The benchmark README defines `cases/`, `templates/`, generated resettable `workspaces/`, preserved `user-runs/`, the install command, the current draft case, and the paired `source-only/` plus `with-memory/` generated workspace layout. | L1-L30; L32-L71 | [benchmark README](agents-remember-md/benchmarks/README.md) |
| The benchmark methodology says `prepare` generates source-only and memory-enabled environments, keeps user outputs under `benchmarks/user-runs/`, and treats generated workspaces as excluded benchmark state. | L3-L8; L22-L24 | [benchmark methodology](agents-remember-md/benchmarks/docs/benchmarks-methodology.md) |
| The draft case manifest pins the code repository URL/commit, memory repository URL/commit, file-count scope, workspace fixture path, source-only root, memory-enabled root, shared repo-relative path inside each environment, coordination root, prompt variant CWDs, and author result location. | L1-L55 | [case manifest](agents-remember-md/benchmarks/cases/agents-remember-md-drift-workflow/case.json) |
| The workspace instruction template carries placeholders for case id, target repository name, target checkout, coordination root, and memory repository name; the runner replaces those placeholders when preparing a case workspace. | L1-L14 | [workspace AGENTS template](agents-remember-md/benchmarks/templates/workspace-AGENTS.md) |
| The runner discovers benchmark roots, loads schema-versioned case manifests, and selects all cases or one requested case id. | L78-L119 | [benchmark runner](agents-remember-md/runtime/scripts/run-benchmarks.py) |
| Workspace preparation uses long-path-aware git commands, cleans existing generated checkouts before checkout, resolves `source-only` and `with-memory` environment roots, prunes legacy top-level workspace paths, renders `AGENTS.md` only in the memory-enabled root, prepares both pinned source checkouts, syncs runtime assets, and clones or refreshes the pinned memory repo under the memory-enabled coordination root. | L213-L231; L234-L347 | [benchmark runner](agents-remember-md/runtime/scripts/run-benchmarks.py) |
| Run execution builds the `codex exec --json` command, writes JSONL/stderr/metadata artifacts, defaults to manifest repetitions, and stores output under `user-runs`. | L377-L461 | [benchmark runner](agents-remember-md/runtime/scripts/run-benchmarks.py) |
| Analysis extracts JSONL metrics and writes grouped Markdown summaries with metric ranges and per-run detail rows. | L493-L651 | [benchmark runner](agents-remember-md/runtime/scripts/run-benchmarks.py) |
| The CLI exposes `list`, `prepare`, `run`, and `analyze` commands with dry-run and selection options. | L666-L750 | [benchmark runner](agents-remember-md/runtime/scripts/run-benchmarks.py) |

## Cross-Repo References

The draft case points at a GitHub repository URL for cloning, but this onboarding file does not rely on a sibling repository checkout.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No sibling-repository boundary evidence is required for the runner implementation. | n/a | n/a |

## Update History

- 2026-05-16T12:09+02:00: Updated after benchmark preparation moved to paired `source-only/` and `with-memory/` environment roots, and after git preparation became long-path-aware and recovery-safe for interrupted generated checkouts. Verification metadata should be refreshed after the source change is committed.
- 2026-05-15T17:32+02:00: Updated after workspace `AGENTS.md` generation moved to `templates/workspace-AGENTS.md`, source-side empty workspaces were removed, and runtime asset sync started ignoring Python bytecode caches. Verification metadata remains blank until the new source file is committed.
- 2026-05-15T15:50+02:00: Created onboarding for the new benchmark runner and analyzer. Verification metadata is intentionally blank until the new source file is committed.
