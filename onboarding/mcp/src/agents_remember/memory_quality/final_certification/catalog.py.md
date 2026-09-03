# mcp/src/agents_remember/memory_quality/final_certification/catalog.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/final_certification/catalog.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T01:48+02:00 |
| lastVerifiedCommitHash | `16d1a4d6d6f8e8572b4bca10b8a4a84485449604` |
| lastVerifiedCommitDate | 2026-09-04T00:55:21+02:00 |
| governingOverview | `../overview.md` |

## Governing Overview

[memory_quality overview](../overview.md)

## Purpose

Owns the deterministic complete final catalog of the CCR-R08 Gate-5 full memory-coherence
certification: the closed catalog population, the exact plan bound to one code/memory candidate
pair, and the executed attestation that proves exhaustion of the planned population. Every
applicable memory checker (drift + style), the missing-onboarding and route-index alignment
owners, the R07 affected-closure plan, the canonical curator-coherence record, and the exact
code/memory candidate pair appear exactly once; a weaker incremental-only acceptance is never a
valid substitute. All outputs are content-addressed, and every refusal is a typed
`FinalCertificationError`.

## Code Commentary

### Logic

Module-level surface:

- `FINAL_FULL_CATALOG_VERSION` (line 44) - the catalog item version `1.0.0`; the fixed item
  ids `MISSING_ONBOARDING_ITEM_ID` / `ROUTE_INDEX_ALIGNMENT_ITEM_ID` / `AFFECTED_CLOSURE_ITEM_ID` /
  `COHERENCE_RECORD_ITEM_ID` / `CANDIDATE_PAIR_ITEM_ID` (lines 46-50) and the seven standard
  checker ids in `_STANDARD_CHECK_IDS` (lines 52-61) close the population.
- `ExecutedFinalCatalog` (class, lines 65-75) - one executed complete catalog plus the
  authority statuses it observed (missing-onboarding/stale-route-index counts, affected-closure,
  coherence and pair statuses, full-only rerun flag, coherence record digest).
- `ReadinessProjectionInput` (class, lines 79-89) - the repair-loop view of one full run that
  is never certification-eligible (see `final_catalog_readiness`).
- `complete_final_catalog` (lines 92-122) - returns the closed catalog population in
  canonical order and refuses (gate-five-catalog-incomplete) whenever the declared checker scope
  registry diverges from `AVAILABLE_CHECKS`.
- `compile_final_catalog_plan` (lines 125-164) - binds the plan to the exact candidate pair:
  verifies the affected-closure plan names the same code and memory trees with a
  non-accepting/full-final-required disposition, requires a nonempty canonical coherence
  subrecord set, and digests the whole payload into `planDigest`.
- `final_catalog_attestation` (lines 167-232) - maps one executed run into the exhaustive
  typed attestation; item results are standard-check, count-based (missing-onboarding /
  stale-route-index), or authority-based (affected-closure / coherence-record / candidate-pair)
  via `_standard_result` / `_count_result` / `_authority_result` (lines 331-385).
- `final_catalog_readiness` (lines 235-328) - the deterministic Gate-5 surface projection
  published by the interactive controller full run: complete population, per-item typed status,
  and blocked items naming the exact missing authority, with
  `finalizationEligible=false` and `fullFinalRequired=true`.
- Guards `_require_affected_closure_bound` (392-418),
  `_require_pending_full_only_population` (421-438) and
  `_require_executed_population` (441-455) make code/memory binding, R07 pending-full-only
  coverage, and executed standard-check exhaustion structural.

### Conventions

Item results are content-addressed via `content_digest`; a blocked item always carries a
nonempty `blockedBy`; unknown item ids refuse through `_refuse_unknown_item` (462-467).

### Invariants And Boundaries

- The catalog is closed and deterministic; nothing outside the declared population can be
  attested, and the attestation must exhaust exactly the planned population.
- Certification never mutates code or memory; the readiness projection cannot claim
  certification eligibility.
- The full catalog must cover the complete current memory checker registry and every R07
  pending full-only checker.

### Todos

None.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Returns the closed deterministic catalog population. | `complete_final_catalog` | mcp/src/agents_remember/memory_quality/final_certification/catalog.py:92-122 |
| Compiles the exact plan bound to one candidate pair with a self-digest. | `compile_final_catalog_plan` | mcp/src/agents_remember/memory_quality/final_certification/catalog.py:125-164 |
| Maps an executed run into the exhaustive typed attestation. | `final_catalog_attestation` | mcp/src/agents_remember/memory_quality/final_certification/catalog.py:167-232 |
| Publishes the non-certifying readiness projection for the repair loop. | `final_catalog_readiness` | mcp/src/agents_remember/memory_quality/final_certification/catalog.py:235-328 |
| Closes the executed/observed authority shapes of one run. | `ExecutedFinalCatalog`; `ReadinessProjectionInput` | mcp/src/agents_remember/memory_quality/final_certification/catalog.py:65-75; mcp/src/agents_remember/memory_quality/final_certification/catalog.py:79-89 |
| Standard, count, and authority result builders. | `_standard_result`; `_count_result`; `_authority_result` | mcp/src/agents_remember/memory_quality/final_certification/catalog.py:331-344; mcp/src/agents_remember/memory_quality/final_certification/catalog.py:347-358; mcp/src/agents_remember/memory_quality/final_certification/catalog.py:361-385 |
| Code/memory binding, pending full-only coverage, and executed-population guards. | `_require_affected_closure_bound`; `_require_pending_full_only_population`; `_require_executed_population` | mcp/src/agents_remember/memory_quality/final_certification/catalog.py:392-418; mcp/src/agents_remember/memory_quality/final_certification/catalog.py:421-438; mcp/src/agents_remember/memory_quality/final_certification/catalog.py:441-455 |
| The typed refusal and unknown-item refusal helpers. | `_refuse`; `_refuse_unknown_item` | mcp/src/agents_remember/memory_quality/final_certification/catalog.py:458-459; mcp/src/agents_remember/memory_quality/final_certification/catalog.py:462-467 |

## Update History

- 2026-09-04T01:48+02:00 — 260831-CCR-L08 Gate-5 memory pass: created this file-level
  onboarding card for the new CCR-R08 deterministic complete final catalog module (catalog
  population, exact plan, exhaustive attestation, readiness projection) delivered in code commit
  16d1a4d6; anchors and ranges derived from the current worktree source and pinned to that commit.
