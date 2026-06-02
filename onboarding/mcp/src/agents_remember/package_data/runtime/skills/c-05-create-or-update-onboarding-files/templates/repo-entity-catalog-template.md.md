# repo-entity-catalog-template.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/c-05-create-or-update-onboarding-files/templates/repo-entity-catalog-template.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-24T18:10+02:00                     |
| lastVerifiedCommitHash | `dc25f5a63de359926985c925096aad9019968bf4`         |
| lastVerifiedCommitDate | 2026-06-02T18:31:01+02:00|

## Purpose

This template defines the repo-level entity catalog shape used by `c-05-create-or-update-onboarding-files` skill, including the parseable `Entity Fingerprints` section used by `c-02-memory-quality-control` skill and its required match to `Entity Inventory` entries.

## Notes

Changes here affect how durable repository concepts, boundaries, source references, cross-layer projections, and deterministic evidence fingerprints are captured outside file-specific onboarding units.

The `Entity Fingerprints` section uses one row per inventory entity. Each row records `git-blob-set-v1`, the stored `sha256:<digest>`, and semicolon-separated repo-relative evidence paths.

## Update History

- 2026-05-24T18:10+02:00: Moved onboarding to mirror the packaged runtime source route under `mcp/src/agents_remember/package_data/runtime/` after F-10 packaged runtime asset discovery.
- 2026-05-15T12:57+02:00: Clarified that every `Entity Inventory` entry must have one matching fingerprint row. Verification metadata remains pinned until closeout commits the source change.
- 2026-05-15T11:46+02:00: Updated after adding the parseable `Entity Fingerprints` table and `git-blob-set-v1` guidance. Verification metadata remains pinned until closeout commits the source change.
- 2026-05-15T01:55+02:00: Created with pending verification metadata for the runtime skill-tree move.
