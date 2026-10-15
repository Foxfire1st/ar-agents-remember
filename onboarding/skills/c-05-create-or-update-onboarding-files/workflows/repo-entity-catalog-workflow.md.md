# skills/c-05-create-or-update-onboarding-files/workflows/repo-entity-catalog-workflow.md

## Governing Overview

[overview.md](../../../overview.md)

## Purpose

This source defines the retained repo-level `entities.md` catalog workflow: select load-bearing real entities that recur across layers, explain their canonical meaning and naming drift, and curate deterministic evidence fingerprints for review. The catalog lives once per repository under the resolved onboarding root and complements its overview; it is neither a glossary nor an exhaustive ontology. This card documents that source and its template without treating retained legacy metadata/history instructions as converted-memory permission.

## Code Commentary

### Logic

Discovery uses the resolved `system/sources.md` `Domain Documentation` category to investigate source-of-truth, naming drift and cross-layer projections. Adjacent onboarding is not enough when more authoritative domain, protocol or architecture evidence exists. Where local and live sources coexist, live documentation is authoritative and the cache is orientation only; missing or stale cached evidence prompts live retrieval before an absence claim. The registry is only a discovery index. Cite the actual documentation, implementation, generated artifact or boundary source that proves an entity claim.

The retained creation sequence checks for an existing catalog, reads the repo overview and proving materials, selects deterministic evidence paths, computes the initial fingerprints, fills the template and seeds the most confusion-prone entities first. It may add a lightweight overview pointer for discoverability. Maintenance updates existing entries instead of synonyms, reviews changed evidence paths before changing prose, and keeps the catalog selective. This describes the workflow sequence, not a record that the sequence or a quality check ran.

### Entity Meaning And Selection

Canonical entity names are headings. Prefer the real entity over a drifted UI or storage label, record synonyms as naming drift rather than duplicate entities, identify the current canonical source of truth when knowable, and compare representations across layers. Good candidates have multiple names across layers, matter to a migration/refactor, are confused with neighbors or matter to cross-repo tracing. Pure vocabulary, very local implementation details and wording-only duplicates do not qualify.

The catalog template makes this practical through category, real-world referent, description, source of truth, naming drift, identifiers, parent/child relationships, confusion risks, source references and migration notes. It provides cross-layer projections and optional catalog ownership notes. These fields explain durable reusable concepts and ownership boundaries; task-only checklists and arbitrary file names are not substitutes for stable entities.

### Fingerprint Review Contract

Every Entity Inventory entry has one matching Entity Fingerprints row. The workflow names `git-blob-set-v1`: sort the curated repo-relative evidence paths, resolve the current `HEAD:<path>` blob hashes, hash the path-plus-blob-hash list and store `sha256:<digest>`. Definition, mapper, schema/interface and lifecycle files are preferable to broad roots or every consumer. This is the algorithm description in the workflow and template, not a newly inferred byte serialization or a computation performed here.

A changed fingerprint is a review prompt, not automatic proof that prose is wrong. Inspect changed evidence and decide whether meaning, identifiers, relationships, naming drift, references or projections need correction before refreshing the fingerprint, even if prose remains correct. Missing inventory coverage requires curated evidence and a row; orphaned rows or missing paths require checking whether the entity was removed, renamed or moved before deleting content or replacing evidence. Review also checks that entities are real and stable, neighbors are distinguished, names have not drifted into canonical labels, layer tracing works, and evidence remains small and deterministic. The canonical c-05 skill describes c-05 as curating/refreshing these paths and c-02 as comparing fingerprints and inventory coverage; that is source-level role allocation, not an independent verification of the c-02 implementation.

### Retained Legacy Shape And Converted Applicability

The retained workflow/template place `entities.md` directly under the onboarding root alongside, not instead of, `overview.md`. They include repository, document type, `lastUpdated`, draft/active status and newest-first append-only Update History. Maintenance refreshes the timestamp when entries, prose, evidence paths or fingerprints meaningfully change. Those are the retained catalog's schema instructions, not fields or a history section to add to this converted file card.

The canonical skill's Converted Memory section governs file cards and overviews even though this catalog workflow has no local converted-memory preamble. It directs converted cards to `converted-card-workflow.md`, makes unconverted memory read-only after cutover and prohibits hand-authored sidecar JSON. The converted-card workflow uses a canonical source title, nearest-governing relative link, purpose and commentary, with temporary citation-table input before the fixer authors references. The fixer owns reference allocation; the writer owns typed entries and source/nearest-route history rows. Catalog templates do not grant operations or establish that a legacy-format catalog can be written into converted memory unchanged.

### Invariants And Boundaries

Preserve current reusable entity meaning and source-backed cross-layer relationships rather than turning the catalog into a checklist. Keep provider selection in configured discovery inputs, not hard-coded documentation systems. A live authoritative source is not replaceable by a local cache, and a missing evidence path is a relocation/deletion question before it is a cleanup opportunity. The workflow defines the retained catalog schema and lifecycle, not universal authority over converted knowledge or an observed quality result.

### Retained Notes And Discovery Scope

The inherited TODO calls for verification-metadata refresh after its working-tree change lands. Preserve it as a historical legacy-format follow-up, not an operative converted-card stamp instruction or a claim that landing occurred. The inherited documentation notes say this repository-local workflow required no external domain documentation, the then-resolved registry had no configured Domain Documentation entries, and no relevant external material was found after live checks. Its boundary notes say sibling evidence was unnecessary and no meaningful cross-repo references were found. These remain scoped past-discovery statements, not fresh registry or network observations. Source and template evidence support the contract description; the discovery observations remain historical.

## Evidence

- The workflow selects one repo-level catalog of load-bearing real entities, not a glossary or exhaustive ontology. [1]
- Entity discovery follows configured domain evidence, treats live sources as authoritative and cites proving materials rather than the registry. [2]
- The retained catalog complements the root overview and carries legacy timestamp and draft/active metadata. [3]
- Fingerprints use git-blob-set-v1 and curated load-bearing paths; drift requires review and missing/orphaned rows require relocation/deletion investigation. [4]
- Canonical names, explicit drift and selective entry criteria prevent duplicate synonyms and vocabulary-only entries. [5]
- Creation, maintenance and review inspect evidence, seed useful entities, handle fingerprint coverage and preserve legacy history. [6]
- The catalog template records fingerprints, real referents, canonical ownership, relationships, naming drift and cross-layer projections. [7]
- The template retains metadata and append-only Update History as legacy catalog shape, not converted-card requirements. [8]
- The canonical skill describes c-05 fingerprint curation and c-02 comparison/coverage roles. [9]
- Canonical converted-memory precedence forbids hand-written sidecar JSON and does not permit ordinary unconverted writes. [10]
- Converted cards use a source-path title, relative governing link and temporary evidence-table authoring with fixer-owned references. [11]
- Converted no-impact answers use writer-owned source and route history rows, and converted cards exclude legacy metadata/history and self-assigned references. [12]
