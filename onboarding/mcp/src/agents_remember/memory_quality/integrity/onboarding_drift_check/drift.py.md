# mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/drift.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/drift.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-02T01:05+02:00|
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb` |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Data records and constants. | `DriftRow` | mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/models.py:58-69 |
| Git boundary and fingerprints. | `compute_git_blob_set_fingerprint` | mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/git_ops.py:65-73 |
| Discovery and metadata parsing. | `discover_onboarding_files` | mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/discovery.py:43-48 |
| Sidecar/overview classifiers. | `classify_overview_onboarding`; `classify_sidecar_onboarding_units` | mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/sidecar.py:214-265; mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/sidecar.py:289-342 |
| Entity and inline classifiers. | `classify_entity_fingerprint`; `classify_inline_source` | mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/entities.py:222-280; mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/inline.py:91-175 |
| Report rendering and path resolution. | `write_markdown_report` | mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/report.py:112-173 |
| Summary generation reuses the facade's classifiers. | `run_drift_summary` | mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/summary.py:25-73 |
| The re-exported `run_git` and `main`'s git-repository guard resolve here, not to `git_ops`. | `run_git` | mcp/src/agents_remember/kernel/git_command.py:85-151 |

## Update History

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-04T18:40+02:00 — 260731-EFA-L6 S18-B17 curator: repaired the seven malformed rows with
  exact anchors and plain sources (`DriftRow`, `compute_git_blob_set_fingerprint`,
  `discover_onboarding_files`, the sidecar/overview classifier pair, `write_markdown_report`,
  `run_drift_summary`, `run_git`), and split the pooled "Sidecar/overview and entity/inline
  classifiers" row into two — the entity and inline classifiers live in `entities.py` and
  `inline.py`, not `sidecar.py`. Spurious `agents-remember/` prefixes dropped.
- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-31T20:55+02:00 — 260731-EFA-L3 curator: `run_git` is now imported from
  `kernel.git_command` rather than the sibling `git_ops`, so the facade's re-export (still in
  `__all__`) and `main`'s `rev-parse --show-toplevel` guard resolve to the single owner. Recorded
  that in Logic, noted the runner as the one implementation that lives outside the module list in
  Invariants, and added the `git_command.py` reference row. `__all__` and every classifier are
  unchanged.
- 2026-07-31T00:00+02:00 — 260731-EFA-L2: call-site update only — `main()` now builds a
  `CoordinationHints` for `resolve_coordination_context`. No flag, classifier or report changed.
  Verification metadata pinned until closeout stamps the L2 commit.
- 2026-05-31T12:50+02:00 — Replaced the `sidecar_storage_label` import/re-export with the boolean `is_sidecar_storage` predicate from `coordination_context_resolver` (now used in `classify_source`), and dropped the no-longer-re-exported `is_file_level_onboarding` from the imports and `__all__`; corrected the Conventions note to name `is_sidecar_storage` (1.0.0 review remediation).
- 2026-05-29T18:35+02:00: Extracted `_collect_drift_rows` and `_print_drift_rows` from `main` to reduce complexity; behavior-preserving (commit `e3dab63`).
- 2026-05-29T12:10+02:00: Split into focused modules (`models`, `git_ops`, `discovery`, `entities`, `inline`, `sidecar`, `report`); `drift.py` is now a re-exporting facade with `classify_source` + `main`. Cleared the file-size hard limit, MI rank C, and the drift CRAP offenders. Metadata pending closeout refresh to the split commit.
- 2026-05-24T02:47+02:00: Moved from the top-level `drift` package into `memory_quality.integrity.onboarding_drift_check`.
- 2026-05-23T22:37+02:00: Created during quality-pass closeout after direct-closeout preview found the changed file lacked sidecar onboarding.
