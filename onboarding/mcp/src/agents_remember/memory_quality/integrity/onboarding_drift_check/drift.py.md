# mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/drift.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/drift.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-29T18:35+02:00|
| lastVerifiedCommitHash | `01f503dcba3a6eacc1587941f6a89fce0bcc72a2` |
| lastVerifiedCommitDate | 2026-05-29T18:32:57+02:00|
| governingOverview      | `../../../../../overview.md`               |

## Purpose

`drift.py` is the thin facade for the package-local C-02 drift classifier. It
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
backward-compatible boundary. `main()` is the CLI/dev facade; production callers
go through `summary.py` / the MCP controllers.

### Invariants And Boundaries

- C-02 detects and reports drift; it must not rewrite onboarding.
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
| Data records and constants. | [models.py](agents-remember-md/mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/models.py) |
| Git boundary and fingerprints. | [git_ops.py](agents-remember-md/mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/git_ops.py) |
| Discovery and metadata parsing. | [discovery.py](agents-remember-md/mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/discovery.py) |
| Sidecar/overview and entity/inline classifiers. | [sidecar.py](agents-remember-md/mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/sidecar.py) |
| Report rendering and path resolution. | [report.py](agents-remember-md/mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/report.py) |
| Summary generation reuses the facade's classifiers. | [summary.py](agents-remember-md/mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/summary.py) |

## Update History

- 2026-05-29T18:35+02:00: Extracted `_collect_drift_rows` and `_print_drift_rows` from `main` to reduce complexity; behavior-preserving (commit `e3dab63`).
- 2026-05-29T12:10+02:00: Split into focused modules (`models`, `git_ops`, `discovery`, `entities`, `inline`, `sidecar`, `report`); `drift.py` is now a re-exporting facade with `classify_source` + `main`. Cleared the file-size hard limit, MI rank C, and the drift CRAP offenders. Metadata pending closeout refresh to the split commit.
- 2026-05-24T02:47+02:00: Moved from the top-level `drift` package into `memory_quality.integrity.onboarding_drift_check`.
- 2026-05-23T22:37+02:00: Created during quality-pass closeout after direct-closeout preview found the changed file lacked sidecar onboarding.
