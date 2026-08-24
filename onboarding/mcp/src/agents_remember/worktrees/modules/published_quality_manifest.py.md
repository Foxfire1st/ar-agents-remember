# mcp/src/agents_remember/worktrees/modules/published_quality_manifest.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/modules/published_quality_manifest.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:19+02:00 |
| lastVerifiedCommitHash |  `f95487ec993b58d34911bba0206a7fa6ef9684eb`|
| lastVerifiedCommitDate |  2026-08-24T15:28:18+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[worktrees/modules overview](overview.md)

## Purpose

Defines the sole strict reader and immutable value model for the atomic current-quality-generation
manifest consumed by quality recovery.

## Code Commentary

### Logic

`load_published_quality_manifest` reads `quality-report-set.json` exactly once and validates it as
schema `1.0`. The root must be an object with only `schemaVersion`, `generation`, `files`, and
optional `attestation`. Generation and file digests are lowercase SHA-256 strings; file records
contain exactly `sha256` and a non-negative integer `size`; attestations contain string pairs.
Parsed file and attestation mappings are immutable. `require_file` selects a declared artifact
without constructing an unverified path.

### Invariants And Boundaries

- There is one current schema and one reader; alternate roots, legacy shapes, unknown fields, and
  partial records are rejected.
- All filesystem, JSON, and structural failures collapse to the stable chained
  `PublishedQualityManifestError` boundary.
- The parsed snapshot is immutable so one recovery cannot silently mix manifest generations.
- The manifest declares evidence; downstream recovery still verifies declared digest and size.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies; this is an internal publication format.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The loader reads the sole manifest pointer and returns one strict snapshot. | `load_published_quality_manifest` | mcp/src/agents_remember/worktrees/modules/published_quality_manifest.py:45-55 |
| Schema version, root vocabulary, generation, files, and attestation are validated without compatibility readers. | `_parse_manifest` | mcp/src/agents_remember/worktrees/modules/published_quality_manifest.py:57-95 |
| Each file record has an exact digest/size shape. | `_parse_file` | mcp/src/agents_remember/worktrees/modules/published_quality_manifest.py:98-107 |

## Cross-Repo References

No meaningful cross-repository implementation reference applies.

## Update History

- 2026-08-24T14:19+02:00 — 260821-DAGQC-L2: created for the strict schema-1.0 published-quality manifest boundary. Verification remains blank until architect-owned closeout stamps the code commit.
