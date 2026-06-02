# repo-entity-catalog-workflow.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/c-05-create-or-update-onboarding-files/workflows/repo-entity-catalog-workflow.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-24T18:10+02:00                     |
| lastVerifiedCommitHash | `dc25f5a63de359926985c925096aad9019968bf4` |
| lastVerifiedCommitDate | 2026-06-02T18:31:01+02:00|

## Purpose

This workflow defines how `c-05-create-or-update-onboarding-files` skill creates and maintains the repo-level `entities.md` catalog for recurring real concepts in a repository, including deterministic entity fingerprints used by `c-02-memory-quality-control` skill drift detection, the required one-to-one coverage between inventory entries and fingerprint rows, and the provider-neutral documentation discovery rules used while reviewing entity source-of-truth claims.

## Code Commentary

### Logic

The workflow starts from source inspection, reads sources resolved by the `c-08-ar-coordination-context-resolver` skill, writes `entities.md` under the resolved onboarding root, chooses entities that represent stable concepts rather than file names alone, records ownership and confusion risks, keeps update history append-only, and curates the load-bearing evidence paths used for each entity's `git-blob-set-v1` fingerprint. Its source-discovery rules make the resolved `Domain Documentation` category the entity-review discovery plan, treat live documentation sources named there as authoritative, use local mirrors only as orientation caches, and require live retrieval before recording that no relevant documentation exists. It requires `c-05-create-or-update-onboarding-files` skill to add missing fingerprint rows for inventory entries and to review orphaned rows or missing evidence paths as possible removed, renamed, or moved entities before deleting anything.

### Conventions

Entity catalogs are repo-level onboarding artifacts directly under the resolved onboarding root. They are not comprehensive glossaries and should avoid task-only concepts unless those concepts represent durable repository entities. Fingerprint evidence paths should be small and deterministic rather than exhaustive, and every inventory entry should have exactly one matching fingerprint row. Provider-specific documentation systems are selected by each memory layer's source registry, not by this workflow source.

### Invariants And Boundaries

The catalog should explain current reusable concepts and current design entities, not checklist tasks. It should link back to source evidence for each entity and avoid treating local documentation caches as canonical when the resolved source registry provides a live source.

### Todos

After this working-tree update lands, refresh verification metadata to the committed workflow revision.

### Docs References

No external domain documentation is required for this repository-local workflow. The resolved `agents-remember-md` source registry has no configured `Domain Documentation` entries, so the relevant evidence for this workflow is repository source.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found after checking live sources. | n/a | n/a |

## Repo-Internal References

The workflow defines the current entity-catalog schema and lifecycle.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Source discovery rules require the resolved `Domain Documentation` category, authoritative live documentation retrieval when the registry names it, local mirrors as orientation only, and actual evidence citations instead of source registries. | L17-L24 | [repo entity workflow](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/c-05-create-or-update-onboarding-files/workflows/repo-entity-catalog-workflow.md) |
| Placement and metadata rules define `entities.md` directly under the resolved onboarding root and keep it complementary to `overview.md`. | L26-L40 | [repo entity workflow](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/c-05-create-or-update-onboarding-files/workflows/repo-entity-catalog-workflow.md) |
| Entity fingerprint rules define `git-blob-set-v1`, small curated evidence paths, required inventory coverage, acceptable false-positive review prompts, and removed/renamed/moved review before deleting stale rows or evidence paths. | L41-L49 | [repo entity workflow](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/c-05-create-or-update-onboarding-files/workflows/repo-entity-catalog-workflow.md) |
| Entity criteria define what belongs in a repo entity catalog. | L51-L72 | [repo entity workflow](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/c-05-create-or-update-onboarding-files/workflows/repo-entity-catalog-workflow.md) |
| Creation, maintenance, and review steps require source evidence, fingerprint curation, missing/orphaned fingerprint row handling, drift inspection, and update-history preservation. | L74-L106 | [repo entity workflow](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/c-05-create-or-update-onboarding-files/workflows/repo-entity-catalog-workflow.md) |

## Cross-Repo References

No sibling repository evidence is needed for the workflow itself.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-24T18:10+02:00: Moved onboarding to mirror the packaged runtime source route under `mcp/src/agents_remember/package_data/runtime/` after F-10 packaged runtime asset discovery.
- 2026-05-22T13:32+02:00: Updated after entity-catalog source discovery became provider-neutral while requiring live registry-named documentation checks before recording no domain docs. Verification metadata remains pinned until closeout commits the source change.
- 2026-05-15T12:57+02:00: Clarified required coverage between inventory entries and fingerprint rows, including missing-row creation and orphaned-row review for removed, renamed, or moved entities. Verification metadata remains pinned until closeout commits the source change.
- 2026-05-15T11:46+02:00: Refreshed after the workflow added deterministic `git-blob-set-v1` entity fingerprint creation and maintenance rules. Verification metadata remains pinned until closeout commits the source change.
- 2026-05-14T21:16+02:00: Refreshed for resolved onboarding-root placement of `entities.md` and current source-discovery wording. Verification metadata remains pinned to the last committed source until closeout.
- 2026-05-09T21:15: Created first file-level onboarding baseline for the `c-05-create-or-update-onboarding-files` skill repo-entity workflow.
