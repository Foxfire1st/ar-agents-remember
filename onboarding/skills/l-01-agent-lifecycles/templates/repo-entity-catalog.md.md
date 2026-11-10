# skills/l-01-agent-lifecycles/templates/repo-entity-catalog.md

## Governing Overview

[overview](../overview.md)

## Purpose

The layout Curators copy to describe a repository's real entities and how each is represented across layers.

## Code Commentary

A leading comment sends the Curator to `reference/curator/card-formats-and-citations.md#maintain-the-entity-catalog`. The catalog is selective: a header table (repository, lastUpdated, status), Purpose, an Entity Fingerprints table (entity, `git-blob-set-v1` algorithm, `sha256:` fingerprint, evidence paths), an Entity Inventory with one field table per canonical entity (category, what it represents, description, source of truth, naming drift, identifiers, relationships, often-confused-with, source references, constraints), Cross-Layer Projections per entity and optional Ownership Notes.

## Evidence

- Fingerprint rows name the entity, the `git-blob-set-v1` algorithm, the digest and evidence paths. [1]
- Each entity has an inventory table and a cross-layer projection table. [2]
- The card-format reference points to this layout before the entity catalog is created or maintained. [3]
