# mcp/src/agents_remember/worktrees/modules/quality/published_manifest.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/modules/quality/published_manifest.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-31T04:50+02:00 |
| lastVerifiedCommitHash | `f2b7c648f540efb9d64ceea22e11e651cb5cc914` |
| lastVerifiedCommitDate | 2026-08-31T15:32:32+02:00 |
| governingOverview | `../overview.md` |

## Governing Overview

[worktrees/modules overview](../overview.md)

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

Each manifest key is also a strict POSIX relative report path. Empty, absolute, backslash-bearing,
non-normalized, or dot-segment paths are rejected before a `PublishedQualityFile` is constructed.
Nested evidence is therefore addressable, but a manifest can never escape the immutable generation
root or smuggle a platform-dependent alternate path spelling.

### Invariants And Boundaries

- There is one current schema and one reader; alternate roots, legacy shapes, unknown fields, and
  partial records are rejected.
- All filesystem, JSON, and structural failures collapse to the stable chained
  `PublishedQualityManifestError` boundary.
- The parsed snapshot is immutable so one recovery cannot silently mix manifest generations.
- The manifest declares evidence; downstream recovery still verifies declared digest and size.
- Nested file names must be canonical safe relative POSIX paths; path traversal and alternate
  separator spellings are invalid manifest evidence.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies; this is an internal publication format.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The loader reads the sole manifest pointer and returns one strict snapshot. | `load_published_quality_manifest` | mcp/src/agents_remember/worktrees/modules/quality/published_manifest.py:45-55 |
| Schema version, root vocabulary, generation, files, and attestation are validated without compatibility readers. | `_parse_manifest` | mcp/src/agents_remember/worktrees/modules/quality/published_manifest.py:57-95 |
| Each file record has an exact digest/size shape. | `_parse_file` | mcp/src/agents_remember/worktrees/modules/quality/published_manifest.py:98-107 |
| Manifest file keys are safe canonical relative paths before they become evidence records. | `is_safe_relative_report_path` | mcp/src/agents_remember/worktrees/modules/quality/published_manifest.py:119-127 |

## Cross-Repo References

No meaningful cross-repository implementation reference applies.

## 260824-PDLS — Strict Schema-2 Evidence Pointer

The manifest reader is the one strict parser for the current immutable Dagger generation. It
requires schema `2.0`, candidate tree, generation digest, exact file digests/sizes, and typed
attestation. Schema `1.0` remains deliberately rejected by both public readers; optional crash
recovery may report no recoverable generation, but there is no permanent compatibility reader or
silent fallback.

## Update History

- 2026-08-31T04:50+02:00 — 260821-ARSPAWN-L5 independent-review repair: added the explicit
  nested-path safety contract for immutable report manifests. Verification remains closeout-owned.

- 2026-08-25T08:16+02:00 — 260824-PDLS wave 004: moved this preserved sidecar with its behavior-preserving package split, repointed source evidence, and verified the emergency-landed source path at code commit `cb6623775a04cbdeb0509dc26f08a8268189c3f6`; this is onboarding provenance, not Dagger certification.

- 2026-08-24T21:23+02:00 — 260824-PDLS centralized strict manifest parsing and retained explicit
  schema-1 rejection after advisory review.

- 2026-08-24T14:19+02:00 — 260821-DAGQC-L2: created for the strict schema-1.0 published-quality manifest boundary. Verification remains blank until architect-owned closeout stamps the code commit.
