# mcp/tests/test_final_catalog_plan_attestation.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Gate-5 final catalog population and affected-coherence binding.

## Code Commentary

### Logic

Attestation must exhaust the frozen planned population. Green, red and blocked executed outcomes retain exact counts and blocking reasons. An affected closure for another memory tree refuses; coherence subrecords must cover every affected member.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Fixture results supply executed facts to the catalog contract. These tests do not execute all memory producers or independently certify a real closeout.

### Todos

No file-local implementation change is requested by this reconciliation.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

- Attestation must exhaust the planned population. [1]
- Attestation green and red and blocked. [2]
- Plan refuses affected closure bound to another memory tree. [3]
- Coherence subrecords require affected coverage. [4]

### Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

Fixture repositories and protocol doubles do not establish a live external integration.

## CCR-L42 current candidate

The final-catalog tests now import the moved `FinalFullCatalogPlan` model and cover shared-evidence subrecord deduplication plus conflicting shared-reference digest refusal. They remain fixture-level contract tests and do not independently certify closeout.
