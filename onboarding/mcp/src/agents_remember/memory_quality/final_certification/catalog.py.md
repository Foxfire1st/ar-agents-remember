# mcp/src/agents_remember/memory_quality/final_certification/catalog.py

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
  checker ids in `_STANDARD_CHECK_IDS` (lines 52-60) close the population.
- `ExecutedFinalCatalog` (class, lines 64-75) - one executed complete catalog plus the
  authority statuses it observed (missing-onboarding/stale-route-index counts, affected-closure,
  coherence and pair statuses, full-only rerun flag, coherence record digest).
- `ReadinessProjectionInput` (class, lines 78-89) - the repair-loop view of one full run that
  is never certification-eligible (see `final_catalog_readiness`).
- `complete_final_catalog` (lines 92-122) - returns the closed catalog population in
  canonical order and refuses (gate-five-catalog-incomplete) whenever the declared checker scope
  registry diverges from `AVAILABLE_CHECKS`.
- `compile_final_catalog_plan` (lines 125-164) - binds the plan to the exact candidate pair:
  verifies the affected-closure plan names the same code and memory trees with a
  non-accepting/full-final-required disposition, requires a nonempty canonical coherence
  subrecord set, and digests the whole payload into `planDigest`.
- `final_catalog_attestation` (lines 167-234) - maps one executed run into the exhaustive
  typed attestation; item results are standard-check, count-based (missing-onboarding /
  stale-route-index), or authority-based (affected-closure / coherence-record / candidate-pair)
  via `_standard_result` / `_count_result` / `_authority_result` (lines 348-402).
- `final_catalog_readiness` (lines 237-329) - the deterministic Gate-5 surface projection
  published by the interactive controller full run: complete population, per-item typed status,
  and blocked items naming the exact missing authority, with
  `finalizationEligible=false` and `fullFinalRequired=true`.
- Guards `_require_affected_closure_bound` (409-435),
  `_require_pending_full_only_population` (438-455) and
  `_require_executed_population` (458-472) make code/memory binding, R07 pending-full-only
  coverage, and executed standard-check exhaustion structural.
- `_executed_result` (lines 332-345, L37) is the one lookup of a standard check's executed result, for the
  attestation, the readiness projection and the executed-population guard. On a converted tree the drift slot runs
  the knowledge validator and stores its result as `knowledge.converted` (`CONVERTED_KNOWLEDGE_CHECK`, MIK-R24
  rule 5); asked for the drift check's own name, the lookup answers that result, so the drift item of a
  converted run reads the converted check's `pass`, or its `fail` with the findings. A run that executed neither
  spelling reads `fail`.

### Conventions

Item results are content-addressed via `content_digest`; a blocked item always carries a
nonempty `blockedBy`; the typed catalog contracts come from the lower-level
`certification.final_certification_models` module; unknown item ids refuse through
`_refuse_unknown_item` (461-466).

### Invariants And Boundaries

- The catalog is closed and deterministic; nothing outside the declared population can be
  attested, and the attestation must exhaust exactly the planned population.
- Certification never mutates code or memory; the readiness projection cannot claim
  certification eligibility.
- The full catalog must cover the complete current memory checker registry and every R07
  pending full-only checker.

### Todos

None.

## Evidence

### Repo-Internal References

- Returns the closed deterministic catalog population. [1]
- Compiles the exact plan bound to one candidate pair with a self-digest. [2]

- Maps an executed run into the exhaustive typed attestation. [3]
- Publishes the non-certifying readiness projection for the repair loop. [4]

- Closes the executed/observed authority shapes of one run. [5]
- Standard, count, and authority result builders. [6]

- Code/memory binding, pending full-only coverage, and executed-population guards. [7]

- The typed refusal and unknown-item refusal helpers. [8]

- One standard check's executed result; the drift item of a converted tree is the converted check's. [9]
- The drift item of a converted run reads pass, fail with its findings, or fail when neither spelling ran. [10]
