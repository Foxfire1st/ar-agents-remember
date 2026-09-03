# mcp/tests/test_l5_quality_and_recovery_edges.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_l5_quality_and_recovery_edges.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `4e0ea4b3c493a2c89ca18367e89e4cb42ee8c5f3` |
| lastVerifiedCommitDate | 2026-09-03T00:47:35+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[governing overview](../overview.md)

## Purpose

Forces the residual report, certificate, public ledger-kind, series-prefix, and integration-only lifecycle boundaries around organizational completion, and — since CCR-R05@v3 — the exact-candidate admission, prior-red corrective, certificate-recovery, and durable finalization-leg boundaries with zero gate starts.

## Code Commentary

The suite has two layers. Module-level pytest tests (R05 boundary layer) drive
`compile_lifecycle_admission`, `validate_lifecycle_admission_currentness`, the prior-red
disposition machinery, `compile_certification_recovery_record`, and the finalization manifest
authority against a portable fixture scenario (`_scenario`, lines 132-160) that compiles a real
R22 repository profile and R11 registry/plan, proving admission freezes every authority without
running or mutating, invalid owner authority and worktree shapes refuse with zero starts,
prior-red requires every failed/blocked root with exact changed inputs, recovery journals R21 reuse
for code/memory/unchanged interruption, and partial finalization resumes the exact leg. The
unittest layer (`L5QualityAndRecoveryEdgeTests`, now at line 967) keeps the narrow seams where
the Dagger quality and recovery paths touch the surrounding lifecycle: residual report
publication, certification revalidation, ledger-kind and series-prefix constraints on the
external-memory mapping, and the integration-only boundary that ordinary leaves never cross
(`clean_quality_executor`/Dagger attestation/manifest seams).

## Invariants And Boundaries

- Exercises production owners rather than copied guards.
- Refusal cases assert the boundary is enforced without ref or ledger mutation.
- Admission/finalization refusals emit `gateStarts: 0`; an unchanged red candidate always
  refuses.
- An unchanged interruption resumes the exact durable finalization leg with zero certification
  starts.

## Docs References

No Domain Documentation source is configured for this memory root. The governing task artifact
below closes the informational gap for the enforced boundaries.

| Finding | Anchor | Source |
| --- | --- | --- |
| CCR-R05@v3 admission and finalization required behavior; the suite's zero-start refusal and exact-leg resume assertions mirror it. | "Admission Required Behavior"; "Finalization Required Behavior" | ar-coordination/tasks/agents-remember/260831_closeout-certification-reform/requirements/CCR-R05-v3-exact-candidate-admission-and-recovery.md |
| L05 committed exact-candidate admission and recovery evidence into this suite. | "S2 — Implement only CCR-R05" | ar-coordination/tasks/agents-remember/260831_closeout-certification-reform/05_exact-candidate-admission-and-recovery.md |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The suite admits one supplied authority set and refuses invalid authority/worktree with zero starts. | `test_admission_freezes_all_authorities_without_running_or_mutating`; `test_admission_refuses_invalid_owner_authority_with_zero_starts` | mcp/tests/test_l5_quality_and_recovery_edges.py:515-556; mcp/tests/test_l5_quality_and_recovery_edges.py:557-576 |
| Currentness and prior-red edges refuse movement and enforce exact corrective dispositions. | `test_currentness_refuses_candidate_or_authority_movement`; `test_prior_red_requires_every_root_and_allows_blocked_dependant_to_cite_repair`; `test_prior_red_refuses_unchanged_or_diagnostic_catalog_authority` | mcp/tests/test_l5_quality_and_recovery_edges.py:577-593; mcp/tests/test_l5_quality_and_recovery_edges.py:594-729; mcp/tests/test_l5_quality_and_recovery_edges.py:730-795 |
| Recovery and finalization resume the exact journaled leg with zero certification starts. | `test_recovery_journals_r21_reuse_for_code_memory_and_unchanged_interruption`; `test_partial_finalization_resumes_exact_leg_with_zero_gate_starts`; `test_finalization_refuses_movement_lost_authority_and_cancellation` | mcp/tests/test_l5_quality_and_recovery_edges.py:796-833; mcp/tests/test_l5_quality_and_recovery_edges.py:834-918; mcp/tests/test_l5_quality_and_recovery_edges.py:919-941 |
| Finalization journal progress is forced non-monotonic-refusing and ambiguity-refusing. | `test_finalization_journal_rejects_nonmonotonic_or_ambiguous_progress` | mcp/tests/test_l5_quality_and_recovery_edges.py:942-965 |
| The unittest layer owns the Dagger quality attestation, manifest, and integration seams. | `L5QualityAndRecoveryEdgeTests` | mcp/tests/test_l5_quality_and_recovery_edges.py:967-1186 |
| The fixture compiles real R22 profile and R11 registry/plan authorities. | `_scenario`; `fixture_profile`; `agents_remember_profile_execution` | mcp/tests/test_l5_quality_and_recovery_edges.py:132-160; mcp/tests/test_l5_quality_and_recovery_edges.py:104-109 |
| The suite drives production owners such as `LifecycleOperationStore` and the clean quality executor. | `LifecycleOperationStore`; `clean_quality_executor`; `code_quality_gate` | mcp/tests/test_l5_quality_and_recovery_edges.py:97-102 |

## Documentation References

No configured domain-documentation or cross-repository source applies to this file.

## 260821-DAGQC-L2 Quality Recovery Edges

The quality edge cases now reject hostile/non-object/extra-root manifest shapes through the shared
error, verify declared artifact integrity from one snapshot, and assert recovered responses retain
the stable wrapper report separately from the immutable published result.

## 260824-PDLS Recovery Evidence Proof

Recovery fixtures now publish schema-2 generations with candidate trees and require typed
certifying evidence in fresh success payloads. Invalid/unreadable result exports refuse publication,
and recovered evidence must match the current Git tree. Schema `1.0` remains a deliberate public
reader refusal, not a compatibility route.

## 2026-08-26 Quality Callback Fidelity

The organizational quality-gate test now supplies the fixture through the mocked gate's
`side_effect`, exercising the same request-dependent callback shape as the production boundary
instead of returning a precomputed value. The asserted certification and recovery contracts are
unchanged, but the test double can no longer bypass argument-sensitive evidence construction.

## Update History

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for 4e0ea4b3c493a2c89ca18367e89e4cb42ee8c5f3 (CCR-R05@v3/L05): documented the R05 exact-candidate admission, prior-red, recovery, and finalization edge layer added to this suite; refreshed the `L5QualityAndRecoveryEdgeTests` anchor from lines 23-122 to the current class at line 967 and added the production-owner fixture citations. Verification metadata rebased from `ae8c47ce` to the L05 owning commit.

- 2026-08-26T10:44:52+02:00 — Updated the organizational gate test double to invoke the candidate-aware quality fixture through the production callback shape.
- 2026-08-24T21:23+02:00 — Updated quality recovery for candidate-bound certifying evidence.

- 2026-08-24T14:19+02:00 — 260821-DAGQC-L2: extended focused recovery edges for strict manifest authority and distinct stable/published result paths. Verification metadata remains pinned until architect-owned closeout.


- 2026-08-24T00:51+02:00 — No content impact: 260821-CLIVE-L2 the test only repoints `LifecycleOperationStore` to its moved integration lifecycle package. Verified at code commit `1d446724`.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-17T12:09+02:00 — 260815-DAG-L5: created onboarding for the L5 quality-and-recovery boundary suite.
