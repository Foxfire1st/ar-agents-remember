# mcp/tests/test_gate_certificate_authority.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_gate_certificate_authority.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:46+00:00 |
| lastVerifiedCommitHash | `d36109038b3f2b500c138f9dc1ea9c9f9a247489`|
| lastVerifiedCommitDate | 2026-09-06T22:21:49+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Content-addressed five-gate certificate and finalization authority contracts.

## Code Commentary

### Logic

The chain separates Gate-2 artifacts from Gate-3 manifests and binds Gate-5 memory inputs and four predecessors. Red, partial, diagnostic or combined results refuse certification. Reuse follows dependencies: memory changes rerun Gate 5, unchanged inputs start none and image changes restart Gate 4. The store enforces exact bounded atomic bytes and admission rejects conflicting semantic inputs.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Certificates require original authority rather than a historical search or recomputed matching label. Finalization currentness is separate from merely holding a five-certificate chain.

### Todos

No file-local implementation change is requested by this reconciliation.

## Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain evidence applies to the file-local claims above. | N/A | N/A |

## Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

| Finding | Anchor | Source |
| --- | --- | --- |
| Five gate chain separates suite artifacts and finalization authority. | `test_five_gate_chain_separates_suite_artifacts_and_finalization_authority` | mcp/tests/test_gate_certificate_authority.py:319-361 |
| Red partial diagnostic and combined results never publish certificates. | `test_red_partial_diagnostic_and_combined_results_never_publish_certificates` | mcp/tests/test_gate_certificate_authority.py:364-407 |
| Reuse is dependency aware and refuses forged or stale identity. | `test_reuse_is_dependency_aware_and_refuses_forged_or_stale_identity` | mcp/tests/test_gate_certificate_authority.py:410-466 |
| Profile mismatch and unproven runtime change fail closed. | `test_profile_mismatch_and_unproven_runtime_change_fail_closed` | mcp/tests/test_gate_certificate_authority.py:469-490 |
| Content store is exact atomic bounded and has no historical lookup. | `test_content_store_is_exact_atomic_bounded_and_has_no_historical_lookup` | mcp/tests/test_gate_certificate_authority.py:493-542 |
| Admission refuses conflicts misalignment and unproven candidate. | `test_admission_refuses_conflicts_misalignment_and_unproven_candidate` | mcp/tests/test_gate_certificate_authority.py:545-614 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-06T21:46+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.


- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for
  6f10c24d72db6171c0d434b307e6806996e2f11d (CCR-R21@v2/L21): created the card for the new
  content-addressed gate-certificate forcing suite (admission freeze, Gate 1-5 issuance and reuse,
  artifact binding, invalidation matrix, store, finalization). Verification is pinned to the
  owning commit.
