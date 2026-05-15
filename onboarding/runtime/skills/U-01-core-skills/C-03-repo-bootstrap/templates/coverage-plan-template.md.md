# coverage-plan-template.md

| Field                  | Value                                                                                   |
| ---------------------- | --------------------------------------------------------------------------------------- |
| repository             | agents-remember-md                                                                      |
| path                   | `runtime/skills/U-01-core-skills/C-03-repo-bootstrap/templates/coverage-plan-template.md`       |
| doc_type               | `file-level-onboarding`                                                                 |
| lastUpdated            | 2026-05-14T21:16+02:00                                                                  |
| lastVerifiedCommitHash | `398184b757e336211e335569284f2cde309cd964`                                                                                      |
| lastVerifiedCommitDate |                                                                                         2026-05-15T04:04:02+02:00|

## Purpose

This template defines the coverage-planning artifact that turns scout and area research into prioritized route, file, evidence, and slice cleanup work.

## Code Commentary

### Logic

The coverage plan records strategy, area coverage goals, route classifications, file classifications, evidence pack needs, deferred routes/files, slice cleanup decisions, developer review questions, and decisions.

### Conventions

Coverage planning happens before governing route maps and waves. It should classify work by risk and value, and in existing-memory slice maintenance it should decide whether stale route memory is refreshed, moved, removed, retired, or preserved.

### Invariants And Boundaries

The plan is scheduling and prioritization input. It should not become durable file behavior documentation or promote low-confidence findings into fact.

### Todos

Fill verification metadata after the source file is committed.

### Docs References

No external documentation is needed for this repository-local template.

| Finding                                   | Citations | Source Path |
| ----------------------------------------- | --------- | ----------- |
| No relevant external documentation found. | n/a       | n/a         |

## Repo-Internal References

| Finding                                                                                           | Citations | Source Path                                                                               |
| ------------------------------------------------------------------------------------------------- | --------- | ----------------------------------------------------------------------------------------- |
| The coverage plan template captures strategy, area goals, route classification, file classification, and evidence pack queues. | L1-L36    | [coverage-plan-template.md](agents-remember-md/runtime/skills/U-01-core-skills/C-03-repo-bootstrap/templates/coverage-plan-template.md) |
| The template records deferred routes/files, slice cleanup decisions, developer review questions, and decisions for later waves. | L38-L65   | [coverage-plan-template.md](agents-remember-md/runtime/skills/U-01-core-skills/C-03-repo-bootstrap/templates/coverage-plan-template.md) |
| C-03 Phase 4A writes `bootstrap/coverage-plan.md` from this template and classifies deleted, moved, or stale onboarding routes when needed. | L735-L780 | [C-03 SKILL.md](agents-remember-md/runtime/skills/U-01-core-skills/C-03-repo-bootstrap/SKILL.md) |

## Cross-Repo References

No sibling repository evidence is needed for this template.

| Finding                                    | Citations | Source Path |
| ------------------------------------------ | --------- | ----------- |
| No meaningful cross-repo references found. | n/a       | n/a         |

## Update History

- 2026-05-14T21:16+02:00: Refreshed for route cleanup classifications, slice cleanup queue, and stale-route review questions. Verification metadata remains pinned to the last committed source until closeout.
- 2026-05-14T18:00+02:00: Created onboarding for the coverage plan template. Verification metadata remains blank until the source file is committed.
