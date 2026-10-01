# repo-entity-catalog-template.md

## Purpose

This template defines the repo-level entity catalog shape used by `c-05-create-or-update-onboarding-files` skill, including the parseable `Entity Fingerprints` section used by `c-02-memory-quality-control` skill and its required match to `Entity Inventory` entries.

## Notes

Changes here affect how durable repository concepts, boundaries, source references, cross-layer projections, and deterministic evidence fingerprints are captured outside file-specific onboarding units.

The `Entity Fingerprints` section uses one row per inventory entity. Each row records `git-blob-set-v1`, the stored `sha256:<digest>`, and semicolon-separated repo-relative evidence paths.
