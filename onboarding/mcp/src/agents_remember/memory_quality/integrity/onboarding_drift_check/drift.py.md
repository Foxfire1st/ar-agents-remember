# mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/drift.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/drift.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T00:00+02:00|
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d` |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
| governingOverview      | `../../../../../overview.md`               |

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
text/JSON/CSV). MCP tools call package-level summary/controller code that reuses
the same classifiers.

### Conventions

`__all__` enumerates the re-exported surface so the facade stays an explicit,
backward-compatible boundary. Since 260731-EFA-L2 `main()` passes `--topology` /
`--coordination-root` / `--settings-path` / `--onboarding-root` to
`resolve_coordination_context` inside a `CoordinationHints(...)`, matching the resolver's current
signature; no CLI flag changed. `main()` is the CLI/dev facade; production callers
go through `summary.py` / the MCP controllers. `classify_source` routes to the
external classifier via the shared `is_sidecar_storage` predicate from
`coordination_context_resolver` (re-exported here); the older
`sidecar_storage_label` helper and the no-longer-re-exported
`is_file_level_onboarding` are gone from `__all__`.

### Invariants And Boundaries

- `c-02-memory-quality-control` skill detects and reports drift; it must not rewrite onboarding.
- Implementation responsibilities live in `models`, `git_ops`, `discovery`,
  `entities`, `inline`, `sidecar`, and `report`; this file must stay a facade
  plus `classify_source`/`main` and not re-accumulate logic.
- Public names removed or renamed here are a compatibility break for `baseline`,
  `summary`, and `check_missing_onboarding`, which import from this module.

### Todos

- The 2026-05-29 split cleared the file-size and maintainability pressure and most
  rank-C functions. Three branch-heavy classifiers remain at Radon `C`
  (`sidecar.classify_overview_onboarding`, `main`, `entities.parse_entity_fingerprint_rows`)
  and are tracked for the Tier-3 complexity pass.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Data records and constants. | [models.py](agents-remember/mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/models.py) |
| Git boundary and fingerprints. | [git_ops.py](agents-remember/mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/git_ops.py) |
| Discovery and metadata parsing. | [discovery.py](agents-remember/mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/discovery.py) |
| Sidecar/overview and entity/inline classifiers. | [sidecar.py](agents-remember/mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/sidecar.py) |
| Report rendering and path resolution. | [report.py](agents-remember/mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/report.py) |
| Summary generation reuses the facade's classifiers. | [summary.py](agents-remember/mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/summary.py) |

## Update History

- 2026-07-31T00:00+02:00 — 260731-EFA-L2: call-site update only — `main()` now builds a
  `CoordinationHints` for `resolve_coordination_context`. No flag, classifier or report changed.
  Verification metadata pinned until closeout stamps the L2 commit.
- 2026-05-31T12:50+02:00 — Replaced the `sidecar_storage_label` import/re-export with the boolean `is_sidecar_storage` predicate from `coordination_context_resolver` (now used in `classify_source`), and dropped the no-longer-re-exported `is_file_level_onboarding` from the imports and `__all__`; corrected the Conventions note to name `is_sidecar_storage` (1.0.0 review remediation).
- 2026-05-29T18:35+02:00: Extracted `_collect_drift_rows` and `_print_drift_rows` from `main` to reduce complexity; behavior-preserving (commit `e3dab63`).
- 2026-05-29T12:10+02:00: Split into focused modules (`models`, `git_ops`, `discovery`, `entities`, `inline`, `sidecar`, `report`); `drift.py` is now a re-exporting facade with `classify_source` + `main`. Cleared the file-size hard limit, MI rank C, and the drift CRAP offenders. Metadata pending closeout refresh to the split commit.
- 2026-05-24T02:47+02:00: Moved from the top-level `drift` package into `memory_quality.integrity.onboarding_drift_check`.
- 2026-05-23T22:37+02:00: Created during quality-pass closeout after direct-closeout preview found the changed file lacked sidecar onboarding.
