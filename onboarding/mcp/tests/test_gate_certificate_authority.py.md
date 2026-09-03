# mcp/tests/test_gate_certificate_authority.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_gate_certificate_authority.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | 6f10c24d72db6171c0d434b307e6806996e2f11d |
| lastVerifiedCommitDate | 2026-09-02T18:10:52+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

The forcing suite for the content-addressed gate-certificate contract (CCR-R21@v2): admission
freezes, five-gate certificate issuance, dependency-aware invalidation/reuse, exact artifact
binding between Gate 2 and Gate 3, the content-addressed store, and finalization authority.

## Code Commentary

### Logic

`_Scenario` builds a canonical registry/profile/plan/admission tower; `_certify_through`
issues a complete Gate 1-5 certificate set. The cases prove the certificate digest binds exact
semantics but not provenance; inventories refuse duplicates; the five-gate chain separates suite
artifacts from finalization authority; red/partial/diagnostic/combined results never publish
certificates; the normative invalidation matrix is exhaustive; reuse is dependency-aware and
refuses forged or stale identity; profile mismatch and unproven runtime changes fail closed; the
content store is exact/atomic/bounded with no historical lookup; forged noncanonical envelopes
refuse; admission refuses conflicts/misalignment/unproven candidates; publication refuses stale
dependencies and incomplete authority; input-change/reuse shapes fail closed; and store capacity
corruption refuses.

### Invariants And Boundaries

- Only a complete green certifying result publishes a certificate; diagnostics never promote.
- Gate 3 accepts only the exact green Gate-2 certificate and verified artifacts.
- Journal/review/approval metadata never perturbs Gate 1-4 identities.
- Unchanged recovery begins with zero gate starts; the store is never queried by newest-success.
- Exact finding codes are asserted on every refusal.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies; CCR-R21@v2 is the governing packet.

| Finding | Anchor | Source |
| --- | --- | --- |
| The R21 packet requires the full invalidation matrix, artifact verification, and store/authority refusal fixtures. | "Expected Verification Evidence" | ar-coordination/tasks/agents-remember/260831_closeout-certification-reform/requirements/CCR-R21-v2-content-addressed-phase-certificates.md:126-135 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Admission and certificate issuance bind exact semantics, not provenance. | `test_admission_and_gate_certificates_bind_exact_semantics_not_provenance` | mcp/tests/test_gate_certificate_authority.py:324-355 |
| The five-gate chain separates suite artifacts and finalization authority; red/diagnostic results never publish. | `test_five_gate_chain_separates_suite_artifacts_and_finalization_authority`; `test_red_partial_diagnostic_and_combined_results_never_publish_certificates` | mcp/tests/test_gate_certificate_authority.py:390-433; mcp/tests/test_gate_certificate_authority.py:435-479 |
| The normative matrix and dependency-aware reuse are forced. | `test_normative_invalidation_matrix`; `test_reuse_is_dependency_aware_and_refuses_forged_or_stale_identity` | mcp/tests/test_gate_certificate_authority.py:481-506; mcp/tests/test_gate_certificate_authority.py:508-565 |
| The content store is exact, atomic, bounded, and has no historical lookup. | `test_content_store_is_exact_atomic_bounded_and_has_no_historical_lookup`; `test_content_store_refuses_publication_and_capacity_corruption` | mcp/tests/test_gate_certificate_authority.py:591-638; mcp/tests/test_gate_certificate_authority.py:964-1020 |
| Forged envelopes, stale dependencies, and incomplete authority refuse with finding codes. | `test_certificate_models_refuse_forged_noncanonical_envelopes`; `test_certificate_publication_refuses_stale_dependencies_and_incomplete_authority` | mcp/tests/test_gate_certificate_authority.py:640-719; mcp/tests/test_gate_certificate_authority.py:793-885 |

## Cross-Repo References

None; the suite is repository-local and exercises production certificate owners.

## Update History

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for
  6f10c24d72db6171c0d434b307e6806996e2f11d (CCR-R21@v2/L21): created the card for the new
  content-addressed gate-certificate forcing suite (admission freeze, Gate 1-5 issuance and reuse,
  artifact binding, invalidation matrix, store, finalization). Verification is pinned to the
  owning commit.
