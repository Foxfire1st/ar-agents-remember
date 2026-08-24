# mcp/tests/test_closeout_mutation_evidence_boundary.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_closeout_mutation_evidence_boundary.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:48+02:00 |
| lastVerifiedCommitHash | `f95487ec993b58d34911bba0206a7fa6ef9684eb` |
| lastVerifiedCommitDate | 2026-08-24T15:28:18+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

Forces the journaled mutation-evidence protocol and all known bypass refusals for non-preview worktree closeout.

## Code Commentary

### Logic

The suite proves that direct synchronous apply, the generic lifecycle starter, and the legacy CLI apply cannot mutate closeout state without journal authority. It separately drives the sanctioned public lease-bound starter and proves that its durable record contains the resolved candidate. A stale public retry after mutation intent reconciles the unchanged repository as `reconciled-unchanged`, preserves attempt one, performs no launch, and remains cancellable instead of laundering the same intent into another mutation attempt.

Two forcing cases exercise failures before durable intent publication through real Git boundaries. A non-repository status error and a missing ref-log both preserve the journal bytes literally and leave evidence at `pre-mutation`; neither mocked snapshot state nor an inferred no-op can advance the record. Exact intent/commit proof and reconciliation cases also cover missing authority before snapshot, changed or incomplete intent, expected output, wrong ref, ref moved and returned, unreadable authorized repository, repository escape, and multi-leg isolation.

A public external-ledger scenario begins and binds mutation intent, prepares an output tree that
differs from the before tree, then restores the index and worktree exactly. Reconciliation preserves
the bound `expectedOutputTree` as intent evidence while publishing `reconciled-unchanged`; the
observed snapshot equals the before snapshot and the operation is cancellable. This proves an
expected tree is not itself commit evidence.

### Invariants And Boundaries

- Intent must be durable before Git.
- Commit proof is exact branch/parent/tree evidence.
- Reflog-sensitive ambiguity refuses; it is not collapsed into “unchanged.”
- Each evidence record is bound to one accepted enabled leg and repository.
- A reconciled-unchanged public retry is still the accepted attempt, not permission to relaunch.
- Reconciled-unchanged preserves bound expected intent even when that tree differs from restored
  HEAD; only an observed matching commit may become commit-proven.
- Git status or reflog observation failure has literal journal/evidence no-effect.

## Docs References

See task `260821-CLIVE-L1` L1-R4 through L1-R6.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Ungoverned entrances fail closed while the public lease-bound closeout route persists its admitted candidate. | `test_direct_closeout_apply_without_journal_authority_refuses_before_route_or_git`, `test_lease_bound_closeout_start_supplies_its_resolved_candidate`, `test_legacy_cli_apply_cannot_bypass_the_journaled_operation` | mcp/tests/test_closeout_mutation_evidence_boundary.py:64-82; mcp/tests/test_closeout_mutation_evidence_boundary.py:102-115; mcp/tests/test_closeout_mutation_evidence_boundary.py:215-232 |
| A stale unchanged-intent retry remains attempt one, does not launch, and stays cancellable. | `test_stale_unchanged_intent_observes_attempt_one_without_relaunch` | mcp/tests/test_closeout_mutation_evidence_boundary.py:118-149 |
| Real Git status and removed-reflog failures leave journal bytes and pre-mutation evidence unchanged. | `test_git_mutation_status_failure_has_no_durable_progress`, `test_git_mutation_ref_log_failure_has_no_durable_progress` | mcp/tests/test_closeout_mutation_evidence_boundary.py:152-177; mcp/tests/test_closeout_mutation_evidence_boundary.py:180-212 |
| Authority, binding, and proof reject changed or incomplete intent before mutation evidence can advance. | `test_git_mutation_helper_cannot_silently_run_without_evidence_authority`, `test_bind_and_proof_refuse_changed_or_incomplete_intent` | mcp/tests/test_closeout_mutation_evidence_boundary.py:235-244; mcp/tests/test_closeout_mutation_evidence_boundary.py:289-329 |
| Snapshot reconciliation distinguishes exact, ambiguous, escaped, unreadable, and multi-leg outcomes. | `test_reconciliation_distinguishes_unchanged_ambiguous_and_proven_output`, `test_one_unchanged_leg_cannot_hide_another_legs_proven_commit` | mcp/tests/test_closeout_mutation_evidence_boundary.py:333-363; mcp/tests/test_closeout_mutation_evidence_boundary.py:881-924 |
| Exact restore preserves the differing bound output tree while producing cancellable reconciled-unchanged evidence. | `test_reconciliation_preserves_bound_output_after_exact_restore` | mcp/tests/test_closeout_mutation_evidence_boundary.py:366-417 |

## Cross-Repo References

No meaningful cross-repository reference applies.

## 260821-CLIVE-L2 Current Regression Contract

The current forcing seams include `test_direct_closeout_apply_without_journal_authority_refuses_before_route_or_git`, `test_generic_lifecycle_start_cannot_bypass_raw_closeout_admission`, `test_lease_bound_closeout_start_supplies_its_resolved_candidate`, `test_stale_unchanged_intent_observes_attempt_one_without_relaunch`. The L2 additions force immutable normalized input, exact generation retention, evidence-derived cancellation/recovery, and pre-authority refusal of invalid calls. A failed first call remains task-addressably recoverable without amending accepted intent.

### Reconciled Source Evidence

| Finding | Citations | Source Path |
| --- | --- | --- |
| The current test source exercises `test_direct_closeout_apply_without_journal_authority_refuses_before_route_or_git`, `test_generic_lifecycle_start_cannot_bypass_raw_closeout_admission`, `test_lease_bound_closeout_start_supplies_its_resolved_candidate`, `test_stale_unchanged_intent_observes_attempt_one_without_relaunch`. | L64-L82; L85-L99; L102-L115; L118-L149 | `mcp/tests/test_closeout_mutation_evidence_boundary.py` |

## Current Contract — 260821 CLIVE Final

This is the current source-backed contract for this test card. It supersedes any earlier
queue-lifecycle, blocker-row, replan/drain, or compatibility-reader wording where present.

Forces journal-owned Git mutation authority and reconciliation across ordinary closeout, external memory, ledger crash cuts, ambiguous output, restored pre-state, moved refs, and repository confinement.

### Current Invariants

- Direct or legacy entry points cannot bypass journal admission.
- Recovery continues the same accepted generation and preserves exact conflict evidence without raw-Git fallback.

## Update History

- 2026-08-24T14:48+02:00 — DAGQC cumulative CLIVE final-gap curation: reconciled this test card to current source while preserving prior history and verification provenance.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this test card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-22T11:29+02:00 — 260821-CLIVE-L1 candidate12 rebind: added the real
  begin/bind/restore/reconcile proof that a differing expected tree survives exact restoration
  without becoming commit proof, and that the reconciled generation is cancellable. Bound to
  reviewed candidate tree `8f03b256fe24aa77262da805f1538ee39ccb4dd6`, full diff SHA
  `ccb36a898b455cd67ca00c378e5ba0f18851be01faf3d26eced3b9af062f429e`, same-reviewer PASS;
  test verification remains closeout-owned.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1 candidate-11: rebound public unchanged-intent retry semantics plus real status/reflog failure no-effect forcing against accepted tree `4241908c`; test verification remains closeout-owned.
