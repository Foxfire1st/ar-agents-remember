# mcp/tests/test_closeout_generation_boundary.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_closeout_generation_boundary.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:48+02:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d` |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

Forces closeout generation identity and admission ordering: invalid input cannot observe integration authority, accepted duplicates retain their immutable plan, no-op finalization retains the generation by exact publication hash, and a new generation requires real contract/candidate advancement.

## Code Commentary

### Logic

The suite contrasts invalid same-kind and cross-kind requests with valid conflicts, proves that validation precedes lifecycle-state disclosure, rejects invalid-generation laundering, and distinguishes recovery cells from authoritative mutation/finalization evidence. Candidate 11 retains two forcing seams: a retained generation remains recoverable when worker relaunch itself fails, and a generation with proven code mutation is retained until real contract/candidate advancement admits the next generation.

### Invariants And Boundaries

- Invalid input has no authority or operation-state effect.
- Duplicate requests validate against accepted immutable intent.
- Completion alone does not create a new generation.
- Exact canonical finalization retains no-op generations without fake Git evidence.

## Docs References

See task `260821-CLIVE-L1` L1-R2, L1-R3, L1-R5, and L1-R6.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Validation precedes same/cross-kind lifecycle decisions. | `test_invalid_closeout_precedes_active_integrate_decision_without_authority`, `test_valid_closeout_conflicts_with_active_integrate_only_after_validation` | mcp/tests/test_closeout_generation_boundary.py:55-116; mcp/tests/test_closeout_generation_boundary.py:119-145 |
| No-op finalization and incomplete recovery projection retain only the evidence-backed generation. | `test_noop_finalization_retry_observes_the_same_generation`, `test_recovery_cells_without_exact_finalization_state_do_not_retain_generation` | mcp/tests/test_closeout_generation_boundary.py:153-191; mcp/tests/test_closeout_generation_boundary.py:287-313 |
| Proven mutation retains its generation and requires an explicit disposition before advancement. | `test_completed_mutated_generation_retains_intent_and_requires_explicit_disposition` | mcp/tests/test_closeout_generation_boundary.py:400-436 |

## Cross-Repo References

No meaningful cross-repository reference applies.

## 260821-CLIVE-L2 Current Regression Contract

The current forcing seams include `test_invalid_closeout_precedes_active_integrate_decision_without_authority`, `test_valid_closeout_conflicts_with_active_integrate_only_after_validation`, `test_noop_finalization_retry_observes_the_same_generation`, `test_invalid_duplicate_cannot_observe_noop_finalized_external_generation`. The L2 additions force immutable normalized input, exact generation retention, evidence-derived cancellation/recovery, and pre-authority refusal of invalid calls. A failed first call remains task-addressably recoverable without amending accepted intent.

### Reconciled Source Evidence

| Finding | Anchor | Source |
| --- | --- | --- |
| The current test source exercises `test_invalid_closeout_precedes_active_integrate_decision_without_authority`, `test_valid_closeout_conflicts_with_active_integrate_only_after_validation`, `test_noop_finalization_retry_observes_the_same_generation`, `test_invalid_duplicate_cannot_observe_noop_finalized_external_generation`. | `test_invalid_closeout_precedes_active_integrate_decision_without_authority`; `test_valid_closeout_conflicts_with_active_integrate_only_after_validation`; `test_noop_finalization_retry_observes_the_same_generation`; `test_invalid_duplicate_cannot_observe_noop_finalized_external_generation` | mcp/tests/test_closeout_generation_boundary.py:57-124; mcp/tests/test_closeout_generation_boundary.py:127-154; mcp/tests/test_closeout_generation_boundary.py:157-197; mcp/tests/test_closeout_generation_boundary.py:200-227 |

## Current Contract — 260821 CLIVE Final

This is the current source-backed contract for this test card. It supersedes any earlier
queue-lifecycle, blocker-row, replan/drain, or compatibility-reader wording where present.

Forces validation ordering and retained same-generation recovery across no-op finalization, partial output, worker relaunch failure, candidate movement, and completed-unintegrated disposition.

### Current Invariants

- Invalid effective input refuses before operation authority or side effects.
- A durable incomplete or completed-unintegrated generation remains journal-addressable and cannot be replaced by a newer candidate.

## Update History

- 2026-08-26T10:44:52+02:00 — No content impact: reviewed closeout recovery-projection and lifecycle-worker package relocations; generation-boundary forcing is unchanged.

- 2026-08-24T14:48+02:00 — DAGQC cumulative CLIVE final-gap curation: reconciled this test card to current source while preserving prior history and verification provenance.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this test card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: created from accepted candidate tree `4241908c`; first verification stamp remains closeout-owned.