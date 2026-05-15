# file-card-template.md

| Field                  | Value                                                                               |
| ---------------------- | ----------------------------------------------------------------------------------- |
| repository             | agents-remember-md                                                                  |
| path                   | `runtime/skills/U-01-core-skills/C-03-repo-bootstrap/templates/file-card-template.md`       |
| doc_type               | `file-level-onboarding`                                                             |
| lastUpdated            | 2026-05-14T18:00+02:00                                                              |
| lastVerifiedCommitHash | `398184b757e336211e335569284f2cde309cd964`                                                                                  |
| lastVerifiedCommitDate |                                                                                     2026-05-15T04:04:02+02:00|

## Purpose

This template defines the file-card work order that constrains a future file-level onboarding worker.

## Code Commentary

### Logic

The file card records source and onboarding targets, classification, governing context, why the file matters, what the worker must explain, required inputs, allowed and disallowed reads, required onboarding sections, reference expectations, traps, open questions, and done criteria.

### Conventions

File cards are created before assigning file-level onboarding work except for tiny repositories. They keep file workers scoped and prevent broad rediscovery.

### Invariants And Boundaries

A file card does not replace C-05. It prepares bounded instructions for C-05 file-level onboarding and must keep task planning out of durable onboarding.

### Todos

Fill verification metadata after the source file is committed.

### Docs References

No external documentation is needed for this repository-local template.

| Finding                                   | Citations | Source Path |
| ----------------------------------------- | --------- | ----------- |
| No relevant external documentation found. | n/a       | n/a         |

## Repo-Internal References

| Finding                                                                                      | Citations | Source Path                                                                       |
| -------------------------------------------------------------------------------------------- | --------- | --------------------------------------------------------------------------------- |
| The file card template records classification, governing context, worker inputs, allowed/disallowed reads, required sections, reference expectations, traps, questions, and done criteria. | L1-L100   | [file-card-template.md](agents-remember-md/runtime/skills/U-01-core-skills/C-03-repo-bootstrap/templates/file-card-template.md) |
| C-03 Phase 4G writes file cards for priority source files and requires them before file-level onboarding unless the repo is tiny. | L861-L884 | [C-03 SKILL.md](agents-remember-md/runtime/skills/U-01-core-skills/C-03-repo-bootstrap/SKILL.md) |
| C-03 Phase 4H says each file worker receives one file card and follows C-05 for file-level onboarding. | L886-L916 | [C-03 SKILL.md](agents-remember-md/runtime/skills/U-01-core-skills/C-03-repo-bootstrap/SKILL.md) |

## Cross-Repo References

No sibling repository evidence is needed for this template.

| Finding                                    | Citations | Source Path |
| ------------------------------------------ | --------- | ----------- |
| No meaningful cross-repo references found. | n/a       | n/a         |

## Update History

- 2026-05-14T18:00+02:00: Created onboarding for the file card template. Verification metadata remains blank until the source file is committed.
