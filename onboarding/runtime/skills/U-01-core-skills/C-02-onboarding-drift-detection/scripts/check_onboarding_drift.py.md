# check_onboarding_drift.py

| Field                  | Value                                                                                       |
| ---------------------- | ------------------------------------------------------------------------------------------- |
| repository             | agents-remember-md                                                                          |
| path                   | `runtime/skills/U-01-core-skills/C-02-onboarding-drift-detection/scripts/check_onboarding_drift.py` |
| doc_type               | `file-level-onboarding`                                                                     |
| lastUpdated            | 2026-05-15T12:57+02:00                                                                      |
| lastVerifiedCommitHash | `810a54351caa86a8e7f13677d284bd5e03147296`                                                  |
| lastVerifiedCommitDate | 2026-05-15T13:31:02+02:00|

## Purpose

`check_onboarding_drift.py` implements the C-02 drift helper. It reads onboarding metadata, compares it with Git/source state, writes a drift report, and emits machine-readable or human-readable results for file-level onboarding, route overviews, repo overviews, repo entity catalogs, and inline blocks.

## Code Commentary

### Logic

The script imports C-08 coordination resolver helpers, discovers supported sidecar onboarding artifacts by `doc_type`, classifies sidecar and inline onboarding, compares recorded verification commits or deterministic fingerprints to current Git state, and writes a Markdown report under the resolved temporary artifact root by default. Its CLI passes the repository path to C-08 as `code_repository_root` and the directory name as `code_repository_name`. For repo entity catalogs, it parses both `## Entity Inventory` headings and `## Entity Fingerprints` rows so missing and orphaned fingerprint rows become deterministic drift signals.

`resolve_report_path` keeps drift reports as coordination artifacts. Relative `--report` paths resolve under `temp_root`; absolute paths outside the coordination root are redirected to `temp_root/drift-reports/<repo>/`; absolute paths inside the durable `memory_root` are also redirected there so a lingering drift report cannot dirty the versioned memory repo.

### Conventions

Sidecar onboarding is detected through Markdown table metadata with supported `doc_type` values: `file-level-onboarding`, `repo-overview`, `route-local-overview`, and `repo-entity-catalog`. File-level sidecars mirror the source path with `.md` appended. Overviews verify a recorded `sourceRoute`. Entity catalogs verify one row per inventory entity in the `Entity Fingerprints` table by recomputing `git-blob-set-v1` over the curated evidence paths; missing rows are missing verification, and rows without inventory entries are orphaned.

### Invariants And Boundaries

The script should never update onboarding content. It can create or overwrite the drift report under C-08's coordination-local temp area, but the report is a maintenance artifact that should not be treated as stable current-state documentation and should not be written into the durable memory repo.

### Todos

No current implementation todo is recorded.

### Docs References

The helper uses Python standard-library modules and repository-local C-08 imports.

| Finding                                                                | Citations | Source Path |
| ---------------------------------------------------------------------- | --------- | ----------- |
| No external library documentation is required for this current helper. | n/a       | n/a         |

## Repo-Internal References

The script is the current executable implementation of drift checking.

