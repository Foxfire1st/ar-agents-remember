# mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/drift.py

## Governing Overview

[overview.md](../../../../../overview.md)

## Purpose

`drift.py` is the thin facade for the package-local `c-02-memory-quality-control` skill drift classifier. It
keeps the orchestration entry point and CLI here and re-exports the public names
so existing imports keep working, while the implementation lives in focused
sibling modules.

## Code Commentary

### Logic

The module re-exports the package's public surface (models/constants, git
helpers, discovery, entity/inline/sidecar classifiers, and report renderers) and
keeps two things local: `classify_source` (routes one source path to the right
classifier by storage mode) and `main` (the CLI/dev entry point that resolves
context, discovers onboarding, classifies, writes the report, and prints
text/JSON/CSV). MCP tools call package-level summary/application code that reuses
the same classifiers.

Since 260731-EFA-L3 one re-exported name is no longer package-local: `run_git` is imported from
`agents_remember.kernel.git_command` (the single owner) instead of from the sibling `git_ops`. It is
still listed in `__all__`, so `drift.run_git` keeps resolving — now to the one runner. `main` is the
only local caller: `git_check = run_git(code_repository_root, ["rev-parse", "--show-toplevel"])`,
the guard that rejects a `--code-repository-root` that is not a git repository. That guard is exactly
the kind of call the consolidation matters for, since it now runs with the repository selectors
scrubbed rather than answering out of whatever `GIT_DIR` names.

### Conventions

`__all__` enumerates the re-exported surface so the facade stays an explicit,
backward-compatible boundary. Since 260731-EFA-L2 `main()` passes `--topology` /
`--coordination-root` / `--settings-path` / `--onboarding-root` to
`resolve_coordination_context` inside a `CoordinationHints(...)`, matching the resolver's current
signature; no CLI flag changed. `main()` is the CLI/dev facade; production callers
go through `summary.py` / the MCP application entry points. `classify_source` routes to the
external classifier via the shared `is_sidecar_storage` predicate from
`coordination_context_resolver` (re-exported here); the older
`sidecar_storage_label` helper and the no-longer-re-exported
`is_file_level_onboarding` are gone from `__all__`.

### Invariants And Boundaries

- `c-02-memory-quality-control` skill detects and reports drift; it must not rewrite onboarding.
- Implementation responsibilities live in `models`, `git_ops`, `discovery`,
  `entities`, `inline`, `sidecar`, and `report`; this file must stay a facade
  plus `classify_source`/`main` and not re-accumulate logic. The git subprocess runner is the one
  re-exported name that lives outside the package, in `kernel.git_command`.
- Public names removed or renamed here are a compatibility break for `baseline`,
  `summary`, and `check_missing_onboarding`, which import from this module.

### Todos

- The 2026-05-29 split cleared the file-size and maintainability pressure and most
  rank-C functions. Three branch-heavy classifiers remain at Radon `C`
  (`sidecar.classify_overview_onboarding`, `main`, `entities.parse_entity_fingerprint_rows`)
  and are tracked for the Tier-3 complexity pass.

## Evidence

### Repo-Internal References

- Data records and constants. [1]
- Git boundary and fingerprints. [2]
- Discovery and metadata parsing. [3]
- Sidecar/overview classifiers. [4]
- Entity and inline classifiers. [5]
- Report rendering and path resolution. [6]
- Summary generation reuses the facade's classifiers. [7]
- The re-exported `run_git` and `main`'s git-repository guard resolve here, not to `git_ops`. [8]
