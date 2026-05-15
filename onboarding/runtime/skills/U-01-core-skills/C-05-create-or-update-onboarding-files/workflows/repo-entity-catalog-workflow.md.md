# repo-entity-catalog-workflow.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `runtime/skills/U-01-core-skills/C-05-create-or-update-onboarding-files/workflows/repo-entity-catalog-workflow.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-15T12:57+02:00                     |
| lastVerifiedCommitHash | `810a54351caa86a8e7f13677d284bd5e03147296` |
| lastVerifiedCommitDate | 2026-05-15T13:31:02+02:00|

## Purpose

This workflow defines how C-05 creates and maintains the repo-level `entities.md` catalog for recurring real concepts in a repository, including deterministic entity fingerprints used by C-02 drift detection and the required one-to-one coverage between inventory entries and fingerprint rows.

## Code Commentary

### Logic

The workflow starts from source inspection, reads C-08-resolved sources, writes `entities.md` under the resolved onboarding root, chooses entities that represent stable concepts rather than file names alone, records ownership and confusion risks, keeps update history append-only, and curates the load-bearing evidence paths used for each entity's `git-blob-set-v1` fingerprint. It requires C-05 to add missing fingerprint rows for inventory entries and to review orphaned rows or missing evidence paths as possible removed, renamed, or moved entities before deleting anything.

### Conventions

Entity catalogs are repo-level onboarding artifacts directly under the resolved onboarding root. They are not comprehensive glossaries and should avoid task-only concepts unless those concepts represent durable repository entities. Fingerprint evidence paths should be small and deterministic rather than exhaustive, and every inventory entry should have exactly one matching fingerprint row.

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
| Entity fingerprint rules define `git-blob-set-v1`, small curated evidence paths, required inventory coverage, acceptable false-positive review prompts, and removed/renamed/moved review before deleting stale rows or evidence paths. | L41-L49 | [repo entity workflow](agents-remember-md/runtime/skills/U-01-core-skills/C-05-create-or-update-onboarding-files/workflows/repo-entity-catalog-workflow.md) |
| Entity criteria define what belongs in a repo entity catalog. | L51-L72 | [repo entity workflow](agents-remember-md/runtime/skills/U-01-core-skills/C-05-create-or-update-onboarding-files/workflows/repo-entity-catalog-workflow.md) |
| Creation, maintenance, and review steps require source evidence, fingerprint curation, missing/orphaned fingerprint row handling, drift inspection, and update-history preservation. | L74-L106 | [repo entity workflow](agents-remember-md/runtime/skills/U-01-core-skills/C-05-create-or-update-onboarding-files/workflows/repo-entity-catalog-workflow.md) |

## Cross-Repo References

No sibling repository evidence is needed for the workflow itself.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-15T12:57+02:00: Clarified required coverage between inventory entries and fingerprint rows, including missing-row creation and orphaned-row review for removed, renamed, or moved entities. Verification metadata remains pinned until closeout commits the source change.
- 2026-05-15T11:46+02:00: Refreshed after the workflow added deterministic `git-blob-set-v1` entity fingerprint creation and maintenance rules. Verification metadata remains pinned until closeout commits the source change.
- 2026-05-14T21:16+02:00: Refreshed for resolved onboarding-root placement of `entities.md` and current source-discovery wording. Verification metadata remains pinned to the last committed source until closeout.
- 2026-05-09T21:15: Created first file-level onboarding baseline for the C-05 repo-entity workflow.
