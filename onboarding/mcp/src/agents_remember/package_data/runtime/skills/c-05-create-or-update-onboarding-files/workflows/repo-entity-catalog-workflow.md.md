# repo-entity-catalog-workflow.md

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

No external domain documentation is required for this repository-local workflow. The resolved `agents-remember` source registry has no configured `Domain Documentation` entries, so the relevant evidence for this workflow is repository source.

No relevant external documentation found after checking live sources.

## Evidence

### Repo-Internal References

The workflow defines the current entity-catalog schema and lifecycle.

- Source discovery rules require the resolved `Domain Documentation` category, authoritative live documentation retrieval when the registry names it, local mirrors as orientation only, and actual evidence citations instead of source registries. [1]
- Placement and metadata rules define `entities.md` directly under the resolved onboarding root and keep it complementary to `overview.md`. [2]
- Entity fingerprint rules define `git-blob-set-v1`, small curated evidence paths, required inventory coverage, acceptable false-positive review prompts, and removed/renamed/moved review before deleting stale rows or evidence paths. [3]
- Entity criteria define what belongs in a repo entity catalog. [4]
- Creation, maintenance, and review steps require source evidence, fingerprint curation, missing/orphaned fingerprint row handling, drift inspection, and update-history preservation. [5]

### Cross-Repo References

No sibling repository evidence is needed for the workflow itself.

No meaningful cross-repo references found.
