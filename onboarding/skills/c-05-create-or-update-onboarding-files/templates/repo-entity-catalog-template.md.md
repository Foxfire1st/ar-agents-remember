# skills/c-05-create-or-update-onboarding-files/templates/repo-entity-catalog-template.md

## Governing Overview

[overview.md](../../../overview.md)

## Purpose

This template describes a repository-level entity catalog for load-bearing real entities and their cross-layer projections, outside file-specific onboarding. Its fingerprint section matches inventory entities to a deterministic evidence basis. This converted card documents the catalog template source; it is not an entity catalog instance.

## Code Commentary

### Logic

The source carries catalog identification/status placeholders, purpose, entity fingerprints, inventory and cross-layer projections, optional ownership notes and a legacy newest-first history comment. Each inventory entry describes category, represented real/stable object, description, canonical source of truth, naming drift, identifiers, parent/child relationships, confusable neighbors, source references and active migration notes. The projection example separates Reality, Firmware, Backend and Frontend representations.

Every inventory entity has one matching fingerprint row. The template specifies `git-blob-set-v1`: sort evidence paths, resolve current `HEAD:<path>` blobs, hash the path-plus-blob list and record a `sha256:<digest>`. The row carries the entity name, algorithm, digest and semicolon-separated repository-relative evidence paths. Curate the smallest practical load-bearing file set; false-positive review prompts are acceptable. No fingerprint is computed or certified by reading this template.

### Conventions

Catalog content should describe real entities and their projections, not a generic glossary. Ownership notes collect boundaries and naming caveats not local to one entity and are omitted when empty; migration notes apply only to active drift or deferred renaming. Changes to this template therefore affect how durable concepts, boundaries, source references, cross-layer projections and evidence fingerprints are captured outside individual file cards.

### Invariants And Boundaries

The template describes the fingerprint/inventory match but implements no comparer or parser. The retained entity workflow under c-05 requires review of changed evidence and names c-05 as the reporter of fingerprint drift, missing fingerprint rows and orphaned rows or missing paths. This is the instruction contract, not an independent execution of a comparer. The catalog template’s metadata and history comment are legacy source-description details, not requirements for the converted card documenting this file.

This card describes a template as source; it is not an instance of that template. Converted onboarding uses mirrored Markdown and a companion authored by the supported writers: no metadata table or in-card Update History, and no hand-authored companion JSON. Citation tables are authoring input for the fixer, not the final evidence representation. Describing an older template format does not authorize new legacy-format memory writes.

## Evidence

### Docs References

The inherited card contained no external-documentation section or search result; no new search result is asserted. Repository-local source is sufficient for the bounded template description.

### Repo-Internal References

The source supplies the inventory, projection and fingerprint shapes. The actual c-05 package identifies entity-catalog routing and the evidence-path/comparison ownership split. The inherited short card had no companion, reference-note tuples or typed-entry rows to move.

- The entity template requires a fingerprint for every inventory entity and describes sorted current Git blob evidence with a smallest-practical load-bearing source set. [1]
- The entity inventory retains real-object meaning, source authority, naming drift, identifiers, relationships, confusions, references and migration notes. [2]
- The source describes Reality/Firmware/Backend/Frontend projections, optional catalog ownership notes and legacy history syntax. [3]
- The c-05 source names file-level units and repository entity catalogs as its two artifact types. [4]

- The retained c-05 entity workflow requires evidence review and names its current fingerprint-drift and inventory-coverage reporting owner; the template itself performs neither comparison nor parsing. [5]
- The converted workflow requires a source-mirrored Markdown/companion card without manually authored metadata, history or sidecar JSON. [6]

### Cross-Repo References

Reality/Firmware/Backend/Frontend labels describe possible layers, not evidence that this template crosses repositories or authorizes reading or updating a sibling repository.
