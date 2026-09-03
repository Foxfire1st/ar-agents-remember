# mcp/src/agents_remember/memory_quality/final_certification/models.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/final_certification/models.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T01:48+02:00 |
| lastVerifiedCommitHash | `16d1a4d6d6f8e8572b4bca10b8a4a84485449604` |
| lastVerifiedCommitDate | 2026-09-04T00:55:21+02:00 |
| governingOverview | `../overview.md` |

## Governing Overview

[memory_quality overview](../overview.md)

## Purpose

Closed typed contracts for the final full memory-coherence certification (CCR-R08 Gate 5).
Every model is frozen with `extra="forbid"`, so the catalog plan, the executed attestation,
and the certification result are immutable and self-validating: digests must match content,
statuses must match their findings, and only a green certification can be finalization
eligible. The application and certification surfaces share these models through the package
`__init__`.

## Code Commentary

### Logic

Module-level surface:

- Status vocabulary: `FinalItemStatus` (line 26, pass/fail/blocked/not-applicable) and
  `FinalCertificationState` (line 27, green/red/blocked).
- `FinalCertificationModel` (class, lines 30-33) - closed immutable base
  (`extra="forbid", frozen=True`).
- `FinalCatalogItemIdentity` (class, lines 36-44) - one closed catalog member
  (`itemId` pattern, `version` semver, tuple `key`).
- `FinalCatalogItemResult` (class, lines 47-65) - one typed result with content-addressed
  `subresultDigest`; the after-validator `_require_status_shape` (58-65) forces blocked
  items to carry `blockedBy` and forbids findings on pass/not-applicable items.
- `FinalFullCatalogPlan` (class, lines 68-100) - schema
  `memory-final-full-catalog-plan/v1`; `_require_canonical_plan` (86-100) forces unique
  canonical catalog/subrecord tuples and a self-consistent `planDigest`.
- `FinalFullCatalogAttestation` (class, lines 103-140) - schema
  `memory-final-full-catalog-attestation/v1`; `_require_complete_population` (120-140)
  forces the attested population to exhaust exactly the planned one and status counts/ok to
  derive from the results.
- `FinalCertificationResult` (class, lines 143-190) - schema
  `memory-final-full-coherence-certification/v1`; `_require_memory_binding` (168-178)
  binds plan and attestation memory trees/plan digests and requires a Git-tree memory input;
  `_require_green_state` (180-190) requires a fully passing catalog, assembled Gate-5
  inputs, a current coherence record, and the reused green Gate 1-4 prefix for any green result.
- `_require_unique_canonical` (lines 193-196) - shared uniqueness-and-order guard.

### Conventions

Patterns for digests (`^[0-9a-f]{64}T@), trees (40-64 hex), ids and semver versions are
module constants (lines 16-24); validators raise `ValueError` so callers translate them
into typed refusals at their boundary.

### Invariants And Boundaries

- Models are closed and frozen: no extra fields and no mutation after construction.
- Attestation exhaustiveness is structural: the observed catalog must equal the planned
  population exactly.
- Only a green certification is finalization-eligible; red/blocked never are.

### Todos

None.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The status and state vocabularies. | `FinalItemStatus`; `FinalCertificationState` | mcp/src/agents_remember/memory_quality/final_certification/models.py:26-27 |
| One closed final-catalog member with a canonical key. | `FinalCatalogItemIdentity` | mcp/src/agents_remember/memory_quality/final_certification/models.py:36-44 |
| One typed Gate-5 result with content-addressed subresult and status shape guard. | `FinalCatalogItemResult` | mcp/src/agents_remember/memory_quality/final_certification/models.py:47-65 |
| The deterministic complete plan with self-digest. | `FinalFullCatalogPlan` | mcp/src/agents_remember/memory_quality/final_certification/models.py:68-100 |
| The executed attestation that must exhaust its planned population. | `FinalFullCatalogAttestation` | mcp/src/agents_remember/memory_quality/final_certification/models.py:103-140 |
| The typed green/red/blocked certification over the exact pair. | `FinalCertificationResult` | mcp/src/agents_remember/memory_quality/final_certification/models.py:143-190 |
| Shared uniqueness-and-canonical-order guard. | `_require_unique_canonical` | mcp/src/agents_remember/memory_quality/final_certification/models.py:193-196 |

## Update History

- 2026-09-04T01:48+02:00 — 260831-CCR-L08 Gate-5 memory pass: created this file-level
  onboarding card for the new CCR-R08 closed typed final-certification contract models module
  delivered in code commit 16d1a4d6; anchors and ranges derived from the current worktree
  source and pinned to that commit.
