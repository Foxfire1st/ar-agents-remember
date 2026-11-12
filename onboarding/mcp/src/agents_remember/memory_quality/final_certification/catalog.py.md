# mcp/src/agents_remember/memory_quality/final_certification/catalog.py

## Governing Overview

[memory_quality overview](../overview.md)

## Purpose

Owns the closed deterministic memory-quality catalog and non-certifying repair-loop readiness projection. Four standard checks and five fixed items (missing onboarding, route-index alignment, affected closure, coherence record and candidate pair) appear once in canonical order. Results carry content digests and typed statuses; the interactive projection cannot authorize finalization. Plan compilation and executed-attestation assembly are not part of this surviving module.

## Code Commentary

### Logic

`complete_final_catalog` sorts the four standard checker identities and five fixed items by their keys and raises typed `gate-five-catalog-incomplete` when scope-registry membership differs from `AVAILABLE_CHECKS`.

`ReadinessProjectionInput` carries executed check mappings, missing-card/stale-index counts, coherence status/digest, candidate-pair authority digest, optional affected-plan digest and memory tree. `final_catalog_readiness` produces every catalog item with typed status, named blocked authorities and content-addressed subresults; its flags remain `finalizationEligible=false` and `fullFinalRequired=true`.

`_executed_result` first reads the item's own name and, for the drift item only, falls back to `knowledge.converted`. Missing execution reads fail. `_standard_result` binds `ok` to pass/fail and digests the supplied result; `_count_result` passes only at zero; `_authority_result` retains nonempty `blockedBy` for blocked authorities. No planner, exhaustive executed-population attestation or green-prefix validator is present.

### Conventions

Item results are content-addressed via `content_digest`; blocked items carry `blockedBy`. Typed models come from `certification.final_certification_models`; `_refuse_unknown_item` raises `FinalCertificationError` with `gate-five-catalog-item-unknown` and `next_action="memory_quality_check"`.

### Invariants And Boundaries

- The catalog is closed and deterministic and must cover the complete current checker registry.
- Readiness never mutates code or memory and always remains non-finalization-eligible.
- An absent affected-plan digest produces the named blocked item; this projection does not compile or execute a closure.

### Todos

None.

## Evidence

### Repo-Internal References

- Returns the closed deterministic catalog population. [1]




- Publishes the non-certifying readiness projection for the repair loop. [4]


- ReadinessProjectionInput closes the repair-loop executed/count/authority inputs; no ExecutedFinalCatalog survives. [5]

- Standard, count, and authority result builders. [6]




- Unknown catalog items raise typed gate-five-catalog-item-unknown with memory_quality_check recovery. [8]


- One standard check's executed result; the drift item of a converted tree is the converted check's. [9]

- The drift item of a converted run reads pass, fail with its findings, or fail when neither spelling ran. [10]
