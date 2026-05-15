# repo-entity-catalog-template.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `runtime/skills/U-01-core-skills/C-05-create-or-update-onboarding-files/templates/repo-entity-catalog-template.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-15T12:57+02:00                     |
| lastVerifiedCommitHash | `810a54351caa86a8e7f13677d284bd5e03147296`         |
| lastVerifiedCommitDate | 2026-05-15T13:31:02+02:00|

## Purpose

This template defines the repo-level entity catalog shape used by C-05, including the parseable `Entity Fingerprints` section used by C-02 and its required match to `Entity Inventory` entries.

## Notes

Changes here affect how durable repository concepts, boundaries, source references, cross-layer projections, and deterministic evidence fingerprints are captured outside file-specific onboarding units.

The `Entity Fingerprints` section uses one row per inventory entity. Each row records `git-blob-set-v1`, the stored `sha256:<digest>`, and semicolon-separated repo-relative evidence paths.

## Update History

- 2026-05-15T12:57+02:00: Clarified that every `Entity Inventory` entry must have one matching fingerprint row. Verification metadata remains pinned until closeout commits the source change.
- 2026-05-15T11:46+02:00: Updated after adding the parseable `Entity Fingerprints` table and `git-blob-set-v1` guidance. Verification metadata remains pinned until closeout commits the source change.
- 2026-05-15T01:55+02:00: Created with pending verification metadata for the runtime skill-tree move.
