# run-benchmarks.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `runtime/scripts/run-benchmarks.py`        |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-15T17:32+02:00                     |
| lastVerifiedCommitHash |                                            `e7c1ee4f983a7309d51c05b97f94e27443c3cf90`|
| lastVerifiedCommitDate |                                            2026-05-15T18:10:44+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[overview.md](../../overview.md)

## Purpose

`run-benchmarks.py` is the installed benchmark runner and analyzer for the optional Agents Remember benchmark package. It discovers manifest-defined cases, renders generated benchmark workspace instructions from templates, prepares resettable benchmark workspaces, runs paired `codex exec --json` variants, stores user outputs under `benchmarks/user-runs/`, and generates Markdown summaries from JSONL plus sidecar metadata.

## Code Commentary

### Logic

The script locates the benchmark root from either an installed coordinator or the source checkout, loads every `cases/*/case.json` manifest with schema version `1`, and lets callers select all cases or one case by id. Preparation renders `workspaces/<case-id>/AGENTS.md` from `templates/workspace-AGENTS.md` using case metadata, clones or fetches the case's shared pinned repository checkout under the case workspace `repos/` tree, checks out the manifest commit, resets and cleans the checkout, syncs runtime assets into the case workspace-local `ar-coordination/` root without copying Python bytecode caches, then clones or refreshes the manifest-pinned memory repository under `ar-coordination/memory-repos/`.

Running a case optionally prepares the workspace, creates a unique `user-runs/<case>/<run-id>/` output root, and runs each selected prompt/variant/repetition through `codex exec --json`. The command always uses `--skip-git-repo-check`, `--sandbox danger-full-access`, and `approval_policy="never"` because benchmark prompts must run headlessly. Each run writes JSONL, stderr, and metadata sidecars.

Analysis scans JSONL recursively under a run root, loads sidecar metadata when present, extracts event counts, detected command/tool events, token counters, errors, duration, exit code, and JSONL size, then emits grouped range summaries by prompt and variant.

### Conventions

- Benchmark manifests own code repository URL, memory repository URL, pinned commits, workspace fixture path, shared repo path, coordination root path, prompt paths, and variant CWDs.
- Source benchmark packages own manifests, prompts, author results, docs, and templates. They do not commit generated workspace folders.
- `benchmarks/workspaces/` is a generated resettable fixture area. It is not where user run outputs belong.
- `benchmarks/user-runs/` is the preserved output area for local JSONL, stderr, metadata, and generated summaries.
- Variants are execution modes and result groups; they do not get separate code checkout trees.
- Runtime asset sync excludes `__pycache__`, `.pyc`, and `.pyo` files so local validation artifacts do not become benchmark fixture content.
- The script uses only Python standard-library modules so the installed runtime does not need additional dependencies.

### Invariants And Boundaries

The runner can execute networked `git clone`/`fetch` and expensive Codex runs, so verification should prefer `list`, `prepare --dry-run`, `run --dry-run`, and `analyze` with fixture JSONL unless the developer explicitly wants to spend benchmark tokens.

The analyzer is schema-tolerant rather than schema-authoritative. It keeps the largest observed token counter for known token keys because Codex JSONL streams may contain cumulative usage updates.

The runner renders the workspace root `AGENTS.md` before syncing runtime assets into the benchmark-local coordination root and materializing the pinned memory repo at `ar-coordination/memory-repos/ar-<repo>/`.

### Todos

- Refresh verification metadata after this new runner is committed.
- Extend JSONL parsing if future Codex versions expose richer stable metrics.

### Docs References

No external documentation is needed for the runner itself. The benchmark methodology is documented in-repository.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The benchmark methodology defines paired source-only and onboarding-enabled variants, records raw JSONL/stderr/metadata/summaries, and treats token parsing defensively because JSONL schemas can evolve. | L3-L8; L35-L62 | [benchmark methodology](agents-remember-md/docs/benchmarks-methodology.md) |
| The methodology says source packages commit manifests/prompts/results/templates rather than workspaces; `prepare` generates resettable workspaces, renders the workspace `AGENTS.md`, clones pinned code and memory repos, and keeps user outputs separately under `benchmarks/user-runs/`. | L10-L24 | [benchmark methodology](agents-remember-md/docs/benchmarks-methodology.md) |

## Repo-Internal References

The runner is tied to the benchmark package layout and manifest shape.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The benchmark README defines `cases/`, `templates/`, generated resettable `workspaces/`, preserved `user-runs/`, the install command, and the current draft case. | L1-L30 | [benchmark README](agents-remember-md/benchmarks/README.md) |
| The benchmark README says memory repos are pinned in manifests and cloned during preparation instead of vendored under `cases/<case>/memory/`; generated workspaces and `user-runs/` stay out of onboarding. | L32-L69 | [benchmark README](agents-remember-md/benchmarks/README.md) |
| The draft case manifest pins the code repository URL/commit, memory repository URL/commit, file-count scope, workspace fixture path, shared repo path, coordination root, prompt variants, and author result location. | L1-L53 | [case manifest](agents-remember-md/benchmarks/cases/agents-remember-md-drift-workflow/case.json) |
| The workspace instruction template carries placeholders for case id, target repository name, target checkout, coordination root, and memory repository name; the runner replaces those placeholders when preparing a case workspace. | L1-L14 | [workspace AGENTS template](agents-remember-md/benchmarks/templates/workspace-AGENTS.md) |
| The runner discovers benchmark roots, loads schema-versioned case manifests, and selects all cases or one requested case id. | L78-L119 | [benchmark runner](agents-remember-md/runtime/scripts/run-benchmarks.py) |
| Workspace preparation renders the workspace `AGENTS.md`, clones or fetches one shared pinned code checkout, syncs runtime assets while ignoring Python bytecode caches, clones or fetches the pinned memory repo, and verifies the workspace memory repo path. | L40-L45; L159-L304 | [benchmark runner](agents-remember-md/runtime/scripts/run-benchmarks.py) |
| Run execution builds the `codex exec --json` command, writes JSONL/stderr/metadata artifacts, defaults to manifest repetitions, and stores output under `user-runs`. | L331-L456 | [benchmark runner](agents-remember-md/runtime/scripts/run-benchmarks.py) |
| Analysis extracts JSONL metrics and writes grouped Markdown summaries with metric ranges and per-run detail rows. | L459-L617 | [benchmark runner](agents-remember-md/runtime/scripts/run-benchmarks.py) |
| The CLI exposes `list`, `prepare`, `run`, and `analyze` commands with dry-run and selection options. | L620-L718 | [benchmark runner](agents-remember-md/runtime/scripts/run-benchmarks.py) |

## Cross-Repo References

The draft case points at a GitHub repository URL for cloning, but this onboarding file does not rely on a sibling repository checkout.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No sibling-repository boundary evidence is required for the runner implementation. | n/a | n/a |

## Update History

- 2026-05-15T17:32+02:00: Updated after workspace `AGENTS.md` generation moved to `templates/workspace-AGENTS.md`, source-side empty workspaces were removed, and runtime asset sync started ignoring Python bytecode caches. Verification metadata remains blank until the new source file is committed.
- 2026-05-15T15:50+02:00: Created onboarding for the new benchmark runner and analyzer. Verification metadata is intentionally blank until the new source file is committed.
