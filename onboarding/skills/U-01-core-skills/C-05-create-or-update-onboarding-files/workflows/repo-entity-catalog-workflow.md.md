# repo-entity-catalog-workflow.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `skills/U-01-core-skills/C-05-create-or-update-onboarding-files/workflows/repo-entity-catalog-workflow.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-09T21:45                           |
| lastVerifiedCommitHash | `c394f66fb3f2e9fe727ebb6c06a9dd0350921c78` |
| lastVerifiedCommitDate | 2026-05-06T15:25                           |

## Purpose

This workflow defines how C-05 creates and maintains repo-level entity catalogs for recurring real concepts in a repository.

## Code Commentary

### Logic

The workflow starts from source inspection, chooses entities that represent stable concepts rather than file names alone, records ownership and confusion risks, and keeps update history append-only.

### Conventions

Entity catalogs are repo-level onboarding artifacts. They are not comprehensive glossaries and should avoid task-only concepts unless those concepts represent durable repository entities.

### Invariants And Boundaries

The catalog should explain current reusable concepts and current design entities, not checklist tasks. It should link back to source evidence for each entity.

### Todos

Future worktree implementation should add implemented entities when code exists, rather than relying only on roadmap-spec entities.

### Docs References

No external domain documentation is required for this repository-local workflow.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

The workflow defines the current entity-catalog schema and lifecycle.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Metadata and entity criteria define what belongs in a repo entity catalog. | L37-L57 | [repo entity workflow](agents-remember-md/skills/U-01-core-skills/C-05-create-or-update-onboarding-files/workflows/repo-entity-catalog-workflow.md) |
| Creation, maintenance, and review steps require source evidence and update-history preservation. | L65-L89 | [repo entity workflow](agents-remember-md/skills/U-01-core-skills/C-05-create-or-update-onboarding-files/workflows/repo-entity-catalog-workflow.md) |

## Cross-Repo References

No sibling repository evidence is needed for the workflow itself.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-09T21:15: Created first file-level onboarding baseline for the C-05 repo-entity workflow.
