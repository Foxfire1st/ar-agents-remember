# repo-entity-catalog-workflow.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `runtime/skills/U-01-core-skills/C-05-create-or-update-onboarding-files/workflows/repo-entity-catalog-workflow.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-14T21:16+02:00                     |
| lastVerifiedCommitHash | `398184b757e336211e335569284f2cde309cd964` |
| lastVerifiedCommitDate | 2026-05-15T04:04:02+02:00|

## Purpose

This workflow defines how C-05 creates and maintains the repo-level `entities.md` catalog for recurring real concepts in a repository.

## Code Commentary

### Logic

The workflow starts from source inspection, reads C-08-resolved sources, writes `entities.md` under the resolved onboarding root, chooses entities that represent stable concepts rather than file names alone, records ownership and confusion risks, and keeps update history append-only.

### Conventions

Entity catalogs are repo-level onboarding artifacts directly under the resolved onboarding root. They are not comprehensive glossaries and should avoid task-only concepts unless those concepts represent durable repository entities.

### Invariants And Boundaries

The catalog should explain current reusable concepts and current design entities, not checklist tasks. It should link back to source evidence for each entity.

### Todos

After this working-tree update lands, refresh verification metadata to the committed workflow revision.

### Docs References

No external domain documentation is required for this repository-local workflow.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

The workflow defines the current entity-catalog schema and lifecycle.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Placement and metadata rules define `entities.md` directly under the resolved onboarding root and keep it complementary to `overview.md`. | L1-L39 | [repo entity workflow](agents-remember-md/runtime/skills/U-01-core-skills/C-05-create-or-update-onboarding-files/workflows/repo-entity-catalog-workflow.md) |
| Entity criteria define what belongs in a repo entity catalog. | L41-L62 | [repo entity workflow](agents-remember-md/runtime/skills/U-01-core-skills/C-05-create-or-update-onboarding-files/workflows/repo-entity-catalog-workflow.md) |
| Creation, maintenance, and review steps require source evidence and update-history preservation. | L64-L88 | [repo entity workflow](agents-remember-md/runtime/skills/U-01-core-skills/C-05-create-or-update-onboarding-files/workflows/repo-entity-catalog-workflow.md) |

## Cross-Repo References

No sibling repository evidence is needed for the workflow itself.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-14T21:16+02:00: Refreshed for resolved onboarding-root placement of `entities.md` and current source-discovery wording. Verification metadata remains pinned to the last committed source until closeout.
- 2026-05-09T21:15: Created first file-level onboarding baseline for the C-05 repo-entity workflow.
