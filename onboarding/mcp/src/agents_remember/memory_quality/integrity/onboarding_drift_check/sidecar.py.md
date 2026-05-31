# mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/sidecar.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/sidecar.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-31T12:50+02:00|
| lastVerifiedCommitHash | `c20a3292e667d227a3be0c1fb276f8a701df814f` |
| lastVerifiedCommitDate | 2026-05-31T14:17:11+02:00|
| governingOverview      | `../../../../../overview.md`               |

## Purpose

`sidecar.py` classifies file-level sidecar onboarding and repo/route overview
onboarding against the current source tree, routing entity-catalog sidecars to
`entities.py`.

## Code Commentary

### Logic

`classify_external_onboarding` compares a source file against its recorded
`lastVerifiedCommitHash` (handling missing source, missing commit, clean, and
drifted cases); `classify_overview_onboarding` does the same for repo/route
overviews by `sourceRoute`; `classify_external_source` maps a source to its
mirrored sidecar; `classify_sidecar_onboarding_units` dispatches by `doc_type`
(overview / entity-catalog / file-level) and storage mode.

### Invariants And Boundaries

- Reports drift only; it must not rewrite onboarding.
- `disabled` (path-rule excluded) and non-sidecar storage modes are reported
  explicitly rather than treated as drift; the sidecar test uses the boolean
  `is_sidecar_storage` predicate from `coordination_context_resolver`.
- Entity-catalog classification is delegated to `entities.classify_entity_catalog`.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Metadata parsing, path mirroring, and `rel` come from `discovery`. | [discovery.py](agents-remember-md/mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/discovery.py) |
| Source diff and change notes come from `git_ops`; entity catalogs are delegated to `entities`. | [entities.py](agents-remember-md/mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/entities.py) |

## Update History

- 2026-05-31T12:50+02:00 — `classify_sidecar_onboarding_units` now gates non-sidecar storage via the boolean `is_sidecar_storage` predicate instead of the removed `sidecar_storage_label` helper (both imported from `coordination_context_resolver`); corrected the Invariants note to name `is_sidecar_storage` (1.0.0 review remediation).
- 2026-05-29T18:35+02:00: Extracted an `_early_classification` closure in `classify_overview_onboarding` to reduce complexity; behavior-preserving (commit `e3dab63`).
- 2026-05-29T12:10+02:00: Created when `drift.py` was split into focused modules; the unused `classify_sidecar_onboarding` aggregator was dropped during the split. Metadata pending closeout refresh to the split commit.
