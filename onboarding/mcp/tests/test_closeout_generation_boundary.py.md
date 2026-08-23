# mcp/tests/test_closeout_generation_boundary.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_closeout_generation_boundary.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-23T16:08+02:00 |
| lastVerifiedCommitHash | `1d446724d099517f6f52d596b47827ae2391a2a4` |
| lastVerifiedCommitDate | 2026-08-24T00:21:10+02:00 |
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
| Proven mutation retains its generation, then real candidate advancement admits a new one. | `test_completed_mutated_generation_retains_intent_then_allows_advancement` | mcp/tests/test_closeout_generation_boundary.py:399-436 |

## Cross-Repo References

No meaningful cross-repository reference applies.

## 260821-CLIVE-L2 Current Regression Contract

The current forcing seams include `test_invalid_closeout_precedes_active_integrate_decision_without_authority`, `test_valid_closeout_conflicts_with_active_integrate_only_after_validation`, `test_noop_finalization_retry_observes_the_same_generation`, `test_invalid_duplicate_cannot_observe_noop_finalized_external_generation`. The L2 additions force immutable normalized input, exact generation retention, evidence-derived cancellation/recovery, and pre-authority refusal of invalid calls. A failed first call remains task-addressably recoverable without amending accepted intent.

### Reconciled Source Evidence

| Finding | Citations | Source Path |
| --- | --- | --- |
| The current test source exercises `test_invalid_closeout_precedes_active_integrate_decision_without_authority`, `test_valid_closeout_conflicts_with_active_integrate_only_after_validation`, `test_noop_finalization_retry_observes_the_same_generation`, `test_invalid_duplicate_cannot_observe_noop_finalized_external_generation`. | L55-L116; L119-L145; L153-L191; L195-L221 | `mcp/tests/test_closeout_generation_boundary.py` |

## Update History

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this test card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: created from accepted candidate tree `4241908c`; first verification stamp remains closeout-owned.
