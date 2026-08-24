# mcp/src/agents_remember/worktrees/modules/published_quality_manifest.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/modules/published_quality_manifest.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T21:23+02:00 |
| lastVerifiedCommitHash | `b99501852bcfa5f499a25e7183063751f6133a28` |
| lastVerifiedCommitDate | 2026-08-24T21:21:58+02:00 |
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

## 260824-PDLS — Strict Schema-2 Evidence Pointer

The manifest reader is the one strict parser for the current immutable Dagger generation. It
requires schema `2.0`, candidate tree, generation digest, exact file digests/sizes, and typed
attestation. Schema `1.0` remains deliberately rejected by both public readers; optional crash
recovery may report no recoverable generation, but there is no permanent compatibility reader or
silent fallback.

## Update History

- 2026-08-24T21:23+02:00 — 260824-PDLS centralized strict manifest parsing and retained explicit
  schema-1 rejection after advisory review.

- 2026-08-24T14:19+02:00 — 260821-DAGQC-L2: created for the strict schema-1.0 published-quality manifest boundary. Verification remains blank until architect-owned closeout stamps the code commit.
