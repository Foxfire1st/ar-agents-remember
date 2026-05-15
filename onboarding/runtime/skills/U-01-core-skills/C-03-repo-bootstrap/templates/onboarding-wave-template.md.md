# onboarding-wave-template.md

| Field                  | Value                                                                                   |
| ---------------------- | --------------------------------------------------------------------------------------- |
| repository             | agents-remember-md                                                                      |
| path                   | `runtime/skills/U-01-core-skills/C-03-repo-bootstrap/templates/onboarding-wave-template.md`      |
| doc_type               | `file-level-onboarding`                                                                 |
| lastUpdated            | 2026-05-14T18:00+02:00                                                                  |
| lastVerifiedCommitHash | `398184b757e336211e335569284f2cde309cd964`                                                                                      |
| lastVerifiedCommitDate |                                                                                         2026-05-15T04:04:02+02:00|

## Purpose

This template defines route-overview and file-onboarding wave manifests.

## Code Commentary

### Logic

The wave manifest records wave metadata, goal, included cards, excluded/deferred paths, evidence requirements, worker instructions, assignments, done criteria, and developer review questions.

### Conventions

Waves are small, bounded units. Workers read assigned cards first, read only listed evidence, keep planning notes out of durable onboarding, preserve strict one-to-one file mapping, and return changed paths plus unresolved questions.

### Invariants And Boundaries

The wave manifest coordinates workers; it is not durable source behavior documentation. Every included target needs onboarding output or an explicit blocker plus curator review.

### Todos

Fill verification metadata after the source file is committed.

### Docs References

No external documentation is needed for this repository-local template.

| Finding                                   | Citations | Source Path |
| ----------------------------------------- | --------- | ----------- |
| No relevant external documentation found. | n/a       | n/a         |

## Repo-Internal References

| Finding                                                                                       | Citations | Source Path                                                                               |
| --------------------------------------------------------------------------------------------- | --------- | ----------------------------------------------------------------------------------------- |
| The onboarding wave template records wave metadata, cards, deferred targets, evidence needs, worker instructions, assignments, done criteria, and review questions. | L1-L65    | [onboarding-wave-template.md](agents-remember-md/runtime/skills/U-01-core-skills/C-03-repo-bootstrap/templates/onboarding-wave-template.md) |
| C-03 Phase 4H writes onboarding wave manifests and gives each file worker a file card plus C-05 instructions. | L886-L916 | [C-03 SKILL.md](agents-remember-md/runtime/skills/U-01-core-skills/C-03-repo-bootstrap/SKILL.md) |

## Cross-Repo References

No sibling repository evidence is needed for this template.

| Finding                                    | Citations | Source Path |
| ------------------------------------------ | --------- | ----------- |
| No meaningful cross-repo references found. | n/a       | n/a         |

## Update History

- 2026-05-14T18:00+02:00: Created onboarding for the onboarding wave template. Verification metadata remains blank until the source file is committed.