| Finding                                                                                                                                                                                                                                                                                                              | Citations            | Source Path                                                                                                                               |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `DriftRow` defines the classification record emitted by the helper.                                                                                                                                                                                                                                                  | L69-L80              | [check_onboarding_drift.py](agents-remember-md/runtime/skills/U-01-core-skills/C-02-onboarding-drift-detection/scripts/check_onboarding_drift.py) |
| Markdown table metadata and supported sidecar `doc_type` detection drive sidecar discovery.                                                                                                                                                                                                                          | L151-L190            | [check_onboarding_drift.py](agents-remember-md/runtime/skills/U-01-core-skills/C-02-onboarding-drift-detection/scripts/check_onboarding_drift.py) |
| File-level sidecar classification checks source path, verification hash, source existence, commit existence, diff to HEAD, and local changes.                                                                                                                                                                        | L214-L319            | [check_onboarding_drift.py](agents-remember-md/runtime/skills/U-01-core-skills/C-02-onboarding-drift-detection/scripts/check_onboarding_drift.py) |
| Overview classification verifies the recorded source route against the recorded commit and local working-tree changes.                                                                                                                                                                                               | L322-L441            | [check_onboarding_drift.py](agents-remember-md/runtime/skills/U-01-core-skills/C-02-onboarding-drift-detection/scripts/check_onboarding_drift.py) |
| Entity catalog classification parses the `Entity Fingerprints` table and `Entity Inventory` headings, recomputes `git-blob-set-v1`, reports missing fingerprint rows, orphaned rows, missing evidence paths, unsupported algorithms, fingerprint mismatches, and local evidence-file changes. | L467-L789            | [check_onboarding_drift.py](agents-remember-md/runtime/skills/U-01-core-skills/C-02-onboarding-drift-detection/scripts/check_onboarding_drift.py) |
| Missing sidecar onboarding is classified when a managed source lacks the mirrored file.                                                                                                                                                                                                                              | L676-L694            | [check_onboarding_drift.py](agents-remember-md/runtime/skills/U-01-core-skills/C-02-onboarding-drift-detection/scripts/check_onboarding_drift.py) |
| `classify_sidecar_onboarding_units` can return several rows for one `entities.md`, while the older single-row wrapper remains available for compatibility.                                                                                                                                                            | L813-L883            | [check_onboarding_drift.py](agents-remember-md/runtime/skills/U-01-core-skills/C-02-onboarding-drift-detection/scripts/check_onboarding_drift.py) |
| Default drift report helpers place reports under `<temp_root>/drift-reports/<repo-name>/`; `resolve_report_path` keeps relative paths inside `temp_root`, allows explicit non-memory coordination-root paths, redirects paths outside coordination, and redirects paths inside the durable memory root back to temp. | L107-L118; L1026-L1044 | [check_onboarding_drift.py](agents-remember-md/runtime/skills/U-01-core-skills/C-02-onboarding-drift-detection/scripts/check_onboarding_drift.py) |
| CLI resolution uses C-08 context via `code_repository_name` and `code_repository_root`, then writes the report through the resolved `coordination_root`, `temp_root`, and `memory_root` so reports cannot land in versioned memory.                                                                                  | L1112-L1194          | [check_onboarding_drift.py](agents-remember-md/runtime/skills/U-01-core-skills/C-02-onboarding-drift-detection/scripts/check_onboarding_drift.py) |

## Cross-Repo References

No sibling repository evidence is needed for the helper's current logic.

| Finding                                    | Citations | Source Path |
| ------------------------------------------ | --------- | ----------- |
| No meaningful cross-repo references found. | n/a       | n/a         |

## Update History

- 2026-05-15T12:57+02:00: Updated after entity catalog drift detection began reconciling inventory headings with fingerprint rows and surfacing missing/orphaned rows. Verification metadata remains pinned until closeout commits the source change.
- 2026-05-15T11:46+02:00: Updated after C-02 gained deterministic route-overview drift and per-entity `git-blob-set-v1` fingerprint classification. Verification metadata remains pinned until closeout commits the source change.
- 2026-05-11T19:42: Refreshed verification metadata against commit `aa85d3862bf21fed791e3170e6957f9288c319e8` after coordination rename verification.
- 2026-05-11T18:34: Updated after C-02 switched its resolver call to `code_repository_name` and `code_repository_root`.
- 2026-05-10T03:11: Updated after explicit drift report paths under `memory_root` began redirecting to coordination temp.
- 2026-05-10T00:36: Refreshed verification metadata after the temp-root drift report helpers landed on main.
- 2026-05-09T23:22: Updated after drift reports moved from task folders to C-08's temporary artifact root.
- 2026-05-09T21:15: Created first file-level onboarding baseline for the C-02 helper implementation.
