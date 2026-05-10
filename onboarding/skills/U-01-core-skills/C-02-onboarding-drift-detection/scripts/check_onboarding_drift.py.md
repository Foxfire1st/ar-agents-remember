# check_onboarding_drift.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `skills/U-01-core-skills/C-02-onboarding-drift-detection/scripts/check_onboarding_drift.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-10T03:11                           |
| lastVerifiedCommitHash | `d4843af1edfb808a95072504577289ae9dda40bd` |
| lastVerifiedCommitDate | 2026-05-10T03:14:28+02:00|

## Purpose

`check_onboarding_drift.py` implements the C-02 drift helper. It reads file-level onboarding metadata, compares it with Git/source state, writes a drift report, and emits machine-readable or human-readable results.

## Code Commentary

### Logic

The script imports C-08 resolver helpers, discovers file-level onboarding files by metadata, classifies sidecar and inline onboarding, compares recorded verification commits to current HEAD, and writes a Markdown report under the resolved temporary artifact root by default.

`resolve_report_path` keeps drift reports as coordination artifacts. Relative `--report` paths resolve under `temp_root`; absolute paths outside the coordination root are redirected to `temp_root/drift-reports/<repo>/`; absolute paths inside the durable `memory_root` are also redirected there so a lingering drift report cannot dirty the versioned memory repo.

### Conventions

External file-level onboarding is detected through a Markdown table with `doc_type` equal to `file-level-onboarding`. For sidecar storage, each onboarding file mirrors the source path with `.md` appended.

### Invariants And Boundaries

The script should never update onboarding content. It can create or overwrite the drift report under C-08's coordination-local temp area, but the report is a maintenance artifact that should not be treated as stable current-state documentation and should not be written into the durable memory repo.

### Todos

No current implementation todo is recorded.

### Docs References

The helper uses Python standard-library modules and repository-local C-08 imports.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No external library documentation is required for this current helper. | n/a | n/a |

## Repo-Internal References

The script is the current executable implementation of drift checking.

| Finding | Citations | Source Path |
| --- | --- | --- |
| `DriftRow` defines the classification record emitted by the helper. | L62-L70 | [check_onboarding_drift.py](agents-remember-md/skills/U-01-core-skills/C-02-onboarding-drift-detection/scripts/check_onboarding_drift.py) |
| Markdown table metadata and file-level onboarding detection drive sidecar discovery. | L136-L159 | [check_onboarding_drift.py](agents-remember-md/skills/U-01-core-skills/C-02-onboarding-drift-detection/scripts/check_onboarding_drift.py) |
| External onboarding classification checks source path, verification hash, source existence, commit existence, diff to HEAD, and local changes. | L191-L289 | [check_onboarding_drift.py](agents-remember-md/skills/U-01-core-skills/C-02-onboarding-drift-detection/scripts/check_onboarding_drift.py) |
| Missing sidecar onboarding is classified when a managed source lacks the mirrored file. | L299-L315 | [check_onboarding_drift.py](agents-remember-md/skills/U-01-core-skills/C-02-onboarding-drift-detection/scripts/check_onboarding_drift.py) |
| Markdown reports are generated with summary counts and actionable rows. | L562-L615 | [check_onboarding_drift.py](agents-remember-md/skills/U-01-core-skills/C-02-onboarding-drift-detection/scripts/check_onboarding_drift.py) |
| Default drift report helpers place reports under `<temp_root>/drift-reports/<repo-name>/`; `resolve_report_path` keeps relative paths inside `temp_root`, allows explicit non-memory coordination-root paths, redirects paths outside coordination, and redirects paths inside the durable memory root back to temp. | L100-L111; L626-L644 | [check_onboarding_drift.py](agents-remember-md/skills/U-01-core-skills/C-02-onboarding-drift-detection/scripts/check_onboarding_drift.py) |
| CLI resolution uses C-08 context and writes the report through the resolved `coordination_root`, `temp_root`, and `memory_root` so reports cannot land in versioned memory. | L721-L781 | [check_onboarding_drift.py](agents-remember-md/skills/U-01-core-skills/C-02-onboarding-drift-detection/scripts/check_onboarding_drift.py) |

## Cross-Repo References

No sibling repository evidence is needed for the helper's current logic.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-10T03:11: Updated after explicit drift report paths under `memory_root` began redirecting to coordination temp.
- 2026-05-10T00:36: Refreshed verification metadata after the temp-root drift report helpers landed on main.
- 2026-05-09T23:22: Updated after drift reports moved from task folders to C-08's temporary artifact root.
- 2026-05-09T21:15: Created first file-level onboarding baseline for the C-02 helper implementation.
